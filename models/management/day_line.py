# -*- coding: utf-8 -*-
"""
	Day Line

	Created: 			15 Jan 2019
	Last up: 			15 Jan 2019
"""
from __future__ import print_function

from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars

class DayLine(models.Model):
	"""
	high level support for doing this and that.
	"""

	_name = 'openhealth.management.day.line'

	_inherit = 'openhealth.management.line'

	_order = 'amount desc'




# ----------------------------------------------------------- Redefined ---------------------------
	amount = fields.Float(
			'Venta por dia',
			digits=(16, 1),
		)


# ----------------------------------------------------------- Primitives --------------------------

	date = fields.Date(
			'Fecha',
		)

	week_day = fields.Selection(
			selection=ord_vars._week_day_list,
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

	nr_days = fields.Integer(
			'Nr dias',
		)

	projection = fields.Float(
			'Proyección a final del mes',
		)
