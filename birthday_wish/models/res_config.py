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

class base_config_settings(models.Model):
    _inherit = 'base.config.settings'

    birthday_mail_template = fields.Many2one('mail.template', string='Birthday Wishes Template',
                                                                                          help="This will set the default mail template for birthday wishes.")

    @api.multi
    def get_default_birthday_mail_template(self):
        user = self.env['res.users'].browse(self._uid)
        return {'birthday_mail_template': user.company_id.birthday_mail_template.id}

    @api.multi
    def set_birthday_mail_template(self):
        user = self.env['res.users'].browse(self._uid)
        user.company_id.write({'birthday_mail_template': self.birthday_mail_template.id})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
