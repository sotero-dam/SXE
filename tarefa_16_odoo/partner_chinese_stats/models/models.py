# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class partner_chinese_stats(models.Model):
#     _name = 'partner_chinese_stats.partner_chinese_stats'
#     _description = 'partner_chinese_stats.partner_chinese_stats'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

