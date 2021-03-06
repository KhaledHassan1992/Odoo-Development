{
    'name': "Earn Leaves Management",
    'version': '10.0.0.0',
    'author': "Metamorphosis",
    'category': 'Extra Tools',
    'summary':'Module for managing the Annual/Earn Leaves Request',
    'maintainer':'Metamorphosis',
    'website':'metamorphosis.com',
    'sequence':'-1',
    'license': 'AGPL-3',
    'depends': ['mail','base','hr_holidays','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_inherited_view.xml',
        'views/annual_leave_assign.xml',
        'data/data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
