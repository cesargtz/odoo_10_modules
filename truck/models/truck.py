# -*- coding: utf-8 -*-

from odoo import api, fields, models
import datetime
import pytz

class Truck(models.AbstractModel):
    _inherit = 'vehicle'
    _name = 'truck'

    driver = fields.Char('Conductor')
    car_plates = fields.Char('Placas')
    date = fields.Datetime('Fecha')

    input_kilos = fields.Float('Kilos de entrada origen')
    output_kilos = fields.Float('Kilos de salida origen')

    @api.one
    @api.depends('input_kilos', 'output_kilos')
    def _compute_raw_kilos(self):
        self.raw_kilos = self.input_kilos - self.output_kilos


    @api.onchange('contract_id')
    def _onchange_date(self):
        local = pytz.timezone("America/Chihuahua")
        utc = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
        local_hr = local.localize(utc, is_dst=None)
        print(local_hr)
        self.date = local_hr
