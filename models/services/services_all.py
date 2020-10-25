# -*- coding: utf-8 -*-
"""
Services All

Created: 			28 Jul 2020
Last mod: 			28 Jul 2020

class ServiceAll
"""
from openerp import models, fields, api

# --------------------------------------- All --------------------------------
class ServiceAll(models.Model):
	"""
	Service All
	"""
	_name = 'openhealth.service_all'
	_inherit = 'openhealth.service'
