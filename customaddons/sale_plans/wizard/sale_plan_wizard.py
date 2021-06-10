# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SalePlanWizard(models.TransientModel):
    _name = 'sale.plan.wizard'
    _description = 'Init Sale Plan'

    name = fields.Char('Name')
    info = fields.Text('Information', required=True)
    quotation_id = fields.Many2one('sale.order', string='Quotation', readonly=True)
    partner_lines = fields.Many2many('res.partner')

    def init_sale_plan_submit(self):
        record = self.env['sale.plan.order'].sudo().create({
            'name': self.name,
            'info': self.info,
            'quotation_id': self.quotation_id.id,
        })
        for partner in self.partner_lines:
            self.env['sale.plan.order.line'].create({
                'sale_plan_id': record.id,
                'partner_id': partner.id
            })
        self.quotation_id.sale_plan = record.id
        return
