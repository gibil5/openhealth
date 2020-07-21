# -*- coding: utf-8 -*-
"""
 	Family Line 

	Only Data model. No functions.

	Created: 			20 Aug 2018
	Last up: 			 9 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from . import mgt_vars

class FamilyLine(models.Model):
	"""
	Only Data model. No functions.

	Should not be inherited
	"""
	_inherit = 'openhealth.management.line'

	_name = 'openhealth.management.family.line'

	_order = 'amount desc'

