# -*- coding: utf-8 -*-
#
# 	Repo
# 
# Created: 				28 Mayo 2018
#
from openerp import models, fields, api
#import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np
#import collections


class Repo(models.Model):

	#_inherit='sale.closing'

	_name = 'openhealth.repo'

	#_order = 'create_date desc'
	#_order = 'date_begin asc,name asc'




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





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Set Stats
	@api.multi
	def set_stats(self):  

		print 
		print 'Set Stats'
		print 






# ----------------------------------------------------------- Update Repo ------------------------------------------------------

	# Update orders
	@api.multi
	def update_repo(self):  

		print
		print 'Update Repo'
		print






