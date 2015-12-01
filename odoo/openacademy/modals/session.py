from openerp import models, fields, api, _
from openerp.exceptions import Warning
class Session(models.Model):
	_name = 'openacademy.session'
	_inherit = ['mail.thread','ir.needaction_mixin']

	name = fields.Char(required=True)
	state = fields.Selection([('draft','Draft'),('confirm', 'Confirm'),('cancel','Cancel'),('done','Done')], required=True,default='draft')
	duration = fields.Float()
	seats=fields.Integer()
	start_date = fields.Date()
	active = fields.Boolean(default=True)
	description = fields.Text()
	course = fields.Many2one('openacademy.course')
	instructor = fields.Many2one('res.partner')
	attendees = fields.Many2many('res.partner')
	course_info = fields.Text(related="course.description")
	occupation = fields.Float(compute="calculate_occupation")
	color = fields.Integer('Color Index')
	# upper = fields.Char(compute='_compute_upper', inverse='_inverse_upper')

	# @api.depends('name')
	# def _compute_upper(self):
	# 	for rec in self:
	# 		rec.upper = rec.name.upper() if rec.name else False
	# def _inverse_upper(self):
	# 	for rec in self:
	# 		rec.upper = rec.name.upper() if rec.name else False

	@api.multi
	@api.depends('seats','attendees')
	def calculate_occupation(self):
		for rec in self:
			if rec.seats:
				rec.occupation = len(rec.attendees)*100/rec.seats
			else:
				rec.occupation = 0

	@api.onchange('course')
	def onchnage_course(self):
		if self.course and not self.name:
			self.name = self.course.name + 'Session'

	@api.constrains('attendees', 'instructor')
	def attendess_constrains(self):
		if self.instructor.id in self.attendees.ids:
			raise Warning('you can not add instructor as a attendee')


	@api.one
	def do_confirm(self):
		self.state = 'confirm'

	@api.one
	def do_done(self):
		self.state = 'done'
	
	@api.one
	def do_cancel(self):
		self.state = 'cancel'
	
	@api.one
	def do_reset(self):
		self.state = 'draft'
	@api.one
	def do_delay(self):
		self.state == 'draft'

	# @api.one
	# def _needaction_domain_get(self):
	# 	return [('state', '=', 'draft')]

	# def _needaction_domain_get(self, cr, uid, context=None):

	# 	valueTest = [('state', '=', 'draft')] 
 #        return valueTest


	# def calculate(self,cr,uid,seats,attandees):



