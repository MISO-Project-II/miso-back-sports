# test: $ pytest -v
from flask import Flask
from . import sports_api_blueprint
from sports.sports_api.routes import sports
import json

# pytest of GET metods

def test_get_route_sports_success():
    app = Flask(__name__)
    app.register_blueprint(sports_api_blueprint, url_prefix='/sports')
    
    rv = app.test_client().get('/sports')
    
    assert rv.status == '200 OK'
