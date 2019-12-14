import requests

base_url="http://127.0.0.1:5000/"


def test_GET_existing_employee():
        url=base_url+'employees/1'
        response=requests.get(url)
        assert response.status_code == 200 , 'should be 200, employee exists'


def test_GET_non_existing_employee():
    url=base_url+'employees/4'
    response = requests.get(url)
    assert response.status_code == 404, f'got {response.status_code}, should be 404 because employee num 4 is deleted'


def test_POST_existing_employee():
    url=base_url+'''employees?name="the new guy"&works_on=2&adress="whatever'''
    response = requests.post(url)
    assert response.status_code == 400, f'got response {response.status_code}, {response.text}'


def test_POST_existing_project():
    url=base_url+'''projects?name="test proj"&begin_date="28-3-2001"&end_date="12-12-2001"'''
    response = requests.post(url)
    assert response.status_code == 400, f'''should be 400, because project "tet proj" already exists'''


def test_POST_new_project():
    url=base_url+'''projects?name="project X"&begin_date="28-3-2001"&end_date="12-12-2001"'''
    response = requests.post(url)
    assert response.status_code == 201, f'''got{response.status_code}, but "temp proj" doesn't exists'''


def test_DELETE_employee():
    url = base_url+'''employees?id=6'''
    response = requests.delete(url)
    assert response.status_code == 200, f'got {response.status_code}, {response.text}'
