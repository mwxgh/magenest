# -*- coding: utf-8 -*-

from odoo import api, fields, models


class UpdateCustomerCode(models.TransientModel):
    _name = 'update.custom.product.warranty'
    _description = 'Mass Update Product Warranty'

    product_warranty = fields.Text(string="Product Warranty Code", readonly=True, compute='update')
    date_stop = fields.Date(string='Date To')
    date_start = fields.Date(string='Date From')

    @api.depends('date_start', 'date_stop')
    def update(self):
        date_stop = self.date_stop
        date_start = self.date_start
        if date_start and date_stop:
            date_stop = date_stop.strftime('%d%m%-y')
            date_start = date_start.strftime('%d%m%-y')
        else:
            self.product_warranty = ''
        lists = self.env['product.template'].browse(self._context['active_ids'])
        for rec in lists:
            rec.date_stop = self.date_stop
            rec.date_start = self.date_start
            rec.product_warranty = self.product_warranty
            if date_start and date_stop:
                self.product_warranty = 'PWR/' + str(date_stop) + '/' + str(date_start)
            else:
                self.product_warranty = ''

