# -*- coding: utf-8 -*-
#
# 		Counter
#
# 		Created: 			26 Aug 2016
# 		Last up: 	 		 3 Sep 2018
# 
from openerp import models, fields, api
import count_vars
import user 

class Counter(models.Model):
	
	_name = 'openhealth.counter'




# ----------------------------------------------------------- QC ------------------------------------------------------

	delta = fields.Integer(
			string="Delta", 
			compute="_compute_delta",
		)

	@api.multi
	#@api.depends('total')
	def _compute_delta(self):
		#print
		#print 'Counter - Compute Delta'
		for record in self:
			if record.x_type in ['sale']: 
				record.delta = user.get_delta(record)
			else:
				record.delta = -55


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name
	name = fields.Selection(
			selection=count_vars._counter_name_list, 			
			string="Nombre", 
		)


	# Value 
	value = fields.Integer(
			string="Valor", 
			default=1, 
		)


	# Type
	x_type = fields.Selection(
			selection=count_vars._counter_type_list, 			
			string="Tipo", 
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

