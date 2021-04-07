# -*- coding: utf-8 -*-
"""
	Sale Order Line	
	Created:            26 Aug 2016
	Last mod:            3 Jun 2019

	- Respect the Law of Demeter. Avoid Train Wrecks.
"""
from __future__ import print_function
from openerp import models, fields, api
from . import chk_order_line
				
#from . import px_vars  		# Dep

class SaleOrderLine(models.Model):
	""" 
	Sale Order Line
	""" 
	_inherit = 'sale.order.line'



# ----------------------------------------------------------- Get Product -------------------------------
	def get_product(self):
		return self.product_id.name




# ----------------------------------------------------------- Is Current Price List -------------------------------

	def is_current_price_list(self):
		#print()
		#print('Order Line - Is Current Price List')

		#if self.product_id.pl_price_list in ['2019']:		# Train Wreck of Size 2
		if self.product_id.is_current_price_list():			# Respects the LOD
			is_current = True

		else:		
			is_current = False

		return is_current


# ----------------------------------------------------------- Remove Myself -------------------------------

	@api.multi
	def remove_myself(self):
		"""
		Remove Myself
		"""
		print()
		print('Remove Myself')

		self.state = 'draft'
		self.unlink()




# ----------------------------------------------------------- Print Ticket -------------------------------

	def get_price_unit(self):
		"""
		Used by Print Ticket.
		"""
		#if self.pl_transfer_free:
		#	value = 0
		#else:
		#	value = self.price_unit
		value = self.price_unit
		return value



	def get_price_subtotal(self):
		"""
		Used by Print Ticket.
		"""
		#if self.pl_transfer_free:
		if self.order_id.pl_transfer_free:
			value = 0
		else:
			value = self.price_subtotal
		return value




	def get_quantity(self):
		"""
		Used by Print Ticket.
		"""
		return int(self.product_uom_qty)





# ---------------------------------------- Constraints Python - Important -------------------------

	# Check Price List
	@api.constrains('pl_price_list')
	def check_pl_price_list(self):
		"""
		Check Pl Price List
		"""
		chk_order_line.check_pl_price_list(self)





# ---------------------------------------------- Fields - Categorized -----------------------------
	
	#pl_price_list = fields.Selection(
	pl_price_list = fields.Char(
			#selection=px_vars._price_list_list,		# Dep
			string='Lista de Precios',

			compute='_compute_pl_price_list',
		)

	@api.multi
	#@api.depends('state')
	def _compute_pl_price_list(self):
		"""
		high level support for doing this and that.
		"""
		for record in self:

			record.pl_price_list = record.product_id.pl_price_list




# ----------------------------------------------------------- Product ----------
	product_id = fields.Many2one(
		'product.product',
		string='Product',

		
		#domain=[('sale_ok', '=', True)],
		domain=[
					('sale_ok', '=', True),
					('pl_price_list', '=', '2019'),
				],


		change_default=True,
		ondelete='restrict',
		required=True
		)

