# -*- coding: utf-8 -*-

from odoo import models, fields, api

class account_invoice_tons(models.Model):
    _inherit = 'account.invoice'

    tons = fields.Float(compute='_compute_tons', store=True)
    product = fields.Char(compute='_compute_product',store=True)

    contract_type = fields.Selection([
        ('axc', 'AxC'),
        ('pf', 'Precio Fijo'),
        ('pm', 'Precio Maximo'),
        ('pd', 'Precio Despues'),
	    ('sv', 'Servicios'),
        ('na', 'No aplica'),
    ], default='na', required=True)


    @api.one
    @api.depends('invoice_line_ids.quantity')
    def _compute_tons(self):        
        for line in self.invoice_line_ids:           
           self.tons += line.quantity

    @api.one
    @api.depends('product')
    def _compute_product(self):
      if len(self.invoice_line_ids) > 0:
        for line in self.invoice_line_ids:
          product_id = line.product_id.name
          break
        self.product = product_id
      else:
        self.product = "s/p"






