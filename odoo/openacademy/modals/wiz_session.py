from openerp import models, fields, api

class Session(models.TransientModel):
	"""docstring for Session"""
	_name = 'wiz.openacademy.session'

	sessions = fields.One2many('wiz.openacademy.session.data', 'wiz_id')
	different_data = fields.Boolean()

	@api.one
	def add_session(self):
		# print "===================================="
		# import pdb; pdb.set_trace()
		session_obj = self.env['openacademy.session']
		# print session_obj
		for session in self.sessions:
			old_session = session_obj.search([("course", '=', session.course.id), ("start_date", "=", session.date)])
			# print old_session
			if old_session:
				old_session.write({"name":session.name, "description":session.description})
			else:
				value ={
				"name":session.name,
				"course":session.course.id,
				"description":session.description,
				"start_date":session.date

				}
				session_obj.create(value)
			# print "saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
class Sessiondata(models.TransientModel):
	_name = 'wiz.openacademy.session.data'

	wiz_id = fields.Many2one('wiz.openacademy.session')
	name = fields.Char()
	course = fields.Many2one('openacademy.course')
	description = fields.Text()
	date = fields.Date()