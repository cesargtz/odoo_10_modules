# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Waterhole(models.Model):
    _name = 'waterhole.hired'

    purchase_order_id = fields.Many2one('purchase.order')
    waterhole_id = fields.Many2one('waterhole', 'Pozo')
    owner = fields.Char('Propietario', related='waterhole_id.owner', readonly=True)
    cubic_meters = fields.Float('Capacidad', related='waterhole_id.cubic_meters', readonly=True)
    coordinates = fields.Char('Coordenadas', related='waterhole_id.coordinates', readonly=True)
    expiration_date = fields.Date('Vencimiento', related="waterhole_id.expiration_date", readonly=True)

class WaterholeInherit(models.Model):
    _inherit = 'purchase.order'

    waterhole_hired_ids = fields.One2many('waterhole.hired', 'purchase_order_id')
