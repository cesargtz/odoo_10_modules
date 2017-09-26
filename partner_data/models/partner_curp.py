# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, exceptions, fields, models, _


class PartnerCURP(models.Model):
    _inherit = 'res.partner'

    curp = fields.Char('CURP')
    clave = fields.Char('Clave de acceso')
    @api.one
    @api.constrains('curp')
    def _check_curp(self):
        if self.curp:
            if len(self.curp) != 18:
                raise exceptions.ValidationError(_('Invalid CURP'))
