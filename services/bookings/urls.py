from flask import Blueprint
from .views import booking_views, admin_bookings

# router register blueprint
bookings_router = Blueprint('bookings_api', __name__)

# register urls
bookings_router.add_url_rule('/getBookings/', view_func=booking_views, methods=['GET', 'POST'])
bookings_router.add_url_rule('/adminBookings/', view_func=admin_bookings, methods=['GET'])
