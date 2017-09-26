# -*- coding: utf-8 -*-
{
    'name': "account_invoice_tons",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
		'base',
		'account',
        'sale',
     
		],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    'views/account_invoice_tons.xml',
	'views/account_invoice_supplier_tons.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
