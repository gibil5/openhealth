# -*- coding: utf-8 -*-
"""
 	test_cases_pat.py

 	Test Cases - Patients

	Created: 			28 Sep 2018
	Last up: 	 		28 Sep 2018
"""
from . import creates as cre


# ---------------------------------------------------- Test Cases ---------------------------------
# Test Cases - Patients
def test_cases(self, container_id, doctor_id):
	"""
	Test Cases - Patients.
	"""


	# Init
	_pars = [
				# Patient 1 - REVILLA RONDON JOSE JAVIER - DNI
				{
						'active': 		False,
						'test_case': 	'dni',

						'name': 		'REVILLA RONDON JOSE JAVIER',
						'name_last': 	'revilla rondon',
						'name_first':  	'jose javier',

						'id_doc_type': 	'dni',
						'id_doc':  		'09817194',
						#'id_doc_type': 	False,
						#'id_doc':  		False,

						'ruc': 			'10098171946',
						'firm': 		'Revilla y Asociados',

						'sex': 			'Male',
						'address': 		'Av. San Borja Norte 610,San Borja,lima',

						'dni':			False,
						'id_code':  	False,
				},




				# Patient 2 - Passport
				{
						'active': 		False,
						'test_case': 	'passport',

						'name': 		'NUÑEZ NUÑEZ FATIMA',
						'name_last': 	'nuñez nuñez',
						'name_first':  	'fatima',

						'ruc': 			'12345678904',
						'firm': 		'Nuñez y Asociados',

						'id_doc_type': 	'passport',
						'id_doc':  		'PA-123456789',
						'dni':			False,

						'sex': 			'Female',
						'address': 		'Av. San Borja Norte 610,San Borja,lima',

						'id_code':  	False,
				},




				# Patient 3 - PTP
				{
						'active': 		False,
						'test_case': 	'ptp',

						'name': 		'TOTTI TOTTI FRANCESCO',
						'name_last': 	'totti totti',
						'name_first':  	'francesco',
						'ruc': 			False,
						'firm': 		False,

						'id_doc_type': 	'ptp',
						'id_doc':  		'PTP-12345678',
						'dni':			False,

						'sex': 			'Male',
						'address': 		'Av. San Borja Norte 610,San Borja,lima',

						'id_code':  	False,
				},



				# Patient 4 - OTHER
				{
						'active': 		False,
						'test_case': 	'other',

						'name': 		'MICHELOT MICHELOT IVANNA',
						'name_last': 	'michelot michelot',
						'name_first':  	'ivanna',
						'ruc': 			False,
						'firm': 		False,

						'id_doc_type': 	'other',
						'id_doc':  		'1234567',
						'dni':			False,

						'sex': 			'Female',
						'address': 		'Av. San Borja Norte 610,San Borja,lima',

						'id_code':  	False,
				},



				# Patient 5 - CE
				{
						'active': 		False,
						'test_case': 	'foreign_card',

						'name': 		'RABELAIS RABELAIS FRANCOIS',
						'name_last': 	'rabelais rabelais',
						'name_first':  	'francois',

						'ruc': 			'12345678903',
						'firm': 		'Rabelais y Asociados',

						'id_doc_type': 	'foreign_card',

						'id_doc':  		'CE-123456789',
						'dni':			False,

						'sex': 			'Male',
						'address': 		'Av. San Borja Norte 610,San Borja,lima',

						'id_code':  	False,
				},



				# Patient 6 - CE OLD
				{
						'active': 		False,
						'test_case': 	'ce_old',

						'name': 		'COMANECI COMANECI NADIA',
						'name_last': 	'comaneci comaneci',
						'name_first':  	'nadia',

						'id_doc_type': 	'foreigner_card',

						'id_doc':  		'123456790',

						'sex': 			'Female',
						'address': 		'Av. San Borja Norte 610,San Borja,lima',

						'ruc': 			'12345678903',
						'firm': 		'Comaneci y Asociados',
						'dni':			False,
						'id_code':  	False,
				},
		]




	# Loop
	pat_array = []

	for par in _pars:

		# Init
		active = par['active']


		if active:

			#print par
			#print par['test_case']
			#print par['name']
			#print

			test_case = par['test_case']
			id_doc_type = par['id_doc_type']
			id_doc = par['id_doc']
			dni = par['dni']
			name = par['name']
			name_last =	par['name_last']
			name_first = par['name_first']
			sex = par['sex']
			address = par['address']
			id_code = par['id_code']

			# Nils
			name_last = par['name_last']
			name_first = par['name_first']
			ruc = par['ruc']
			firm = par['firm']



			# Create

			patient = cre.create_patient(self, container_id, test_case, name, sex, address, \
																					id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first, id_code, dni)

			pat_array.append(patient)

	return pat_array
	# test_cases
