# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    is_key_customer = fields.Boolean('Key customer', help='''Indicates that the partner is a key customer''')
