from flask import Blueprint
from .views import *

# router register blueprint
appointment_router = Blueprint('appointments_api', __name__)

# register urls
appointment_router.add_url_rule('/getAppointments/', view_func=appointment_views, methods=['GET'])
