# -*- coding: utf-8 -*-
"""
	Productivity Day
	Simplified version of Day Line

	Just an empty shell

	Created: 			 8 Dec 2019
	Last up: 			 8 Dec 2019
"""

from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars


class ProductivityDay(models.Model):
	"""
	Productivity Day
	All names must be extremely descriptive
	"""
	_name = 'productivity.day'


# ----------------------------------------------------------- Relational --------------------------

	management_id = fields.Many2one(
			'openhealth.management',

			ondelete='cascade',  	# When the management is deleted, the productivity_day is also deleted

			required=True,
		)

	configurator_emr_id = fields.Many2one(

			'openhealth.configurator.emr',

			#required=True,
		)



# ----------------------------------------------------------- Dep ? --------------------------
	#state = fields.Selection(
	#		selection=[
	#						('today', 'Hoy'),
							#('holiday', 'Feriado'),
	#		],
	#		string='Estado',
	#	)






# ----------------------------------------------------------- Required - At creation --------------------------
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




# ----------------------------------------------------------- Computes --------------------------
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




# ----------------------------------------------------------- Primitives - After creation --------------------------

	holiday = fields.Boolean(
			'Feriado',
			default=False,
			#readonly=True,
		)


	amount = fields.Float(
			'Venta por dia',
			digits=(16, 1),
		)



	# Cumulative
	cumulative = fields.Float(
			'Acumulado',
			#digits=(16, 1),
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
			#digits=(16, 1),
		)

	projection = fields.Float(
			'Proyección a final del mes',
		)

