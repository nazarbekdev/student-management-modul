# -*- coding: utf-8 -*-

from odoo import models, fields


class CourseGroup(models.Model):
    _name = 'course.group'
    _description = 'Group'

    name = fields.Char(string="Group Name", required=True)
    course_id = fields.Many2one('course.course', string="Course", required=True)
    teacher_id = fields.Many2one('teacher.teacher', string="Teacher")
    student_ids = fields.One2many('student.student', 'group_id', string="Students")
    payment_ids = fields.One2many('course.payment', 'group_id', string="Payments")  # Yangi maydon
