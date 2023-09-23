# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError, AccessError


class school_SchoolMod(models.Model):
    _name = 'school.school'
    # _description = 'school_module.school_module'

    name = fields.Char()
    is_school = fields.Boolean(string="Is School")


    # @api.model
    # def school_count(self):
    #     if self.env['school.school'].search_count([]) > 1:
    #         raise ValidationError(("This employee already has an user."))


class school_Class(models.Model):
    _name = 'school.class'
    _description = 'school_module.school_module'

    name = fields.Char("Class")
    seq_number = fields.Char("Sequence Number")



class school_Division(models.Model):
    _name = 'school.division'
    _description = 'school_module.school_module'

    name = fields.Char("Division")
    seq_number = fields.Char("Sequence Number")


class school_Standerds(models.Model):
    _name = 'school.standards'
    _description = 'school_module.school_module'
    _rec_name = "standard"

    standard = fields.Char(compute= '_compute_standard', required= True, store=True, default=0)
    seq_number = fields.Char("Sequence Number")
    school_class = fields.Many2one('school.class')
    school_division = fields.Many2one('school.division')
    number_of_seats = fields.Integer("Number of Seats",default=50)

    _sql_constraints = [
        ('standard_uniq', 'unique (standard)', 'The  standard must be unique !')
    ]

    @api.depends('school_class','school_division')
    def _compute_standard(self):
        self.standard = 0
        if  self.school_class and self.school_division:
            self.standard = self.school_class.name + '-' + self.school_division.name
