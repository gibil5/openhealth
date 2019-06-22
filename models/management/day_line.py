# -*- coding: utf-8 -*-
"""
	Day Line

	Created: 			15 Jan 2019
	Last up: 			15 Jan 2019
"""
from __future__ import print_function
import numpy as np
from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars
from . import mgt_funcs

from openerp.addons.openhealth.models.libs import lib

class DayLine(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.management.day.line'

	_inherit = 'openhealth.management.line'

	_order = 'date asc'



# ----------------------------------------------------------- Relational --------------------------
	configurator_emr_id = fields.Many2one(
			'openhealth.configurator.emr'
		)


# ----------------------------------------------------------- Redefined ---------------------------
	amount = fields.Float(
			'Venta por dia',
			digits=(16, 1),
		)


# ----------------------------------------------------------- Primitives --------------------------

	state = fields.Selection(
			selection=[
							('today', 'Hoy'),
							#('holiday', 'Feriado'),
			],
			string='Estado',
		)


	today = fields.Boolean(
			'Hoy',
			default=False,

			compute='_compute_today',
		)

	@api.multi
	#@api.depends('order_line')
	def _compute_today(self):
		for record in self:
			
			if lib.is_today_date(record.date):
			
				record.today = True




	holiday = fields.Boolean(
			'Feriado',
			default=False,
			#readonly=True,
		)





	date = fields.Date(
			'Fecha',
		)

	weekday = fields.Selection(
			selection=ord_vars._weekday_list,
			string='Dia de semana',
		)

	cumulative = fields.Float(
			'Acumulado',
			#digits=(16, 1),
		)

	avg_amount = fields.Float(
			'Promedio diario',
			#digits=(16, 1),
		)


	projection = fields.Float(
			'Proyección a final del mes',
		)

	duration = fields.Float(
			'Duracion',
		)


	nr_days = fields.Float(
			'Nr dias',
		)

	nr_days_total = fields.Float(
			'Total dias',
		)




# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update_projection(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update - Projection')
		self.projection = self.avg_amount * self.nr_days_total

# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update_avg(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update - Average')
		self.avg_amount = self.cumulative / self.nr_days

# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update_amount(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update - amount')

		# Search
		orders, count = mgt_funcs.get_orders_filter_fast(self, self.date, self.date)
		#print(orders)
		#print(count)

		data_amount = []

		for order in orders:

			#data_amount.append(order.amount_total)

			# Sales and CNs
			#if order.state in ['credit_note']:
			#	data_amount.append(-order.amount_total)
			#elif order.state in ['sale']:
			#	data_amount.append(order.amount_total)

			# All
			data_amount.append(order.x_amount_flow)



		self.x_count = len(data_amount)
		if self.x_count != 0:
			self.amount = np.sum(data_amount)

			#amax = np.amax(self.data)
			#amin = np.amin(self.data)
			# Mean of sales, compounded with number of days
			#self.avg_amount = np.mean(data_amount)			# Not correct !

	# update_amount
