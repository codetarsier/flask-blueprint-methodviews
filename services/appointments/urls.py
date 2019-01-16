from flask import Blueprint
from .views import *

# router register blueprint
appointment_router = Blueprint('appointments_api', __name__)

# register urls
appointment_router.add_url_rule('/getStuff', view_func=stuffview, methods=['GET'])
