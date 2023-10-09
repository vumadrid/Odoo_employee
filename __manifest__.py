# -*- coding: utf-8 -*-
{
    'name': "Ev-employee",

    'summary': """
       Employee-company""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'web'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/id_view.xml",
        "views/id_department.xml",
        "views/id_features.xml",
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
