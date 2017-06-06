# -*- coding: utf-8 -*-







# Consultation
_state_list = [
					('draft', 	'Inicio'),

					('inprogress', 	'En progreso'),

					('done', 	'Completo'),
				]


_hash_progress = {

						'draft':          	10, 
						'inprogress': 		50,
						'done': 			100, 
				}	





# Evaluation
EVALUATION_TYPE = [
		('Pre-arraganged Appointment', 'Consulta'),
		('Ambulatory', 'Procedimiento'),
		('Periodic Control', 'Control'),

		('Session', 'Sesión'),
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