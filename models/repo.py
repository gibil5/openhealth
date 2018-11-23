# -*- coding: utf-8 -*-
"""
 	Repo - Inherited by Management and Marketing

 	Created: 				28 May 2018
 	Last up: 				23 Nov 2018
"""
from openerp import models, fields, api

class Repo(models.Model):
	_name = 'openhealth.repo'
	#_inherit=''
	#_order = ''


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
		)

	# Count
	total_count = fields.Integer(
			#'Total Ventas',
			#'Nr Pacientes',
			'Nr Ventas',
			readonly=True, 
		)

	# Spacing
	vspace = fields.Char(
			' ', 
			readonly=True
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
