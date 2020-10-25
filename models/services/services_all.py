# -*- coding: utf-8 -*-
"""
Services All

Created: 			28 Jul 2020
Last mod: 			28 Jul 2020

class ServiceLaser
"""
from openerp import models, fields, api

# --------------------------------------- Laser --------------------------------
#class ServiceLaser(models.Model):
class ServiceAll(models.Model):
	"""
	Service All
	"""
	_name = 'openhealth.service_all'
	_inherit = 'openhealth.service'
