# -*- coding: utf-8 -*-
# from odoo import http


# class IggaEventos(http.Controller):
#     @http.route('/igga_eventos/igga_eventos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/igga_eventos/igga_eventos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('igga_eventos.listing', {
#             'root': '/igga_eventos/igga_eventos',
#             'objects': http.request.env['igga_eventos.igga_eventos'].search([]),
#         })

#     @http.route('/igga_eventos/igga_eventos/objects/<model("igga_eventos.igga_eventos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('igga_eventos.object', {
#             'object': obj
#         })

