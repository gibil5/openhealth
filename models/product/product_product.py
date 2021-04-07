# -*- coding: utf-8 -*-
"""
	*** Product Product
 
 	Created: 			 3 nov 2018
 	Last up: 	 		24 mar 2021
"""
from openerp import models, fields, api
from . import px_vars

class ProductProduct(models.Model):
	_inherit = 'product.product'


# ----------------------------------------------------------- Members ----------
	pl_subfamily = fields.Char()

	x_name_ticket = fields.Char()

	pl_price_list = fields.Selection(
			[
				('2019', '2019'),
				('2018', '2018'),
			],
			string='Lista de Precios',
			#required=True,
			required=False,
		)

	#pl_treatment = fields.Char()
	pl_treatment = fields.Selection(
			selection=px_vars._treatment_list,
			string='Treatment',
			required=False,
		)

	#pl_family = fields.Char()		# added: 24 mar 2021
	pl_family = fields.Selection(
			selection=px_vars._family_list,
			string='Family',
			#required=True,
			required=False,
		)

	#company_id = fields.Char()


# ----------------------------------------------------------- Methods - Dep ! ----------------------------------

# ----------------------------------------------------------- Print Ticket -----
	#def get_name_ticket(self):
	def get_name_ticket_dep(self):
		"""
		Used by Print Ticket
		"""
		return self.x_name_ticket

# ----------------------------------------------------------- Electronic - Get Code ----------------------------
	#@api.constrains('name') - Commented because of Warning
	def get_code(self):
		"""
		Get code
		Used by Electronic new - pl_lib_exp
		"""
		code = '5555555555'
		return code

# ----------------------------------------------------------- Is Vip Card -------------------------
	#def is_vip_card(self):					
	def is_vip_card_dep(self):					
		"""
		Introspection compliant
		"""
		if self.pl_family in ['card']:
			is_vip_card = True
		else:
			is_vip_card = False
		return is_vip_card
