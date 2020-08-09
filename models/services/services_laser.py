# -*- coding: utf-8 -*-
"""
Services Laser
Created: 			28 Jul 2020
Last mod: 			28 Jul 2020

class ServiceCo2
class ServiceExcilite
class ServiceIpl
class ServiceNdyag
class ServiceQuick
"""
from openerp import models, fields, api
from . import px_vars
from . import px_vars_ext

# ---------------------------------------------- Co2 -------------------------------------
class ServiceCo2(models.Model):
	"""
	Service Co2
	"""
	#_name = 'price_list.service_co2'
	#_inherit = 'price_list.service'
	_name = 'openhealth.service_co2'
	_inherit = 'openhealth.service'

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



# ---------------------------------------------- Exc -------------------------------------

class ServiceExcilite(models.Model):
	"""
	Service Excilite
	"""
	_name = 'openhealth.service_excilite'
	_inherit = 'openhealth.service'

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

# ---------------------------------------------- Ipl -------------------------------------
class ServiceIpl(models.Model):
	"""
	Service Ipl
	"""
	_name = 'openhealth.service_ipl'
	_inherit = 'openhealth.service'

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
	_name = 'openhealth.service_ndyag'
	_inherit = 'openhealth.service'

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

# ---------------------------------------------- Quick -------------------------------------
class ServiceQuick(models.Model):
	"""
	Service Quick
	"""
	_name = 'openhealth.service_quick'
	_inherit = 'openhealth.service'

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
