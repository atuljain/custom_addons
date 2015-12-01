
{
	'name': 'openacademy',
	'category': 'Training',
	'version':"1.0",
	'author':"test",
	'depends':['base','sale', 'mail'],
	'sequence':1,
	'description': """
Open Academy module for managing trainings:
 - training courses
 - training sessions
 - attendee registration
""",
	'data':[
		'security/opeacademy_security.xml',
		'security/ir.model.access.csv',
		'views/menu.xml',
		'views/course_view.xml',
		'views/session_view.xml',
		'views/sales_view_inherit.xml',
		'views/wiz_session.xml',
		'report/report_session.xml',
		'views/sessioni_workflow.xml',
		'views/dashboard.xml',
		'views/webpage_template.xml',
		'views/snippet.xml'

	],
	'installable':True,
	'auto_install':False

}
