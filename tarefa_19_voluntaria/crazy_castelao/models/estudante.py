# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError 

# NIVEL 3 Herdanza 
class ResPartner(models.Model):
    _inherit = 'res.partner'
    acoge_fct = fields.Boolean(string="Acolle FCT?")

class EscolaEstudante(models.Model):
    _name = 'escola.estudante'
    _description = 'Ficha de Alumno'

    # NIVEL 1 Básicos, dinme conta tarde de que xa me daban un arquivo en esemtia
    name = fields.Char(string="Nombre Completo", required=True)
    ciclo = fields.Char(string="Ciclo Formativo")
    horas_ciclo = fields.Integer(string="Horas del Ciclo", default=2000)
    horas_aprobadas = fields.Integer(string="Horas Aprobadas")
    nota_media = fields.Float(string="Nota Media")
    data_nacemento = fields.Date(string="Fecha de Nacimento")
    idade = fields.Integer(string="Edad")
    email = fields.Char(string="Correo Electrónico")
    foto = fields.Binary(string="Foto")
    
    via_acceso = fields.Selection([
        ('eso', 'ESO'), ('medio', 'Ciclo Medio'), ('bach', 'Bachillerato'),
        ('proba', 'Prueba de Acceso'), ('outros', 'Otros')
    ], string="Vía de Acceso")

    estado = fields.Selection([
        ('fct', 'FCT'), ('en_curso', 'EN CURSO')
    ], string="Estado", default='en_curso')

    # NIVEL 2 Cálculo de progreso
    progreso_actual = fields.Float(string="Progreso Actual", compute="_compute_progreso", store=True)

    @api.depends('horas_aprobadas', 'horas_ciclo')
    def _compute_progreso(self):
        for record in self:
            if record.horas_ciclo > 0:
                record.progreso_actual = (record.horas_aprobadas / record.horas_ciclo) * 100
            else:
                record.progreso_actual = 0.0

    # NIVEL 3 Empresa
    empresa_id = fields.Many2one(
        'res.partner', 
        string="Centro de Prácticas",
        domain="[('is_company', '=', True), ('acoge_fct', '=', True)]"
    )

    # NIVEL 4 Titor
    tutor_id = fields.Many2one(
        'res.partner', 
        string="Tutor na Empresa",
        domain="[('parent_id', '=', empresa_id)]"
    )

    @api.onchange('empresa_id')
    def _onchange_empresa_id(self):
        self.tutor_id = False

    # NIVEL 5 Integridade
    @api.constrains('empresa_id', 'horas_aprobadas', 'horas_ciclo')
    def _check_progreso_empresa(self):
        for record in self:
            progreso = (record.horas_aprobadas / record.horas_ciclo * 100) if record.horas_ciclo else 0
            if record.empresa_id and progreso < 50:
                raise ValidationError(
                    "Erro de Integridade: Non se pode asignar unha empresa se o "
                    "alumno non ten superado o 50%% das horas." % progreso
                )