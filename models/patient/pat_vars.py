# -*- coding: utf-8 -*-



# First Contact
_first_contact_list = [
						('facebook','Facebook'), 					# New
						('instagram','Instagram'), 					# New
						('callcenter','Call Center'), 				# New 
						('old_patient','Paciente Antiguo'), 		# New 		

						('mail_campaign','Mailing'), 
						('recommendation','Recomendación'), 
						('tv','Tv'), 
						('radio','Radio'), 		
						('website','Web'), 

						# Deprecated
						('internet','Internet'), 
						('none','Ninguno'), 
]






# Id Doc Type
_id_doc_type_list = [
					('dni', 			'DNI'),
					('passport', 		'Pasaporte'),
					('foreign_card', 	'CE'),
					('ptp', 			'PTP'),
					('other', 			'Otro'),
					
					# Dep
					('foreigner_card', 	'CE - Antiguo'),
]



# Id Doc Code
_dic_id_doc_code = {
					'dni': 			'1',
					'ruc': 			'6',

					'other': 		'0',
					'ptp': 			'0',
					'foreign_card': '4',
					'foreigner_card': '4',		# Legacy				
					'passport': 	'7',
					
					#'sale_note': 		'15',
					False: 		'x',
}






_education_level_type = [
			('first', 'Primaria'),
			('second', 'Secundaria'),
			('technical', 'Instituto'),
			('university', 'Universidad'),
			('masterphd', 'Posgrado'),
]





_FAMILY_RELATION = [
			
			('none', 'Ninguno'),

			('Father', 'Padre'),
			('Mother', 'Madre'),
			('Brother', 'Hermano'),
			('Grand Father', 'Abuelo'),
			('Friend', 'Amigo'),
			('Husband', 'Esposo'),
			('Other', 'Otro'),
			#('Sister', 'Hermana'),
			#('Wife', 'Esposa'),
			#('Grand Mother', 'Abuela'),
			#('Aunt', 'Tía'),
			#('Uncle', 'Tío'),
			#('Nephew', 'Sobrino'),
			#('Niece', 'Sobrina'),
			#('Cousin', 'Primo'),
			#('Relative', 'Pariente'),
]



_sex_type_list = [
					('Male', 'Masculino'),
					('Female', 'Femenino'),
]



zip_dic_inv =  {
		
		1:	'Lima',
		2:	'Ancón',
		3:	'Ate',
		4:	'Barranco',
		5:	'Breña',
		6:	'Carabayllo',
		7:	'Comas',
		8:	'Chaclacayo',
		9:	'Chorrillos',
		10:	'El Agustino',
		
		11:	'Jesús María',
		12:	'La Molina',
		13:	'La Victoria',
		14:	'Lince',
		15:	'Lurigancho',
		16:	'Lurín',
		17:	'Magdalena del Mar',
		18:	'Miraflores',
		19:	'Pachacamac',
		20:	'Pucusana',
		
		21:	'Pueblo Libre',
		22:	'Puente Piedra',
		23:	'Punta Negra',
		24:	'Punta Hermosa',
		25:	'Rímac',
		26:	'San Bartolo',
		27:	'San Isidro',
		28:	'Independencia',
		29:	'San Juan de Miraflores',
		30:	'San Luis',
		
		31:	'San Martín de Porres',
		32:	'San Miguel',
		33:	'Santiago de Surco',
		34:	'Surquillo',
		35:	'Villa María del Triunfo',
		36:	'San Juan de Lurigancho',
		37:	'Santa María del Mar',
		38:	'Santa Rosa',
		39:	'Los Olivos',
		40:	'Cieneguilla',
		
		41:	'San Borja',
		42:	'Villa El Salvador',
		43:	'Santa Anita',

		False: '',		
}




#------------------------------------------------ Getters -----------------------------------------

def get_id_doc_type_list():
	"""
	high level support for doing this and that.
	"""
	return _id_doc_type_list



def get_sex_type_list():
	"""
	high level support for doing this and that.
	"""
	return _sex_type_list



def get_first_contact_list():
	"""
	high level support for doing this and that.
	"""
	return _first_contact_list



def get_education_level_type():
	"""
	high level support for doing this and that.
	"""
	return _education_level_type


def get_FAMILY_RELATION():
	"""
	high level support for doing this and that.
	"""
	return _FAMILY_RELATION


def get_dic_id_doc_code(x_type):
	"""
	high level support for doing this and that.
	"""
	return _dic_id_doc_code[x_type]


def get_zip_dic_inv(x_type):
	"""
	high level support for doing this and that.
	"""
	return zip_dic_inv[x_type]


