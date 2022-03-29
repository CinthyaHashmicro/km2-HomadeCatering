from odoo import api, fields, models


class Protein(models.Model):
    _name = 'homade.protein'
    _description = 'Daftar macam pilihan protein Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    img = fields.Binary(string='Gambar')
    
    
