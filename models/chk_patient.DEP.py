

# 12 Noc 2018




# ----------------------------------------------------------- Constants ------------------------------------------------------
_MODEL = 'oeh.medical.patient'


# ----------------------------------------------------------- Name ------------------------------------------------------
#def _check_name(self):
	#print
	#print 'Check Name'

	# Init 
#	_name = 'name'
#	_length = False
#	_bad = False

#	uniqueness = True
#	format_number = False
#	content = False

	# Check
#	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)



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
#def _check_x_ruc_dep(self):
	#print
	#print 'Check Ruc'
	
	# Init 
#	_name = 'x_ruc'
#	_length = 11
#	_bad = [
#				'00000000000', 
#				'11111111111', 
#				'12345678901', 
#			]

#	uniqueness = True
#	format_number = True
#	content = True

	# Check
#	check_var_patient(self, _MODEL, _name, _length, _bad, uniqueness, format_number, content)




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


