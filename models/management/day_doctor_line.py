# -*- coding: utf-8 -*-
"""
	Day Doctor Line

	Created: 			25 Jan 2019
	Last up: 			25 Jan 2019
"""
from __future__ import print_function

from openerp import models, fields, api

class DayDoctorLine(models.Model):
	"""
	high level support for doing this and that.
	"""

	_name = 'openhealth.management.day.doctor.line'

	_inherit = 'openhealth.management.day.line'

	_order = 'date asc'




	amount = fields.Float(
			'Monto Total',
			#digits=(16, 1),
		)


	nr_consultations = fields.Integer(
			'Nr Consultas',
		)

	nr_procedures = fields.Integer(
			'Nr Procs',
		)

	ratio_pro_con = fields.Float(
			'Ratio (proc/con) %',
		)


