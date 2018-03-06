# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Order Legacy 
# 

# Created: 				5 Mar 2018
# Last updated: 	 	id


from openerp import models, fields, api

#from datetime import datetime
#from datetime import timedelta
from . import leg_funcs



class OrderLegacy(models.Model):

	#_order = 'write_date desc'

	_description = 'Order Legacy'

	_inherit = 'openhealth.legacy'



	_name = 'openhealth.legacy.order'







# ----------------------------------------------------------- Primitives ------------------------------------------------------

	#RazonSocialEmp,
	#RucEmp,
	#codigoejecutivo,
	#codigomoneda,
	#nnlocal

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


# ----------------------------------------------------------- Computed ------------------------------------------------------


	serial_nr = fields.Char(

			compute='_compute_serial_nr', 
		)

	@api.multi
	def _compute_serial_nr(self):		
		for record in self:		

			record.serial_nr = record.NumeroSerie + '-' + record.NumeroFactura








	Punit = fields.Float(

			compute='_compute_Punit', 
		)

	@api.multi
	def _compute_Punit(self):		
		for record in self:		

			record.Punit = float(record.totalitem) / float(record.cantidadtotal)









	# Datetimes
	FechaFactura_d = fields.Datetime(

			compute='_compute_FechaFactura_d', 
		)

	@api.multi
	def _compute_FechaFactura_d(self):		
		for record in self:		

			record.FechaFactura_d = leg_funcs.get_date_from_char(self,record.FechaFactura)
	
			record.FechaFactura_d = leg_funcs.correct_time(self,record.FechaFactura_d)









