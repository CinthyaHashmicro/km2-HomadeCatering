# -*- coding: utf-8 -*-
# from odoo import http


# class HomadeCatering(http.Controller):
#     @http.route('/homade_catering/homade_catering/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/homade_catering/homade_catering/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('homade_catering.listing', {
#             'root': '/homade_catering/homade_catering',
#             'objects': http.request.env['homade_catering.homade_catering'].search([]),
#         })

#     @http.route('/homade_catering/homade_catering/objects/<model("homade_catering.homade_catering"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('homade_catering.object', {
#             'object': obj
#         })
