from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'  # Model name
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),], string='Gender', required=True)
