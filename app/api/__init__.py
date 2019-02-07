from flask import Blueprint 
from flask_restful import Api,Resource
from app.api.v1.view.office_views import Offices,Office
from app.api.v1.view.party_views  import Parties,Party

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)

api.add_resource (Offices, '/offices')
api.add_resource (Office, '/offices/<int:office_id>')
api.add_resource (Parties, '/parties')
api.add_resource (Party, '/parties/<int:party_id>')

