# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class PartnerCredential(models.Model):
    _inherit = 'res.partner'

    identification_type = fields.Selection([
        ('ife', 'IFE'),
        ('pasaporte', 'Pasaporte'),
    ], 'Tipo de Identificación')
    identification_number = fields.Char('Numero de identificación')
    expiration_date = fields.Date('Vencimiento')
    elector_key = fields.Char('Clave de Elector')
