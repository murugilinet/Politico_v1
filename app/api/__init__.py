from flask import Blueprint 
from flask_restful import Api,Resource
from app.api.v1.view.office_views import Offices

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)

api.add_resource(Offices, '/offices')  
