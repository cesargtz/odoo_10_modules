# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Truck(models.AbstractModel):
    _inherit = 'vehicle'
    _name = 'truck'

    driver = fields.Char('Conductor')
    car_plates = fields.Char('Placas')
    date = fields.Date('Fecha', default=fields.Date.today)

    input_kilos = fields.Float('Kilos de entrada origen')
    output_kilos = fields.Float('Kilos de salida origen')

    @api.one
    @api.depends('input_kilos', 'output_kilos')
    def _compute_raw_kilos(self):
        self.raw_kilos = self.input_kilos - self.output_kilos
