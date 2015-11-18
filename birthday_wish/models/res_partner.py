# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015 Medma - http://www.medma.net
#    All Rights Reserved.
#    Medma Infomatix (info@medma.net)
#
#    Coded by: Turkesh Patel (turkesh.patel@medma.in)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models, _
from datetime import datetime

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    birth_date = fields.Date(string='Birthdate')

    @api.model
    def send_birthday_email(self):
        partner_obj = self.env['res.partner']
        wish_template_id = self.env['ir.model.data'].get_object('birthday_wish', 'email_template_birthday_wish')
        channel_id = self.env['ir.model.data'].get_object('birthday_wish', 'channel_birthday')
        today = datetime.now()
        today_month_day = '%-' + today.strftime('%m') + '-' + today.strftime('%d')
        partner_ids = partner_obj.search([('birth_date', 'like', today_month_day)])
        if partner_ids:
            for partner_id in partner_ids:
                if partner_id.email:
                    template = partner_id.company_id.birthday_mail_template or wish_template_id
                    template.send_mail(partner_id.id, force_send=True)
                res = channel_id.message_post(body=_('Happy Birthday Dear %s.') % (partner_id.name), partner_ids=[partner_id.id])
                res.write({'channel_ids':[[6, False, [channel_id.id]]]})
                partner_id.message_post(body=_('Happy Birthday.'))
        return None
