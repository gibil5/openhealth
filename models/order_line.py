# -*- coding: utf-8 -*-

"""
	Sale Order Line
"""

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
import lib

class SaleOrderLine(models.Model):
	"""
	Sale Order Line
	"""
	_inherit = 'sale.order.line'



# ----------------------------------------------------------- Compact Name ------------------------
	# Description
	x_description = fields.Text(
		string='Nombre compacto',

		compute='_compute_x_description',
	)

	@api.multi
	def _compute_x_description(self):
		for record in self:
			if record.product_id.x_name_short in ['generic_product', 'generic_service']:
				record.x_description = record.name
			else:
				record.x_description = record.product_id.x_name_ticket





# ----------------------------------------------------------- Prices ------------------------------
	# Price Unit
	price_unit = fields.Float(
		#'Unit Price',
		'Precio',
		required=True,
		digits=dp.get_precision('Product Price'),
		default=0.0,
	)


	# Price manual
	x_price_manual = fields.Float(
		string="Precio manual",
		required=False,
		default=-1,
	)


	# Price std
	x_price_std = fields.Float(
		string="Precio Std",
		required=False,

		compute='_compute_price_std',
	)

	@api.multi
	def _compute_price_std(self):
		for record in self:
			record.x_price_std = record.product_id.list_price



	# Price Vip
	x_price_vip = fields.Float(
		string="Precio Vip",
		required=False,

		compute='_compute_price_vip',
	)

	@api.multi
	def _compute_price_vip(self):
		for record in self:
			record.x_price_vip = record.product_id.x_price_vip



	# Price Vip Return
	x_price_vip_return = fields.Float(
		string="Precio Vip R",
		required=False,

		compute='_compute_price_vip_return',
	)

	@api.multi
	def _compute_price_vip_return(self):
		for record in self:
			record.x_price_vip_return = record.product_id.x_price_vip_return




	# Quantity
	product_uom_qty = fields.Float(
			string='Quantity',

			digits=(16, 0),
			
			required=False,
			default=1.0,
		)


	#x_qty_int = fields.Integer(
	x_qty = fields.Integer(
			compute='_compute_x_qty',
		)

	@api.multi
	def _compute_x_qty(self):
		for record in self:
			record.x_qty = record.product_uom_qty




# ----------------------------------------------------------- Vip ---------------------------------

	# Vip in progress
	x_vip_inprog = fields.Boolean(
			default=False,
			compute='_compute_vip_inprog',
		)

	@api.multi
	def _compute_vip_inprog(self):
		for record in self:
			for line in record.order_id.order_line:
				if line.product_id.default_code == '495':
					record.x_vip_inprog = True




# ----------------------------------------------------------- Recommendations ---------------------

	service_product_id = fields.Many2one(
			'openhealth.service.product',
			string='Product',
		)

	service_consultation_id = fields.Many2one(
			'openhealth.service.consultation',
			string='Consultation',
		)

	service_co2_id = fields.Many2one(
			'openhealth.service.co2',
			string='Co2',
		)

	service_quick_id = fields.Many2one(
			'openhealth.service.quick',
			string='Quick',
		)

	service_vip_id = fields.Many2one(
			'openhealth.service.vip',
			string='Vip',
		)

	service_excilite_id = fields.Many2one(
			'openhealth.service.excilite',
			string='Excilite',
		)

	service_ipl_id = fields.Many2one(
			'openhealth.service.ipl',
			string='Ipl',
		)

	service_ndyag_id = fields.Many2one(
			'openhealth.service.ndyag',
			string='Ndyag',
		)

	service_medical_id = fields.Many2one(
			'openhealth.service.medical',
			string='Medical',
		)

	service_cosmetology_id = fields.Many2one(
			'openhealth.service.cosmetology',
			string='Cosmetology',
		)




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



# ----------------------------------------------------------- Update ------------------------------
	# Update Recommendations
	#@api.multi
	def update_recos(self):
		"""
		high level support for doing this and that.
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
			print

		# Products
		else:
			lib.change_state(self.service_product_id, 'sale')

	# update_recos
