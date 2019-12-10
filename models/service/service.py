# -*- coding: utf-8 -*-
"""
	Service

	Created: 			20 Sep 2016
 	Last up: 	 		24 April 2019

	Used by: Treatment

	24 Apr 2019:		Cleanup after 2019 PL. Must disappear:
						- Onchanges. 
"""
from __future__ import print_function
from openerp import models, fields, api

from openerp.addons.openhealth.models.product import prodvars

from . import vars_ipl


class Service(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.service'


# ----------------------------------------------------------- Relational - Dep ------------------------------
	# Nex zone
	#nex_zone = fields.Many2one(
	#		'openhealth.zone',
	#		string="Nex Zone",
	#	)

	# Nex Pathology
	#nex_pathology = fields.Many2one(
	#		'openhealth.pathology',	
	#		string="Nex Pathology",
	#	)




# ----------------------------------------------------------- Natives ------------------------------
	# Service
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
					],
			string="Producto",
			required=True,
		)


# ----------------------------------------------------------- Prices ------------------------------
	# Price
	price = fields.Float(
			string='Precio',

			compute='_compute_price',
		)
	#@api.multi
	@api.depends('service')
	def _compute_price(self):
		for record in self:
			record.price= (record.service.list_price)


	# Price VIP
	price_vip = fields.Float(
			compute='_compute_price_vip',

			string='Precio VIP',
		)
	#@api.multi
	@api.depends('service')
	def _compute_price_vip(self):
		for record in self:
			record.price_vip= (record.service.x_price_vip)


	# Price Manual
	price_manual = fields.Float(
			string="Precio Manual",
			default=-1,
		)


	# Price Applied
	price_applied = fields.Float(
			#string='Precio Aplicado',
			default=-1,
		)


# ----------------------------------------------------------- Primitives --------------------------

	# Name
	name = fields.Char(
			default='SE',
			string='Servicio #',
			compute='_compute_name',
			#required=True,
		)
	@api.multi
	def _compute_name(self):
		for record in self:
			record.name = 'SE00' + str(record.id)



	# Name short
	name_short = fields.Char(
			compute='_compute_name_short',
			#string='Short name'
		)

	@api.depends('service')
	def _compute_name_short(self):
		for record in self:
			record.name_short = record.service.x_name_short


	# State
	state = fields.Selection(
			[
				('draft', 		'Inicio'),
				('budget', 		'Presupuestado'),
				('sale', 		'Pagado'),
			],
			#selection = serv_vars._state_list,
			string='Estado',
			default = 'draft',
		)


	# Family
	family = fields.Selection(
			string="Familia",
			selection=prodvars._family_list,
		)


	# Laser
	laser = fields.Selection(
			selection = prodvars._laser_type_list,
			string="Láser", 
			default='none',
			#required=True,
			index=True
		)


	# Sessions
	sessions = fields.Selection(
			#selection = jxvars._pathology_list,
			selection = prodvars._sessions_list,
			string="Sesiones",
		)

	# Comeback
	comeback = fields.Boolean(
			string='Regreso',
		)

	# Treatment (for Product)
	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
			string="Tratamiento",
		)

	# Zone
	zone = fields.Selection(
			selection = prodvars._zone_list,
			string="Zona",
		)

	# Pathology
	pathology = fields.Selection(
			selection = prodvars._pathology_list,
			string="Patología",
		)

	# Vertical space
	vspace = fields.Char(
			' ',
			readonly=True
		)

	# Time
	time = fields.Char(
			default='',
			string="Tiempo",
		)


	_time_list = [
					('15 min','15 min'),
					('30 min','30 min'),
					('none',''),
		]

	time_1 = fields.Selection(
			#selection = exc._time_list,
			selection = _time_list,
			string="Tiempo",
			default='none',
			)


	# Nr sessions
	nr_sessions = fields.Char(
			default='',
	)


	nr_sessions_1 = fields.Selection(
			selection = vars_ipl._nr_sessions_list,
			string="Número de sesiones",
			default='none',
	)


	# Code
	code = fields.Char(
			string='Code',

			compute='_compute_code',
			)
	@api.depends('service')
	def _compute_code(self):
		for record in self:
			record.code= record.service.name


	# Title
	title = fields.Char(
			string='Title',
			default='',
			readonly=True,
		)

	# Over notebook
	notebook_over = fields.Char(
			string='Over notebook',
			default='',
			readonly=True,
		)


# ----------------------------------------------------------- Relationals -------------------------
	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			'Paciente',
		)

	# Physician
	physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			index=True
		)


	# Treatement
	treatment = fields.Many2one('openhealth.treatment',
			ondelete='cascade',
			string="Tratamiento",
			readonly=True,
			#required = True,
		)








# ---------------------------------------------- Open Line Current --------------------------------

	# Open Line
	@api.multi
	def open_line_current(self):
		"""
		high level support for doing this and that.
		"""
		service_id = self.id
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Service Current',
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': service_id,
				'target': 'current',
				'flags': {
							'form': {'action_buttons': True, }
						},
				'context': {}
		}
	# open_line_current
