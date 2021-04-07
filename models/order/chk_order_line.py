# -*- coding: utf-8 -*-
"""
 		chk_order_line.py

 		Python Constraints - Product. Contains Specifications.
 
 		Created: 			 22 Apr 2019
		Last up: 	 		 22 Apr 2019
"""

from openerp.exceptions import ValidationError



#------------------------------------------------ Name ---------------------------------------------------
# Check Pl Price List - Uniqueness
def check_pl_price_list(self):
	print()
	print('Check - Pl Price List')

	# Init 	
	var_name = 'Pl Price List'


	# Loop 
	for record in self:

		# Init 	
		var_value = record.pl_price_list


		# Content 
		#if record.name == '0':
		#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)

		if record.pl_price_list not in ['2019']:
			raise ValidationError("C Warning: Pl Price List not valid: %s" % record.pl_price_list)



		# Uniqueness 
		#if record.name != False: 
		#	count = self.env['product.template'].search_count([
		#															('name', '=', record.name),
		#															('pl_price_list', '=', '2019'),
		#								])
		#	if count > 1: 
		#		raise ValidationError("Warning: %s already exists: %s" % (var_name, record.name)) 

	# all records passed the test, don't return anything


