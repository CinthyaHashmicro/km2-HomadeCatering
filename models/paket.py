from odoo import api, fields, models


class Paket(models.Model):
    _name = 'homade.paket'
    _description = 'Daftar macam pilihan paket makanan Homade Catering'

    name = fields.Char(string='Name')
    jenis = fields.Selection(string='Jenis Paket Makanan',selection=[('vege','Vegetarian'),('nonvege','Non-Vegetarian')])
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Char(compute="_compute_harga",string='Harga')
    protein_id = fields.Many2one(comodel_name="homade.protein", 
                                string = "Pilihan Protein", 
                                required=True)
    karbo_id = fields.Many2one(comodel_name="homade.karbohidrat", 
                                string = "Pilihan Karbohidrat", 
                                required=True)
    lauk_id = fields.Many2one(comodel_name="homade.lauk", 
                                string = "Pilihan Lauk", 
                                required=True)
    tambahan_id = fields.Many2one(comodel_name="homade.tambahan", 
                                string = "Pilihan Makanan Tambahan")

    des_protein = fields.Char(compute='_compute_des_protein', string='Deskripsi Protein')

    @api.depends('protein_id','karbo_id','lauk_id','tambahan_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.protein_id.harga + record.karbo_id.harga + record.lauk_id.harga + record.tambahan_id.harga
    
    @api.depends('protein_id')
    def _compute_des_protein(self):
        for record in self:
            record.des_protein = record.protein_id.deskripsi

    des_karbo = fields.Char(compute='_compute_des_karbo', string='Deskripsi Karbohidrat')
    
    @api.depends('karbo_id')
    def _compute_des_karbo(self):
        for record in self:
            record.des_karbo = record.karbo_id.deskripsi
    
    des_lauk = fields.Char(compute='_compute_des_lauk', string='Deskripsi Lauk')
    
    @api.depends('lauk_id')
    def _compute_des_lauk(self):
        for record in self:
            record.des_lauk = record.lauk_id.deskripsi

    des_tambahan = fields.Char(compute='_compute_des_tambahan', string='Deskripsi Makanan Tambahan')
    
    @api.depends('tambahan_id')
    def _compute_des_tambahan(self):
        for record in self:
            record.des_tambahan = record.tambahan_id.deskripsi


    
    
