# -*- coding: utf-8 -*-
"""
Services All
Created: 			28 Jul 2020
Last mod: 			28 Jul 2020
"""
from openerp import models, fields, api
from . import px_vars
from . import px_vars_ext
from . import px_vars_echo
from . import px_vars_gyn
from . import px_vars_promo

# ---------------------------------------------- Co2 -------------------------------------
class ServiceCo2(models.Model):
	"""
	Service Co2
	"""
	_name = 'price_list.service_co2'
	_inherit = 'price_list.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_co2,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_co2,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			pl_treatment = 'LASER CO2 FRACCIONAL'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_treatment', '=', pl_treatment),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Relational -------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_treatment', '=', 'LASER CO2 FRACCIONAL'),
					],
		)

# ----------------------------------------------------------- Categorized ------
	time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
			required=False,
		)


# ---------------------------------------------- Cosmeto -------------------------------------

class ServiceCosmetology(models.Model):
	"""
	Service Cosmetology
	"""
	_name = 'price_list.service_cosmetology'
	_inherit = 'price_list.service'

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
			pl_family = 'cosmetology'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_family', '=', pl_family),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_family', '=', 'cosmetology'),
					],
		)

# ----------------------------------------------------------- Categorized ------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)

# ---------------------------------------------- Echo -------------------------------------

class ServiceEchography(models.Model):
	"""
	Service echo
	"""
	_name = 'price_list.service_echography'
	_inherit = 'price_list.service'

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
			pl_family = 'echography'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_family', '=', pl_family),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_family', '=', 'echography'),
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

# ---------------------------------------------- Exc -------------------------------------

class ServiceExcilite(models.Model):
	"""
	Service Excilite
	"""
	_name = 'price_list.service_excilite'
	_inherit = 'price_list.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_exc,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------

	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_exc_ipl,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			pl_treatment = 'LASER EXCILITE'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_treatment', '=', pl_treatment),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Relational -------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_treatment', '=', 'LASER EXCILITE'),
					],
	)

# ----------------------------------------------------------- Categorized ------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)

# ---------------------------------------------- Gyn -------------------------------------
class ServiceGynecology(models.Model):
	"""
	Service Gyn
	"""
	_name = 'price_list.service_gynecology'
	_inherit = 'price_list.service'

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
			pl_family = 'gynecology'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_family', '=', pl_family),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),

						('pl_family', '=', 'gynecology'),
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

# ---------------------------------------------- Ipl -------------------------------------
class ServiceIpl(models.Model):
	"""
	Service Ipl
	"""
	_name = 'price_list.service_ipl'
	_inherit = 'price_list.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_ipl,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_exc_ipl,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			pl_treatment = 'LASER M22 IPL'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_treatment', '=', pl_treatment),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Relational -------
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_treatment', '=', 'LASER M22 IPL'),
					],
	)

# ----------------------------------------------------------- Categorized ------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)

# ---------------------------------------------- Ndyag -------------------------------------
class ServiceNdyag(models.Model):
	"""
	Service Ndyag
	"""
	_name = 'price_list.service_ndyag'
	_inherit = 'price_list.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_ndy,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_ndy,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			pl_treatment = 'LASER M22 ND YAG'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_treatment', '=', pl_treatment),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Relational -------
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_treatment', '=', 'LASER M22 ND YAG'),
					],
	)

# ----------------------------------------------------------- Categorized ------
	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			required=False,
		)

# ---------------------------------------------- Prod -------------------------------------

class ServiceProduct(models.Model):
	"""
	Service Product - 2019
	"""
	_name = 'price_list.service_product'
	_inherit = 'price_list.service'


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
	_name = 'price_list.service_promotion'
	_inherit = 'price_list.service'

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
			pl_family = 'promotion'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_family', '=', pl_family),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Natives ----------
	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),

						('pl_family', '=', 'promotion'),
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

# ---------------------------------------------- Quick -------------------------------------
class ServiceQuick(models.Model):
	"""
	Service Quick
	"""
	_name = 'price_list.service_quick'
	_inherit = 'price_list.service'

# ---------------------------------------------- Pl Treatment ------------------
	pl_treatment = fields.Selection(
			selection=px_vars_ext._treatment_list_qui,
			string='Treatment',
			required=True,
		)

# ----------------------------------------------------------- Select -----------
	sel_zone = fields.Selection(
			selection=px_vars_ext._zone_list_qui,
			string='Seleccionar Zona',
			required=True,
		)

	# Sel Zone
	@api.onchange('sel_zone')
	def _onchange_sel_zone(self):
		if self.sel_zone != False:
			pl_treatment = 'QUICKLASER'
			return {'domain': {'service': [
												('pl_price_list', '=', '2019'),
												('pl_treatment', '=', pl_treatment),
												('pl_zone', '=', self.sel_zone),
			],},}

# ----------------------------------------------------------- Relational -------
	service = fields.Many2one(
			'product.template',
			domain=[
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
						('pl_treatment', '=', 'QUICKLASER'),
					],
	)

# ----------------------------------------------------------- Categorized ------
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
