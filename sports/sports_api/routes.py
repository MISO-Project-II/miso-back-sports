from . import sports_api_blueprint
from .. import db
from .. models import Sports
from flask import jsonify, request

# Sports

@sports_api_blueprint.route('/sports', methods=['GET'])
def sports():
    sports = []
    for row in Sports.query.all():
        sports.append(row.to_json())
        
    response = jsonify({'results': sports})
    return response

@sports_api_blueprint.route('/sport/add', methods=['POST'])
def add_sport():
    sport = Sports()
    sport.name = request.form['name']
    sport.description = request.form['description']
    
    db.session.add(sport)
    db.session.commit()
    
    response = jsonify({'message': 'Sport Added', 'sport': sport.to_json()})
    return response



    