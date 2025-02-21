# -*- coding: utf-8 -*-
from odoo import models, fields

class Evento(models.Model):
    _name = 'igga_eventos.evento'
    _description = 'Evento'

    name = fields.Char(string="Nombre del Evento", required=True)
    fecha = fields.Date(string="Fecha del Evento", required=True)
    lugar = fields.Char(string="Lugar del Evento", required=True)
    cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)
    estado = fields.Selection([
        ('planificacion', 'Planificacion'),
        ('en_curso', 'En curso'),
        ('finalizado', 'Finalizado')
    ], string="Estado", default='planificacion')
    imagen = fields.Binary(string="Imagen del Evento")
    tarea_ids = fields.One2many('igga_eventos.tarea', 'evento_id', string="Tareas")
    invitado_ids = fields.One2many('igga_eventos.invitado', 'evento_id', string="Invitados")
