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
	#_inherit=''
	#_order = ''



# ----------------------------------------------------------- Django ------------------------------------------------------
	# State
	state = fields.Selection(
			
			selection=[
							('stable', 'Estable'),
							('unstable', 'Inestable'),
			],

			string='Estado',
			#readonly=False,
			default='unstable',
			#index=True,
		)


	# Date Test
	date_test = fields.Datetime(
			string="Fecha Test", 
		)



# ----------------------------------------------------------- Inherited ------------------------------------------------------

	# Name 
	name = fields.Char(
			string="Nombre", 		
			required=True, 
		)

	# Dates 
	date_begin = fields.Date(
			string="Fecha Inicio", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)

	date_end = fields.Date(
			string="Fecha Fin", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)

	# Amount
	total_amount = fields.Float(
			#'Total Monto',
			#'Total',
			'Monto Total',
			readonly=True,

			default=0,
		)

	# Count
	total_count = fields.Integer(
			#'Total Ventas',
			'Nr Ventas',
			readonly=True, 
		)

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




# ----------------------------------------------------------- Actions -----------------------------
	# Set Stats
	@api.multi
	def set_stats(self):
		#print
		#print 'Set Stats'
		pass

	# Update orders
	@api.multi
	def update_repo(self):
		#print
		#print 'Update Repo'
		pass

