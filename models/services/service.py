# -*- coding: utf-8 -*-
"""
	Service

	Created: 			20 Sep 2016
	Last up: 			26 oct 2020
"""
from __future__ import print_function
from openerp import models, fields, api
from . import px_vars

class Service(models.Model):
	"""
	Service
	"""
	_name = 'openhealth.service'

# ----------------------------------------------------------- Many2one ------
	# Service
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('pl_price_list', '=', '2019'),
					],

			string="Producto",
			required=True,
		)

	qty = fields.Integer(
			default=1,
		)




	# Treatement
	treatment = fields.Many2one('openhealth.treatment',
			ondelete='cascade',
			#string="Tratamiento",
			string="Acta",
			readonly=True,
			required = True,
		)

	# Physician
	physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			index=True,
		)





# ----------------------------------------------------------- Select -----------
	family = fields.Selection(
			selection=px_vars._family_list,
			string='Familia',
			required=True,
		)

	subfamily = fields.Selection(
			selection=px_vars._subfamily_list,
			string='Subfamilia',
			required=True,
		)

	zone = fields.Selection(
			selection=px_vars._zone_list,
			string='Zona',
			#required=True,
			required=False,
		)

	pathology = fields.Selection(
			selection=px_vars._pathology_list,
			string='Pathology',
			#required=True,
			required=False,
		)

	sessions = fields.Selection(
			selection=px_vars._sessions_list,
			string='Sessions',
			#required=True,
			required=False,
		)

	level = fields.Selection(
			selection=px_vars._level_list,
			string='Level',
			#required=True,
			required=False,
		)

	time = fields.Selection(
			selection=px_vars._time_list,
			string='Time',
			#required=True,
			required=False,
		)


	# Zone
	sel_zone = fields.Selection(
			selection=px_vars._zone_list,
			string='Seleccionar Zona',
			#required=True,
		)

	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Tratamiento',
			#required=True,
			required=False,
		)



# ---------------------------------------------------------------- Fields ------
	# Price Manual
	price_manual = fields.Float(
			string="Precio Manual",			
		)

	# Price Applied
	price_applied = fields.Float(
			required=True,
		)


# ---------------------------------------------- Fields - Floats ---------------
	price = fields.Float(
			'Price',
		)

	price_vip = fields.Float(
			'Price vip',
		)

	price_company = fields.Float(
			'Price company',
		)

	price_session = fields.Float(
			'Price session',
		)

	price_session_next = fields.Float(
			'Price session next',
		)

	price_max = fields.Float(
			'Price max',
		)

# ----------------------------------------------------------- Fields -----------
	price_list = fields.Selection(
			selection=px_vars._price_list_list,
			string='Price list',
			default='2019',
			#required=True,
		)

	price_policy = fields.Selection(
			selection=px_vars._price_policy_list,
			string='Tipo de Precio',
			required=True,
			default='normal',
		)

	manufacturer = fields.Selection(
			selection=px_vars._manufacturer_list,
			string='Manufacturer',
		)

	brand = fields.Selection(
			selection=px_vars._brand_list,
			string='brand',
		)



# ----------------------------------------------------------- On changes -------
	# Price policy
	@api.onchange('price_policy')
	def _onchange_price_policy(self):		
		print()
		print('On change price policy')
		print(self.price_policy)
		if self.price_policy in ['normal']:
			self.price_applied = self.service.list_price
		elif self.price_policy in ['vip']:
			self.price_applied = self.service.pl_price_vip
		elif self.price_policy in ['company']:
			self.price_applied = self.service.pl_price_company
		elif self.price_policy in ['manual']:
			self.price_applied = self.price_manual

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		
		if self.service != 'none':
		
			self.family = self.service.pl_family
			self.subfamily = self.service.pl_subfamily

			self.pl_treatment = self.service.pl_treatment
			self.zone = self.service.pl_zone
			self.pathology = self.service.pl_pathology

			self.level = self.service.pl_level
			self.sessions = self.service.pl_sessions
			self.time = self.service.pl_time

			self.price = self.service.list_price
			self.price_vip = self.service.pl_price_vip
			self.price_company = self.service.pl_price_company

			self.price_session = self.service.pl_price_session
			self.price_session_next = self.service.pl_price_session_next
			self.price_max = self.service.pl_price_max

			self.price_applied = self.service.list_price

			self.manufacturer = self.service.pl_manufacturer
			self.brand = self.service.pl_brand


# ----------------------------------------------------------- Methods ----------

# ---------------------------------------------- Open Line Current -------------
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
				'context': {
				}
		}
	# open_line_current
