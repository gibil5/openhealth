# -*- coding: utf-8 -*-



# Family
_family_list = [
#		('private','Private'), 
		('product','Producto'), 
		('consultation','Consulta'), 
		('procedure','Procedimiento'), 


		('cosmetology','Cosmiatría'), 
]




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

				('empty', 			'Inicio'),		# OK

				('appointment', 	'Cita'),		# OK



				#('budget_consultation', 	'Presupuesto-C'),		# Dep ? 


				
				#('invoice_consultation', 	'Caja - Con'),			# OK 
				('invoice_consultation', 	'Facturado'),			# OK 


				('consultation', 			'Consulta'),			# OK
				

				('service', 				'Recomendación'),		# OK
				

				#('budget_procedure', 		'Presupuesto-P'),	# Dep ? 



				#('invoice_procedure', 		'Caja - Pro'),				# OK
				('invoice_procedure', 		'Facturado'),				# OK



				('procedure', 				'Procedimiento'),			# OK
				

				('sessions', 				'Sesiones'),				# OK
				

				('controls', 				'Controles'),				# OK


				('done', 					'Alta'),					# OK 
			]


