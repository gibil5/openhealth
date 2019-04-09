# -*- coding: utf-8 -*-
"""
		*** Product Product - Deprecated ? 
 
 		Created: 			 3 Nov 2018
 		Last up: 	 		 9 Apr 2019
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
