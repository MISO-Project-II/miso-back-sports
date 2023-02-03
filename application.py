from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, Blueprint
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_migrate import Migrate

db = SQLAlchemy()


class Sports(db.Model):
    idsports = db.Column(db.Integer, primary_key=True)
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


def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@0.0.0.0:5432/db_sportapp'
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
