# -*- coding: utf-8 -*-
"""
	Product Vars
	Created: 			 01 Nov 2016
	Last up: 			 05 dec 2020
"""

# Laser
_laser_type_list = [

		# 2019
		#('LASER CO2 FRACCIONAL',	'LASER CO2 FRACCIONAL'),

		# 2018
		# Consultation
		('consultation',			'consultation'),

		# Laser
		('laser_co2','Laser Co2'),
		('laser_excilite','Laser Excilite'),
		('laser_ipl','Laser Ipl'),
		('laser_ndyag','Laser Ndyag'),
		('laser_quick','QuickLaser'),

		# Medical
		('medical',					'Tratamiento médico'),
		('criosurgery', 			'Criocirugía'),
		('botulinum_toxin', 		'Toxina botulínica'),
		('hyaluronic_acid', 		'Acido hialurónico'),
		('hyaluronic_acid_repair', 	'Acido hialurónico - Repair'),
		('intravenous_vitamin', 	'Vitamina intravenosa'),
		('lepismatic', 				'Lepismático'),
		('mesotherapy_nctf', 		'Mesoterapia NCTF'),
		('plasma', 					'Plasma'),
		('sclerotherapy', 			'Escleroterapia'),
		('infiltration_keloid', 	'Infiltracion Queloide'),
		('infiltration_scar', 		'Infiltracion Cicatriz'),
		# 12 Jul 2019
		('infiltration', 	'Infiltracion'),

		# Cosmetology
		('cosmetology','Cosmiatría'),

		# Cos
		('diamond_tip',									'diamond_tip'),
		('triactive_carboxytherapy_reductionchamber',	'triactive_carboxytherapy_reductionchamber'),
		('carboxytherapy',								'carboxytherapy'),
		('triactive_carboxytherapy',					'triactive_carboxytherapy'),

		('none',		'none'),
]

_time_list = [
				('15 min','15 min'),
				('30 min','30 min'),
				('60 min','60 min'),
				('none',''),
]


#------------------------------------------------ Vars ----------------------
_h_subfamily = {
					'product' : 		'Producto',
					'consultation' : 	'Consulta',
					'cosmetology' : 	'Cosmeatria',

					'laser_co2' : 		'Laser Co2',
					'laser_excilite' : 	'Laser Exc',
					'laser_ipl' : 		'Laser Ipl',
					'laser_ndyag' : 	'Laser Ndyag',
					'laser_quick' : 	'Quick Laser',

					'criosurgery' : 			'Criocirugia',
					'intravenous_vitamin' : 	'Vitamina Intravenosa',
					'botulinum_toxin' : 		'Toxina Botulinica',
					'hyaluronic_acid' : 		'Acido Hialuronico',
					'mesotherapy_nctf' :		'Mesoterapia NCTF',

					False: False,
}

# Zone
_level_list = [
		('1',	'1'),
		('2',	'2'),
		('3',	'3'),
		('4',	'4'),
		('5',	'5'),
]

# Zone
_zone_list = [
		# Infiltrations
		('any',		'any'),

		# Quick
		('face_all_neck',	'Todo Rostro Cuello'),
		('face_all_hands',	'Todo Rostro Manos'),
		('neck_hands',		'Cuello Manos'),

		# Other
		('areolas',		'areolas'),
		('armpits',		'armpits'),
		('arms',		'arms'),
		('back',		'back'),
		('belly',		'belly'),
		('body_local',	'Localizado Cuerpo'),
		('breast',		'breast'),
		('cheekbones',	'Pómulos'),
		('face',		'face'),
		('face_all',	'face_all'),
		('face_hands',	'face_hands'),
		('face_local',	'face_local'),
		('face_neck',	'face_neck'),
		('face_neck_hands',	'face_neck_hands'),
		('feet',		'feet'),
		('gluteus',		'gluteus'),
		('hands',		'Manos'),
		('head',		'head'),
		('legs',		'legs'),
		('neck',		'Cuello'),
		('package',		'package'),
		('shoulders',	'shoulders'),
		('vagina',		'vagina'),

		('1_zone',		'1_zone'),
		('1_hypodermic','1_hypodermic'),
		('1_hypodermic_repair','1_hypodermic_repair'),
		('x',		'x'),

		('na',		'na'),

		# Cosmetology
		('body_all',		'body_all'),
		('body',		'body'),
		('face_doublechin_neck',		'face_doublechin_neck'),

		('none',		'none'),
		('',		''),
]

