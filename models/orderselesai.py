from email.policy import default
from odoo import api, fields, models


class Pengiriman(models.Model):
    _name = 'homade.pengiriman'
    _description = 'Daftar order Homade Catering yang sudah dikirim'

    name = fields.Char(compute='_compute_nama_penyewa', string='Nama Customer')
    order_id = fields.Many2one(
        comodel_name='homade.order', 
        string='Order',
        domain = "[('sudah_dikirim','=',False)]")
    tgl_pengiriman = fields.Date(string='Tanggal Pengiriman', default = fields.Date.today())
    tagihan = fields.Char(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total

    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.name = self.env['homade.order'].search([('id','=',record.order_id.id)]).mapped('customer_id').name

    @api.model
    def create(self,vals):
        record = super(Pengiriman, self).create(vals)
        if record.tgl_pengiriman:
            self.env['homade.order'].search([('id','=',record.order_id.id)]).write({'sudah_dikirim':True})
            if record.order_id.metode_bayar == 'kredit':
                self.env['homade.akunting'].create({'kredit':record.tagihan, 'name' : record.name})
            else:
                self.env['homade.akunting'].create({'cash':record.tagihan, 'name' : record.name})
            return record

    def unlink(self):
        for wiku in self:
            self.env['homade.order'].search([('id','=',wiku.order_id.id)]).write({'sudah_dikirim':False})
        record = super(Pengiriman, self).unlink()
