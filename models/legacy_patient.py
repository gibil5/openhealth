# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Patient Legacy 
# 

# Created: 				23 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api

#from datetime import datetime
#from datetime import timedelta
from . import leg_funcs



class PatientLegacy(models.Model):

	#_order = 'write_date desc'

	_description = 'Patient Legacy'

	_inherit = 'openhealth.legacy'



	_name = 'openhealth.legacy.patient'







# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Char 
	FechaRegistro = fields.Char()
	FechaCreacion = fields.Char()
	FechaNacimiento = fields.Char()


	# Datetimes
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






	CODIGOhistoria = fields.Char()

	NombreCompleto = fields.Char()

	NumeroDocumento = fields.Char()


	
	Direccion = fields.Char()

	Distrito = fields.Char()
	
	Telefono1 = fields.Char()
	
	Telefono2 = fields.Char()


	
	Correo = fields.Char()
	
	
	Sexo = fields.Char()





