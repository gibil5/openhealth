# -*- coding: utf-8 -*-
"""
	Patient session

	Created: 			25 Sep 2019
	Last mod: 			25 Sep 2019
"""
#from __future__ import print_function

from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

class patient_session(models.Model):
	"""
	Patient session Class
	"""

	_name = 'openhealth.patient.session'

	_description = 'Openhealth Patient Session'

	_inherit = 'openhealth.patient.report'


