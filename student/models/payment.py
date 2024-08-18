# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CoursePayment(models.Model):
    _name = 'course.payment'
    _description = 'Payment'

    student_id = fields.Many2one('student.student', string="Student", required=True)
    amount = fields.Float(string="Amount", required=True)
    date = fields.Date(string="Payment Date", default=fields.Date.today)
    description = fields.Text(string="Description")
    group_id = fields.Many2one('course.group', string="Group", required=True)
    check_number = fields.Char(string="Check Number", required=True, copy=False, readonly=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('course.payment.check'))

    @api.model
    def create(self, vals):
        if not vals.get('check_number'):
            vals['check_number'] = self.env['ir.sequence'].next_by_code('course.payment.check') or '/'
        return super(CoursePayment, self).create(vals)
