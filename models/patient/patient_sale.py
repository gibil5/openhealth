# -*- coding: utf-8 -*-
"""
	Patient Sale

	Created: 			25 Sep 2019
	Last mod: 			25 Sep 2019
"""
#from __future__ import print_function

from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

class patient_sale(models.Model):
	"""
	Patient Sale Class
	"""
	
	_name = 'openhealth.patient.sale'

	_description = 'Openhealth Patient Sale'

	_inherit = 'openhealth.patient.report'


# ----------------------------------------------------------- Relational -------------------------------


	# Nr lines
	nr_lines = fields.Integer(
			string='Nr lineas',
		)




	# Amount
	amount = fields.Float(
			string="Total",
		)


