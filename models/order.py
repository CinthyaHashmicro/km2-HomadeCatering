from email.policy import default
from odoo import api, fields, models
import datetime
from odoo.exceptions import ValidationError 


class Order(models.Model):
    _name = 'homade.order'
    _description = 'Order paket makanan lengkap dengan packaging Homade Catering'

    orderdetails_ids = fields.One2many(
        comodel_name='homade.orderdetails', 
        inverse_name='order_id', 
        string='Detail Order')
    customer_id = fields.Many2one(comodel_name="res.partner", 
                                string = "Customer", 
                                required=True,
                                domain = "[('is_customer','=','true')]")
    alamat = fields.Char(string='Alamat Pengiriman',required=True)
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    name = fields.Char(string='Kode Order',required=True)
    metode_bayar = fields.Selection(string='Metode Pembayaran',selection=[('kredit','Kredit'),('cash','Cash')],required=True)
    sudah_dikirim = fields.Boolean(string='sudah Dikirim', default = False)
    tanggal_pesan = fields.Date(string='Tanggal Pemesanan', default=fields.Date.today(),required=True)
    tanggal_kirim = fields.Datetime(string = 'Tanggal Pengiriman', default = fields.Datetime.now() + datetime.timedelta(days=1),required=True)
    
    @api.depends('orderdetails_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['homade.orderdetails'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total = a
    
    def kembali_barang(self):
        pass
    


class Orderdetails(models.Model):
    _name = 'homade.orderdetails'
    _description = 'Order detail dari Order'

    makanan_id = fields.Many2one(comodel_name='homade.paket', string='Paket Makanan')
    package_id = fields.Many2one(comodel_name='homade.package', string='Packaging Makanan')
    order_id = fields.Many2one(comodel_name='homade.order', string='Order')
    name = fields.Selection(string='Name', selection=[('makanan', 'Paket Makanan'),('packaging', 'Packaging Makanan')])
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Jumlah')
    harga_satuanm = fields.Integer(compute='_compute_harga_satuanm', string='Harga Makanan')
    harga_satuanp = fields.Integer(compute='_compute_harga_satuanp', string='Harga Packaging')

    @api.constrains('qty')
    def _check_stock(self):
        for record in self:
            bahan = self.env['homade.package'].search([('stok','<',record.qty),('id','=',record.id)])
            if bahan:
                raise ValidationError("Stok packaging yang dipilih tidak cukup")
    
    @api.depends('makanan_id')
    def _compute_harga_satuanm(self):
        for record in self:
            record.harga_satuanm = record.makanan_id.harga
    
    @api.depends('package_id')
    def _compute_harga_satuanp(self):
        for record in self:
            record.harga_satuanp = record.package_id.harga

    @api.depends('harga_satuanm','harga_satuanp','qty')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuanm * record.qty + record.harga_satuanp * record.qty
    

    @api.model
    def create(self,vals):
        record = super(Orderdetails, self).create(vals)
        if record.qty:
            self.env['homade.package'].search([('id','=',record.package_id.id)]).write({'stok':record.package_id.stok-record.qty})
            return record

    
        

    
        
    
    