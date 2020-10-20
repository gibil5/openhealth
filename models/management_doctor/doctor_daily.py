# -*- coding: utf-8 -*-
"""
	Doctor Daily - Too complex - Refactor !

	Inherits - doctor_line

	Created: 			 8 Dec 2019
	Last up: 			 8 Dec 2019
"""

from openerp import models, fields, api

class DoctorDaily(models.Model):
	"""
	DoctorDaily
		DoctorLine
			ManagementLine
	"""
	_inherit = 'openhealth.management.doctor.line'

	_name = 'doctor.daily'



# ----------------------------------------------------------- Relational -------
	management_id = fields.Many2one(
			'openhealth.management',
			#ondelete='cascade',
			required=True,
		)

