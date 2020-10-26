# -*- coding: utf-8 -*-
"""
Services Other
Created: 			28 Jul 2020
Last mod: 			28 Jul 2020

class ServiceCosmetology
class ServiceEchography
class ServiceGynecology
class ServiceProduct
class ServicePromotion
"""
from openerp import models, fields, api
from . import px_vars
from . import px_vars_ext
from . import px_vars_echo
from . import px_vars_gyn
from . import px_vars_promo

# ---------------------------------------------- Cosmeto -------------------------------------
class ServiceCosmetology(models.Model):
	"""
	Service Cosmetology
	"""
	_name = 'openhealth.service_cosmetology'
	_inherit = 'openhealth.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_cos,
			string='Seleccionar Zona',
			#required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
					],
		)

# ----------------------------------------------------------- Categorized ------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)


# ---------------------------------------------- Echo ------------------------------------------
class ServiceEchography(models.Model):
	"""
	Service echo
	"""
	_name = 'openhealth.service_echography'
	_inherit = 'openhealth.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_echo._treatment_list,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_echo,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
					],
	)

	zone = fields.Selection(
			selection=px_vars_echo._zone_list,
			string='Zone',
			required=False,
		)

	pathology = fields.Selection(
			selection=px_vars_echo._pathology_list,
			string='Pathology',
			required=False,
		)

	sessions = fields.Selection(
			selection=px_vars_echo._sessions_list,
			string='Sessions',
			required=True,
		)

	level = fields.Selection(
			selection=px_vars_echo._level_list,
			string='Level',
			required=False,
		)

	time = fields.Selection(
			selection=px_vars_echo._time_list,
			string='Time',
			required=False,
		)


# ---------------------------------------------- Gyn -------------------------------------
class ServiceGynecology(models.Model):
	"""
	Service Gyn
	"""
	_name = 'openhealth.service_gynecology'
	_inherit = 'openhealth.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_gyn._treatment_list,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_gyn,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
					],
	)

# ----------------------------------------------------------- Modified ---------
	zone = fields.Selection(
			selection=px_vars_gyn._zone_list,
			string='Zone',
			required=True,
		)

	pathology = fields.Selection(
			selection=px_vars_gyn._pathology_list,
			string='Pathology',
			required=True,
		)

	sessions = fields.Selection(
			selection=px_vars_gyn._sessions_list,
			string='Sessions',
			required=False,
		)

	level = fields.Selection(
			selection=px_vars_gyn._level_list,
			string='Level',
			required=False,
		)

	time = fields.Selection(
			selection=px_vars_gyn._time_list,
			string='Time',
			required=False,
		)


# ---------------------------------------------- Prod -------------------------------------
class ServiceProduct(models.Model):
	"""
	Service Product - 2019
	"""
	_name = 'openhealth.service_product'
	_inherit = 'openhealth.service'

# ----------------------------------------------------------- Natives ----------
	# Service - Pricelist 2019
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'product'),
						('pl_price_list', '=', '2019'),
					],
			string="Servicio",
			required=True,
		)


# ---------------------------------------------- Promo -------------------------------------
class ServicePromotion(models.Model):
	"""
	Service Promo
	"""
	_name = 'openhealth.service_promotion'
	_inherit = 'openhealth.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_promo._treatment_list,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_promo,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
					],

	)

# ----------------------------------------------------------- Modified ---------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)

	time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
			required=False,
		)
