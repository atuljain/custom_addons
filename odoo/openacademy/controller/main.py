from openerp import http
from openerp.http import request


class website_openacademy(http.Controller):

	@http.route('/hello/world', auth='public')
	def test_controller(self):
		return "Helo World"

	@http.route('/hello/world2', auth='public')
	def test_controller2(self):
		return "<h1>Helo World</h1>"

	@http.route('/hello/world3', auth='user')
	def test_controller3(self):
		return "<h1>Helo,  %s</h1>"%(request.env.user.name)
	

	@http.route('/static_page', auth='user', website=True)
	def simplae_page(self):
		return request.website.render("openacademy.static_page", {})
		#render_to_response(PAGENAME, CONTEXT)


	@http.route('/dynamic_page', auth='user', website=True)
	def dynamic_page(self):
		context = {'user':request.env.user, 'my_f':self.my_func}
		return request.website.render("openacademy.dynamic_page",  context)
	def my_func(self, name):
		a = 15
		b = 10
		c = 8.5
		d = (a+b*c)/(b+c)
		return d

	@http.route('/openacademy/course/', auth='user', website=True)
	def course(self):
		courses = request.env['openacademy.course'].search([])
		return request.website.render("openacademy.course", {'courses':courses})

	@http.route("/openacademy/course/<model('openacademy.course'):course>", auth='user', website=True)
	def course_detail(self, course):
		return request.website.render("openacademy.course_detail", {'course':course})

	@http.route('/openacademy/snip',auth='user',website=True)
	def course_snip(self):
		course = request.env['openacademy.course'].search([])
		return request.website.render("openacademy.snippet", {'course':course})
