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
	def _get_default_configurator(self):
		#print()
		#print('Default Configurator')

		# Search
		configurator = self.env['openhealth.configurator.emr'].search([
																		#('active', 'in', [True]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		return configurator



	configurator_id = fields.Many2one(
			'openhealth.configurator.emr',
			ondelete='cascade', 
			required=True,

			default=_get_default_configurator,
		)



# ----------------------------------------------------------- Fields --------------------------

	# Dep !
	#name = fields.Many2one(
	#		'oeh.medical.physician',
	#	)


	physician = fields.Many2one(
			'oeh.medical.physician',
			required=True,
		)


	#active = fields.Boolean(
	x_active = fields.Boolean(
			default=False,
		)

