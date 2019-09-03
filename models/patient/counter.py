# -*- coding: utf-8 -*-
"""
		Counter
		Still very useful

		Created: 			26 Aug 2016
		Last up: 	 		 2 Sep 2019
"""
from openerp import models, fields, api
from . import count_vars

from openerp.addons.openhealth.models.libs import user

class Counter(models.Model):
	
	_name = 'openhealth.counter'



# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name
	name = fields.Selection(

			#selection=count_vars._counter_name_list,		
			selection=count_vars._name_list,		

			string="Nombre", 
			default="emr",
			required=True,
		)


	# Type
	x_type = fields.Selection(

			#selection=count_vars._counter_type_list, 			
			selection=count_vars._type_list, 			
		
			string="Tipo", 
			default="medical",
			required=True,
		)


	# Value 
	value = fields.Integer(
			string="Valor", 
			default=1, 
			required=True,
		)


	# Separator 
	separator = fields.Char(
			string="Separador",
			default="",
			#required=True,
		)


	# Prefix 
	prefix = fields.Char(
			string="Prefijo", 
			default="0", 
			required=True,
		)


	# Padding
	padding = fields.Integer(
			string="Padding",
			default=5,
			required=True,
		)




	# Date created 
	date_created = fields.Datetime(
			string="Fecha de creación", 
			default = fields.Date.today,
			required=True, 
			)

	# Date modified
	date_modified = fields.Datetime(
			string="Ultima modificación", 
			default = fields.Date.today,
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



# ----------------------------------------------------------- Computes - Delta ------------------------------------------------------

	# Delta - For QC
	delta = fields.Integer(
			string="Delta", 

			compute="_compute_delta",
		)

	@api.multi
	def _compute_delta(self):
		#print
		#print 'Counter - Compute Delta'
		for record in self:
			if record.x_type in ['sale']: 
				record.delta = user.get_delta(record)
			else:
				record.delta = -55

