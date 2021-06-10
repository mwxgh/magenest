import requests
from odoo import fields, models, api


class TikiCategories(models.Model):
    _name = "tiki.categories"
    _description = "Categories"

    category_id = fields.Char('Category ID')
    name = fields.Char('Name')
    status = fields.Char('Status')
    is_primary = fields.Boolean('Primary')
    parent_id = fields.Char('Parent ID')

    # url_key = fields.Char('URL Key')
    # path = fields.Char('Path')
    # level = fields.Integer('Level')
    # include_in_menu = fields.Integer('Include in Menu')
    # typical_product = fields.Boolean('Typical Product')
    # is_default = fields.Boolean('Default')
    # position = fields.Integer('Position')
    # is_document_required = fields.Boolean('Document Required')

    def get_categories_tiki(self):
        url = "https://api-sellercenter.tiki.vn/integration/categories"
        payload = {}

        # 'parent_id': '1'
        # tiki_seller.secret

        headers = {
            'tiki-api': 'a3a041f4-9420-45ca-8bef-4abe1eb5bdd0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        categories = response.json()
        val = {}

        for cate in categories:
            if ('id' and 'name' and 'status' and 'is_primary') in cate:
                val['category_id'] = cate['id']
                val['name'] = cate['name']
                val['status'] = cate['status']
                val['is_primary'] = cate['is_primary']

            existed_category = self.env['tiki.categories'].search([('category_id', '=', cate['id'])], limit=1)
            if len(existed_category) < 1:
                self.create(val)
            else:
                existed_category.write(val)
