from flask import Flask
from services.appointments.urls import appointment_router
from services.bookings.urls import bookings_router

app = Flask(__name__)

# register all internal app blueprints
app.register_blueprint(appointment_router,  url_prefix='/api/v2/')
app.register_blueprint(bookings_router,  url_prefix='/api/v2/')
