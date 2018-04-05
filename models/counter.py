# -*- coding: utf-8 -*-
#
# 	counter
# 
from openerp import models, fields, api
#from . import ord_vars
from . import count_vars


class counter(models.Model):
	
	_name = 'openhealth.counter'




# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Type
	x_type = fields.Selection(

			selection=count_vars._counter_type_list, 			

			string="Tipo", 
			#default='receipt', 
		)







	# Name
	name = fields.Selection(

			#selection=ord_vars._counter_type_list, 			
			selection=count_vars._counter_name_list, 			

			string="Nombre", 
		)





	# separator 
	separator = fields.Char(
			string="Separador",
			#default='',  
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




	# Total 
	total = fields.Char(

			string="Total", 
		
			compute='_compute_total', 
		)

	@api.multi
	#@api.depends()
	def _compute_total(self):
		
		for record in self:
		
			if record.prefix != False:
				#record.total = record.prefix + str(record.value)
				#record.total = record.prefix + str(record.value).zfill(record.padding)
				#record.total = record.prefix  +  '-'  +  str(record.value).zfill(record.padding)

				if record.separator != False: 
					record.total = record.prefix  +  record.separator  +  str(record.value).zfill(record.padding)
				else:
					record.total = record.prefix  +  str(record.value).zfill(record.padding)







	# Value 
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


