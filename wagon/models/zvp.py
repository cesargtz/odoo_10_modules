# -*- coding: utf-8 -*-

from odoo import fields, models


class ZVP(models.Model):
    _name = 'zvp'

    name = fields.Char()
    partner = fields.Char()
