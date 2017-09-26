# -*- coding: utf-8 -*-
{
    'name': "truck_transfer",

    'summary': """
     Truck Transfer in locations  
     """,

    'description': """
       This module complete to tuck_internal
    """,

    'author': "Yecora",
    'website': "http://www.yecora.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'warehouse',
    'version': '10.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
		'vehicle',
		'stock'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	    #'views/truck_transfer.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
