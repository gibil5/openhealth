# -*- coding: utf-8 -*-
"""
 		*** Doctor
 
		Created: 				1 Feb 2019
		Last up:				1 Feb 2019
"""

from openerp import models, fields, api


# ----------------------------------------------------------- Physician ------------------------------------------------------

class Doctor(models.Model):

	_name = 'openhealth.doctor'
	
	_order = 'name'
	#_order = 'idx asc'

	#_inherit = 'oeh.medical.physician'
	




# ----------------------------------------------------------- Fields --------------------------

	#name = fields.One2many(
	#name = fields.Char(
	name = fields.Many2one(
			'oeh.medical.physician',
		)


	active = fields.Boolean(
			default=False,
		)



# ----------------------------------------------------------- Relational --------------------------

	configurator_emr_id = fields.Many2one(
			'openhealth.configurator.emr'
		)
