# -*- coding: utf-8 -*-
"""
		chk_electronic.py

		Check Electronic Order fields

		Created: 			 4 Nov 2018
		Last up: 	 		 4 Nov 2018
"""
from openerp.exceptions import ValidationError


# -----------------------------------------------------------  Serial Nr --------------------------
# Check Serial Nr
#def check_serial_nr(self):
def check_serial_nr(self, container_id):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Check Serial Nr'

	var_name = 'Serial Nr'
	name = 'serial_nr'
	x_length = 13


	# Loop
	for record in self:


		prefix = record.serial_nr.split('-')[0]
		number = record.serial_nr.split('-')[1]


		# Content
		if record.serial_nr in ['1234567890123', False]:
			#raise ValidationError("Warning: Ruc not valid: %s" % record.x_ruc)
			raise ValidationError("Warning: %s not valid: %s" % (name, record.serial_nr))

		#if prefix not in ['B001', 'F001']:
		if prefix not in ['B001', 'F001', 'BC01', 'FC01']:
			raise ValidationError("Warning: %s PREFIX not valid: %s" % (name, record.serial_nr))

		# Is Digit
		if not number.isdigit():
			raise ValidationError("Warning: %s NUMBER must be a Digit: %s" % (name, record.serial_nr))

		# Has Length
		if len(number) != 8:
			raise ValidationError("Warning: %s NUMBER must have 8 numbers: %s" % (name, record.serial_nr))



		# Format

		# Is Digit
		#if not record.serial_nr.isdigit():
		#	raise ValidationError("Warning: %s must be a Digit: %s" % (name, record.serial_nr))


		# Has Length
		if len(record.serial_nr) != x_length:
			raise ValidationError("Warning: %s must have %s numbers: %s"\
																		% (name, str(x_length), record.serial_nr))




		# Uniqueness
		count = self.env['openhealth.electronic.order'].search_count([
																		('serial_nr', '=', record.serial_nr),
																		('container_id', '=', container_id),
										])

		if count > 1:
			#raise ValidationError("Warning: NAME already exists: %s" % record.name)
			raise ValidationError("Warning: %s already exists: %s" % (var_name, record.serial_nr))


	# all records passed the test, don't return anything
