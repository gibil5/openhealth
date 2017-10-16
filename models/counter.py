# -*- coding: utf-8 -*-
#
# 	counter
# 
#

from openerp import models, fields, api

from . import ord_vars


class counter(models.Model):
	
	_name = 'openhealth.counter'




	name = fields.Selection(

			#selection=ord_vars._sale_doc_type_list, 			
			selection=ord_vars._counter_type_list, 			


			string="Nombre", 
			#default='receipt', 
		)





	vspace = fields.Char(
			' ', 
			readonly=True
			)



	value = fields.Integer(
			string="Valor", 
			default=1, 
		)

	@api.onchange('value')
	def _onchange_value(self):
		#print
		#print 'onchange - Value'
		#print 
		self.date_modified = fields.datetime.now()




	# Date created 
	date_created = fields.Datetime(
			string="Fecha de creación", 
			default = fields.Date.today,
			#readonly=True,
			required=True, 
			)


	# Date modified
	date_modified = fields.Datetime(
			string="Ultima modificación", 
			default = fields.Date.today,
			#readonly=True,
			required=True, 
			)





	# Increase
	@api.multi 
	def increase(self):
		self.value = self.value + 1
		self.date_modified = fields.datetime.now()

	# Decrease
	@api.multi 
	def decrease(self):
		self.value = self.value - 1
		self.date_modified = fields.datetime.now()


	# Reset
	@api.multi 
	def reset(self):
		self.value = 1
		self.date_modified = fields.datetime.now()


