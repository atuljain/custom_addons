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
    'name': 'Aardug Reports Template',
    'category': 'Custom Report Module',
    'version': '0.1',
    'author': 'Atul Jain<info@netbeam.in>',
    'depends': ['account', 'stock'],
    'sequence': 1,
    'description': """
Changes in Reports Template 
""",
    'data': [
        'invoice/view/report_invoice.xml',
        'invoice/account_report.xml',
        'packingslip/views/report_stockpicking.xml',
        'packingslip/stock_report.xml',
        'purchase/purchase_order.xml',
        'purchase/view/report_purchaseorder_new.xml'
        
        
    ],
    "installable": True,

}
