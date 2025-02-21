# -*- coding: utf-8 -*-

from odoo import models, fields

class Invitado(models.Model):
    _name = 'igga_eventos.invitado'
    _description = 'Invitado'

    nombre = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Correo Electrónico", required=True)
    confirmacion = fields.Boolean(string="Confirmación", default=False)
    evento_id = fields.Many2one('igga_eventos.evento', string="Evento", required=True)