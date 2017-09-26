# -*- coding: utf-8 -*-
{
    'name': 'Waterhole',
    'version': '10.0',
    'author': 'QX UNIT DE MÉXICO SA DE CV',
    'website': 'http://www.qxunit.com.mx',
    'depends': ['purchase', 'purchase_contract_type'],
    'data': [
        'security/waterhole_access_rules.xml',
        'security/ir.model.access.csv',
        'views/waterhole.xml',
        "views/purchase_waterhole.xml",
    ]
}
