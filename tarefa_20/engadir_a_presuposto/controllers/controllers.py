# -*- coding: utf-8 -*-
# from odoo import http


# class EngadirAPresuposto(http.Controller):
#     @http.route('/engadir_a_presuposto/engadir_a_presuposto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/engadir_a_presuposto/engadir_a_presuposto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('engadir_a_presuposto.listing', {
#             'root': '/engadir_a_presuposto/engadir_a_presuposto',
#             'objects': http.request.env['engadir_a_presuposto.engadir_a_presuposto'].search([]),
#         })

#     @http.route('/engadir_a_presuposto/engadir_a_presuposto/objects/<model("engadir_a_presuposto.engadir_a_presuposto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('engadir_a_presuposto.object', {
#             'object': obj
#         })

