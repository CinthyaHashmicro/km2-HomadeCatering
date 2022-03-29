from odoo import api, fields, models


class Karbohidrat(models.Model):
    _name = 'homade.karbohidrat'
    _description = 'Daftar macam pilihan karbohidrat Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')