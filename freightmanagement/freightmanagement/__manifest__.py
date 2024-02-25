
{
    'name': 'Freight Management',
    'version': '1.0',
    'summary': 'Freight Management',
    'description': 'Freight Management',
    'author': 'CA',
    'company': 'Group X',
    'website': 'https://test.com/',
    'depends': ['prt_report_attachment_preview', 'base', 'product', 'account', 'muk_web_theme'],
    'images': ['static/description/banner.png',
                'static/description/icon.png',],
    'data': [
        'security/ir.model.access.csv',
        'data/freight_order_data.xml',
        'views/freight_order.xml',
        'views/freight_port.xml',
        'views/freight_container.xml',
        'views/custom_clearance.xml',
        'views/order_track.xml',
        'report/report_order.xml',
        'report/report_tracking.xml',
        'wizard/custom_revision.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
