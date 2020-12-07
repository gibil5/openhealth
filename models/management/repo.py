# -*- coding: utf-8 -*-
"""
 	Repo. Inherited by Management and Marketing - Dep !

	Only Data model. No functions.

 	Created: 			28 May 2018
	Last up: 			 6 dec 2020
"""
from openerp import models, fields, api

class Repo(models.Model):
	_name = 'openhealth.repo'
	_inherit='openhealth.django.interface'

# ----------------------------------------------------------- Inherited ------------------------------------------------------
	# Average Total Amount
	avg_total_amount = fields.Float(
			'Promedio Anual',
		)
