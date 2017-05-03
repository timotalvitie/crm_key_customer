# -*- coding: utf-8 -*-
from openerp import api, fields, models, _
from openerp.exceptions import Warning


class CustomerLevel(models.Model):

    _name = 'crm_key_customer.customer_level'
    _description = 'Customer Level'

    def show_statistics(self):
        ''' When the Show Statistics button is clicked, calculate how many
        individuals and companies are on the customer list, and show the
        information in a popup window '''

        company_count = 0
        individual_count = 0

        for partner in self.partner_ids:
            if partner.is_company is True:
                company_count += 1
            else:
                individual_count += 1

        popup_message = _('This customer level contains\n')
        popup_message += _('-{} companies\n').format(company_count)
        popup_message += _('-{} individuals').format(individual_count)

        raise Warning(popup_message)

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
