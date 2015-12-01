# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2013-Present NetbeamERP Technology (www.netbeam.in).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _
#from openerp.osv import fields, osv
#import time
#from openerp.tools.translate import _
#from datetime import datetime

class hr_compilance(models.Model):
    _name = 'hr.compilance'
  #  _inherit = "ir.attachment"
    
    name = fields.Char('Title')
    department = fields.Many2one('hr.department', string='Department')
    attachments = fields.Many2many('ir.attachment')
    description = fields.Text('Description')
   # _columns = {
#                'name':fields.char('Title'),
 #               'department':fields.many2one('hr.department', 'Department'),
  #              'attachments':fields.many2many('ir.attachment', 'Attachments'),
   #             'description':fields.text('Description')
    #            }
    