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
				('empty', 					'Inicio'),
				#('appointment', 			'Cita'),		# Dep
				('budget_consultation', 	'Presu C'),		
				('invoice_consultation', 	'Caja C'),		
				('consultation', 			'Consulta'),	
				('service', 				'Recom'),		
				('budget_procedure', 		'Presu P'),		
				('invoice_procedure', 		'Caja P'),		
				('procedure', 				'Proc'),		
				('sessions', 				'Sesion'),		
				('controls', 				'Control'),					
				('done', 					'Alta'),		
]
