# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Char(string='Age', required=True, default=0)
    phone_number = fields.Char(string='Phone Number', required=True)
    payment_ids = fields.One2many('course.payment', 'student_id', string='Payments')
    group_id = fields.Many2one('course.group', string='Group')
