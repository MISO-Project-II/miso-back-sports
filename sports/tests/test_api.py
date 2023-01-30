# # test: $ pytest -v
# from flask import Flask
# from . import sports_api_blueprint
# from sports.sports_api.routes import sports
# import json
# from fastapi.testclient import TestClient
# from sports.sports_api import sports_api_blueprint

# # pytest of GET metods

# def test_get_route_sports_fail():
#     app = Flask(__name__)
#     app.register_blueprint(sports_api_blueprint, url_prefix='/sports')
#     rv = app.test_client().get('/sports')
#     assert rv.status == '404 NOT FOUND'

# def test_get_sports():
#     client = TestClient(sports_api_blueprint)
#     response = client.get('/sports')
#     assert response.status_code == 200
#     assert response.json() == {'mesage':'I am alive'}
    
import requests

ENDPOINT = "http://127.0.0.1:7001/sport"

def test_get_call():
    response = requests.get(ENDPOINT + "s")
    assert response.status_code == 200

def test_post_call():
    sports = {
        'name' : "Montañismo",
        'description' : "Deporte de esfuerzo y resistencia"
    }
    response = requests.post("http://127.0.0.1:7001/sport/add", data=sports)
    assert response.status_code == 200
    
    data = response.json()
    print(data)
