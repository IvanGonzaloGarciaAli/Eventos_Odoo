# -*- coding: utf-8 -*-
from odoo import models, fields,api

class Evento(models.Model):
    _name = 'igga_eventos.evento'
    _description = 'Evento'

    name = fields.Char(string="Nombre del Evento", required=True)
    fecha = fields.Date(string="Fecha del Evento", required=True)
    lugar = fields.Char(string="Lugar del Evento", required=True)
    #Relacion many2one ya que un cliente puede tener muchos eventos
    cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)
    estado = fields.Selection([
        ('planificacion', 'Planificacion'),
        ('en_curso', 'En curso'),
        ('finalizado', 'Finalizado')
    ], string="Estado", default='planificacion')
    imagen = fields.Binary(string="Imagen del Evento")
    #Un evento tendrá muchas tareas asociadas a este
    tarea_ids = fields.One2many('igga_eventos.tarea', 'evento_id', string="Tareas")
    #Un evento tendrá muchos invitados
    invitado_ids = fields.One2many('igga_eventos.invitado', 'evento_id', string="Invitados")
    #Un mismo proveedor puede pertenecer a varios eventos, lo que también significa que en un evento existen muchos proveedores
    proveedor_ids = fields.Many2many(
        'igga_eventos.proveedor',  #modelo relacionado
        'evento_proveedor_rel',  # tabla intermedia
        'evento_id',  #campo de la tabla que hace referencia al evento
        'proveedor_id', #campo de la tabla que hace referencia al proveedor
        string="Proveedores"
    )
    #Campo calculado que mostrará el precio final del evento(solo teniendo en cuenta el precio de los proveedores)
    total_costo = fields.Float("Costo Total", compute="_compute_total_costo", store=True)
    #Método que calcula el costo total del evento sumando los costos de los proveedores
    @api.depends('proveedor_ids.costo')
    def _compute_total_costo(self):
        # Sumo el costo de todos los proveedores relacionados con el evento
        for record in self:
            record.total_costo = sum(proveedor.costo for proveedor in record.proveedor_ids)