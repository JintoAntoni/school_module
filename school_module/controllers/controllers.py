# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class SchoolModule(http.Controller):
    @http.route('/student', type="http", auth="public", website=True)
    def student(self, **kw):
        student = request.env['school.student'].sudo().search([])
        students = {}
        students.update({'student':student})
        return request.render("school_module.student_template",students)

    @http.route('/custom', type="http", auth="public", website=True)
    def custom(self, **kw):
        print("xxxxxxxxxxxxxxxxxx111111111111111111111111111111")
        students = request.env['school.student'].search([])
        # standard = request.env['school.standards'].sudo().search([])
        # students = {}
        # standard = {'standard': standard}
        # students.update({'student': student})
        student = {'students': students}
        return request.render("school_module.custom_webpage",student)




    @http.route('/add/student', type="http", auth="public", website=True)
    def addStudent(self, **kw):
        standard = request.env['school.standards'].sudo().search([])
        # students = {}
        standard = {'standard':standard}
        # students.update({'student': student})
        return request.render("school_module.student_application_form",standard)


    @http.route('/create/student', type="http", auth="public",csrf=False, website=True)
    def createStudent(self, **kw):

        val_dict = {}
        if kw.get('description'):
            description = kw.get('description')
        if kw.get('student_name'):
            name = kw.get('student_name')
            partner_id = request.env['res.partner'].sudo().create({'name': name})
            print("partner_id--------->>",partner_id.id)
            # val_dict.update('name':student_name)
        request.env['school.student'].create({'description':description,'name':partner_id.id})
        return request.render('school_module.student_created',{'partner':partner_id.name})


    @http.route('/delete_student', type="http", auth="public", website=True,csrf=False)
    def deleteStudent(self, **kw):
        student = request.env['school.student'].sudo().search([('name', '=', kw.get('student_name'))])
        print(student)
        for stud in student:
            stud.unlink()
            ret = "yes"
        return json.dumps({'result': ret})
        # standard = {'standard': standard}
        # students.update({'student': student})
        # return request.render("school_module.student_application_form", standard)

