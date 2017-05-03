# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class CustomerLevel(models.Model):

    _name = 'crm_key_customer.customer_level'
    _description = 'Customer Level'

    def get_partner_count(self):
        ''' Loop through each customer level, calculate how many customer it has,
        and show the numeric value '''
        for level in self:
            number_of_partners = len(level.partner_ids)
            level.partner_count = number_of_partners

    name = fields.Char('Level name', help='''E.g. bronze, silver...''')
    description = fields.Text('Level description')
    partner_ids = fields.One2many('res.partner', 'customer_level_id', 'Customers', help='''Customers that are on this level''')
    partner_count = fields.Integer(compute='get_partner_count', string='Number of Customers')
