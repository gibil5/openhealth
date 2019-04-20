# -*- coding: utf-8 -*-
"""
		chk_order.py

		Python Constraints - Order 
		Contains All Specifications 
 
		Created: 			26 Aug 2018
		Last up: 	 		27 Sep 2018
"""
from openerp.exceptions import ValidationError
from . import chk
_MODEL = 'sale.order'



# -----------------------------------------------------------  Ruc --------------------------------------
# Check Ruc
def check_ruc(self):
	#print
	#print 'Chk - Check Ruc'

	var_name = 'Ruc'
	_name = 'x_ruc'
	_length = 11


	# Loop 
	for record in self:

		# Content
		if record.x_ruc in ['12345678901', False]:
			raise ValidationError("Check: Ruc not valid: %s" % record.x_ruc)



		# Format - Is Digit
		if not record.x_ruc.isdigit():
			raise ValidationError("Check: %s must be a Digit: %s" % (_name, record.x_ruc))
		
		# Format - Has Length
		if len(record.x_ruc) != _length: 
			raise ValidationError("Check: %s must have %s numbers: %s" % (_name, str(_length), record.x_ruc))



		# Uniqueness 
		#count = self.env['sale.order'].search_count([
		#												('x_ruc', '=', record.x_ruc),
		#								])
		#if count > 1: 
			#raise ValidationError("Warning: NAME already exists: %s" % record.name)
		#	raise ValidationError("Warning: %s already exists: %s" % (var_name, record.x_ruc)) 


	# all records passed the test, don't return anything
