# -*- coding: utf-8 -*-
"""
	Productivity Day - Simplified version of Day Line - Just an empty shell

	Created: 			 8 dec 2019
	Last up: 	 		29 mar 2021
"""
from __future__ import print_function
from __future__ import absolute_import

import numpy as np
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars

#from openerp.addons.openhealth.models.libs import lib
#from openerp.addons.openhealth.models.commons.libs import lib
from openerp.addons.openhealth.models.commons.libs import commons_lib as lib

#from .lib import mgt_db
from .management_db import ManagementDb

# -------------------------------------------------------------------------------------------------
#class ProductivityDay(models.Model):
class MgtProductivityDay(models.Model):
	"""
	Productivity Day
	"""
	_name = 'productivity.day'


# ----------------------------------------------------------- Interface -------
	management_id = fields.Many2one(
			'openhealth.management',
			ondelete='cascade',  	# When the management is deleted, the productivity_day is also deleted
			required=True,
		)

	#configurator_emr_id = fields.Many2one(
	#		'openhealth.configurator.emr',
			#required=True,
	#	)


# -------------------------------------------------- Required at creation ------
	name = fields.Char(
			'Name',
			required=True,
		)

	date = fields.Date(
			'Fecha',
			required=True,
		)

	weekday = fields.Selection(
			selection=ord_vars._weekday_list,
			string='Dia de semana',
			required=True,
		)

	duration = fields.Float(
			'Duracion',
			required=True,
		)

# ----------------------------------------------------------- Computes ---------
	today = fields.Boolean(
			'Hoy',
			default=False,
			compute='_compute_today',
		)
	@api.multi
	def _compute_today(self):
		for record in self:
			if lib.is_today_date(record.date):
				record.today = True

# -------------------------------------------- Primitives - after creation -----
	holiday = fields.Boolean(
			'Feriado',
			default=False,
		)

	amount = fields.Float(
			'Venta por dia',
			digits=(16, 1),
		)

	# Cumulative
	cumulative = fields.Float(
			'Acumulado',
		)

	nr_days = fields.Float(
			'Nr dias',
		)

	nr_days_total = fields.Float(
			'Total dias',
		)

	# Average
	avg_amount = fields.Float(
			'Promedio diario',
		)

	projection = fields.Float(
			'Proyección a final del mes',
		)

# ----------------------------------------------------------- Methods ------------------------------
	# Update
	@api.multi
	def update_amount(self):
		"""
		Update Amount
		"""
		#print()
		#print('MgtProductivityDay - Update amount')

		# Init
		data_amount = []

		# Search
		#orders, count = mgt_db.get_orders_filter_fast(self, self.date, self.date)
		orders, count = ManagementDb.get_orders_filter_fast(self, self.date, self.date)
		#print(orders)
		#print(count)

		# All
		for order in orders:
			data_amount.append(order.x_amount_flow)

		# Total
		self.x_count = len(data_amount)
		if self.x_count != 0:
			self.amount = np.sum(data_amount)
	# update_amount

# ----------------------------------------------------------- Update Average ------------------------------
	# Update
	@api.multi
	def update_avg(self):
		"""
		Update Average
		"""
		self.avg_amount = self.cumulative / self.nr_days

# ----------------------------------------------------------- Update Projection ------------------------------
	# Update
	@api.multi
	def update_projection(self):
		"""
		Update Projection
		"""
		self.projection = self.avg_amount * self.nr_days_total
