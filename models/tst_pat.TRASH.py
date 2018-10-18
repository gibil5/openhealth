
# ----------------------------------------------------------- Test Integration - Treatment ------------------------------------------------------
# Test Init - Patient  
def test_init(self, container_id, patient_id=False, partner_id=False, doctor_id=False, treatment_id=False, pl_id=False):
	print 
	print 'Tst - Patient - Test Init'
	print self 


	# Init
	patient_1 = False
	patient_2 = False
	patient_3 = False
	patient_4 = False
	patient_5 = False
	patient_6 = False
	patient_7 = False



# Patient 1 - Passport

	# Init
	test_case = 'passport, ticket_receipt'

	id_doc_type = 'passport'
	id_doc = 'PA-123456789'

	name = 'NUÑEZ NUÑEZ FATIMA'
	name_last = 'nuñez nuñez'
	name_first = 'fatima'

	sex = 'Female'
	address = 'Av. San Borja Norte 610,San Borja,Lima'
	
	# Nils 
	name_last = ''
	name_first = ''
	#doctor_id = False
	ruc = False
	firm = False


	# Create 
	patient = cre.create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first)

	patient_1 = patient




# Patient 2 - CE

	# Init
	test_case = 'foreign_card, ticket_receipt'

	id_doc_type = 'foreign_card'
	id_doc = 'CE-123456789'


	name = 'RABELAIS RABELAIS FRANCOIS'

	sex = 'Male'
	address = 'Av. San Borja Norte 610,San Borja,Lima'
	



	# Nils 
	name_last = 'rabelais rabelais'
	name_first = 'francois'
	#doctor_id = False
	ruc = False
	firm = False


	# Create 
	patient = cre.create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first)
	patient_2 = patient



# Patient 3 - PTP

	# Init
	test_case = 'ptp, ticket_receipt'

	id_doc_type = 'ptp'
	id_doc = 'PTP-12345678'


	name = 'TOTTI TOTTI FRANCESCO'

	sex = 'Male'
	address = 'Av. San Borja Norte 610,San Borja,Lima'
	



	# Nils 
	name_last = 'totti totti'
	name_first = 'francesco'
	#doctor_id = False
	ruc = False
	firm = False


	# Create 
	patient = cre.create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first)
	patient_3 = patient



# Patient 4 - OTHER

	# Init
	test_case = 'other, ticket_receipt'

	id_doc_type = 'other'
	id_doc = '1234567'


	name = 'MICHELOT MICHELOT IVANNA'

	sex = 'Female'
	address = 'Av. San Borja Norte 610,San Borja,Lima'



	# Nils 
	name_last = 'michelot michelot'
	name_first = 'ivanna'
	#doctor_id = False
	ruc = False
	firm = False


	# Create 
	patient = cre.create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first)
	patient_4 = patient




# Patient 5 - DNI

	# Init
	test_case = 'dni, ticket_receipt'

	id_doc_type = 'dni'
	#id_doc = 'x2345678'
	id_doc = '12345678'


	name = 'REVILLA REVILLA JOSEX'


	sex = 'Male'
	address = 'Av. San Borja Norte 610,San Borja,Lima'



	# Nils 
	name_last = 'revilla revilla'
	name_first = 'josex'
	#doctor_id = False
	ruc = False
	firm = False


	# Create 
	patient = cre.create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first)
	patient_5 = patient





# Patient 6 - RUC

	# Init
	test_case = 'other, ticket_invoice'

	id_doc_type = 'other'
	id_doc = '12345'


	name = 'RONDON RONDON SEBASTIAN'
	sex = 'Male'
	address = 'Av. San Borja Norte 610,San Borja,Lima'

	name_last = 'rondon rondon'
	name_first = 'sebastian'
	ruc = '12345678902'
	firm = 'Rondon y Asociados'



	# Create 
	patient = cre.create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first)
	patient_6 = patient





# Patient 7 - DNI, Legacy 

	# Init
	test_case = 'dni, ticket_receipt, legacy'

	id_doc_type = False
	id_doc = False
	dni = '49171890'


	name = 'NEO NEO NEODIUMX'
	sex = 'Male'
	address = 'Av. San Borja Norte 610,San Borja,Lima'

	name_last = 'neo neo'
	name_first = 'neodiumx'

	ruc = False
	firm = False


	# Extras 
	id_code = '000003'


	# Create 
	patient = cre.create_patient(self, container_id, test_case, name, sex, address, id_doc_type, id_doc, ruc, firm, doctor_id, name_last, name_first, id_code, dni)
	patient_7 = patient



	# Rets 
	pat_array = [patient_1, patient_2, patient_3, patient_4, patient_5, patient_6, patient_7]

	return pat_array

# test_init





# 17 Oct 2018 

				# x
				#{
				#		'test_case': 	'', 

				#		'name': 		'', 
				#		'name_last': 	'', 
				#		'name_first':  	'', 
				#		'ruc': 			False, 
				#		'firm': 		False, 

				#		'id_doc_type': 	'', 
				#		'id_doc':  		'', 
				#		'dni':			False, 

				#		'sex': 			'Female', 
				#		'address': 		'Av. San Borja Norte 610,San Borja,Lima',						

				#		'id_code':  	False,
				#}, 
