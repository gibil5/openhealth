# -*- coding: utf-8 -*-
"""
	Eval vars
		Used by: Consultation, Procedure...
	
	Created: 			02 Aug 2020
	Last up: 			13 apr 2021
"""

# Evaluation
EVALUATION_TYPE = [
	('consultation', 'Consulta'),	
	('procedure', 'Procedimiento'),
	('control', 'Control'),
	('session', 'Sesión'),
]

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
