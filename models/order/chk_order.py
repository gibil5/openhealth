# -*- coding: utf-8 -*-
"""
 		chk_order.py

 		Python Constraints - Order. 
 		Contains some specifications.
 
 		Created: 			17 Dec 2018
		Last up: 	 		17 Dec 2018
"""
from __future__ import print_function
from openerp.exceptions import ValidationError

# -----------------------------------------------------------  Serial Nr --------------------------
def check_serial_nr(self):
	#print()
	#print('Check Serial Nr')
	
	_name = 'Nr de Serie'

	# Loop 
	for record in self:

		# Init 	
		_value = record.x_serial_nr

		# Check Content 
		if record.x_serial_nr != False: 
			if len(_value.split('-')) != 2:
				raise ValidationError("Error %s - El formato es incorrecto: %s" % (_name, record.x_serial_nr)) 

