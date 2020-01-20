# -*- coding: utf-8 -*-
"""
		Pat Vars - Should migrate to Patient. As Class Vars

		Created: 			26 Aug 2016
		Last updated: 	 	21 Nov 2019
"""



_function_list = [
			('student', 		'Estudiante'),
			('employee', 		'Trabajador Dependiente'),
			('employee_independent', 	'Trabajador Independiente'),
			('entrepreneur', 	'Empresario'),
			('housekeeper', 	'Ama/o de casa'),
			('unemployed', 		'Desempleado'),
]

#Estudiante
#Trabajador Dependiente
#Trabajador Independiente
#Empresario
#Ama/o de casa
#Desempleado



_sex_type_list = [
					('Male', 'Masculino'),
					('Female', 'Femenino'),
]


_education_level_type = [
			('first', 'Primaria'),
			('second', 'Secundaria'),
			('technical', 'Instituto'),
			('university', 'Universidad'),
			('masterphd', 'Posgrado'),
]






zip_dic =  {
		
		'Lima':			1,
		'Ancón':		2,
		'Ate':			3,
		'Barranco':		4,
		'Breña':		5,
		'Carabayllo':	6,
		'Comas':		7,
		'Chaclacayo':	8,
		'Chorrillos':	9,
		'El Agustino':	10,
		'Jesús María':	11,
		'La Molina':	12,
		'La Victoria':	13,
		'Lince':		14,
		'Lurigancho':	15,
		'Lurín':		16,
		'Magdalena del Mar':	17,
		'Miraflores':	18,
		'Pachacamac':	19,
		'Pucusana':		20,
		'Pueblo Libre':	21,
		'Puente Piedra':22,
		'Punta Negra':	23,
		'Punta Hermosa':24,
		'Rímac':		25,
		'San Bartolo':	26,
		'San Isidro':	27,
		'Independencia':	28,
		'San Juan de Miraflores':	29,
		'San Luis':	30,
		'San Martín de Porres':	31,
		'San Miguel':	32,
		'Santiago de Surco':	33,
		'Surquillo':	34,
		'Villa María del Triunfo':	35,
		'San Juan de Lurigancho':	36,
		'Santa María del Mar':	37,
		'Santa Rosa':	38,
		'Los Olivos':	39,
		'Cieneguilla':	40,
		'San Borja':	41,
		'Villa El Salvador':	42,
		'Santa Anita':	43,		
}




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


