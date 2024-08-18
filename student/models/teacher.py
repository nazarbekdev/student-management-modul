# -*- coding: utf-8 -*-

from odoo import models, fields


class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    position = fields.Char(string='Position', required=True)
