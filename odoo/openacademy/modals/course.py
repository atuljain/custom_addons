from openerp import models, fields, api, _

class Course(models.Model):
# _name is using for define modal name , this will create table in database , table name will be openacademy_course
	_name = 'openacademy.course'
# field define here 
	# _rec_name = {'name'} 
	name = fields.Char(string='Title', required=True)
	image = fields.Binary()
	description = fields.Text()
	html = fields.Html()
	duration = fields.Integer()
	responsible = fields.Many2one('res.users')#In many2one case always name field will be call, if we need to call other field then add that field in _rec_name  
	sessions = fields.One2many('openacademy.session', 'course', copy=False)
	
	@api.model
	def create(self, values):
		#  values = {'name':'ODOO-8.0', 
		# 		   'duration': 10
		# 			}
		# import pdb; pdb.set_trace()
		return super(Course, self).create(values)
		# create({'name': 'python'})
	@api.multi
	def write(self,values):
		return super(Course, self).write(values)

	@api.multi
	def unlink(self):
		return super(Course, self).unlink()

	@api.one
	def copy(self, default):
		default['name'] = self.name + "(copy of)"
		return super(Course, self).copy(default)