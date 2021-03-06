# -*- coding: utf-8 -*-
"""
	Day Doctor Line

	Inherits  - day_line

	Created: 			25 Jan 2019
	Last: 				27 mar 2021
"""
from __future__ import print_function
from __future__ import absolute_import

import datetime
from openerp import models, fields, api

#from openerp.addons.openhealth.models.order import ord_vars
from ..order import ord_vars

#class MgtDayDoctorLine(models.Model):
class MgtDoctorDayLine(models.Model):
	"""
	MgtDayDoctorLine
		DayLine
			ManagementLine
	"""
	_name = 'openhealth.management.day.doctor.line'
	_order = 'date asc'
	_inherit = 'openhealth.management.day.line'



# ----------------------------------------------------------- Relational --------------------------
	# Doctor line
	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',
			ondelete='cascade',
		)

	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'doctor_day_id',
		)



# ----------------------------------------------------------- Primitive ---------------------------

	amount = fields.Float(
			'Monto Total',
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


