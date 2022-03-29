from odoo import api, fields, models


class Tambahan(models.Model):
    _name = 'homade.tambahan'
    _description = 'Daftar macam pilihan makanan tambahan Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    
    
