# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Waterhole(models.Model):
    _name = 'waterhole'

    name = fields.Char(string="Pozo", required=True)
    owner = fields.Char('Propietario', required=True)
    cubic_meters = fields.Float('Capacidad', required=True)
    coordinates = fields.Char('Coordenadas')
    expiration_date = fields.Date('Vencimiento', required=True)

    _sql_constraints = [
        ('waterhole_id_unique',
         'UNIQUE(name)',
         _("The waterhole id must be unique")),
    ]
