from odoo import models, fields, api

class videojuego(models.Model):
	_name = 'mercado.videojuego'
	_description = 'Modelo de videojuego'

	name = fields.Char(string='Código', required=True)
	nombre = fields.Char(string='Nombre',required=True)
	genero = fields.Char(string='Género(s)',required=False)
	plataforma = fields.Char(string="Plataforma(s)", required=True)
	lanzamiento = fields.Date(string="Fecha de lanzamiento")
	tienda = fields.Many2many("mercado.tienda", string = "Tienda(s)")
	preciobase = fields.Float(string="Precio base(€)", required = True)
	impuesto = fields.Many2one("mercado.impuesto", string="Impuesto", required=True)
	pvp = fields.Float(string="PVP(€)", readonly=True, compute="_get_total")

	@api.depends('preciobase')
	def _get_total(self):
		for vj in self:
			vj.pvp = vj.preciobase + (vj.preciobase * (vj.impuesto.cantidad/100))

class impuesto(models.Model):
	_name = 'mercado.impuesto'
	_description = 'Impuestos'
	name = fields.Char('Tipo', required = True)
	cantidad = fields.Integer(string ='Cantidad(%)', required=True)

class tienda(models.Model):
	_name = 'mercado.tienda'
	_description = 'Modelo de tienda'
	name = fields.Char('CIF', required=True, size=9)
	nombre = fields.Char(string='Nombre', required=True)
	localidad = fields.Char(string='Localidad', required=True)
	provincia = fields.Char(string='Provincia', required=True)
	productos = fields.Many2many("mercado.videojuego", "tienda",string='Videojuegos')









