from odoo import models, fields, api

class CafeteroSueno(models.Model):
    _name = 'cafetero.sueno'
    _description = 'Calcula bebida sopor'

    alumno = fields.Char(string='Nome do Alumno', required=True)
    nivel_sueno = fields.Integer(string='Nivel de Sono (1-10)', required=True)
    
    bebida_recomendada = fields.Char(
        string='Bebida Recomendada',
        compute='_compute_bebida_recomendada',
        store=True,
    )

    @api.depends('nivel_sueno')
    def _compute_bebida_recomendada(self):
        for record in self:
            sueno = record.nivel_sueno
            
            if 1 <= sueno <= 3:
                record.bebida_recomendada = 'Café con leite (meh, básico)'
            elif 4 <= sueno <= 6:
                record.bebida_recomendada = 'Café só longo (día regular)'
            elif 7 <= sueno <= 9:
                record.bebida_recomendada = 'Café só larguísimo (día durísimo)'
            elif sueno == 10:
                record.bebida_recomendada = 'Inxección de adrenalina (imprime voante hospital)'
            else:
                record.bebida_recomendada = 'Ey, iso non vale'