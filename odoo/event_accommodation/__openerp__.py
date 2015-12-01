{
    'name' : 'Event Accommodation',
    'version': '1.0',
    'author': 'Event Accommodation',
    'category': 'Hidden',
    'description': "",
    'depends': ['event', 'website_event'],
    'data': [
        'views/accommodation.xml',
		'event_accommodation_view.xml',
        'data/accommodation_data.xml',
		'report/report_event_accommodation_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
