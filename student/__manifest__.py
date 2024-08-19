{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage students, courses, and payments',
    'sequence': 10,
    'description': 'A module to manage students, courses, and payments for a learning center',
    'category': 'Education',
    'author': 'Mr Uzdev',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/student_menus.xml',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/teacher_views.xml',
        'views/group_views.xml',
        'views/payment_views.xml',
        'views/payment_sequence.xml',
        'views/teacher_payment_views.xml',
        'views/account_move_views.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
