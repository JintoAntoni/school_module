# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta

class school_Student(models.Model):
    _name = 'school.student'
    _description = 'school student'

    name = fields.Many2one('res.partner')
    dob = fields.Date()
    age = fields.Char()
    parent_name = fields.Many2one('res.partner')
    standard = fields.Many2one('school.standards')
    address = fields.Text()
    description = fields.Text()
    seats_avail = fields.Integer(
        'Seats Available',
        related='standard.number_of_seats', readonly=False)
    gender = fields.Selection([
        ('male', "Male"), ('female', "Female"), ('other', "Other")],
        string="Gender", default='male')


    @api.onchange('standard')
    def _onchange_seat_availability(self):
        if self.standard:
            self.seats_avail = self.seats_avail - 1

    @api.onchange('dob')
    def compute_age(self):
        from dateutil.relativedelta import relativedelta
        if self.dob:
            now = datetime.now()
            age = relativedelta(now, self.dob)
            years = age.years
            print(years)
            print("age.years + age.months + age.days",age.years + age.months + age.days)
            self.age = f"{years} years, {age.months} months, and {age.days} days."



