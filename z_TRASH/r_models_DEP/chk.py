# -*- coding: utf-8 -*-
#
# 		chk.py
#
# 		Python Constraints - Abstract 
# 
# 		Created: 			26 Aug 2018
# 		Last up: 	 		27 Sep 2018
#
from openerp.exceptions import ValidationError


# ----------------------------------------------------------- Check ------------------------------------------------------
# Check Var - Uniqueness
def check_var(self, model, _name, _length, _bad, _value, uniqueness, format_number, content):
	#print 
	#print 'Check - Var'


	# Uniqueness 
	if uniqueness: 
		#print 'Uniqueness'
		
		count = self.env[model].search_count([
												(_name, '=', _value),
									])
		
		#print count 

		if count > 1: 
			raise ValidationError("Warning: %s already exists: %s" % (_name, _value)) 



	# Format Number
	if format_number: 
		#print 'Format Number'

		# Is Digit 
		if not _value.isdigit(): 
			raise ValidationError("Warning: %s must be a Digit: %s" % (_name, _value))
		
		if _length != False: 
			# Has Fixed Length 
			if len(str(_value))!= _length: 
				raise ValidationError("Warning: %s must have %s numbers: %s" % (_name, str(_length), _value))



	# Content
	if content: 
		#print 'Content'

		if _value in _bad:
			raise ValidationError("Warning: %s not valid: %s" % (_name, _value))

	# all records passed the test, don't return anything

