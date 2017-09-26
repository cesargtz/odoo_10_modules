# -*- coding: utf-8 -*-

from odoo import models, fields, api

class order_hired(models.Model):
    _inherit = "purchase.order"

    tons_hired = fields.Float(string="Toneladas", compute="_compute_hired")

    @api.one
    @api.depends('order_line')
    def _compute_hired(self):
        if len(self.order_line) > 0:
            for line in self.order_line:
                self.tons_hired += line.product_qty
        else:
            self.tons_hired = 0
