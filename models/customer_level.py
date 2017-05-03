# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class CustomerLevel(models.Model):

    _name = 'crm_key_customer.customer_level'
    _description = 'Customer Level'

    name = fields.Char('Level name', help='''E.g. bronze, silver...''')
    description = fields.Text('Level description')
