# -*- coding: utf-8 -*-
import re

from odoo import api, fields, models


class CustomerDiscountCode(models.Model):
    _inherit = 'res.partner'
    _description = 'Extend with Customer Discount Code'

    customer_discount_code = fields.Char(string='Discount Code', default='VIP_')
    check_valid_discount_code = fields.Boolean(string='Check Discount Code', compute='_check_valid_customer_discount_code', store= True)

    @api.depends('customer_discount_code')
    def _check_valid_customer_discount_code(self):
        for record in self:
            if record.customer_discount_code:
                if re.match("^VIP_([1-9]|[1-9][0-9]|0[1-9])$", record.customer_discount_code):
                    record.check_valid_discount_code = True
                else:
                    record.check_valid_discount_code = False
            else:
                record.check_valid_discount_code = False
