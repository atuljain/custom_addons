from openerp import models, fields, api, _

class Sale(models.Model):

	_inherit = 'sale.order'

	extra = fields.Char()
	# create_course = fields.Boolean('Creat Course')
	course_name = fields.Many2one('openacademy.course')
	# responsible = fields.Text(related="course_name.responsible")


	# @api.model
	# def create(self, values):
	# 	if self.create_course:
	# 		course_obj = self.course_name
	# 		