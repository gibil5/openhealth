# -*- coding: utf-8 -*-
#
# 		chk_patient.py
#
# 		Python Constraints - Patient 
#		Contains All Specifications 
# 
# 		Created: 			26 Aug 2018
# 		Last up: 	 		27 Sep 2018
#
from openerp.exceptions import ValidationError

import chk

# ----------------------------------------------------------- Constants ------------------------------------------------------
_MODEL = 'oeh.medical.patient'


# ----------------------------------------------------------- Name ------------------------------------------------------
def _check_name(self):
	#print
	#print 'Check Name'

	# Init 
	_name = 'name'
	_length = False
	_bad = False

	uniqueness = True
	format_number = False
	content = False

	# Check
	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)



# ----------------------------------------------------------- Id Code ------------------------------------------------------
# Check Id Code - Hr Historia  
def _check_x_id_code(self):
	#print
	#print 'Check Id Code'

	# Init 
	_name = 'x_id_code'
	_length = 6
	_bad = [
				'000000', 
			]

	uniqueness = True
	format_number = True
	content = True

	# Check
	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)




# ----------------------------------------------------------- Name ------------------------------------------------------
# Check Ruc
def _check_x_ruc(self):
	#print
	#print 'Check Ruc'
	
	# Init 
	_name = 'x_ruc'
	_length = 11
	_bad = [
				'00000000000', 
				'11111111111', 
				'12345678901', 
			]

	uniqueness = True
	format_number = True
	content = True

	# Check
	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)




# ----------------------------------------------------------- Name ------------------------------------------------------
# Check Phone 3
def _check_phone_3(self):
	#print
	#print 'Check Phone 3'
	
	# Init 
	_name = 'phone_3'
	_length = False
	_bad = False

	uniqueness = False
	format_number = True
	content = False

	# Check
	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)



# ----------------------------------------------------------- Name ------------------------------------------------------
# Check Phone
def _check_phone(self):
	#print
	#print 'Check Phone'
	
	# Init 
	_name = 'phone'
	_length = False
	_bad = False

	uniqueness = False
	format_number = True
	content = False

	# Check
	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)



# ----------------------------------------------------------- Name ------------------------------------------------------
# Check Mobile
def _check_mobile(self):
	#print
	#print 'Check Mobile'
	
	# Init 
	_name = 'mobile'
	_length = False
	_bad = False

	uniqueness = False
	format_number = True
	content = False

	# Check
	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)






# ----------------------------------------------------------- Patient ------------------------------------------------------
# Check Var Reco
def check_var_patient(self, _model, _name, _length, _bad, uniqueness, format_number, content):
	#print 
	#print 'Check - Var Reco'


	# Loop 
	for record in self:
			
		# Init 
		_dic_reco = {	
						# Patient 
						'name': 		record.name, 
						'x_id_code': 	record.x_id_code, 
						'x_id_doc': 	record.x_id_doc, 
						'x_ruc': 		record.x_ruc, 
						'phone': 		record.phone, 
						'mobile': 		record.mobile, 
						'phone_3': 		record.phone_3, 
		}


		# Value 
		_value = _dic_reco[_name]

		#print _value

		if _value != False: 

			chk.check_var(self, _model, _name, _length, _bad, _value, uniqueness, format_number, content)






# -----------------------------------------------------------  Id Doc ------------------------------------------------------
# Check Id Doc - Documento Identidad - Uniqueness, Format 
def check_x_id_doc(self):
	#print 
	#print 'Check - Id Doc'

	# Init 	
	_name = 'x_id_doc'


	# Loop 
	for record in self:

		# Init 	
		_value = record.x_id_doc
		
		_type = record.x_id_doc_type

		# Init 					
		if _type in ['dni']: 
			length = 8
		elif _type in ['passport', 'ptp', 'foreign_card']: 
			length = 12
		elif _type in ['other']: 
			length = 20



		# Content 
		#if _value == '0000000':
		#	raise ValidationError("C Warning: x_id_doc not valid: %s" % _value)


		# Format
		if _value != False: 

			# Only DNI - Is a Digit
			if  _type in ['dni']: 
				if not _value.isdigit():
					#raise ValidationError("Rec Warning: x_id_doc must be a Digit: %s" % _value)
					raise ValidationError("Rec Warning: %s must be a Digit: %s" % (_name, _value))
						

			# All but Other - Has a fixed length
			if _type not in ['other']:
				if len(str(_value))!= length: 
					#raise ValidationError("Rec Warning: x_id_doc must have " + str(length) + " numbers: %s" % _value)
					raise ValidationError("Rec Warning: %s must have %s numbers: %s" % (_name, str(length), _value))
			

		# Uniqueness 
		if _value != False: 
			count = self.env['oeh.medical.patient'].search_count([
																	('x_id_doc', '=', _value),
										])
			if count > 1: 
				#raise ValidationError("Rec Warning: x_id_doc already exists: %s" % _value)
				raise ValidationError("Rec Warning: %s already exists: %s" % (_name, _value)) 

	# all records passed the test, don't return anything




# -----------------------------------------------------------  Id Code ------------------------------------------------------
# Check Id Code  - Nr Historia - Uniqueness, Content, Format 
def check_x_id_code(self):
	#print 
	#print 'Check - Id Code'

	# Init 	
	_name = 'x_id_code'


	# Loop 
	for record in self:

		# Init 	
		_value = record.x_id_code
		_length = 6


		# Content 
		if _value == '0000000':
			#raise ValidationError("Warning: x_id_code not valid: %s" % _value)
			raise ValidationError("Warning: %s not valid: %s" % (_name, _value))


		# Format
		if _value != False: 

			# Is Digit 
			if not _value.isdigit(): 
				raise ValidationError("Warning: %s must be a Digit: %s" % (_name, _value))
			
			# Fixed Length 
			if len(str(_value))!= _length: 
				raise ValidationError("Warning: %s must have %s numbers: %s" % (_name, str(_length), _value))


		# Uniqueness 
		if _value != False: 
			count = self.env['oeh.medical.patient'].search_count([
																	('x_id_code', '=', _value),
										])
			if count > 1: 
				raise ValidationError("Warning: %s already exists: %s" % (_name, _value)) 

	# all records passed the test, don't return anything




#------------------------------------------------ Name ---------------------------------------------------
# Check Name - Uniqueness
def check_name(self):
	#print 
	#print 'Check - Name'

	# Init 	
	var_name = 'name'


	# Loop 
	for record in self:

		# Init 	
		var_value = record.x_id_code

		# Content 
		#if record.name == '0':
		#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)

		# Uniqueness 
		if record.name != False: 
			count = self.env['oeh.medical.patient'].search_count([
																	('name', '=', record.name),
										])
			if count > 1: 
				#raise ValidationError("Warning: NAME already exists: %s" % record.name)
				raise ValidationError("Warning: %s already exists: %s" % (var_name, record.name)) 

	# all records passed the test, don't return anything



