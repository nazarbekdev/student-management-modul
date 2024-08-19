# -*- coding: utf-8 -*-

from odoo import models, fields


class CoursePayment(models.Model):
    _name = 'course.payment'
    _description = 'Payment'

    student_id = fields.Many2one('student.student', string="Student", required=True)
    amount = fields.Float(string="Amount", required=True)
    date = fields.Date(string="Payment Date", default=fields.Date.today)
    description = fields.Text(string="Description")
    group_id = fields.Many2one('course.group', string="Group", required=True)
    check_number = fields.Char(string="Check Number", required=True, index=True, default='INV/2024/00000')
