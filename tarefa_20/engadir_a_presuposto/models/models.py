# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class engadir_a_presuposto(models.Model):
#     _name = 'engadir_a_presuposto.engadir_a_presuposto'
#     _description = 'engadir_a_presuposto.engadir_a_presuposto'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

