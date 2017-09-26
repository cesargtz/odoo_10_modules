# -*- coding: utf-8 -*-

{
    'name': 'Farm',
    'version': '10.0',
    'author': 'QX UNIT DE MÉXICO SA DE CV',
    'website': 'http://www.qxunit.com.mx',
    'depends': ['purchase', 'purchase_contract_type'],
    'data': [
        'security/farm_access_rules.xml',
        'security/ir.model.access.csv',
        'views/farm.xml',
        'views/farm_purchase.xml',
        'views/axc_contract.xml',
    ]
}
