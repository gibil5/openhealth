# -*- coding: utf-8 -*-
"""
    Doctor
	Created: 			 4 oct 2020
	Last updated: 		 4  2020
"""
from __future__ import print_function
from openerp import models, fields, api

_model_conf = "openhealth.configurator.emr"

# ----------------------------------------------------------- Doctor ------------------------------
class Doctor(models.Model):
	"""
	Used by Configurator Emr
	"""
	_name = 'openhealth.doctor'
	_order = 'physician'

# ----------------------------------------------------------- Relational -------

	# get default
	def _get_default_configurator(self):
		# Search
		configurator = self.env[_model_conf].search([
																		#('active', 'in', [True]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		return configurator

	# config
	configurator_id = fields.Many2one(
			_model_conf,
			ondelete='cascade', 
			required=True,
			default=_get_default_configurator,
		)

# ----------------------------------------------------------- Fields -----------
	physician = fields.Many2one(
			'oeh.medical.physician',
			required=True,
		)
	x_active = fields.Boolean(
			default=False,
		)
