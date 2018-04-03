# -*- coding: utf-8 -*-





# State 
_state_list = [

				('empty', 			'Inicio'),		# OK

				('appointment', 	'Cita'),		# OK



				('budget_consultation', 	'Pres C - Creado'),		# Important	


				
				#('invoice_consultation', 	'Caja - Con'),			# OK 
				#('invoice_consultation', 	'Facturado'),			# OK 
				('invoice_consultation', 	'Caja'),			# OK 

				('consultation', 			'Consulta'),			# OK
				
				#('service', 				'Recomendación'),		# OK
				('service', 				'Recom.'),		# OK
				




				#('budget_procedure', 		'Pres. P - Creado'),	#  Important
				('budget_procedure', 		'Presu Creado'),		




				#('invoice_procedure', 		'Caja - Pro'),				# OK
				#('invoice_procedure', 		'Facturado'),				# OK
				('invoice_procedure', 		'Caja'),				# OK




				#('procedure', 				'Procedimiento'),			# OK
				('procedure', 				'Proc.'),			# OK



				('sessions', 				'Sesiones'),				# OK
				

				#('controls', 				'Controles'),				# OK
				('controls', 				'Control'),					


				('done', 					'Alta'),					# OK 
]












# Family
_family_list = [
#		('private','Private'), 
		('product','Producto'), 

		('consultation','Consulta'), 
		
		('procedure','Procedimiento'), 


		('cosmetology','Cosmiatría'), 
]




# Progress 
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


