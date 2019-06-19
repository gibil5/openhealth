# -*- coding: utf-8 -*-



# Payment Methods
_payment_method_list = [
		('cash',			'Efectivo'), 
		('american_express','American Express'), 
		('cuota_perfecta',	'Cuota perfecta'), 
		('diners',			'Diners'), 
		('credit_master',	'Master - Crédito'), 
		('debit_master',	'Master - Débito'), 
		('credit_visa',		'Visa - Crédito'), 
		('debit_visa',		'Visa - Débito'), 
		#('',''), 
]





# States 
READONLY_STATES = {
		'draft': 		[('readonly', False)], 
		'sale': 		[('readonly', False)], 
		'done': 		[('readonly', True)], 	
		'editable': 	[('readonly', False)], 	
}



_state_list = [
				('draft', 		'Presupuesto'),		
				('sale', 		'Pagado'),				
				('cancel', 		'Anulado'),
]



_sale_doc_type_list = [
						#('ticket_receipt', 	'Ticket Boleta'),
						#('ticket_invoice', 	'Ticket Factura'),
						('ticket_receipt', 		'Boleta Electronica'),
						('ticket_invoice', 		'Factura Electronica'),

						('receipt', 			'Boleta'),
						('invoice', 			'Factura'),
						('advertisement', 		'Canje Publicidad'),
						('sale_note', 			'Canje NV'),
						#('', 			''),
]

