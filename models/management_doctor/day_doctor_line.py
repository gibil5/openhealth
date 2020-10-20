# -*- coding: utf-8 -*-
"""
	Day Doctor Line

	Inherits  - day_line

	Created: 			25 Jan 2019
	Last up: 			25 Jan 2019
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars

class DayDoctorLine(models.Model):
	"""
	DayDoctorLine
		DayLine
			ManagementLine
	"""
	_inherit = 'openhealth.management.day.line'
	_name = 'openhealth.management.day.doctor.line'
	_order = 'date asc'



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


