# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Farm(models.Model):
    _name = 'farm'

    name = fields.Char(string="Predio", required=True)
    folio = fields.Char(size=12, required=True)
    farm_owner = fields.Char('Porpietario')
    city = fields.Many2one('res.country.state', 'Estado', required=True)
    coords = fields.Char('Coordenadas')
    area = fields.Float(required=True)
    municipio = fields.Many2one('base.municipio', 'Municipio')
    localidad_id = fields.Many2one('base.localidad', 'Localidad')

    @api.onchange('city')
    def _on_change_limpiar_municipio(self):
        self.municipio = ''

    @api.onchange('municipio')
    def _on_change_limpiar_loc(self):
        self.localidad = '' 
       


    _sql_constraints = [
        ('farm_id_unique',
         'UNIQUE(name)',
         _("The farm id must be unique")),
    ]
class base_municipio(models.Model):
    _name = 'base.municipio'
    name = fields.Char('Municipio')
    country_id =fields.Many2one('res.country.state','Estado')

class base_localidad(models.Model):
    _name = 'base.localidad'
    name = fields.Char('Localidad')
    municipio_id =fields.Many2one('base.municipio','Municipio')