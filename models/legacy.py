# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Legacy 
# 
# Created: 				24 Feb 2018
# 

from openerp import models, fields, api
from datetime import datetime
from . import leg_funcs




# ----------------------------------------------------------- Legacy ------------------------------------------------------

class Legacy(models.Model):

	_name = 'openhealth.legacy'
	_description = 'Legacy'


	mark = fields.Char(
			string='Mark', 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)





# ----------------------------------------------------------- PatientLegacy ------------------------------------------------------

class PatientLegacy(models.Model):

	_name = 'openhealth.legacy.patient'
	_inherit = 'openhealth.legacy'
	_description = 'Patient Legacy'



	# ----------------------------------------------------------- Vars ------------------------------------------------------

	CODIGOhistoria = fields.Char()

	NombreCompleto = fields.Char()

	NumeroDocumento = fields.Char()
	
	Direccion = fields.Char()

	Distrito = fields.Char()
	
	Telefono1 = fields.Char()
	
	Telefono2 = fields.Char()
	
	Correo = fields.Char()
		
	Sexo = fields.Char()

	FechaRegistro = fields.Char()
	
	FechaCreacion = fields.Char()
	
	FechaNacimiento = fields.Char()

	FechaRegistro_d = fields.Datetime(

			compute='_compute_FechaRegistro_d', 
		)

	@api.multi
	def _compute_FechaRegistro_d(self):		
		for record in self:		
			record.FechaRegistro_d = leg_funcs.get_date_from_char(self,record.FechaRegistro)
			record.FechaRegistro_d = leg_funcs.correct_time(self,record.FechaRegistro_d)


	FechaCreacion_d = fields.Datetime(

			compute='_compute_FechaCreacion_d', 
		)

	@api.multi
	def _compute_FechaCreacion_d(self):		
		for record in self:		
			record.FechaCreacion_d = leg_funcs.get_date_from_char(self,record.FechaCreacion)
			record.FechaCreacion_d = leg_funcs.correct_time(self,record.FechaCreacion_d)

	

	FechaNacimiento_d = fields.Datetime(

			compute='_compute_FechaNacimiento_d', 
		)

	@api.multi
	def _compute_FechaNacimiento_d(self):		
		for record in self:		
			record.FechaNacimiento_d = leg_funcs.get_date_from_char(self,record.FechaNacimiento)
			record.FechaNacimiento_d = leg_funcs.correct_time(self,record.FechaNacimiento_d)








# ----------------------------------------------------------- OrderLegacy ------------------------------------------------------

class OrderLegacy(models.Model):

	_name = 'openhealth.legacy.order'
	_inherit = 'openhealth.legacy'
	_description = 'Order Legacy'



	# ----------------------------------------------------------- Vars ------------------------------------------------------

	nombreejecutivo = fields.Char()

	NumeroSerie = fields.Char()
	
	NumeroFactura = fields.Char()
	
	NombreCompleto = fields.Char()
	
	tipodocumento = fields.Char()
	
	moneda = fields.Char()
	
	neto = fields.Char()
	
	igv = fields.Char()
	
	total = fields.Char()
	
	descripcion = fields.Char()
	
	precioventa = fields.Char()
	
	FechaFactura = fields.Char()

	cantidadtotal = fields.Char()
	
	totalitem = fields.Char()

	serial_nr = fields.Char()



	Punit = fields.Float(

			compute='_compute_Punit', 
		)

	@api.multi
	def _compute_Punit(self):		
		for record in self:		
			record.Punit = float(record.totalitem) / float(record.cantidadtotal)




	FechaFactura_d = fields.Datetime(

			compute='_compute_FechaFactura_d', 
		)

	@api.multi
	def _compute_FechaFactura_d(self):		
		for record in self:		
			record.FechaFactura_d = leg_funcs.get_date_from_char(self,record.FechaFactura)
			record.FechaFactura_d = leg_funcs.correct_time(self,record.FechaFactura_d)









