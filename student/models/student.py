# -*- coding: utf-8 -*-

from odoo import models, fields


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birth_day = fields.Date(string="Birth Day", default=fields.Date.today)
    phone_number = fields.Char(string='Phone Number', required=True, default='+998 ')
    payment_ids = fields.One2many('course.payment', 'student_id', string='Payments')
    group_id = fields.Many2one('course.group', string='Group')
