# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SalePlanExtend(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Plan'

    sale_plan = fields.Many2one('sale.plan.order', string='Sale Plan')

    def init_sale_plan(self):
        return {
            'name': _("Add Sale Plan"),
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'sale.plan.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_quotation_id': self.id}
        }

        ######## other way ###########
        # return self.env['ir.actions.act_window']._for_xml_id("sale_plans.sale_plan_wizard_act_window")

class SalePlanOrder(models.Model):
    _name = 'sale.plan.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sale Plan Order'

    name = fields.Char('Name', required=True)
    quotation_id = fields.Many2one('sale.order', string='Quotation', readonly=True, ondelete='cascade')
    info = fields.Text('Information', required=True, tracking=True)
    sent = fields.Boolean(string='Sent or not', default=False)
    edited = fields.Boolean(string='Edited or not', default=False)
    sale_plan_line_id = fields.Many2one('sale.plan.order.line', string='Censor')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('approved', 'Approved'),
        ('refused', 'Refused')], 'Status', default="draft", compute='_check_status', tracking=True)
    partner_lines = fields.One2many('sale.plan.order.line', 'sale_plan_id', tracking=True)

    def send_plan(self):
        self.sent = True
        if self.edited == False:
            message = _(
                "Plan %(name)s for quotation %(quotation_id)s was created",
                name=self.name,
                quotation_id=self.quotation_id.name
            )
        else:
            message = _(
                "Plan %(name)s for quotation %(quotation_id)s was edited.",
                name=self.name,
                quotation_id=self.quotation_id.name
            )
        self.message_post(body=message, subject='Plan to you', partner_ids=self.partner_lines.partner_id.ids)

    def _check_status(self):
        partner_num = len(self.partner_lines)
        approve_num = 0
        refuse_num = 0
        for partner in self.partner_lines:
            if partner.status == 'approved':
                approve_num += 1
            if partner.status == 'refused':
                refuse_num += 1
        if approve_num == partner_num and partner_num != 0:
            self.state = 'approved'
        elif refuse_num != 0:
            self.state = 'refused'
        else:
            if self.sent == True:
                self.state = 'sent'
            else:
                self.state = 'draft'

    @api.onchange('name', 'info', 'partner_lines')
    def _change_state_when_edited(self):
        self.state = 'draft'
        self.sent = False
        self.edited = True


class SalePlanOrderLine(models.Model):
    _name = 'sale.plan.order.line'
    _description = 'Sale Plan Order'

    sale_plan_id = fields.Many2one('sale.plan.order', string='Sale Plan', ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Censor')
    status = fields.Selection(string='Status', selection=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
    ], required=True, default='pending')
    is_current_user = fields.Boolean(default=False, compute='_check_current_user')

    def _check_current_user(self):
        for rec in self:
            if rec.env.user.partner_id.id == rec.partner_id.id:
                rec.is_current_user = True
            else:
                rec.is_current_user = False

    def check_approve(self):
        self.status = 'approved'
        message = _(
            "%(partner_name)s approved the plan %(plan_name)s.",
            partner_name=self.partner_id.display_name,
            plan_name=self.sale_plan_id.name
        )
        self.sale_plan_id.message_post(body=message, subject='Plan Approving',
                                       partner_ids=self.sale_plan_id.create_uid.partner_id.ids)

    def check_refuse(self):
        self.status = 'refused'
        message = _(
            "%(partner_name)s refused the plan %(plan_name)s.",
            partner_name=self.partner_id.display_name,
            plan_name=self.sale_plan_id.name,
        )
        self.sale_plan_id.message_post(body=message, subject='Plan Refusing',
                                       partner_ids=self.sale_plan_id.create_uid.partner_id.ids)
