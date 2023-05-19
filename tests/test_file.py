import pytest
from app import create_app
import csv


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/home')
    assert response.status_code == 200


def test_login(client):
    # Test GET request
    response = client.get('/login')
    assert response.status_code == 200

    # Test POST request with 6-digit input
    response = client.post(
        '/login', data={'loginInput': '123456', 'password': 'password'})
    assert response.status_code == 302  # status code 302 for redirect

    # Test POST request with email-like input
    response = client.post(
        '/login', data={'loginInput': 'test@example.com', 'password': 'password'})
    assert response.status_code == 302

    # Test POST request with invalid input
    response = client.post(
        '/login', data={'loginInput': 'invalid', 'password': 'password'})
    assert response.status_code == 302


def test_user_profile(client):
    # Test GET request
    response = client.get('/userprofile')
    assert response.status_code == 200

    # Test POST request
    # Providing random inputs for test
    response = client.post(
        '/userprofile',
        data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890'
        }
    )

    assert response.status_code == 302

    # Verify that the data was written to the file
    with open('guests.csv', mode='r') as file:
        reader = csv.reader(file)
        last_line = list(reader)[-1]
        assert last_line[0] == 'johndoe@example.com'

    # Test POST request with missing parameters
    response = client.post('/userprofile', data={'first_name': 'Jane'})
    assert response.status_code == 302
