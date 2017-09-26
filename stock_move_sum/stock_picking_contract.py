# -*- coding: utf-8 -*-
from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
     
 
    contract_type = fields.Char(compute='_contrato',  readonly=True)
    tons = fields.Float(compute="_compute_tons")
    
    
    @api.one
    @api.depends('origin')
    def _contrato(self):
        if self.origin:
          self.purchase_contract_type = self.env['purchase.order'].search([('name', '=', self.origin)])
          if self.purchase_contract_type:
            self.contract_ty = self.purchase_contract_type.contract_type
            if self.contract_ty == "axc":
              self.contract_type = "AxC"
            if self.contract_ty == "pf":
              self.contract_type = "Precio Fijo"
            if self.contract_ty == "pm":
              self.contract_type = "Precio Minimo"
            if self.contract_ty == "pd":
              self.contract_type = "Precio Despues"
            if self.contract_ty ==  "pb":
              self.contract_type = "Precio Base"
            if self.contract_ty == "na":
              self.contract_type = "No Aplica"
          else:
            self.contract_type = ""
                    
                    
    @api.one
    @api.depends('move_lines')
    def _compute_tons(self):
        self.tons = 0
        for line in self.move_lines:
            self.tons += line.product_uom_qty
