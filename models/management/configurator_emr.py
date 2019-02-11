# -*- coding: utf-8 -*-
"""
	Configurator - EMR

	Created: 			25 Jan 2019
	Last updated: 		25 Jan 2019
"""
from __future__ import print_function

from openerp import models, fields, api

class ConfiguratorEmr(models.Model):
	"""
	high level support for doing this and that.
	"""

	_name = 'openhealth.configurator.emr'

	_inherit = 'openhealth.configurator'

	_description = 'Configurator Emr'





# ----------------------------------------------------------- Relational -------------------------------

	# Day Line
	day_line = fields.One2many(
			'openhealth.management.day.line',

			#'management_id',
			'configurator_emr_id',
		)



	# Doctor Line
	doctor_line = fields.One2many(
			'openhealth.doctor',

			'configurator_emr_id',
		)



# ----------------------------------------------------------- Redefined ---------------------------

	name = fields.Selection(			
			[
				#('emr', 'Historias'),
				#('lima', 'Sede Lima'),
				#('tacna', 'Sede Tacna'),
				('Lima', 'Sede Lima'),
				('Tacna', 'Sede Tacna'),
			],
			string="Nombre",
			required=True,
		)


	x_type = fields.Selection(
			[
				('emr', 'emr'),
			],
			string="Tipo",
			required=True,
		)







# ----------------------------------------------------------- Fields ------------------------------

	# Nr Controls
	nr_controls_co2 = fields.Integer(
			'Co2',
			default=-1,
		)

	nr_controls_quick = fields.Integer(
			'Quick',
			default=-1,
		)

	nr_controls_exc = fields.Integer(
			'Exc',
			default=-1,
		)

	nr_controls_ipl = fields.Integer(
			'Ipl',
			default=-1,
		)

	nr_controls_ndyag = fields.Integer(
			'Ndyag',
			default=-1,
		)



	# Nr Sessions
	nr_sessions_co2 = fields.Integer(
			'Co2',
			default=-1,
		)

	nr_sessions_quick = fields.Integer(
			'Quick',
			default=-1,
		)

	nr_sessions_exc = fields.Integer(
			'Exc',
			default=-1,
		)

	nr_sessions_ipl = fields.Integer(
			'Ipl',
			default=-1,
		)

	nr_sessions_ndyag = fields.Integer(
			'Ndyag',
			default=-1,
		)



	# Dates
	date_open = fields.Datetime(
			'Hora Apertura',
			default=fields.Date.today,
		)

	date_close = fields.Datetime(
			'Hora Cierre',
			default=fields.Date.today,
		)


