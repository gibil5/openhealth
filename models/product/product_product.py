# -*- coding: utf-8 -*-
"""
	*** Product Product
 
	Only Data model. No functions.

 	Created: 			 3 Nov 2018
 	Last up: 	 		17 oct 2020
"""
from openerp import models, fields, api

class ProductProduct(models.Model):
	_inherit = 'product.product'



# ----------------------------------------------------------- PL ---------------
	pl_subfamily = fields.Char()


# ----------------------------------------------------------- Print Ticket -----
	x_name_ticket = fields.Char()

	def get_name_ticket(self):
		"""
		Used by Print Ticket.
		"""
		return self.x_name_ticket

# ----------------------------------------------------------- Electronic - Get Code ----------------------------
	# Get Code
	#@api.constrains('name') - Commented because of Warning
	def get_code(self):
		"""
		Used by Electronic
		"""
		#print
		#print 'Get Code'
		code = '5555555555'
		return code
