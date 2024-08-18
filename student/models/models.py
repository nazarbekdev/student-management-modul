# # -*- coding: utf-8 -*-
#
# from odoo import models, fields, api
#
#
# class student(models.Model):
#     _name = 'student.student'
#     _description = 'student.student'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
#


# -*- coding: utf-8 -*-

from odoo import models, fields


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birth_day = fields.Datetime(string='Birth Day', required=True, default=fields.Datetime.now)
    phone_number = fields.Char(string='Phone Number', required=True)
    payment_ids = fields.One2many('student.payment', 'student_id', string='Payments')
    group_id = fields.Many2one('course.group', string='Group')
