from flask.views import MethodView

class BookingView(MethodView):

	def get(self):
		return '{"result" : "bookings goes here"}'

	def post(self):
		return '{"result" : "post booking"}'

booking_views = BookingView.as_view('bookings')


def admin_bookings():
    return '{"result":"more summer wines"}'

