# -*- coding: utf-8 -*-
"""
 		*** Openhealth Doctor
 
		Created: 				 1 Feb 2019
		Last up:				10 Sep 2019
"""
from openerp import models, fields, api


# ----------------------------------------------------------- Physician ------------------------------------------------------

class Doctor(models.Model):

	_name = 'openhealth.doctor'
	
	#_order = 'idx asc'
	#_order = 'name'
	_order = 'physician'

	

# ----------------------------------------------------------- Relational --------------------------
	configurator_id = fields.Many2one(
			'openhealth.configurator.emr',
			ondelete='cascade', 
		)



# ----------------------------------------------------------- Fields --------------------------

	# Dep !
	#name = fields.Many2one(
	#		'oeh.medical.physician',
	#	)


	physician = fields.Many2one(
			'oeh.medical.physician',
		)


	#active = fields.Boolean(
	x_active = fields.Boolean(
			default=True,
		)

