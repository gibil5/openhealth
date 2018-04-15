# -*- coding: utf-8 -*-
#
# 	counter raw
# 
#

from openerp import models, fields, api

from . import ord_vars


class counter(models.Model):
	
	_name = 'openhealth.counter_raw'




	name = fields.Char(
			string="Nombre", 
			default = 'raw_counter', 

			compute='_compute_name', 
		)


	@api.multi

	def _compute_name(self):

		for record in self:
			record.name = str(record.value)




	value = fields.Integer(
			string="Valor", 
			default=0, 
		)



	@api.multi 
	def reset(self):
		self.value = 1



	# Increase
	@api.multi 
	def increase(self):
		print 'jx'
		print 'increase'
		print self.value
		self.value = self.value + 1
		print self.value



	# Decrease
	@api.multi 
	def decrease(self):
		self.value = self.value - 1




