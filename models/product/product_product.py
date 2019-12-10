# -*- coding: utf-8 -*-
"""
		*** Product Product
 
 		Created: 			 3 Nov 2018
 		Last up: 	 		10 Dec 2019
"""

from openerp import models, fields, api

class ProductProduct(models.Model):

	_inherit = 'product.product'

	#_order = 'name'




# ----------------------------------------------------------- Print Ticket -------------------------------

	x_name_ticket = fields.Char()


	def get_name_ticket(self):
		"""
		Used by Print Ticket.
		"""
		return self.x_name_ticket
		#return False



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
