# -*- coding: utf-8 -*-
#
# 	counter
# 
from openerp import models, fields, api

import count_vars
import count_funcs


class counter(models.Model):
	
	_name = 'openhealth.counter'





# ----------------------------------------------------------- Computes - Solved ------------------------------------------------------

	# Total 
	total = fields.Char(
			string="Total", 		
		)






# ----------------------------------------------------------- Onchanges ------------------------------------------------------

	# Value 
	value = fields.Integer(
			string="Valor", 
			default=1, 
		)

	@api.onchange('value')
	def _onchange_value(self):

		# Date 
		self.date_modified = fields.datetime.now()

		# Total 
		name = count_funcs.get_name(self, self.prefix, self.separator, self.padding, self.value)
		self.total = name



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
		)


	# Padding
	padding = fields.Integer(
			string="Padding",
			default=0,  
		)














# ----------------------------------------------------------- Actions ------------------------------------------------------

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







# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Vspace 
	vspace = fields.Char(
			' ', 
			readonly=True
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


