# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Product Warranty',
    'version': '1.1',
    'summary': 'Task 2.1 for Internship',
    'sequence': 10,
    'description': """
    complete or not
    ==============
    of course . complete !!!
    """,
    'category': 'Uncategorized',
    'website': '#',
    'depends': ['base', 'product', 'sale_management'],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'views/custom_product_warranty.xml',
        'views/discount_with_warranty.xml',
        'views/filter_valid_product_warranty.xml',
        'wizard/update_custom_product_warranty.xml',
        'views/template.xml',
    ],
    'demo': [
    ],
    #   'qweb': [
    #      "static/src/xml/account_payment.xml",
    #  ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
