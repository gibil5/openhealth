# -*- coding: utf-8 -*-
"""
Container

Created: 			23 Apr 2019
Last updated: 		10 Aug 2019
"""
from __future__ import print_function

from openerp import models, fields, api

#class PricelistContainer(models.Model):
class ContainerPricelist(models.Model):
	"""
	Pricelist 2019.	
	Creates, updates and manages Products
	"""
	_name = 'openhealth.container.pricelist'

	_description = 'Openhealth Container Pricelist'



# ----------------------------------------------------------- Relational --------------------------

	# Product Pricelist
	product_ids = fields.Char()
	#product_ids = fields.One2many(
	#		'openhealth.product.pricelist',
	#		'container_id',
	#	)




# ----------------------------------------------------------- Configurator -------------------------

	def _get_default_configurator(self):
		print()
		print('Default Configurator')

		# Search
		configurator = self.env['openhealth.configurator.emr'].search([
																		#('active', 'in', [True]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		return configurator


	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			required=True,

			default=_get_default_configurator,
		)


