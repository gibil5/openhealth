# -*- coding: utf-8 -*-
"""
	Patient control

	Created: 			25 Sep 2019
	Last mod: 			25 Sep 2019
"""
#from __future__ import print_function

from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

class patient_control(models.Model):
	"""
	Patient control Class
	"""

	_name = 'openhealth.patient.control'

	_description = 'Openhealth Patient control'

	_inherit = 'openhealth.patient.report'


