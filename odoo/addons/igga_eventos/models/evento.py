# -*- coding: utf-8 -*-
from odoo import models, fields

class Evento(models.Model):
    _name = 'igga_eventos.evento'
    _description = 'Evento'

    name = fields.Char(string="Nombre del Evento", required=True)
    fecha = fields.Date(string="Fecha del Evento", required=True)
    lugar = fields.Char(string="Lugar del Evento", required=True)
