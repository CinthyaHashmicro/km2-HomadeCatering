from odoo import api, fields, models


class Package(models.Model):
    _name = 'homade.package'
    _description = 'Daftar macam pilihan paket packaging Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok Paket Packaging')
    
    kotak_id = fields.Many2one(comodel_name="homade.kotak", 
                                string = "Pilihan Kotak", 
                                required=True)
    aksesoris_id = fields.Many2one(comodel_name="homade.aksesoris", 
                                string='Pilihan Aksesoris',
                                required=True)
    des_kotak = fields.Char(compute='_compute_des_kotak', string='Deskripsi Kotak')
    
    @api.depends('kotak_id')
    def _compute_des_kotak(self):
        for record in self:
            record.des_kotak = record.kotak_id.deskripsi
    
    des_acc = fields.Char(compute='_compute_des_acc', string='Deskripsi Aksesoris')
    
    @api.depends('aksesoris_id')
    def _compute_des_acc(self):
        for record in self:
            record.des_acc = record.aksesoris_id.deskripsi

    
    
