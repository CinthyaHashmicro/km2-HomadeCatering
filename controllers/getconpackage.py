from odoo import http, fields, models
from odoo.http import request
import json

class PackagingCon(http.Controller):
    @http.route(['/packaging','/packaging/<int:idnya>'],auth='public', methods = ['GET'], csrf = True)
    def getPackaging(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            package = request.env['homade.package'].search([])
            for k in package:
                value.append({"id": k.id,
                            "namapackage" : k.name,
                            "deskripsi" : k.deskripsi,
                            "stok_tersedia" : k.stok,
                            "harga" : k.harga,})
            return json.dumps(value)
        else:
            packageid = request.env['homade.package'].search([('id','=',idnya)])
            for k in packageid:
                value.append({"id": k.id,
                            "namapackage" : k.name,
                            "deskripsi" : k.deskripsi,
                            "stok_tersedia" : k.stok,
                            "harga" : k.harga})
            return json.dumps(value)

    @http.route('/createpackaging',auth = 'user', type = 'json', methods = ['POST'])
    def createPackage(self, **kw):
        if request.jsonrequest:
            if kw['name']:
                vals = {
                    'name' : kw['name'],
                    'deskripsi' : kw['deskripsi'],
                    'stok' : kw['stok'],
                    'harga' : kw['harga'],
                    'kotak' : kw['kotak_id'],
                    'aksesoris' : kw['aksesoris_id']
                }
                packagebaru = request.env['homade.package'].create(vals)
                args = {'succeed': True, "ID" : packagebaru}
                return args

