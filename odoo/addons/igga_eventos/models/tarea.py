# -*- coding: utf-8 -*-
from odoo import models, fields

class Tarea(models.Model):
    _name = 'igga_eventos.tarea'
    _description = 'Tarea'

    descripcion = fields.Text(string="Descripcion", required=True)
    responsable_id = fields.Many2one('res.users', string="Responsable", required=True)
    fecha_limite = fields.Date(string="Fecha de limite", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada')
    ], string="Estado", default='pendiente')
    evento_id = fields.Many2one('igga_eventos.evento', string="Evento", required=True)
