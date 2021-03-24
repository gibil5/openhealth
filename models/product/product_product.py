# -*- coding: utf-8 -*-
"""
	*** Product Product
 
 	Created: 			 3 nov 2018
 	Last up: 	 		24 mar 2021
"""
from openerp import models, fields, api


class ProductProduct(models.Model):
	_inherit = 'product.product'


# ----------------------------------------------------------- Members ----------
	pl_family = fields.Char()		# added: 24 mar 2021
	pl_subfamily = fields.Char()
	x_name_ticket = fields.Char()


# ----------------------------------------------------------- Print Ticket -----
	def get_name_ticket(self):
		"""
		Used by Print Ticket
		"""
		return self.x_name_ticket

# ----------------------------------------------------------- Electronic - Get Code ----------------------------
	#@api.constrains('name') - Commented because of Warning
	def get_code(self):
		"""
		Get code
		Used by Electronic
		"""
		code = '5555555555'
		return code

# ----------------------------------------------------------- Is Vip Card -------------------------
	def is_vip_card(self):					
		"""
		Introspection compliant
		"""
		if self.pl_family in ['card']:
			is_vip_card = True
		else:
			is_vip_card = False
		return is_vip_card
