# -*- coding: utf-8 -*-
#
# 	counter
# 
#

from openerp import models, fields, api

import ord_vars


class counter(models.Model):
	
	_name = 'openhealth.counter'



	name = fields.Selection(
			string="Nombre", 
			#default='receipt', 
			selection=ord_vars._sale_doc_type_list, 			
		)



	value = fields.Integer(
			string="Valor", 
			default=1, 
		)



	# Increase
	@api.multi 
	def increase(self):
		self.value = self.value + 1


	# Decrease
	@api.multi 
	def decrease(self):
		self.value = self.value - 1




	# Reset
	@api.multi 
	def reset(self):
		self.value = 1

