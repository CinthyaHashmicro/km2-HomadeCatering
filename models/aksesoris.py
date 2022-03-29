from odoo import api, fields, models


class Aksesoris(models.Model):
    _name = 'homade.aksesoris'
    _description = 'Daftar macam pilihan aksesoris packaging Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    
    
