from flask.views import MethodView

class AppointmentView(MethodView):

	def get(self):
		return '{"result" : "appointments goes here"}'

	def post(self):
		return '{"result" : "post"}'

appointment_views = AppointmentView.as_view('appointment_views')
