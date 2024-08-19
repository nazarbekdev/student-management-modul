# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    transaction_type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense')
    ], string="Transaction Type", default='income')
