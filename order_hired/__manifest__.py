# -*- coding: utf-8 -*-
{
    'name': "order_hired",

    'description': """
        Added in the view of type list one column with the total tons hired
    """,

    'author': "Yecora",
    'website': "http://www.yecora.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        'views/order_hired.xml'
    ],

}
