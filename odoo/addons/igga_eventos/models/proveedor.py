# -*- coding: utf-8 -*-

from odoo import models, fields

class Proveedor(models.Model):
    _name = 'igga_eventos.proveedor'
    _description = 'Proveedor'

    nombre = fields.Char(string="Nombre", required=True)
    servicio = fields.Char(string="Servicio", required=True)
    costo = fields.Float(string="Costo", required=True)
    evento_ids = fields.Many2many('igga_eventos.evento', string="Eventos")