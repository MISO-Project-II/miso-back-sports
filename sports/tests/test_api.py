import requests

ENDPOINT = "http://127.0.0.1:7001/sport"

def test_get_call():
    response = requests.get(ENDPOINT + "s")
    assert response.status_code == 200

def test_post_call():
    sports = {
        'name' : "Test",
        'description' : "Descripcion Test"
    }
    response = requests.post("http://127.0.0.1:7001/sport/add", data=sports)
    assert response.status_code == 200
    
    data = response.json()
    print(data)
