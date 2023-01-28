from flask import Blueprint

sports_api_blueprint = Blueprint('sports_api', __name__)

from . import routes
