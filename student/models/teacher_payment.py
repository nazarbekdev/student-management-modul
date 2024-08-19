# -*- coding: utf-8 -*-

from odoo import models, fields


class TeacherPayment(models.Model):
    _name = 'teacher.payment'
    _description = "Payment of Teacher"

    teacher_id = fields.Many2one('teacher.teacher', string="Teacher", required=True)
    amount = fields.Float(string="Amount", required=True)
    date = fields.Date(string="Payment Date", default=fields.Date.today)
    description = fields.Text(string="Description")
