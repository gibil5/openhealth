# -*- coding: utf-8 -*-
"""
	Sale Order Line
	Created: 			26 Aug 2016
	Last mod: 			25 Apr 2020
"""
from __future__ import print_function
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
from openerp.addons.openhealth.models.libs import lib

class SaleOrderLine(models.Model):
	"""
	Sale Order Line
	"""
	_inherit = 'sale.order.line'

# ----------------------------------------------------------- Ticket - Get Item Lines  ----------------
	# Patient Name
	def get_item_line(self):
		"""
		Used by Ticket
		"""
		print()
		print('Get Item Line')
		#print(self.product_id.get_name_ticket())
		#print(self.get_quantity())
		#print(self.get_price_unit())
		#print(self.get_price_subtotal())
		line_0 = self.format_line(self.product_id.get_name_ticket())
		line_1 = self.format_line(self.get_quantity())
		line_2 = self.format_line(self.get_price_unit())
		line_3 = self.format_line(self.get_price_subtotal())
		line = "<tr>" + line_0 + line_1 + line_2 + line_3 + "</tr>"
		return line

# ----------------------------------------------- Ticket - Get Item Lines  -----
	def format_line(self, value):
		"""
		Used by Ticket - Aux
		"""
		value = str(value)
		line = "<td>\
					<font size='2'>" + value + "</font>\
				</td>"
		return line

# --------------------------------------------------- Print Ticket --------------
	def get_price_unit(self):
		"""
		Used by Ticket - Aux
		"""
		return self.price_unit

	def get_price_subtotal(self):
		"""
		Used by Ticket - Aux
		"""
		return self.price_subtotal

	def get_quantity(self):
		"""
		Used by Ticket - Aux
		"""
		return int(self.product_uom_qty)

# ------------------------------------------------ Get Product Price List ------
	def get_price_list(self):
		"""
		Used by x
		"""
		return self.product_id.pl_price_list

# ----------------------------------------------------------- Get Product Family -------------------------------
	def get_family(self):
		"""
		Used by x
		"""
		_dic_families = {
							'chavarri':			'PRODUCTO',
							'commercial':		'PRODUCTO',
							'consultation':		'CONSULTA',
							'quick':			'QUICK LASER',
							'co2':				'LASER CO2',
							'excilite':				'LASER EXCILITE',
							'm22':				'LASER M22',
							'medical':			'T MEDICO',
							'cosmetology':		'COSMEATRIA',
							'gynecology':		'GINECOLOGIA',
							'echography':		'ECOGRAFIA',
							'promotion':		'PROMOCION'}

		# 2019
		if self.product_id.pl_price_list in ['2019']:
			if self.product_id.pl_subfamily not in [False]:
				if self.product_id.pl_subfamily in _dic_families:
					value = _dic_families[self.product_id.pl_subfamily]
				else:
					value = self.product_id.pl_subfamily
			else:
				value = 'pl'

		# 2018
		else:
			if self.product_id.x_family not in [False]:
				if self.product_id.x_family in _dic_families:
					value = _dic_families[self.product_id.x_family]
				else:
					value = self.product_id.x_family
			else:
				value = 'x'

		return value

# ----------------------------------------------------------- Prices ----------
	# Price Unit
	price_unit = fields.Float(
		#'Unit Price',
		'Precio',
		required=True,
		digits=dp.get_precision('Product Price'),
		default=0.0,
	)

	# Quantity
	product_uom_qty = fields.Float(
			string='Quantity',
			digits=(16, 0),
			required=False,
			default=1.0,
		)

# -------------------------------------------------- Recommendations -----------
	#service_product_id = fields.Many2one(
	#		'openhealth.service.product',
	#		string='Product',
	#	)

	#service_consultation_id = fields.Many2one(
	#		'openhealth.service.consultation',
	#		string='Consultation',
	#	)

	#service_co2_id = fields.Many2one(
	#		'openhealth.service.co2',
	#		string='Co2',
	#	)

	#service_quick_id = fields.Many2one(
	#		'openhealth.service.quick',
	#		string='Quick',
	#	)

	#service_vip_id = fields.Many2one(
	#		'openhealth.service.vip',
	#		string='Vip',
	#	)

	#service_excilite_id = fields.Many2one(
	#		'openhealth.service.excilite',
	#		string='Excilite',
	#	)

	#service_ipl_id = fields.Many2one(
	#		'openhealth.service.ipl',
	#		string='Ipl',
	#	)

	#service_ndyag_id = fields.Many2one(
	#		'openhealth.service.ndyag',
	#		string='Ndyag',
	#	)

	#service_medical_id = fields.Many2one(
	#		'openhealth.service.medical',
	#		string='Medical',
	#	)

	#service_cosmetology_id = fields.Many2one(
	#		'openhealth.service.cosmetology',
	#		string='Cosmetology',
	#	)

# ---------------------------------------------- Open Line Current --------------------------------
	# Open Line
	@api.multi
	def open_line_current(self):
		"""
		high level support for doing this and that.
		"""
		res_id = self.id
		return {
			'type': 'ir.actions.act_window',
			'name': ' Edit Service Current',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': self._name,
			'res_id': res_id,
			'target': 'current',
			'flags': {
				'form': {'action_buttons': True, }
					},
			'context': {}
		}
	# open_line_current

# ----------------------------------------------------------- Update -----------
	# Update Recommendations
	#@api.multi
	def update_recos(self):
		"""
		Used by Order
		"""
		#print
		#print 'Update - Recommendations'

		# Init
		family = self.product_id.x_family
		treatment = self.product_id.x_treatment
		if family in ['laser', 'consultation', 'consultation_gyn']:
			categ = treatment
		else:
			categ = family

		# Co2
		if categ == 'laser_co2':
			lib.change_state(self.service_co2_id, 'sale')

		# Exc
		elif categ == 'laser_excilite':
			lib.change_state(self.service_excilite_id, 'sale')

		# Ipl
		elif categ == 'laser_ipl':
			lib.change_state(self.service_ipl_id, 'sale')

		# Ndyag
		elif categ == 'laser_ndyag':
			lib.change_state(self.service_ndyag_id, 'sale')

		# Quick
		elif categ == 'laser_quick':
			lib.change_state(self.service_quick_id, 'sale')

		# Medical
		elif categ == 'medical':
			lib.change_state(self.service_medical_id, 'sale')

		# Cosmetology
		elif categ == 'cosmetology':
			lib.change_state(self.service_cosmetology_id, 'sale')

		# Consultation
		elif categ == 'consultation':
			#print
			pass

		# Products
		else:
			lib.change_state(self.service_product_id, 'sale')

	# update_recos
