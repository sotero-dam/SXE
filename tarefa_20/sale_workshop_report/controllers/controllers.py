# -*- coding: utf-8 -*-
# from odoo import http


# class SaleWorkshopReport(http.Controller):
#     @http.route('/sale_workshop_report/sale_workshop_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_workshop_report/sale_workshop_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_workshop_report.listing', {
#             'root': '/sale_workshop_report/sale_workshop_report',
#             'objects': http.request.env['sale_workshop_report.sale_workshop_report'].search([]),
#         })

#     @http.route('/sale_workshop_report/sale_workshop_report/objects/<model("sale_workshop_report.sale_workshop_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_workshop_report.object', {
#             'object': obj
#         })