_pathology_list = [

		# 28 Jun 2019
		('varices',			'varices'),

		# Standard
		('varicose',			'varicose'),



		# Med
		('keloid',		'keloid'),



		# Quick
		#('tatoo',			'Tatuaje'),
		('tatoo',			'tatoo'),
		#('tatoo_1',		'tatoo_1'),
		#('tatoo_2',		'tatoo_2'),
		#('tatoo_3',		'tatoo_3'),
		#('tatoo_4',		'tatoo_4'),


		#('rejuvenation',	'Rejuvenecimiento'),
		('rejuvenation',	'rejuvenation'),
		#('rejuvenation_1',	'rejuvenation_1'),
		#('rejuvenation_2',	'rejuvenation_2'),
		#('rejuvenation_3',	'rejuvenation_3'),
		#('rejuvenation_4',	'rejuvenation_4'),





		# Other
		#('wart',		'Verruga'),
		('wart',		'wart'),
		('wart_1',		'wart_1'),
		('wart_2',		'wart_2'),
		('wart_3',		'wart_3'),
		('wart_4',		'wart_4'),
		('wart_5',		'wart_5'),


		#('keratosis',	'Queratosis'),
		('keratosis',	'keratosis'),
		('keratosis_1',	'keratosis_1'),
		('keratosis_2',	'keratosis_2'),
		('keratosis_3',	'keratosis_3'),
		('keratosis_4',	'keratosis_4'),
		('keratosis_5',	'keratosis_5'),



		#('stains',		'Manchas'),
		('stains',		'stains'),
		('stains_1',	'stains_1'),
		('stains_2',	'stains_2'),
		('stains_3',	'stains_3'),
		('stains_4',	'stains_4'),
		('stains_5',	'stains_5'),



		#('cyst',		'Quiste'),
		('cyst',		'cyst'),
		('cyst_1',		'cyst_1'),
		('cyst_2',		'cyst_2'),
		('cyst_3',		'cyst_3'),
		('cyst_4',		'cyst_4'),
		('cyst_5',		'cyst_5'),



		#('acne_sequels',	'Acné y secuelas'),
		('acne_sequels',	'acne_sequels'),
		('acne_sequels_1',	'acne_sequels_1'),
		('acne_sequels_2',	'acne_sequels_2'),
		('acne_sequels_3',	'acne_sequels_3'),
		('acne_sequels_4',	'acne_sequels_4'),
		('acne_sequels_5',	'acne_sequels_5'),


		#('mole',		'Lunar'),
		('mole',		'mole'),
		('mole_1',		'mole_1'),
		('mole_2',		'mole_2'),
		('mole_3',		'mole_3'),
		('mole_4',		'mole_4'),
		('mole_5',		'mole_5'),



		#('scar',		'Cicatriz'),
		('scar',		'scar'),
		('scar_1',		'scar_1'),
		('scar_2',		'scar_2'),
		('scar_3',		'scar_3'),
		('scar_4',		'scar_4'),
		('scar_5',		'scar_5'),



		('rejuvenation_face',	'rejuvenation_face'),
		('rejuvenation_face_repair',	'rejuvenation_face_repair'),

		('rejuvenation_face_1',	'rejuvenation_face_1'),
		('rejuvenation_face_2',	'rejuvenation_face_2'),
		('rejuvenation_face_3',	'rejuvenation_face_3'),
		('rejuvenation_face_4',	'rejuvenation_face_4'),
		('rejuvenation_face_5',	'rejuvenation_face_5'),



		('rejuvenation_neck',	'rejuvenation_neck'),
		('rejuvenation_neck_1',	'rejuvenation_neck_1'),
		('rejuvenation_neck_2',	'rejuvenation_neck_2'),
		('rejuvenation_neck_3',	'rejuvenation_neck_3'),
		('rejuvenation_neck_4',	'rejuvenation_neck_4'),
		('rejuvenation_neck_5',	'rejuvenation_neck_5'),


		('rejuvenation_hands',	'rejuvenation_hands'),
		('rejuvenation_hands_1',	'rejuvenation_hands_1'),
		('rejuvenation_hands_2',	'rejuvenation_hands_2'),
		('rejuvenation_hands_3',	'rejuvenation_hands_3'),
		('rejuvenation_hands_4',	'rejuvenation_hands_4'),
		('rejuvenation_hands_5',	'rejuvenation_hands_5'),









		('rejuvenation_face_neck',	'rejuvenation_face_neck'),




		('acne',			'acne'),


		('acne_active',			'acne_active'),
		('alopecia',			'alopecia'),


		('depilation',			'depilation'),

		('emangiomas',		'emangiomas'),


		('polyp',		'polyp'),
		('ruby_point',	'ruby_point'),

		('monalisa_touch',	'monalisa_touch'),

		('psoriasis',			'psoriasis'),



		('rejuvenation_face_hands',			'rejuvenation_face_hands'),
		('rejuvenation_face_neck_hands',	'rejuvenation_face_neck_hands'),
		('rosacea',			'rosacea'),
		('ruby_points',		'ruby_points'),


		('telangiectasia',	'telangiectasia'),





		('vitiligo',			'vitiligo'),



		('x',		'x'),
		('rejuvenation_capilar',		'rejuvenation_capilar'),
		('na',		'na'),




		# Cosmetology
		('deep_face_cleansing',		'deep_face_cleansing'),

		('reaffirmation',		'reaffirmation'),

		('reduction_weight_measures',		'reduction_weight_measures'),

		('',		''),
		('',		''),
		('',		''),


		('none',		'none'),


		# Legacy
		('body_local',		'body_local'),
		('face_local',		'face_local'),

	]



















