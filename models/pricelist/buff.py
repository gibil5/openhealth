class ProductSubFamilyValueException(Exception):
	pass




# --------------------------------------------- Handle Exceptions subfamily ----
#@api.multi
def handle_exceptions_subfamily(self):
	"""
	Handle Exceptions subfamily
	"""
	#print()
	#print('PROD - Handle Exceptions - Subfamily')

	subfamily_arr = exc_vars._subfamily_list
	#print(subfamily_arr)
	#print(self.pl_subfamily)

	# subfamily
	try:
		if self.pl_subfamily not in subfamily_arr:
		msg = "ERROR: Producto Sub Familia Incorrecta"
		raise ProductSubFamilyValueException

	except ProductSubFamilyValueException:
		class_name = type(self).__name__
		obj_name = self.name
		msg =  msg + '\n' + class_name + '\n' + obj_name
		raise UserError(_(msg))





# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
#def fix_exceptions(self):
def fix_exceptions_dep(self):
	"""
	Fix Exceptions
	"""
	print()
	print('PROD - Fix Exceptions')

	_dic = {

	# Medical
	'VICTAMINA C ENDOVENOSA':	'vitamin_c_intravenous', 
	'CRIOCIRUGIA':	'cryosurgery',
	'ESCLEROTERAPIA': 'sclerotherapy',
	'PLASMA': 'plasma',
	'BOTOX': 'botox', 
	'REDUX': 'redux',
	'ACIDO HIALURONICO': 'hyaluronic_acid',
	'MESOTERAPIA NCTF': 'mesotherapy',
	'INFILTRACIONES': 'infiltrations', 

	# Cosmetology
	'PUNTA DE DIAMANTES': 'diamond_tip', 
	'CARBOXITERAPIA': 'carboxytherapy', 
	'LASER TRIACTIVE + CARBOXITERAPIA': 'laser_triactive_carboxytherapy',

	}

	# Fix
	if self.pl_treatment in _dic:
		self.pl_subfamily = _dic[self.pl_treatment]




# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
def handle_exceptions(self):
	"""
	Handle Exceptions
	"""
	#print()
	#print('Handle Exceptions')

	handle_exceptions_family(self)
	#handle_exceptions_subfamily(self)