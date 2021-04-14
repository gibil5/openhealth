# -*- coding: utf-8 -*-
"""
	Eval vars
	- Used by
	
	Created: 			02 Aug 2020
	Last up: 			 5 dec 2020
"""

# Consultation
_state_list = [
					('cancel', 		'Anulado'),
					('draft', 		'Inicio'),
					('inprogress', 	'En progreso'),
					('done', 		'Completo'),	
				]

_hash_progress = {
					'draft':          	10, 
					'inprogress': 		50,
					'done': 			100, 
				}	

# Evaluation
EVALUATION_TYPE = [
	('Pre-arraganged Appointment', 'Consulta'),
	('consultation', 'Consulta'),
	
	('Ambulatory', 'Procedimiento'),
	('procedure', 'Procedimiento'),

	('Periodic Control', 'Control'),
	('control', 'Control'),

	('Session', 'Sesión'),
	('session', 'Sesión'),
]

FITZ_TYPE = [
		('one','I'),
		('two','II'),
		('three','III'),
		('four','IV'),
		('five','V'),
		('six','VI')
		]

PHOTO_TYPE = [
		('one','I (1,2,3)'),
		('two','II (4,5,6)'),
		('three','III (7,8,9)')
		]

# Chief complaint
_chief_complaint_list = [

			#('acne',			'Acné'),	# Medical 
			#('acne_sequels_1','Acné y Secuelas Grado 1'),
			#('acne_sequels_2','Acné y Secuelas Grado 2'),
			#('acne_sequels_3','Acné y Secuelas Grado 3'),
			#('scar_1','Cicatriz Pequeño'),
			#('scar_2','Cicatriz Mediano'),
			#('scar_3','Cicatriz Grande'),
			#('mole_1','Lunar Pequeño'),
			#('mole_2','Lunar Mediano'),
			#('mole_3','Lunar Grande'),
			#('stains_1','Manchas Grado 1'),
			#('stains_2','Manchas Grado 2'),
			#('stains_3','Manchas Grado 3'),
			#('ruby_points','Puntos Rubi'),
			#('keratosis_1','Queratosis Grado 1'),
			#('keratosis_2','Queratosis Grado 2'),
			#('keratosis_3','Queratosis Grado 3'),			
			#('rejuvenation_face_1','Rejuvenecimiento Facial Grado 1'),
			#('rejuvenation_face_2','Rejuvenecimiento Facial Grado 2'),
			#('rejuvenation_face_3','Rejuvenecimiento Facial Grado 3'),
			#('none',''), 

			# Begin
			('acne_active','Acné Activo'),
			('acne_sequels','Acné y Secuelas'),
			('tatoo','Tatuaje'),
			('cosmetology','Cosmiatria'),
			('alopecia','Alopecias'),
			('scar','Cicatriz'),
			('depilation','Depilación'),
			('emangiomas','Hemangiomas'),
			('mole','Lunar'),
			('stains','Manchas'),
			('monalisa_touch','Monalisa Touch'),
			('polyp','Pólipo'),
			('psoriasis','Psoriasis'),
			('ruby_point','Punto rubí'),
			('keratosis','Queratosis'),
			('cyst','Quiste'),
			('rejuvenation_capilar','Rejuvenecimiento Capilar'),	# Medical 
			('rejuvenation_facial','Rejuvenecimiento Facial'),
			('rejuvenation_hands','Rejuvenecimiento en manos'),
			('rejuvenation_neck','Rejuvenecimiento en cuello'),
			('rejuvenation_face_neck','Rejuvenecimiento Facial + Rejuvenecimiento en Cuello'),
			('rejuvenation_face_hands','Rejuvenecimiento Facial + Rejuvenecimiento en Manos'),
			('rejuvenation_face_neck_hands','Rejuvenecimiento Facial + Rejuvenecimiento en Cuello + Rejuvenecimiento en Manos'),
			('rosacea','Rosácea'),
			('telangiectasia','Telangectacias'),
			('varices','Varices'),
			('wart','Verruga'),
			('vitiligo','Vitiligo'),
			# End 		
]
