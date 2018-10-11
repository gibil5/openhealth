# -*- coding: utf-8 -*-
#
# 		chk_order.py
#
# 		Python Constraints - Order 
#		Contains All Specifications 
# 
# 		Created: 			26 Aug 2018
# 		Last up: 	 		27 Sep 2018
#
from openerp.exceptions import ValidationError

import chk

_MODEL = 'sale.order'



# -----------------------------------------------------------  Serial Nr - Custom ------------------------------------------------------
# Check Serial Nr - Content 
def _check_x_serial_nr(self):
	print
	print 'Check Serial Nr'
	
	_name = 'x_serial_nr'

	# Loop 
	for record in self:

		# Init 	
		_value = record.x_serial_nr
		

		# Check Content 
		if _value != False and record.x_counter_value != 1: 


			# Init 
			x_type = record.x_type

	 		order = self.env['sale.order'].search([
														('x_type', 'in', [x_type]), 
														#('state', 'in', ['sale']), 
														('state', 'in', ['sale', 'cancel']), 
													],
														order='x_counter_value desc',
														limit=1,
													)
	 		last_serial_nr = order.x_serial_nr	

			serial_nr = record.x_serial_nr
	 		
			if last_serial_nr != False: 
		 		sn_1 = int(serial_nr.split('-')[1])
		 		sn_0 = int(last_serial_nr.split('-')[1])
		 		delta = sn_1 - sn_0
		 	else:  
		 		delta = -55


		 	# Prints 
	 		print record.patient.name 
			print serial_nr
			print last_serial_nr
	 		print delta 


			# Content 
			if delta != 1:
				raise ValidationError("Warning: %s not valid: %s" % (_name, _value))





# -----------------------------------------------------------  Ruc ------------------------------------------------------
# Check Ruc
def check_x_ruc(self):
	print
	print 'Check Ruc'
	
	# Init 
	_name = 'x_ruc'
	_length = 11
	_bad = [
				'00000000000', 
				'11111111111', 
				'12345678901', 
			]

	uniqueness = False
	format_number = True
	content = True

	# Check
	check_var_sale(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)




# ----------------------------------------------------------- Sale ------------------------------------------------------
# Check Var Reco
def check_var_sale(self, _model, _name, _length, _bad, uniqueness, format_number, content):
	print 
	print 'Check - Var Sale'


	# Loop 
	for record in self:
			
		# Init 
		_dic_reco = {	
						# Patient 
						'name': 		record.name, 
						'x_id_doc': 	record.x_id_doc, 
						'x_ruc': 		record.x_ruc, 
		}


		# Value 
		_value = _dic_reco[_name]

		#print _value + '.'

		#if _value != False: 
		if _value not in [False, '']: 

			chk.check_var(self, _model, _name, _length, _bad, _value, uniqueness, format_number, content)


