# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Vehicle(models.AbstractModel):
    _name = 'vehicle'

    name = fields.Char()

    product_id = fields.Many2one('product.product', 'Producto', compute="_compute_product_id", store=False, readonly=True)
    location_id = fields.Many2one('stock.location', 'Ubicación')

    humidity_rate = fields.Float('Humedad origen')
    damage_rate = fields.Float('Daño origen')
    break_rate = fields.Float('Quebrado origen')
    impurity_rate = fields.Float('Impureza origen')

    density = fields.Float('Densidad origen')
    temperature = fields.Float('Temperatura origen')
    transgenic = fields.Float('Transgénico origen')

    raw_kilos = fields.Float('Kilos neto origen', compute="_compute_raw_kilos", store=False)

    humid_kilos = fields.Float('kilos húmedos origen', compute="_compute_humid_kilos", store=False)
    damaged_kilos = fields.Float('Kilos dañado origen', compute="_compute_damaged_kilos", store=False)
    broken_kilos = fields.Float('Kilos quebrados origen', compute="_compute_broken_kilos", store=False)
    impure_kilos = fields.Float('Kilos Impuros origen', compute="_compute_impure_kilos", store=False)

    deducted_kilos = fields.Float('Kilos Deducidos', compute="_compute_deducted_kilos", store=False)

    clean_kilos = fields.Float('Kilos Limpios origen', compute="_compute_clean_kilos", store=False)

    ticket = fields.Integer()

    stock_picking_id = fields.Many2one('stock.picking', 'Movimiento de almacen', readonly=True)

    state = fields.Selection(
    [
        ('done', 'Hecho'),
    ])

    @api.multi
    def _compute_raw_kilos(self):
        self.net_kilos = 0

    @api.one
    @api.depends('raw_kilos', 'humidity_rate')
    def _compute_humid_kilos(self):
        if self.humidity_rate > 14:
            self.humid_kilos = self.raw_kilos * (self.humidity_rate - 14) * .0116
        else:
            self.humid_kilos = 0

    @api.one
    def _compute_damaged_kilos(self):
        if self.damage_rate > 5:
            self.damaged_kilos = self.raw_kilos * (self.damage_rate - 5) / 100
        else:
            self.damaged_kilos = 0

    @api.one
    def _compute_broken_kilos(self):
        if self.break_rate > 2:
            self.broken_kilos = self.raw_kilos * (self.break_rate - 2) / 100
        else:
            self.broken_kilos = 0
    @api.one        
    @api.depends('impurity_rate')
    def _compute_impure_kilos(self):
        if self.impurity_rate > 2:
            self.impure_kilos = self.raw_kilos * (self.impurity_rate - 2) / 100
        else:
            self.impure_kilos = 0

    @api.one        
    @api.depends('humid_kilos','damaged_kilos','broken_kilos') 
    def _compute_deducted_kilos(self):
        self.deducted_kilos = self.humid_kilos + self.damaged_kilos + self.broken_kilos + self.impure_kilos

    @api.one
    @api.depends('raw_kilos','deducted_kilos') 
    def _compute_clean_kilos(self):        
        self.clean_kilos = self.raw_kilos - self.deducted_kilos

    @api.multi
    def _compute_product_id(self):
        self.product_id = False
