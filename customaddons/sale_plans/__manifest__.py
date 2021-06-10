# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Approving the Sales Plan',
    'version': '1.1',
    'summary': 'Task 4 for Internship',
    'sequence': 10,
    'description': """
     complete or not
    ==============
    of course . complete !!!
    """,
    'category': 'Uncategorized',
    'website': '#',
    'depends': [
        'sale'
    ],
    'data': [
        'wizard/sale_plan_wizard.xml',
        'views/sale_order_sale_plan_view.xml',
        'views/sale_plan_view.xml',
        'security/ir.model.access.csv',
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
