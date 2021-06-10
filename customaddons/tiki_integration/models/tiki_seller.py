import requests
from odoo.exceptions import UserError, ValidationError
from odoo import fields, models, api


class TikiSeller(models.Model):
    _name = "tiki.seller"
    _description = "Seller"

    seller_id = fields.Char('Seller ID')
    code = fields.Char('Code')
    contract_code = fields.Char('Contact Code')
    name = fields.Char('Name')
    logo = fields.Char('Logo')
    hotline = fields.Char('Hotline')
    email = fields.Char('Email')
    connect_to = fields.Char('Connect to')
    secret = fields.Char('Secret')

    def get_seller_tiki(self):
        url = "https://api-sellercenter.tiki.vn/integration/sellers"
        payload = {}
        # tiki_seller.secret
        headers = {
            'tiki-api': 'a3a041f4-9420-45ca-8bef-4abe1eb5bdd0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        seller = response.json()
        val = {}

        if ('id' and 'name' and 'code' and 'contract_code' and 'secret' and 'email' and 'connect_to' and 'logo') in seller:
            val['seller_id'] = seller['id']
            val['name'] = seller['name']
            val['code'] = seller['code']
            val['contract_code'] = seller['contract_code']
            val['secret'] = seller['secret']
            val['email'] = seller['email']
            val['connect_to'] = seller['connect_to']
            val['logo'] = seller['logo']
        existed_seller = self.env['tiki.seller'].search([('seller_id', '=', seller['id'])], limit=1)
        if len(existed_seller) < 1:
            self.create(val)
        else:
            existed_seller.write(val)
