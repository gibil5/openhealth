# -*- coding: utf-8 -*-
"""
	*** Product Template

	Only Data model. No functions.

	All Fixers are Deprecated. Should be in the Clean Module.

	Created: 			 01 Nov 2016
	Last up: 			 05 dec 2020
"""

from __future__ import print_function
from openerp import models, fields
from . import prod_vars

class ProductTemplate(models.Model):
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

	pl_treatment = fields.Char()

# ----------------------------------------------------------- Canonical - 2018 -------------------------------
	# Family
	x_family = fields.Selection(
			#selection=prod_vars._family_list,
			selection=prod_vars.get_family_list(),
			required=False,
		)

	# Treatment
	x_treatment = fields.Selection(
			#selection=prod_vars._treatment_list,
			selection=prod_vars.get_treatment_list(),
			required=False,
		)

	# Zone
	x_zone = fields.Selection(
			#selection=prod_vars._zone_list,
			selection=prod_vars.get_zone_list(),
			required=False,
		)

	# Pathology
	x_pathology = fields.Selection(
			#selection=prod_vars._pathology_list,
			selection=prod_vars.get_pathology_list(),
			required=False,
		)

	# Sessions
	x_sessions = fields.Char(
			default="",
			required=False,
		)

	# Level
	x_level = fields.Selection(
			#selection=prod_vars._level_list,
			selection=prod_vars.get_level_list(),
			required=False,
		)

	# Time
	x_time = fields.Char(
			#selection=prod_vars._time_list,
			selection=prod_vars.get_time_list(),
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
