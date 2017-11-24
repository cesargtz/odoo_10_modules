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

    @api.onchange('reference')
    def _onchange_tons(self):
        advance_invoiced = 0
        tons_contract =  self.env['purchase.order'].search([('name', '=', self.origin), ('partner_id', '=', self.partner_id.id),('state', '=', 'purchase')])
        for line in self.env['account.invoice'].search([('origin', '=', self.origin), ('partner_id', '=', self.partner_id.id),('state', '=', 'open')]):
            if line.invoice_line_ids.product_id.product_tmpl_id.consider_contract:
                advance_invoiced += line.invoice_line_ids.quantity
        # print(advance_invoiced)
        if (advance_invoiced + self.invoice_line_ids.quantity) > tons_contract.tons_reception:
            return {
                'warning': {
                    'title': "Estas tratando de facturar más de lo contratado.",
                    'message': "Quierar facturar %s tons, pero ya tienes facturadas %s tons. El total disponible es de %s tons" % (self.invoice_line_ids.quantity, advance_invoiced, tons_contract.tons_reception),
                }
            }

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
