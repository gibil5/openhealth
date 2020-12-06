# -*- coding: utf-8 -*-
"""
	Management Business logic

	Created: 			 6 dec 2020
	Last up: 			 6 dec 2020
"""
from __future__ import print_function
from openerp import models, fields, api

class ManagementBusiness(models.Model):
	"""
    Management - Business logic.
    Contains the BL of the company.
	"""
	_inherit = 'openhealth.management'
