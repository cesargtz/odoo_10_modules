# -*- coding: utf-8 -*-

from odoo import api, fields, models


class FarmArea(models.Model):
    _name = 'farm.area'

    purchase_order_id = fields.Many2one('purchase.order')
    farm_id = fields.Many2one('farm', 'Predio')
    hired_area = fields.Float('Contratado')
    expected_performance = fields.Float('Rendimiento Esperado', default=12)
    tons_to_validate = fields.Float('Toneladas a validar', compute="_get_tons_to_validate", store=False)
    regime = fields.Selection([
        ('riego', 'Riego'),
        ('temporal', 'Temporal'),
    ], 'Regimen', default='riego')
    validated_production = fields.Float('Producción validada')
    validated_year = fields.Integer('Año validado', size=4)
    annex_folio = fields.Char('Folio Anexo')
    expiration = fields.Date('Vencimiento')
    client = fields.Many2one('res.partner', 'Proveedor')
    ownership_type = fields.Selection([
        ('propio', 'Propio'),
        ('derivado', 'Derivado'),
    ], 'Tipo de propiedad')

    @api.one
    @api.depends('hired_area', 'expected_performance')
    def _get_tons_to_validate(self):
        self.tons_to_validate = self.hired_area * self.expected_performance

class FarmInherit(models.Model):
    _inherit = 'purchase.order'

    farm_area_ids = fields.One2many('farm.area', 'purchase_order_id')
