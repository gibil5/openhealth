# -*- coding: utf-8 -*-
"""
 		chk_patient.py

 		Python Constraints - Product. Contains Specifications.
 
 		Created: 			 9 Apr 2019
		Last up: 	 		 9 Apr 2019
"""

from openerp.exceptions import ValidationError



#------------------------------------------------ Name ---------------------------------------------------
# Check Name - Uniqueness
def check_name(self):
	#print
	#print 'Check - Name'

	# Init 	
	#var_name = 'name'
	#var_name = 'Nombre'
	var_name = 'NAME'


	# Loop 
	for record in self:

		# Init 	
		var_value = record.name


		# Content 
		#if record.name == '0':
		#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)


		# Uniqueness 
		if record.name != False: 

			count = self.env['product.template'].search_count([
																	('name', '=', record.name),

																	('pl_price_list', '=', '2019'),
										])
			

			if count > 1: 
				raise ValidationError("Warning: %s already exists: %s" % (var_name, record.name)) 

	# all records passed the test, don't return anything


