# -*- coding: utf-8 -*-
"""
	ReportSaleProduct

	Only Data model. No functions.

 	Created: 			    Nov 2016
	Last up: 	 		 10 Dec 2019
"""

from __future__ import print_function
from openerp import models, fields, api

class ReportSaleProduct(models.Model):
	"""
	Uses:
		Product Item Counter
		Report Order Lines
	Used by:
		Caja
	As: 
		Venta de Productos por Fecha
	"""
	
	_name = 'openhealth.report.sale.product'
	
	#_inherit='openhealth.django.interface'



# ----------------------------------------------------------- Relational ------------------------------------------------------	
	# Item Counter
	item_counter_ids = fields.One2many(
			'openhealth.item.counter', 
			'report_sale_product_id', 
		)


	# Order Lines - For detail
	order_line_ids = fields.One2many(
			'openhealth.report.order_line', 
			'report_sale_product_id', 
		)




# ----------------------------------------------------------- Redefined ------------------------------------------------------
	# Name 
	name = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Title 
	title = fields.Char(
			string="Nombre",
		)



	several_dates = fields.Boolean(
			'Varias Fechas',
			default=False,
		)


	# Totals
	total_qty = fields.Integer(
			string="Cantidad", 
		)

	total = fields.Float(
			string="Total", 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
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
