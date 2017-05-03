# -*- coding: utf-8 -*-
from openerp import api, fields, models, _
from openerp.exceptions import Warning


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        '''When the customer is selected, check if they are key customer. If yes,
        show a notification popup '''
        if self.partner_id.is_key_customer is True:
            customer_name = self.partner_id.name
            level = self.partner_id.customer_level_id.name
            raise Warning(_('{} is a level {} key customer!').format(customer_name, level))
