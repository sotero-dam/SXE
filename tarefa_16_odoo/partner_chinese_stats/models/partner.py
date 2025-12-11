from odoo import fields, models, api
from datetime import date

class ResPartner(models.Model):
    _inherit = 'res.partner' 

    birth_date = fields.Date(string='Fecha de Nacimiento')
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)

    partner_code = fields.Char(string='Código de Socio')

    fidelity_level = fields.Char(string='Nivel de Fidelidad', compute='_compute_fidelity_level', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birth_date:
                record.age = today.year - record.birth_date.year - \
                             ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
            else:
                record.age = 0

    chinese_zodiac = fields.Selection([
        ('rat', 'Rata'), ('ox', 'Buey'), ('tiger', 'Tigre'), 
        ('rabbit', 'Conejo'), ('dragon', 'Dragón'), ('snake', 'Serpiente'), 
        ('horse', 'Caballo'), ('goat', 'Cabra'), ('monkey', 'Mono'), 
        ('rooster', 'Gallo'), ('dog', 'Perro'), ('pig', 'Cerdo'),
    ], string='Horóscopo Chino', compute='_compute_chinese_zodiac', store=True)

    @api.depends('birth_date')
    def _compute_chinese_zodiac(self):
        zodiac_signs = [
            'monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 
            'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'goat'
        ]
        
        for record in self:
            if record.birth_date:
                year = record.birth_date.year
                index = (year - 1908) % 12
                record.chinese_zodiac = zodiac_signs[index]
            else:
                record.chinese_zodiac = False

 
    @api.depends('partner_code')
    def _compute_fidelity_level(self):
        for record in self:
            code = record.partner_code
            if code:
                if code.startswith('G') or code.startswith('g'):
                    record.fidelity_level = 'Gold'
                else:
                    record.fidelity_level = 'Premium'
            else:
                record.fidelity_level = 'Estándar'