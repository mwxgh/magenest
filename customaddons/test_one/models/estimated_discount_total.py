# -*- coding: utf-8 -*-

from odoo import api, fields, models


class EstimatedDiscountTotal(models.Model):
    _inherit = 'sale.order'
    _description = 'Extend with Estimated Discount Total'

    customer_discount_code_sale_order = fields.Char(string='Discount Code', related='partner_id.customer_discount_code')
    check_valid_discount_code_sale_order = fields.Boolean(string='Check Discount Code', store=True, readonly=True, related='partner_id.check_valid_discount_code')
    sale_order_discount_estimated = fields.Monetary(string='Discount Estimated', compute='_discount_estimated')
    final_amount_total = fields.Monetary(string='Final Total', compute='_final_amount_total')

    @api.depends('customer_discount_code_sale_order', 'check_valid_discount_code_sale_order', 'amount_untaxed')
    def _discount_estimated(self):
        for record in self:
            if record.check_valid_discount_code_sale_order:
                discount_code_split = self.customer_discount_code_sale_order.split('_')
                discount_code_num = int(discount_code_split[1])
                record.sale_order_discount_estimated = discount_code_num / 100 * record.amount_untaxed
            else:
                record.sale_order_discount_estimated = 0

    @api.depends('amount_total', 'sale_order_discount_estimated')
    def _final_amount_total(self):
        for record in self:
            record.final_amount_total = record.amount_total - record.sale_order_discount_estimated
