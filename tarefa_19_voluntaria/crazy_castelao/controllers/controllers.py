# -*- coding: utf-8 -*-
# from odoo import http


# class CrazyCastelao(http.Controller):
#     @http.route('/crazy_castelao/crazy_castelao', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crazy_castelao/crazy_castelao/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crazy_castelao.listing', {
#             'root': '/crazy_castelao/crazy_castelao',
#             'objects': http.request.env['crazy_castelao.crazy_castelao'].search([]),
#         })

#     @http.route('/crazy_castelao/crazy_castelao/objects/<model("crazy_castelao.crazy_castelao"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crazy_castelao.object', {
#             'object': obj
#         })

