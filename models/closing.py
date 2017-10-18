# -*- coding: utf-8 -*-
#
#
# 	Closing 
# 
# Created: 				18 Oct 2017
# Last updated: 	 	18 Oct 2017
#



from openerp import models, fields, api
import datetime


class Closing(models.Model):
	
	#_inherit='sale.closing'
	_name = 'openhealth.closing'
	




	# Name 
	name = fields.Char(
			string="Cierre de Caja #", 
			
			#compute='_compute_name', 
		)


	vspace = fields.Char(
			' ', 
			readonly=True
		)



	date = fields.Datetime(
			
			string="Fecha y hora", 

			default = fields.Date.today, 
			
			#readonly=True,

			
			#required=False, 
			required=True, 

			#compute='_compute_x_appointment_date', 
		)

