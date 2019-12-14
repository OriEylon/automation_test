import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection


def select_all_from(conn,from_where):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(from_where))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_to_projects(conn,project):
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def insert_to_employees(conn,employee):
    sql = ''' INSERT INTO employees(name,works_on,adress)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid


def delete_employee(conn, id):

    sql = 'DELETE FROM employees WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_employees(conn):

    sql = 'DELETE FROM employees'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    # database = r"C:\Users\Ori's pc\GitHub\automation_test\chinook.db"
    db = r"C:\Users\Ori's pc\GitHub\automation_test\mydb.db"
    # create a database connection
    conn = create_connection(db)
    # with conn:
    #     print("1. Query all employees:")
    #     select_all_employees(conn)
    create_table_projects = '''CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); '''
    create_table_employees = '''CREATE TABLE IF NOT EXISTS employees (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    works_on integer NOT NULL,
                                    adress text,
                                    FOREIGN KEY (works_on) REFERENCES projects (id)
                                    );'''
    # create_table(conn,create_table_projects)
    # create_table(conn, create_table_employees)
    proj1 = ('test proj','12-12-19','14-12-19')
    emp1 = ('ori eylon', '1','sheshet hayamim 50')
    # insert_to_projects(conn, ('proj2','13-12-2019','31-12-2019'))
    # insert_to_projects(conn, ('proj3', '01-01-2020', '31-12-2020'))
    # insert_to_employees(conn, ('employee2','1','eli visel 3'))
    # insert_to_employees(conn, ('employee3', '2', 'azrieli holon 2'))
    # insert_to_employees(conn, ('employee5', '4', 'sheshet hayamim 55'))
    # delete_employee(conn,5)

    select_all_from(conn, 'projects')
    select_all_from(conn, 'employees')
    conn.close()

if __name__ == '__main__':
    main()
