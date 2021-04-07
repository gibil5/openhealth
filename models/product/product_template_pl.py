# -*- coding: utf-8 -*-
"""
	*** Product Template - 2019

	Only functions. Not the data model. 

	Created: 			  8 Apr 2019
	Last up: 	 		 16 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

from . import px_vars
from . import chk_product
from . import pl_prod_vars
from . import exc_prod

class ProductTemplate(models.Model):
	"""
	Product Template - 2019
	"""
	_order = 'pl_idx_int'
	_description = 'Product Template'

	_inherit = 'product.template'


# ----------------------------------------------------------- Fields ------------------------------

	pl_price_list = fields.Selection(
			[
				('2019', '2019'),
				('2018', '2018'),
			],
			string='Lista de Precios',
			required=True,
		)

# ----------------------------------------------------------- Natives ----------
	# Treatment
	x_treatment = fields.Selection(
			selection=pl_prod_vars._treatment_list,		
			required=False,
		)


# ---------------------------------------------- Fields - Categorized ----------
	# Required
	pl_family = fields.Selection(
			selection=px_vars._family_list,
			string='Family',
			required=True,
		)

	pl_subfamily = fields.Selection(
			selection=px_vars._subfamily_list,
			string='Subfamily',
			required=True,
		)

	# Not Required
	pl_manufacturer = fields.Selection(
			selection=px_vars._manufacturer_list,
			string='Fabricante',
		)

	pl_brand = fields.Selection(
			selection=px_vars._brand_list,
			string='Marca',
		)

	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
		)

	pl_zone = fields.Selection(
			selection=px_vars._zone_list,
			string='Zone',
		)

	pl_pathology = fields.Selection(
			selection=px_vars._pathology_list,
			string='Pathology',
		)

	pl_level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
		)

	pl_sessions = fields.Selection(
			selection=px_vars._sessions_list,
			string='Sessions',
		)

	pl_time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
		)

# ---------------------------------------------- Fields - Floats ---------------
	pl_price = fields.Float(
			'Price',
		)

	pl_price_vip = fields.Float(
			'Precio Vip',
		)

	pl_price_company = fields.Float(
			'Precio Empresa',
		)

	pl_price_session = fields.Float(
			'Price session',
		)

	pl_price_session_next = fields.Float(
			'Price session next',
		)

	pl_price_max = fields.Float(
			'Price max',
		)

# ---------------------------------------------- Fields - Chars ----------------
	pl_name_short = fields.Char(
			'Name short',
			required=True,
		)

	pl_prefix = fields.Char(
			'Prefix',
		)

	pl_idx = fields.Char(
			'Idx',
		)

	pl_code = fields.Char(
			'Code',
		)

	pl_idx_int = fields.Integer(
			'Indice',
		)

	pl_account = fields.Char(
			'Cuenta contable',
			required=False,
		)

	pl_time_stamp = fields.Char(
			required=False,
		)


# ----------------------------------------------------------- Configurator ------------------------
	def init_configurator(self):
		"""
		Initializes the Configurator
		Is compatible with Tacna. Does the search by type, not by name
		"""
		# Search
		if self.configurator.name in [False]:
			self.configurator = self.env['openhealth.configurator.emr'].search([
																					('x_type', 'in', ['emr']),
															],
															#order='date_begin,name asc',
															limit=1,
														)
	# Configurator - Used by Product Template Tree
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
		)

# ----------------------------------------------------------- Methods ------------------------

# ----------------------------------------------------------- Getters ----------
	# Get Treatment
	def get_treatment(self):
		"""
		Get Product Treatment
		Used by: Session, Control.
		"""
		# Init
		_dic = {
					'LASER CO2 FRACCIONAL': 	'laser_co2',
					'QUICKLASER': 				'laser_quick',
					'LASER EXCILITE':			'laser_excilite',
					'LASER M22 IPL':			'laser_ipl',
					'LASER M22 ND YAG':			'laser_ndyag',
		}

		treatment = False

		print(self.pl_treatment)

		# 2019
		if self.pl_price_list in ['2019']:
			if self.pl_treatment in _dic:
				treatment = _dic[self.pl_treatment]
			else:
				print('Error: 1')

		# 2018
		elif self.pl_price_list in ['2018']:
			treatment = self.x_treatment

		# Error
		else:
			print('Error: 2')

		return treatment


# ---------------------------------------- Constraints Python - Name -----------
	# Check Name
	@api.constrains('name')
	def check_name(self):
		"""
		Check Name
		"""
		chk_product.check_name(self)
