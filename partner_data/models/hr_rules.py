# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_rules(models.Model):
    _inherit = 'hr.employee'

    job_goals = fields.Text()
    responsibilities = fields.Text()
    additional_functions = fields.Text()
    schedule = fields.Text()
    salary = fields.Float()
    works_hours = fields.Text()
    execution_fees = fields.Text()
    goal = fields.Text()
    bonus = fields.Text() #Aguinaldo
    bonos = fields.Text()
    gasoline = fields.Text()
    date_payment_commissions = fields.Text()
    holidays =  fields.Text()
    loan = fields.Text()
    sanctions = fields.Text()
    others = fields.Text()
    