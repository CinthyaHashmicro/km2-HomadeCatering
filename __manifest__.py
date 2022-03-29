# -*- coding: utf-8 -*-
{
    'name': "HomadeCatering",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application' : True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/protein_views.xml',
        'views/lauk_views.xml',
        'views/karbohidrat_views.xml',
        'views/tambahan_views.xml',
        'views/aksesoris_views.xml',
        'views/kotak_views.xml',
        'views/package_views.xml',
        'views/paket_views.xml',
        'views/order_views.xml',
        'views/staff_views.xml',
        'views/customer_views.xml',
        'views/pengiriman_views.xml',
        'report/report.xml',
        'report/order_report.xml',
        'views/akunting_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
