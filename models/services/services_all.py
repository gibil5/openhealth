# -*- coding: utf-8 -*-
"""
    Services All

    Created: 			25 oct 2020
    Last up: 			26 oct 2020

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
