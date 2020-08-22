# -*- coding: utf-8 -*-
"""
 		Appointment - MIN

 		Created: 			28 Aug 2019
		Last updated: 	 	28 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Appointment(models.Model):
	"""
	high level support for doing this and that.
	"""

	_inherit = 'oeh.medical.appointment'




# ----------------------------------------------------------- Fields ------------------------------

	# Id Doc Type
	x_id_doc_type = fields.Char()

	# Id Doc
	x_id_doc = fields.Char(
		)


	# Day
	x_day = fields.Char(
		)

	# Month
	x_month = fields.Char(
		)

	# Year
	x_year = fields.Char(
		)

	# Time
	x_time = fields.Char(
		)

	# Type
	x_type = fields.Char(
		)




# ----------------------------------------------------------- Canonical ---------------------------
	# Name
	name = fields.Char(
		)

	# Vspace
	vspace = fields.Char(
		)

	# Sub type
	x_subtype = fields.Char(
		)

	# Date End
	#appointment_end = fields.Char(
	#	)

