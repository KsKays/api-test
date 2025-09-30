import requests

BASE_URL = "https://68db59ff23ebc87faa32ae80.mockapi.io/api_test/users";

def test_create_user():
    response = requests.post(f"{BASE_URL}", json={'name': 'Thirayut'})
    assert response.status_code == 201
    response_data = response.json()
    assert 'id' in response_data
    assert response_data['id'] == '31'
    assert response_data['name'] == 'Thirayut'

def test_get_user():
    # Get the created user
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200
   
    # Now process the response
    response_data = response.json()
   
    assert response_data[0]['name'] == 'Mr. Forrest Weber'
    assert response_data[0]['id'] == '1'

def test_delete_user():
    user_id = 29
    # Delete the created user
    response = requests.delete(f"{BASE_URL}/{user_id}")
    assert response.status_code == 200

    # Try to get the deleted user
    # response = requests.get(f"{BASE_URL}/users/{user_id}")
    # assert response.status_code == 404
    # assert response.json()['error'] == 'User not found'