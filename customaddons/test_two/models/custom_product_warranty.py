# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo.exceptions import ValidationError

from odoo import models, fields, api
from datetime import datetime, date


class ProductWarranty(models.Model):
    _inherit = 'product.template'
    _description = 'Extend Product with Warranty Date'

    product_warranty = fields.Char(string='Warranty Code', readonly=True, compute='_create_product_warranty')
    date_start = fields.Date(string='Date Start')
    date_stop = fields.Date(string='Date Stop')
    warranty_interval = fields.Char(string="Warranty Interval", compute='_check_warranty')
    check_valid_warranty = fields.Boolean(string='Check Valid Warranty')

    @api.depends('date_start', 'date_stop')
    def _create_product_warranty(self):
        for record in self:
            date_start = record.date_start
            date_stop = record.date_stop
            if date_start and date_stop:
                date_stop = date_stop.strftime('%d%m%-y')
                date_start = date_start.strftime('%d%m%-y')
                record.product_warranty = 'PWR/' + str(date_stop) + '/' + str(date_start)
                record.check_valid_warranty = True
            else:
                record.product_warranty = ''

    @api.constrains('date_start', 'date_stop')
    def check_date(self):
        for record in self:
            if record.date_stop and record.date_start:
                if record.date_stop < record.date_start:
                    raise ValidationError('Date Stop Warranty is smaller than Date Start Warranty.')

    @api.depends('date_start')
    def _check_warranty(self):
        current_date = datetime.today().date()
        for record in self:
            date_to = record.date_stop
            count_days = ''
            if record.date_stop:
                if current_date < record.date_stop:
                    date_stop = datetime.strptime(str(record.date_stop), "%Y-%m-%d").date()
                    rd = relativedelta(date_to, current_date)
                    if rd.years == 0 and rd.months == 0:
                        count_days = str(rd.days) + " " + "day(s)"
                    elif rd.years == 0 and rd.months != 0:
                        count_days = str(rd.months) + " " + "month(s)" + " " + str(rd.days) + "day(s)"
                    elif rd.years != 0 and rd.months == 0:
                        count_days = str(rd.years) + " " + "year(s)" + " " + str(rd.days) + "day(s)"
                    elif rd.years != 0 and rd.months != 0 and rd.days != 0:
                        count_days = str(rd.years) + " " + "year(s)" + " " + str(rd.months) + "month(s)" + " " + str(
                            rd.days) + "day(s)"
                    else:
                        record.warranty_interval = 'out of warranty'
                record.warranty_interval = count_days
            else:
                record.warranty_interval = 'no warranty'
