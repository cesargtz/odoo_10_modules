# -*- coding: utf-8 -*-
import time

from odoo import models, fields, api


class Suppliers_History(models.Model):
    _name = 'suppliers.history'

    res_partner_id = fields.Many2one('res.partner')
    date = fields.Char()
    hired = fields.Float()
    delivered = fields.Float()
    pending = fields.Float(compute="_compute_pending", store=False, readonly=True)
    progressbar = fields.Float(compute="_compute_progressbar")

    @api.one
    @api.depends('hired','delivered')
    def _compute_pending(self):
        self.pending = self.hired - self.delivered

    @api.one
    @api.depends('hired','delivered')
    def _compute_progressbar(self):
        if self.hired and self.delivered:
            self.progressbar = (self.delivered * 100) / self.hired

    # @api.one
    # def _compute_year(self):
    #     self.date = time.strftime("%Y")  #solo se ejecuta al guardar el registro//Eror
    #     str(time.strftime("%Y"))

class Record_Partner(models.Model):
    _inherit = "res.partner"

    suppliers_history_ids = fields.One2many('suppliers.history','res_partner_id')
    last_year_contract = fields.Char(compute="_compute_last_year", store=True)
    tons_hired = fields.Float(compute="_compute_hired")

    # @api.onchange('suppliers_history_ids')
    @api.one
    @api.depends('suppliers_history_ids')
    def _compute_last_year(self):
        year = 0
        for line in self.suppliers_history_ids:
            try:
                if not isinstance(line.date, int):
                    if int(line.date) > year:
                        year = int(line.date)
            except ValueError:
                year = 0
        if year > 1:
            self.last_year_contract = str(year)
        else:
            self.last_year_contract = ''

    @api.one
    @api.depends('suppliers_history_ids')
    def _compute_hired(self):
        year = 0
        for line in self.suppliers_history_ids:
            try:
                if not isinstance(line.date, int):
                    if int(line.date) > year:
                        year = int(line.date)
                        self.tons_hired = line.hired
            except ValueError:
                year = 0
