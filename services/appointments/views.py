from flask.views import MethodView

__all__ = ['stuffview']

class StuffView(MethodView):

	def get(self):
		return '{"result" : "get goes here"}'

	def post(self):
		return '{"result" : "post"}'

stuffview = StuffView.as_view('stuff_views')
