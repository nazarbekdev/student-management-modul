from odoo import http


class StudentController(http.Controller):
    @http.route('/student', type='http', auth='user', website=True)
    def list_students(self, **kwargs):
        students = http.request.env['student.student'].search([])
        return http.request.render('student.listing', {'students': students})
