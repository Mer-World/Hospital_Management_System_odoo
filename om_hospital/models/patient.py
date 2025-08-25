from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'  # Model name
    _inherit = ['mail.thread', 'mail.activity.mixin']  
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True,tracking=True)
    age = fields.Integer(string='Age',tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),], string='Gender', required=True)
    active = fields.Boolean(string="Active",default=True)
    
