# -*- coding: utf-8 -*-
# from odoo import http


# class Mercado(http.Controller):
#     @http.route('/mercado/mercado/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mercado/mercado/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mercado.listing', {
#             'root': '/mercado/mercado',
#             'objects': http.request.env['mercado.mercado'].search([]),
#         })

#     @http.route('/mercado/mercado/objects/<model("mercado.mercado"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mercado.object', {
#             'object': obj
#         })
