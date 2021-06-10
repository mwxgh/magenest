# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Order Force Code',
    'version': '1.1',
    'summary': 'Task 1.1 for Internship',
    'sequence': 10,
    'description': """
    complete or not
    ==============
    of course . complete !!!
    """,
    'category': 'Sale',
    'website': '#',
    'depends': ['sale','base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/assets_backend.xml',
        'views/customer_discount_code.xml',
        'views/estimated_discount_total.xml',
        'views/filter_valid_customer_discount_code.xml',
        'views/templates.xml',
        'wizard/update_customer_discount_code.xml',

    ],
    'demo': [
    ],
    # 'qweb': [
    #     "static/src/xml/account_payment.xml",
    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
