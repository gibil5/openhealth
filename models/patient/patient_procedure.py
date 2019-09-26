# -*- coding: utf-8 -*-
"""
	Patient procedure

	Created: 			25 Sep 2019
	Last mod: 			25 Sep 2019
"""
#from __future__ import print_function

from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

class patient_procedure(models.Model):
	"""
	Patient procedure Class
	"""

	_name = 'openhealth.patient.procedure'

	_description = 'Openhealth Patient Procedure'

	_inherit = 'openhealth.patient.report'


