# -*- coding: utf-8 -*-

from odoo import api, fields, models


class UpdateCustomerCode(models.TransientModel):
    _name = 'update.customer.code'
    _description = 'Mass Update Customer Code'

    customer_discount_code = fields.Char(string='Discount Code', default='VIP_')

    def update(self):
        code = self.env['res.partner'].browse(self._context['active_ids'])
        for record in code:
            record.customer_discount_code = self.customer_discount_code
