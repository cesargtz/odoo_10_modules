# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from openerp.exceptions import ValidationError
import datetime


class PurchaseDates(models.Model):
    _inherit = 'purchase.order'

    def _get_start_date():
        return datetime.date.today().strftime("%Y") + "-10-15"

    def _get_final_date():
        return datetime.date.today().strftime("%Y") + "-12-30"

    start_date = fields.Date(default=_get_start_date())
    final_date = fields.Date(default=_get_final_date())

    @api.one
    @api.constrains('start_date', 'final_date')
    def _check_dates(self):
        if self.start_date > self.final_date:
            raise ValidationError(_("The start date cannot be greater than final date"))
