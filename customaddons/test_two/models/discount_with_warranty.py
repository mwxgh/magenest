# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DiscountWarranty(models.Model):
    _inherit = 'sale.order'
    _description = 'Discount with Warranty'

    discount_with_warranty = fields.Monetary(string='Discount Warranty', readonly=True,
                                             store=True, compute='_discount_total_with_warranty')

    @api.depends('order_line')
    def _discount_total_with_warranty(self):
        for rec in self:
            estimated_total = 0.0
            for line in rec.order_line:
                estimated_total += line.product_price
            rec.update({'discount_with_warranty': estimated_total})


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    product_price = fields.Monetary(string='Product Price', compute='calculate_price')

    @api.onchange('price_subtotal')
    def calculate_price(self):
        for order in self:
            if order.product_id:
                if not order.product_id.product_warranty:
                    order.product_price = order.price_subtotal * 0.9
                else:
                    order.product_price = order.price_subtotal
