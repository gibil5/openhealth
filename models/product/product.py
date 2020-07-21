# -*- coding: utf-8 -*-
"""
	*** Product Template

	Only Data model. No functions.

	All Fixers are Deprecated. Should be in the Clean Module.

	Created: 			 01 Nov 2016
	Last up: 	 		 10 Dec 2019
"""

from __future__ import print_function
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.addons.openhealth.models.libs import lib
from . import prodvars

class Product(models.Model):
	"""
	Product Template
	Inherited from OeHealth
	"""
	_inherit = 'product.template'

	_order = 'name'



# ----------------------------------------------------------- Relational --------------------------

	# Categ
	categ_id = fields.Many2one(
			'product.category',
			'Internal Category',
			#required=True,
			required=False,
			change_default=True,
			domain="[('type','=','normal')]",
			help="Select category for the current product"
		)

	# Unit of measure
	uom = fields.Many2one(
			'product.uom',
			required=False,
		)




# ----------------------------------------------------------- Price List - 2019 ------------------------
	pl_price_list = fields.Selection(
			[
				('2019', '2019'),
				('2018', '2018'),
			],
			string='Lista de Precios',
		)



# ----------------------------------------------------------- Canonical - 2018 -------------------------------
	# Family
	x_family = fields.Selection(
			selection=prodvars._family_list,
			required=False,
		)

	# Treatment
	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
			required=False,
		)

	# Zone
	x_zone = fields.Selection(
			selection=prodvars._zone_list,
			required=False,
		)

	# Pathology
	x_pathology = fields.Selection(
			selection=prodvars._pathology_list,
			required=False,
		)

	# Sessions
	x_sessions = fields.Char(
			default="",
			required=False,
		)

	# Level
	x_level = fields.Selection(
			selection=prodvars._level_list,
			required=False,
		)

	# Time
	x_time = fields.Char(
			selection=prodvars._time_list,
			required=False,
		)


	# Price Vip
	x_price_vip = fields.Float(
			required=False,
		)

	# Price Vip Return
	x_price_vip_return = fields.Float(
			required=False,
		)


# ----------------------------------------------------------- Test -------------------------------
	x_test = fields.Boolean(
			'Test',
		)

# ----------------------------------------------------------- Account -----------------------------

	x_name_account = fields.Char(
			'Name Account',
		)

	x_code_account = fields.Char(
			'Code Account',
		)

	vspace = fields.Char(
			' ',
			readonly=True
		)


# ----------------------------------------------------------- Codes -------------------------------
	# Go Flag
	x_go_flag = fields.Boolean()

	# Name Unfixed
	x_name_unfixed = fields.Char()

	# Short Name Unfixed
	x_short_unfixed = fields.Char()

	# Name Short
	x_name_short = fields.Char()

	# Counter
	x_counter = fields.Integer(
			'Counter',
		)

	# Code
	x_code = fields.Char(
			'Code',
		)

# ----------------------------------------------------------- Canonical ---------------------------

	# Origin
	x_origin = fields.Selection(
		[
			('legacy', 'Legacy'),
			('test', 'Test'),
			('production', 'Production'),
		],
			required=False,
		)

