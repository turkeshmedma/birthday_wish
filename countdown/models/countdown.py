# -*- encoding: utf-8 -*-

##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp.osv import osv, orm, fields
from openerp.addons.base.ir.ir_qweb import HTMLSafe

class Countdown(orm.AbstractModel):
    _name = 'ir.qweb.field.countdown'
    _inherit = 'ir.qweb.field'
    
    def record_to_html(self, cr, uid, field_name, record, options=None, context=None):
        html = self.pool["ir.ui.view"].render(cr, uid, "countdown.countdown", {'countdown_date':record[field_name], 'options':options}, engine='ir.qweb', context=context).decode('utf8')
        return HTMLSafe(html)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
