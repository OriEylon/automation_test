from flask import Flask
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from flask import jsonify


db_connect = create_engine('sqlite:///mydb.db')
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from employees")  # This line performs query and returns json result
        # return {'employees': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("works_on")
        parser.add_argument("adress")
        args = parser.parse_args()
        check = conn.execute("select name from employees where name ={} ".format(args["name"])).fetchall()
        if check:
            return "employee {} already exists".format(args["name"]), 400

        result = conn.execute("insert into employees(name,works_on,adress) values ({},{},{})".format(args["name"],
                                                                                                     args["works_on"],
                                                                                                     args["adress"]))
        # print(result)
        return 'success', 201
        # return "{} added to db".format(name), 201

    def put(self):
        conn = db_connect.connect()
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        parser.add_argument("works_on")
        parser.add_argument("adress")
        args = parser.parse_args()
        check = conn.execute("update employees set name={},works_on={}, adress={} where id ={} ".format(args["name"],
                                                                                                        args[
                                                                                                            "works_on"],
                                                                                                        args["adress"],
                                                                                                        args["id"]))
        return "employee id num {} updated".format(args["id"]), 200

    def delete(self):
        conn = db_connect.connect()
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        args = parser.parse_args()
        check = conn.execute("delete from employees where id={}".format(args["id"]))
        return "employee id num {} deleted".format(args["id"]), 200


class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        result = conn.execute("select name from employees where id ={} ".format(employee_id)).fetchall()
        if result:
            return jsonify([dict(r) for r in result])
        else:
            return 'employee not found', 404

        # print(query.keys())
        # result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        # return jsonify(result)


class Projects(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from projects")  # This line performs query and returns json result
        # return {'projects': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        parser.add_argument("begin_date")
        parser.add_argument("end_date")
        args = parser.parse_args()
        check = conn.execute("update projects set name={},begin_date={}, end_date={} where id ={} ".format(args["name"],
                                                                                                           args[
                                                                                                               "begin_date"],
                                                                                                           args[
                                                                                                               "end_date"],
                                                                                                           args["id"]))
        return "project id num {} updated".format(args["id"]), 200

    def post(self):
        conn = db_connect.connect()
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("begin_date")
        parser.add_argument("end_date")
        args = parser.parse_args()
        check = conn.execute("select name from projects where name ={} ".format(args["name"])).fetchall()
        if check:
            return "project {} already exists".format(args["name"]), 400

        result = conn.execute("insert into projects(name,begin_date,end_date) values ({},{},{})".format(args["name"],
                                                                                                     args["begin_date"],
                                                                                                     args["end_date"]))
        # print(result)
        return 'success', 201

    def delete(self):
        conn = db_connect.connect()
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        args = parser.parse_args()
        check = conn.execute("delete from projects where id={}".format(args["id"]))
        return "project id num {} deleted".format(args["id"]), 200


api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Projects, '/projects')  # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3

if __name__ == '__main__':
    app.run(port='5000')