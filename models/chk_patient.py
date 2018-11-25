# -*- coding: utf-8 -*-
"""
 		chk_patient.py

 		Python Constraints - Patient. Contains All Specifications.
 
 		Created: 			26 Aug 2018
		Last up: 	 		27 Sep 2018
"""
from openerp.exceptions import ValidationError
import chk



#------------------------------------------------ Name ---------------------------------------------------
# Check Name - Uniqueness
def check_name(self):
	#print
	#print 'Check - Name'

	# Init 	
	#var_name = 'name'
	var_name = 'Nombre'


	# Loop 
	for record in self:

		# Init 	
		var_value = record.name


		# Content 
		#if record.name == '0':
		#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)


		# Uniqueness 
		if record.name != False: 
			count = self.env['oeh.medical.patient'].search_count([
																	('name', '=', record.name),
										])
			if count > 1: 
				raise ValidationError("Warning: %s already exists: %s" % (var_name, record.name)) 

	# all records passed the test, don't return anything




# ----------------------------------------------------------- Ruc ---------------------------------
# Check Ruc
def check_x_ruc(self):
	#print
	#print 'Check Ruc - 2nd version'
	
	# Init
	_name = 'Ruc'
	length = 11


	# Loop 
	for record in self:

		# Init
		_value = record.x_ruc


		# Format
		if record.x_ruc != False: 

			if not record.x_ruc.isdigit():
				raise ValidationError("Check Paciente: %s debe ser un numero: %s" % (_name, _value))

			if len(str(record.x_ruc))!= length: 
				raise ValidationError("Check Paciente: %s debe tener %s digitos: %s" % (_name, str(length), _value))






# -----------------------------------------------------------  Id Doc -----------------------------
# Check Id Doc
def check_x_id_doc(self):
	#print 
	#print 'Check - Id Doc'


	# Init 	
	#_name = 'x_id_doc'
	_name = 'Documento de Identidad'


	# Loop 
	for record in self:

		# Init 	
		_value = record.x_id_doc

		_type = record.x_id_doc_type

		# Init 					
		if _type in ['dni']: 
			length = 8
		#elif _type in ['passport', 'ptp', 'foreign_card']: 
		elif _type in ['passport', 'ptp', 'foreign_card', 'foreigner_card']: 
			length = 12
		elif _type in ['other']: 
			length = 20



		# Content 
		if  _type in ['dni']: 
			if _value in [
							'00000000',
							'11111111',
							'22222222',
							'33333333',
							'44444444',
							'55555555',
							'66666666',
							'77777777',
							'88888888',
							'99999999',
							'12345678',
						]:

				#raise ValidationError("C Warning: x_id_doc not valid: %s" % _value)
				raise ValidationError("Check Paciente: %s no es valido: %s" % (_name, _value))



		# Format
		if _value != False: 

			# Only DNI - Is a Digit
			if  _type in ['dni']: 
				if not _value.isdigit():
					#raise ValidationError("Rec Warning: x_id_doc must be a Digit: %s" % _value)
					#raise ValidationError("Check Paciente: %s must be a Digit: %s" % (_name, _value))
					raise ValidationError("Check Paciente: %s debe ser un numero: %s" % (_name, _value))
						

			# All but Other - Has a fixed length
			if _type not in ['other']:
				if len(str(_value))!= length: 
					#raise ValidationError("Rec Warning: x_id_doc must have " + str(length) + " numbers: %s" % _value)
					#raise ValidationError("Check Paciente: %s must have %s numbers: %s" % (_name, str(length), _value))
					raise ValidationError("Check Paciente: %s debe tener %s digitos: %s" % (_name, str(length), _value))



		# Uniqueness 
		#if _value != False: 
		#	count = self.env['oeh.medical.patient'].search_count([
		#															('x_id_doc', '=', _value),
		#								])
		#	if count > 1: 
		#		raise ValidationError("Check Paciente: %s ya existe en la BDD: %s" % (_name, _value)) 


	# all records passed the test, don't return anything







# -----------------------------------------------------------  Id Code - Nr Historia --------------
# Check Id Code  - Nr Historia - Uniqueness, Content, Format 
def check_x_id_code(self):
	#print 
	#print 'Check - Id Code'

	# Init 	
	#_name = 'x_id_code'
	_name = 'Nr de Historia'


	# Loop 
	for record in self:

		# Init 	
		_value = record.x_id_code
		_length = 6


		# Content 
		if _value == '0000000':
			#raise ValidationError("Warning: x_id_code not valid: %s" % _value)
			#raise ValidationError("Warning: %s not valid: %s" % (_name, _value))
			raise ValidationError("Check Paciente: %s no es valido: %s" % (_name, _value))


		# Format
		if _value != False: 

			# Is Digit 
			if not _value.isdigit(): 
				#raise ValidationError("Warning: %s must be a Digit: %s" % (_name, _value))
				raise ValidationError("Check Paciente: %s debe ser un Digito: %s" % (_name, _value))
			
			# Fixed Length 
			if len(str(_value))!= _length: 
				#raise ValidationError("Warning: %s must have %s numbers: %s" % (_name, str(_length), _value))
				raise ValidationError("Check Paciente: %s debe tener %s numeros: %s" % (_name, str(_length), _value))


		# Uniqueness 
		#if _value != False:
		#	count = self.env['oeh.medical.patient'].search_count([
		#															('x_id_code', '=', _value),
		#								])
		#	if count > 1: 
		#		raise ValidationError("Warning: %s already exists: %s" % (_name, _value)) 

	# all records passed the test, don't return anything

