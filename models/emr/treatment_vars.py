# -*- coding: utf-8 -*-

_test_scenario_list = [
	('all', 'All'),
	('product', 'Product'),
	('laser', 'Laser'),
	('cosmetology', 'Cosmetology'),
	('medical', 'Medical'),
	('new', 'New'),
	('credit_note', 'Nota de Credito'),
	('block_flow', 'Flujo bloqueado'),
]


# State 
_state_list = [
				('empty', 					'Inicio'),		# OK

				#('appointment', 			'Cita'),		# Dep

				('budget_consultation', 	'Presu C'),		# Important	
				('invoice_consultation', 	'Caja C'),			# OK 
				('consultation', 			'Consulta'),			# OK				
				('service', 				'Recom'),		# OK
				('budget_procedure', 		'Presu P'),		
				('invoice_procedure', 		'Caja P'),					# OK
				('procedure', 				'Proc'),					# OK
				('sessions', 				'Sesion'),				# OK
				('controls', 				'Control'),					
				('done', 					'Alta'),					# OK 
]


