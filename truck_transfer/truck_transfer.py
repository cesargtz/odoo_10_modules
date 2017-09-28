#aobject with reference: Product Unit of Measure - product.uom] -*- coding: utf-8 -*-

from odoo import models, fields, api

class truck_transfer(models.Model):
    _name = 'truck.transfer'

    product_ide = fields.Many2one('product.product', 'Producto')
    #uom_id = fields.Many2one('product.template', related="product_ide.uom_id")
    quantity = fields.Float('Cantidad')
    #description = fields.Char()
    uom_id = fields.Integer('Unidad de Medida')
    location_id = fields.Many2one('stock.location', 'Ubicación')
    location_dest_id = fields.Many2one('stock.location', 'Ubicación Destino')

    @api.one
    def action_move(self):
        uom = self.product_ide.product_tmpl_id.uom_id.id
        if (self.stock_destination) and (self.stock_origin == False):
            move_date = {
                'product_id' : self.product_ide.id,
                'product_uom_qty': float(self.clean_kilos_dest/1000),
                'product_uom':uom,
                'name': "Transferencias Internas",
                'location_id': self.location_id.id,
                'location_dest_id': self.location_dest_id.id,
	            'picking_type_id': "5"
                }
        if (self.stock_origin) and (self.stock_destination == False):
            move_date = {
                'product_id' : self.product_ide.id,
                'product_uom_qty': float(self.clean_kilos/1000),
                'product_uom': uom,
                'name': "Transferencias Internas",
                'location_id': self.location_id.id,
                'location_dest_id': self.location_dest_id.id,
                'picking_type_id': "5"
                }
        move = self.env['stock.move'].create(move_date)
        move.action_confirm()
        move.action_done()

        self.stock_picking_id = self.env['stock.picking'].search([('state', 'in', ['done'])], order='date desc', limit=1)
