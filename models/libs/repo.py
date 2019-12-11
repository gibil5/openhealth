# -*- coding: utf-8 -*-
"""
 	Repo. Inherited by Management and Marketing

	Only Data model. No functions.

 	Created: 				28 May 2018
 	Last up: 				 7 Dec 2019
"""
from openerp import models, fields, api

class Repo(models.Model):
	
	_name = 'openhealth.repo'
	
	_inherit='openhealth.django.interface'
	
	#_order = ''



# ----------------------------------------------------------- Inherited ------------------------------------------------------


	# Spacing
	vspace = fields.Char(
			' ', 
			readonly=True
		)



	# Amount Total Year
	total_amount_year = fields.Float(
			'Monto Total Año',
			default=0,
		)


	# Average Total Amount
	avg_total_amount = fields.Float(
			'Promedio Anual',
		)


	# Percentage Total Amount Year
	per_amo_total = fields.Float(
			'Porc Monto Año',
		)