_sessions_list = [
		#('one',			'one'),
		#('six',			'six'),

		('1',			'1'),
		('10',			'10'),

		('2',			'2'),
		('3',			'3'),


		# Cosmetology
		('6',			'6'),
		('12',			'12'),

		('none',		'none'),
		]





_family_list = [

		# 6 Feb 2019
		('credit_note',		'credit_note'),

		# 12 Jul 2018
		('other',			'other'),


		# Service
		('consultation',	'consultation'),
		('consultation_gyn',	'consultation_gyn'),
		('laser',			'laser'),
		('medical',			'medical'),
		('cosmetology',		'cosmetology'),


		# Product
		#('topical',		'Tópico'),
		#('kit',			'Kit'),
		#('card',			'Tarjeta'),
		('topical',			'topical'),
		('kit',				'kit'),
		('card',			'card'),

		('none',		'none'),
]

_treatment_list = [

		# 19 Jul 2018
		('infiltration',			'infiltration'),

		# 12 Jul 2018
		('other',		'other'),

		# 29 May 2018
		('infiltration_scar',		'infiltration_scar'),
		('infiltration_keloid',		'infiltration_keloid'),

		# 28 May 2018
		('product',		'product'),
		('vip_card',		'vip_card'),

		('consultation',		'consultation'),

		('laser_quick',			'laser_quick'),
		('laser_co2',			'laser_co2'),
		('laser_excilite',		'laser_excilite'),
		('laser_ipl',			'laser_ipl'),
		('laser_ndyag',			'laser_ndyag'),
		('laser_m22',			'laser_m22'),

		('criosurgery',			'criosurgery'),
		('hyaluronic_acid',		'hyaluronic_acid'),
		('sclerotherapy',		'sclerotherapy'),
		('lepismatic',			'lepismatic'),
		('plasma',				'plasma'),
		('botulinum_toxin',		'botulinum_toxin'),
		('intravenous_vitamin',	'intravenous_vitamin'),

		# 2017
		('mesotherapy_nctf',		'mesotherapy_nctf'),
		('hyaluronic_acid_repair',		'hyaluronic_acid_repair'),

		# Cosmetology
		('triactive_carboxytherapy_reductionchamber',			'triactive_carboxytherapy_reductionchamber'),
		('carboxytherapy',			'carboxytherapy'),
		('diamond_tip',			'diamond_tip'),
		('triactive_carboxytherapy',			'triactive_carboxytherapy'),
		('',			''),

		#('none',			'none'),
		('none',		'none'),
]


#------------------------------------------------ Getters ----------------------
def get_family_list():
	"""
	Get Family list
	"""
	return _family_list

def get_treatment_list():
	"""
	Get Treatment list
	"""
	return _treatment_list

def get_zone_list():
	"""
	Get Zone list
	"""
	return _zone_list

def get_pathology_list():
	"""
	Get Pathology list
	"""
	return _pathology_list

def get_level_list():
	"""
	Get Level list
	"""
	return _level_list

def get_laser_type_list():
	"""
	Get laser type list
	"""
	return _laser_type_list

def get_time_list():
	"""
	Get time list
	"""
	return _time_list
