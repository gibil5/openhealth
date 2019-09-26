# -*- coding: utf-8 -*-
"""
	Patient consultation

	Created: 			25 Sep 2019
	Last mod: 			25 Sep 2019
"""
#from __future__ import print_function

from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

class patient_consultation(models.Model):
	"""
	Patient consultation Class
	"""

	_name = 'openhealth.patient.consultation'

	_description = 'Openhealth Patient Consultation'

	_inherit = 'openhealth.patient.report'


