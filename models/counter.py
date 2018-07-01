# -*- coding: utf-8 -*-
#
# 	counter
# 
from openerp import models, fields, api

import count_vars
#import count_funcs


class Counter(models.Model):
	
	_name = 'openhealth.counter'



# ----------------------------------------------------------- Static ------------------------------------------------------

	i = 0 


	# Increase Static
	@api.multi 
	def increase_static(self):
		
		print 
		print 'Increase Static'
		print 

		Counter.i = Counter.i + 1


		self.value_static = Counter.i 


		print Counter.i

		print 

		#self.value = self.value + 1
		#self.date_modified = fields.datetime.now()




# ----------------------------------------------------------- Pre ------------------------------------------------------

	# Value 
	value_static = fields.Integer(
			string="Valor Estático", 
			default=1, 
		)


	#@api.onchange('Counter.i')
	#def _onchange_Counter_i(self):
	#	print 
	#	print 'jx'
	#	print 



# ----------------------------------------------------------- Onchanges ------------------------------------------------------

	# Value 
	value = fields.Integer(
			string="Valor", 
			default=1, 
		)






# ----------------------------------------------------------- Primitives ------------------------------------------------------


	# Type
	x_type = fields.Selection(
			selection=count_vars._counter_type_list, 			
			string="Tipo", 
			#default='receipt', 
		)



	# Name
	name = fields.Selection(
			selection=count_vars._counter_name_list, 			
			string="Nombre", 
		)



	# Separator 
	separator = fields.Char(
			string="Separador",
		)



	# Prefix 
	prefix = fields.Char(
			string="Prefijo", 
			default=".", 
		)



	# Padding
	padding = fields.Integer(
			string="Padding",
			default=0,  
		)







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


	# Vspace 
	vspace = fields.Char(
			' ', 
			readonly=True
		)





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Increase
	@api.multi 
	def increase(self):
		self.value = self.value + 1
		self.date_modified = fields.datetime.now()
	# increase



	# Decrease
	@api.multi 
	def decrease(self):
		self.value = self.value - 1
		self.date_modified = fields.datetime.now()
	# decrease



