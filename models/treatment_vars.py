# -*- coding: utf-8 -*-




_hash_progress = {


					#False:          0, 
					'empty':          0, 


					'appointment': 			10, 

					'budget_consultation':  15, 

					'invoice_consultation': 20,





					'consultation': 	30,
					'service': 			40, 


					'budget_procedure': 			50, 
					'invoice_procedure': 			60,


					'procedure': 		70, 
					'sessions': 		80, 
					'controls': 		90, 

					'done': 			100, 

		}





_state_list = [

				('empty', 			'Inicio'),



				('appointment', 			'Cita'),

				('budget_consultation', 	'Presupuesto-C'),
				
				('invoice_consultation', 	'Cancelado - Consulta'),





				('consultation', 	'Consulta'),

				('service', 		'Servicio'),
				


				('budget_procedure', 			'Presupuesto-P'),

				('invoice_procedure', 		'Cancelado - Procedimiento'),


				
				('procedure', 		'Procedimiento'),

				('sessions', 		'Sesiones'),

				('controls', 		'Controles'),



				('done', 			'Completo'),
			]


