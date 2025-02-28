# -*- coding: utf-8 -*-

from odoo import models, fields

class Proveedor(models.Model):
    _name = 'igga_eventos.proveedor'
    _description = 'Proveedor'

    nombre = fields.Char(string="Nombre", required=True)
    servicio = fields.Char(string="Servicio", required=True)
    costo = fields.Float(string="Costo", required=True)
    #relación con el modelo evento 
    evento_ids = fields.Many2many(
        'igga_eventos.evento',  #modelo relacionado
        'evento_proveedor_rel', # tabla intermedia
        'proveedor_id', #campo del proveedor en la tabla
        'evento_id',  #campo del evento en la tabla intermedia
        string="Eventos"
    )

