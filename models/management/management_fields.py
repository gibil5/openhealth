# -*- coding: utf-8 -*-
"""
	Management Fields - Dep !

	Created: 			28 nov 2020
	Last up: 			 6 dec 2020
"""
from openerp import models, fields, api

class ManagementFields(models.Model):
	"""
	Contains the model fields.
	"""
	_name = 'openhealth.management_fields'
	#_inherit = 'openhealth.repo'  	# Dep !
