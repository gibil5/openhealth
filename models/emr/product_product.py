# -*- coding: utf-8 -*-
"""
		*** Product Product
 
 		Created: 			 3 Nov 2018
 		Last up: 	 		 3 Nov 2018
"""

from openerp import models, fields, api

class ProductProduct(models.Model):

	_inherit = 'product.product'

	#_order = 'name'




# ----------------------------------------------------------- Get Code ----------------------------
	# Get Code
	#@api.constrains('name')
	def get_code(self):
		#print
		#print 'Get Code'

		code = '5555555555'

		return code
