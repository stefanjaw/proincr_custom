# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMoveLineCustom(models.Model):
    _inherit = "stock.move.line"

    #1651242870
    automate = fields.Char(compute="automation")
    partner_id = fields.Many2one('res.partner', translate=True)
    
    def automation(self):
        for record in self:
            try:
                record.write({
                    'automate': True,
                    'partner_id': record.move_id.partner_id,
                })
            except:
                record.write({
                    'automate': False,
                })
        return
