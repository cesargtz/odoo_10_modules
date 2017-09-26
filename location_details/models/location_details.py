# -*- coding: utf-8 -*-

from odoo import models, fields, api

class location_details(models.Model):
    _inherit = 'stock.location'

    truck_reception = fields.One2many('truck.reception','location_id')
    truck_outlet = fields.One2many('truck.outlet','location_id')
    wagon_outlet = fields.One2many('wagon.outlet','location_id')
    truck_internal = fields.One2many('truck.internal','location_id')
    truck_internal_dest = fields.One2many('truck.internal','location_dest_id')

    total_tons_reception = fields.Float(compute="_compute_total_reception", store=False, readonly=True, help="Kilos Limpios")
    total_tons_outlet = fields.Float(compute="_compute_total_outlet", store=False, readonly=True, help="Kilos Netos")
    total_tons_available = fields.Float(compute="_compute_total_available", store=False, readonly=True,help="El calculo incluye las transferencias")

    percentage_quality_reception = fields.Float(compute="_compute_quality_reception", store=False, readonly=True,help="Calculo con recepcion de camiones y transferencias de destino") #humedad
    percentage_quality_damaged = fields.Float(compute="_compute_quality_damaged", store=False, readonly=True, help="Calculo con recepcion de camiones y transferencias de destino")
    percentage_quality_impurity = fields.Float(compute="_compute_quality_impurity", store=False, readonly=True, help="Calculo con recepcion de camiones y transferencias de destino")
    percentage_quality_break = fields.Float(compute="_compute_quality_break", store=False, readonly=True,help="Calculo con recepcion de camiones y transferencias de destino")

    wet_kilos_discount = fields.Float(compute="_compute_wet_kilos", store=False, readonly=True,help="Calculo con recepcion de camiones y transferencias de destino")
    damaged_kilos_discount = fields.Float(compute="_compute_damaged_kilos", store=False, readonly=True,help="Calculo con recepcion de camiones y transferencias de destino")
    impure_kilos_discount = fields.Float(compute="_compute_impure_kilos", store=False, readonly=True,help="Calculo con recepcion de camiones y transferencias de destino")
    broken_kilos_discount = fields.Float(compute="_compute_broken_kilos", store=False, readonly=True,help="Calculo con recepcion de camiones y transferencias de destino")

    transfer_origin = fields.Float(compute="_compute_transfer_origin", store=False, readonly=True)
    transfer_dest = fields.Float(compute="_compute_transfer_dest", store=False, readonly=True)

    @api.one
    @api.depends('truck_reception')
    def _compute_total_reception(self):
        if len(self.truck_reception) > 0:
            tons = 0
            for record in self.truck_reception:
                tons += record.clean_kilos
            self.total_tons_reception = tons / 1000
        else:
            self.total_tons_reception = 0    

    @api.one
    @api.depends('truck_outlet','wagon_outlet')
    def _compute_total_outlet(self):
        if len(self.truck_outlet) > 0 or len(self.wagon_outlet) > 0:
            tons_truck = 0
            tons_wagon = 0
            for record in self.truck_outlet:
                tons_truck += record.raw_kilos
            for record in self.wagon_outlet:
                tons_wagon += record.raw_kilos
            self.total_tons_outlet = (tons_truck + tons_wagon) / 1000
        else:
            self.total_tons_outlet = 0


    @api.one
    @api.depends('truck_reception', 'truck_internal_dest')
    def _compute_quality_reception(self):
        sum_total = 0
        total_tons = 0
        if len(self.truck_reception) > 0 or len(self.truck_internal_dest) > 0:
            for record in self.truck_reception:
                quality = record.humidity_rate
                tons = record.clean_kilos / 1000
                total_tons += tons
                total = tons * quality
                sum_total += total    
            for record in self.truck_internal_dest:
                if record.humidity_rate_dest > 0:
                    if record.stock_destination:
                        quality = record.humidity_rate_dest
                        tons = record.clean_kilos_dest / 1000
                    else:
                        quality = record.humidity_rate
                        tons = record.clean_kilos / 1000
                    total_tons += tons
                    total = tons * quality
                    sum_total += total
            self.percentage_quality_reception = float(sum_total / total_tons)
        else:
            self.percentage_quality_reception = 1        

    @api.one
    @api.depends('truck_reception','truck_internal_dest')
    def _compute_wet_kilos(self):
        if len(self.truck_reception) > 0 or len(self.truck_internal_dest) > 0:
            tons = 0
            for record in self.truck_reception:
                tons += record.humid_kilos
            for record in self.truck_internal_dest:
                if record.stock_destination:
                    tons += record.humid_kilos_dest
                else:
                    tons += record.humid_kilos
            self.wet_kilos_discount = tons
        else:
            self.wet_kilos_discount = 0

    @api.one
    @api.depends('truck_reception','truck_internal_dest')
    def _compute_damaged_kilos(self):
        if len(self.truck_reception) > 0 or len(self.truck_internal_dest) > 0:
            tons = 0
            for record in self.truck_reception:
                tons += record.damaged_kilos
            for record in self.truck_internal_dest:
                if record.stock_destination:
                    tons += record.damaged_kilos_dest
                else:
                    tons += record.damaged_kilos
            self.damaged_kilos_discount = tons
        else:
            self.damaged_kilos_discount = 0

    @api.one
    @api.depends('truck_reception','truck_internal_dest')
    def _compute_impure_kilos(self):
        if len(self.truck_reception) > 0 or len(self.truck_internal_dest) > 0:
            tons = 0
            for record in self.truck_reception:
                tons += record.impure_kilos
            for record in self.truck_internal_dest:
                if record.stock_destination:
                    tons += record.impure_kilos_dest
                else:
                    tons += record.impure_kilos
            self.impure_kilos_discount = tons
        else:
            self.impure_kilos_discount = 0

    @api.one
    @api.depends('truck_reception','truck_internal_dest')
    def _compute_broken_kilos(self):
        if len(self.truck_reception) > 0 or len(self.truck_internal_dest) > 0:
            tons = 0
            for record in self.truck_reception:
                tons += record.broken_kilos
            for record in self.truck_internal_dest:
                if record.stock_destination:
                    tons += record.broken_kilos_dest
                else:
                    tons += record.broken_kilos
            self.broken_kilos_discount = tons
        else:
            self.broken_kilos_discount = 0

    @api.one
    @api.depends('truck_reception','truck_internal_dest')
    def _compute_quality_damaged(self):
        if len(self.truck_reception) > 0 or len(self.truck_internal_dest) > 0:
            sum_total = 0
            total_tons = 0
            for record in self.truck_reception:
                quality = record.damage_rate
                tons = record.clean_kilos / 1000
                total_tons += tons
                total = tons * quality
                sum_total += total
            for record in self.truck_internal_dest:
                if record.damage_rate_dest > 0:
                    if record.stock_destination:
                        quality = record.damage_rate_dest
                        tons = record.clean_kilos_dest / 1000
                    else:
                        quality = record.damage_rate
                        tons = record.clean_kilos / 1000
                    total_tons += tons
                    total = tons * quality
                    sum_total += total
            self.percentage_quality_damaged = float(sum_total / total_tons)
        else:
            self.percentage_quality_damaged = 0


    @api.one
    @api.depends('truck_reception','truck_internal_dest')
    def _compute_quality_impurity(self):
        if len(self.truck_reception) > 0 or len(self.truck_internal_dest) > 0:
            sum_total = 0
            total_tons = 0
            for record in self.truck_reception:
                quality = record.impurity_rate
                tons = record.clean_kilos / 1000
                total_tons += tons
                total = tons * quality
                sum_total += total
            for record in self.truck_internal_dest:
                if record.impurity_rate_dest > 0:
                    if record.stock_destination:
                        quality = record.impurity_rate_dest
                        tons = record.clean_kilos_dest / 1000
                    else:
                        quality = record.impurity_rate
                        tons = record.clean_kilos / 1000
                    total_tons += tons
                    total = tons * quality
                    sum_total += total
            self.percentage_quality_impurity = float(sum_total / total_tons)
        else:
            self.percentage_quality_impurity = 0


    @api.one
    @api.depends('truck_reception','truck_internal_dest')
    def _compute_quality_break(self):
        if len(self.truck_reception) > 0  or len(self.truck_internal_dest) > 0:
            sum_total = 0
            total_tons = 0
            for record in self.truck_reception:
                quality = record.break_rate
                tons = record.clean_kilos / 1000
                total_tons += tons
                total = tons * quality
                sum_total += total
            for record in self.truck_internal_dest:
                if record.break_rate_dest > 0:
                    if record.stock_destination:
                        quality = record.break_rate_dest
                        tons = record.clean_kilos_dest / 1000
                    else:
                        quality = record.break_rate
                        tons = record.clean_kilos / 1000
                    total_tons += tons
                    total = tons * quality
                    sum_total += total
            self.percentage_quality_break = float(sum_total / total_tons)
        else:
            self.percentage_quality_break = 0


    @api.one
    @api.depends('total_tons_reception','total_tons_outlet')
    def _compute_total_available(self):
        self.total_tons_available = (self.total_tons_reception + self.transfer_dest) - (self.total_tons_outlet + self.transfer_origin)

    @api.one
    @api.depends('truck_internal')
    def _compute_transfer_origin(self):
        if len(self.truck_internal) > 0:
            tons_origin = 0
            for record in self.truck_internal:
                if record.stock_destination:
                    tons_origin += record.clean_kilos_dest / 1000
                else:
                    tons_origin += record.clean_kilos / 1000
            self.transfer_origin = tons_origin
        else:
            self.transfer_origin = 0.0

    @api.one
    @api.depends('truck_internal_dest')
    def _compute_transfer_dest(self):
         if len(self.truck_internal_dest) > 0:
            tons_dest = 0
            for record in self.truck_internal_dest:
                if record.stock_destination:
                    tons_dest += record.clean_kilos_dest / 1000
                else:
                    tons_dest += record.clean_kilos / 1000
            self.transfer_dest = tons_dest
         else:
            self.transfer_dest = 0.0
