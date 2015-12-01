
{
	'name': 'Procurement hide and restrict Partner',
	'category': 'Sales General',
	'version':"1.0",
	'author':"Atul Jain<jain.atul43@gmail.com>",
	'website': "https://github.com/atuljain",
	'depends':['base','sale', 'product'],
	'sequence':1,
	'description': """
	Hide some field for particular group
This module will hide procurement tab for particular user group, 
Users with group "Sale - Own Leads" can only see partners that are assigned to him or partners assigned to no one.
""",
	'data':[
		'product.xml',
		'security/security.xml'

	],
	'installable':True,
	'auto_install':False

}














# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


