# -*- coding: utf-8 -*-
from odoo import models,fields

class Libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Libro'

    name = fields.Char(string='Título',required=True,help="Introduce el título del libro")
    precio = fields.Float(string='Precio',required=True,help="Introduce el precio")
    ejemplares = fields.Integer(string='Ejemplares',required=True,help="Introduce el número de ejemplares en inventario")
    fecha_compra = fields.Date(string='Fecha de compra',required=True,help="Introduce fecha de compra")
    segmano = fields.Boolean(string='Segunda mano',required=True,help="Marca si es de segunda mano")
    estado = fields.Selection([
        ('0','Bueno'),
        ('1','Regular'),
        ('2','Malo')
    ], string = 'Estado',default='0')