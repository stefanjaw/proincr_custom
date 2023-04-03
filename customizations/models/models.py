# -*- coding: utf-8 -*-

from odoo import models, fields, api

class fields(models.Model):
   _inherit = "sale.order"

   delivery_time = fields.Char(string="Tiempo de entrega", )
   place_of_delivery = fields.Text(string="Lugar de entrega", )
