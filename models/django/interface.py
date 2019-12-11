# -*- coding: utf-8 -*-
"""
	Django - Interface

	Data model. And functions.

 	Created: 				10 Dec 2019
 	Last up: 				10 Dec 2019
"""
from openerp import models, fields, api

class DjangoInterface(models.Model):
	
	_name = 'openhealth.django.interface'
	
	#_inherit=''
	
	#_order = 'name'


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




# ----------------------------------------------------------- Repo ------------------------------------------------------
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





# ----------------------------------------------------- Django Interface --------------------------

	@api.multi
	def set_state(self, state):
		"""
		Django interface
		so_model.set_state(state)
		"""
		print()
		print('Set State')
		self.state = state



	@api.multi
	def get_name(self):
		"""
		Django interface
		"""
		print()
		print('Get name')
		return self.name



	@api.multi
	def get_date_begin(self):
		"""
		Django interface
		"""
		print()
		print('Get date')
		return self.date_begin


	@api.multi
	def get_date_end(self):
		"""
		Django interface
		"""
		print()
		print('Get date')
		return self.date_end



	@api.multi
	def get_date_test(self):
		"""
		Django interface
		"""
		print()
		print('Get date')
		return self.date_test




	@api.multi
	def get_total(self):
		"""
		Django interface
		"""
		print()
		print('Get total')
		if self.total_amount not in [False]:
			return self.total_amount
		else:
			return 0



	@api.multi
	def get_count(self):
		"""
		Django interface
		"""
		print()
		print('Get count')
		if self.total_count not in [False]:
			return self.total_count
		else:
			return 0



	@api.multi
	def get_state(self):
		"""
		Django interface
		"""
		print()
		print('Get state')
		return self.state


