from odoo import fields, models, api


class TikiSellerProduct(models.Model):
    _name = "tiki.seller.product"
    _description = "Seller Product"

    id = fields.Integer('Product ID')
    sku = fields.Integer('SKU')
    name = fields.Char('Product Name')
    master_id = fields.Integer('Master ID', nullable=True)
    super_id = fields.Integer('Super ID')
    min_code = fields.Integer('Min Code')
    seller_product_code = fields.Char('Seller Product Code')
    productset_id = fields.Integer('Product Set ID')
    type = fields.Char('Type')
    status = fields.Integer('Status')
    visibility = fields.Integer('Visibility')
    availability = fields.Integer('Availability')
    price = fields.Float('Price')
    list_price = fields.Float('List Price')
    thumbnail = fields.Char('Thumbnail')
    images = fields.Many2many(comodel_name='tiki.product.image', string='Product Images')
    categories = fields.Many2many(comodel_name='tiki.categories', string='Product Categories')
    # configurable_attributes = fields.Char('Configurable Attributes')