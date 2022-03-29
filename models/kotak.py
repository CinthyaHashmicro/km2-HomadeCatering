from odoo import api, fields, models


class Kotak(models.Model):
    _name = 'homade.kotak'
    _description = 'Daftar macam pilihan kotak packaging Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')

    
