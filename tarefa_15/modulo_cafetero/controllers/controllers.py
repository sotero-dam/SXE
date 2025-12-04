# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloCafetero(http.Controller):
#     @http.route('/modulo_cafetero/modulo_cafetero', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_cafetero/modulo_cafetero/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_cafetero.listing', {
#             'root': '/modulo_cafetero/modulo_cafetero',
#             'objects': http.request.env['modulo_cafetero.modulo_cafetero'].search([]),
#         })

#     @http.route('/modulo_cafetero/modulo_cafetero/objects/<model("modulo_cafetero.modulo_cafetero"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_cafetero.object', {
#             'object': obj
#         })

