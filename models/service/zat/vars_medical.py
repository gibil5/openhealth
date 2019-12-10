# -*- coding: utf-8 -*-



# ---------------------------------------------- Treatment - Medical --------------------------------------------------------

# Criosurgery
_med_crio_list = [
		('1',			'1 Sesión'),	
		('10',			'10 Sesiones'),

		('none',''),
		]


# Hialuronic
_med_hia_list = [
		('hialuronic',			'1 Jeringa - Rejuvenecimiento Facial'),	
		('hialuronic_repair',	'1 Jeringa - Rejuvenecimiento Facial - REPAIR'),
		('none',''),
		]


# Sclerotherapy
_med_scle_list = [
		('sclerotherapy',		'Piernas - Varices'),	
		('none',''),
		]


# Botulinum Toxin
_med_bot_list = [
		('botulinum_toxin',		'1 Zona - Rejuvenecimiento Facial'),	
		('none',''),
		]


# Intravenous
_med_int_list = [
		('intravenous_vitamin',		'VITAMINA C ENDOVENOSA - na - na - 1'),	
		('none',''),
		]



# Lepismatic
_lep_dic_zone = {
	'lepismatic_back_acne': 	'back', 	
	'lepismatic_back_stains': 	'back',	
	'lepismatic_face_acne': 	'face_all',	
	'lepismatic_face_stains': 	'face_all',	
}

_lep_dic_pathology = {
	'lepismatic_back_acne': 	'acne', 	
	'lepismatic_back_stains': 	'stains',	
	'lepismatic_face_acne': 	'acne',	
	'lepismatic_face_stains': 	'stains',	
}

_med_lep_list = [
		('lepismatic_back_acne',		'Espalda - Acne'),	
		('lepismatic_back_stains',		'Espalda - Manchas'),	
		('lepismatic_face_acne',		'Todo Rostro - Acne'),	
		('lepismatic_face_stains',		'Todo Rostro - Manchas'),	
		('none',''),
	]




# Plasma
_pla_dic = {
		'plasma_head_rejuvenation_1':		{"zone":"head",	"pathology":"rejuvenation_capilar", "sessions": "1"},
		'plasma_head_rejuvenation_2':		{"zone":"head",	"pathology":"rejuvenation_capilar", "sessions": "2"},	
		'plasma_head_rejuvenation_3':		{"zone":"head",	"pathology":"rejuvenation_capilar", "sessions": "3"},	
		'plasma_face_rejuvenation_1':		{"zone":"face_all",	"pathology":"rejuvenation_face", "sessions": "1"},	
		'plasma_face_rejuvenation_2':		{"zone":"face_all",	"pathology":"rejuvenation_face", "sessions": "2"},	
		'plasma_face_rejuvenation_3':		{"zone":"face_all",	"pathology":"rejuvenation_face", "sessions": "3"},	
}

_med_pla_list = [
		('plasma_head_rejuvenation_1',		'Rejuvenecimiento Capilar - 1 Sesión'),	
		('plasma_head_rejuvenation_3',		'Rejuvenecimiento Capilar - 3 Sesiones'),	
		('plasma_face_rejuvenation_1',		'Rejuvenecimiento Facial - 1'),	
		('plasma_face_rejuvenation_3',		'Rejuvenecimiento Facial - 3'),	
		('none',''),
	]

