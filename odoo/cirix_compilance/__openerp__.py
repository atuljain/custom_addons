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

{
    'name': 'CIRIX Compilance Module',
    'category': 'Custom Module',
    'version': '0.1',
    'author': 'NetbeamERP<info@netbeam.in>',
    'depends': ['hr'],
    'sequence': 1,
    'description': """
Openerp changes for CIRIX.
""",
    'data': [
             'hr_compilance_view.xml',
             'security/hr_compilance_security.xml'
#        'base/res_partner_view.xml',
 #       'project/project_view.xml',
 #       'account/invoice_report.xml'
        
    ],
    "installable": True,

}
