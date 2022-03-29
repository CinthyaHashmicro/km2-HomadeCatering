from odoo import api, fields, models


class Lauk(models.Model):
    _name = 'homade.lauk'
    _description = 'Daftar macam pilihan Lauk Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    
