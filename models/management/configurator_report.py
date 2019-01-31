# -*- coding: utf-8 -*-
"""
	Configurator - Report

	Created: 			25 Jan 2019
	Last updated: 		25 Jan 2019
"""
from __future__ import print_function

from openerp import models, fields, api

class ConfiguratorReport(models.Model):
	"""
	high level support for doing this and that.
	"""

	_name = 'openhealth.configurator.report'

	_inherit = 'openhealth.configurator'

	_description = 'Configurator Report'




# ----------------------------------------------------------- Fields --------------------------

	date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
		)


	date_end = fields.Date(
			string="Fecha Fin",
			default=fields.Date.today,
		)

	x_type = fields.Selection(
			[
				('fast', 'Fast'),
				('all', 'All'),
			],
			string="Type",
			required=True,
		)


	# Globals
	total_amount_year_2018 = fields.Float(
			string="Monto Total Año 2018",
		)

	total_nr_year_2018 = fields.Integer(
			string="Nr Total Año 2018",
		)

	total_amount_year_2019 = fields.Float(
			string="Monto Total Año 2019",
		)

	total_nr_year_2019 = fields.Integer(
			string="Nr Total Año 2019",
		)


	month_create = fields.Boolean(
			string="Month",
			default=False,
		)

	year_create = fields.Boolean(
			string="Year",
			default=False,
		)




# ----------------------------------------------------------- Update --------------------------
	# Update
	@api.multi
	def update(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update')

		self.total_nr_year_2018 = 5
		self.total_amount_year_2018 = 5

		self.total_nr_year_2019 = 55
		self.total_amount_year_2019 = 55



