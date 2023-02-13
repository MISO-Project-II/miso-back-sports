import json

from apiflask import APIFlask, Schema
from apiflask.fields import String
from flask import Flask, jsonify, request, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = APIFlask(__name__, spec_path='/openapi.yaml')
app.config['SPEC_FORMAT'] = 'yaml'
import json

db = SQLAlchemy()


class SportOut(Schema):
    name = String()
    description = String()


class Sports(db.Model):
    idsports = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)

    def to_json(self):
        return {
            'idsports': self.idsports,
            'name': self.name,
            'description': self.description
        }


class SportSchema(SQLAlchemyAutoSchema):
    class meta:
        model = Sports
        load_instance = True


sport_schema = SportSchema()

sports_api_blueprint = Blueprint('sports_api', __name__)


# @app.get('/sports')
# @sports_api_blueprint.route('/sports', methods=['GET'])
# def sports():
#     sports = []
#     for row in Sports.query.all():
#         sports.append(row.to_json())
#
#     response = jsonify({'message': 'success',
#                         'success': True,
#                         'result': sports
#                         })
#     return response


@sports_api_blueprint.route('/sports', methods=['GET', 'POST'])
def add_sport():
    if request.method == 'POST':
        sport = Sports()
        req_data = request.get_json()
        sport.name = req_data['name']
        sport.description = req_data['description']
        try:
            db.session.add(sport)
            db.session.commit()
        except Exception as e:
            response = jsonify({'message': 'Error data exits',
                                'success': False,
                                'result': req_data
                                })
            return response
        response = jsonify({'message': 'success',
                            'success': True,
                            'result': req_data
                            })
        return response
    elif request.method == 'GET':

        sports = []
        for row in Sports.query.all():
            sports.append(row.to_json())
        response = jsonify({'message': 'success',
                            'success': True,
                            'result': sports
                            })
        return response




def create_app():
    Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    application = app
    application.config['SPEC_FORMAT'] = 'yaml'
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/db_sportapp'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(application)
    with application.app_context():
        application.register_blueprint(sports_api_blueprint)
        db.init_app(application)
        db.create_all()
        return application


application = create_app()
migrate = Migrate(application, db)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
