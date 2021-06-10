# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _


class TikiImage(models.Model):
    _name = "tiki.product.images"
    _description = "Images"

    id = fields.Integer('ID Image')
    path = fields.Text('Image Path')
    position = fields.Integer('Position')
    is_gallery = fields.Integer('Gallery')
    is_default = fields.Integer('Default')
    is_disable = fields.Integer('Disable')
    is_new = fields.Boolean('New')
    is_info = fields.Boolean('Info')
    width = fields.Float('Width')
    height = fields.Float('Height')
