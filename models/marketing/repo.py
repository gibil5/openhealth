# -*- coding: utf-8 -*-
"""
 	Repo. Inherited by Management and Marketing - Dep !

	Only Data model. No functions.

 	Created: 			28 May 2018
	Last up: 			 6 dec 2020
"""
from openerp import models, fields, api


class Repo(models.Model):
	_name = 'openhealth.repo'
	#_inherit='openhealth.django.interface'


# ----------------------------------------------------------- Inherited ------------------------------------------------------
	# Average Total Amount
	avg_total_amount = fields.Float(
			'Promedio Anual',
		)

# -------------------------------------------------- Inherited from interface.py ----------------------------


# ----------------------------------------------------------- Django -----------
	# Date Test
	date_test = fields.Datetime(
			string="Fecha Test", 
		)

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

# ----------------------------------------------------------- Configurator -----
	# Default Configurator
	def _get_default_configurator(self):
		configurator = self.env['openhealth.configurator.emr'].search([
																			('x_type', 'in', ['emr']),
																		],
																			#order='date_begin,name asc',
																			limit=1,
			)
		return configurator

	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			
			default=_get_default_configurator,
		)


# ----------------------------------------------------------- Repo -------------
	# Name 
	name = fields.Char(
			string="Nombre", 		
			required=True, 
		)

	# Dates 
	date_begin = fields.Date(
			string="Fecha Inicio", 
			default = fields.Date.today, 
			required=True, 
		)

	date_end = fields.Date(
			string="Fecha Fin", 
			default = fields.Date.today, 
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

# ----------------------------------------------------- Django Interface -------
	@api.multi
	def get_configurator(self):
		"""
		Django interface
		"""
		print()
		print('Get state')
		return self.configurator.name

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

	# Dates
	#@api.multi
	#def get_date(self):
	#	"""
	#	Django interface
	#	"""
	#	print()
	#	print('Get date')
	#	return self.date

	@api.multi
	def get_date_begin(self):
		"""
		Django interface
		"""
		print()
		print('Get date begin')
		return self.date_begin

	@api.multi
	def get_date_end(self):
		"""
		Django interface
		"""
		print()
		print('Get date end')
		return self.date_end

	@api.multi
	def get_date_test(self):
		"""
		Django interface
		"""
		print()
		print('Get date test')
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


