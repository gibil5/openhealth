# -*- coding: utf-8 -*-






_sale_doc_type_list = [

				('receipt', 			'Recibo'),
				('invoice', 			'Factura'),

				('advertisement', 		'Canje publicidad'),
				('sale_note', 			'Nota de venta'),

				('ticket_receipt', 		'Ticket boleta'),
				('ticket_invoice', 		'Ticket factura'),

				#('', 			''),
	]






_x_state_list = [
				('draft', 			'Presupuesto'),



				('payment', 		'Pagado'),

				('proof', 		      'Comprobante'),



				('machine', 		'Reservación de Sala'),



				
				('sale', 			'Venta'),
				('invoice', 		'Facturado'),



				('done', 		'Completo'),
				('cancel', 		'Cancelado'),
	]




_state_list = [

				#('draft', 'Quotation'),
				#('sent', 'Quotation Sent'),
				#('sale', 'Sale Order'),
				#('done', 'Done'),
				#('cancel', 'Cancelled'),
					#('pre-draft', 	'Presupuesto consulta'),


				#('draft', 			'Presupuesto'),
				#('payment', 		'Pagado'),
				#('proof', 			'Comprobante'),
				#('machine', 		'Reserva de sala'),
				#('sale', 			'Confirmado'),
				#('invoice', 		'Facturado'),



				('draft', 		'Presupuesto'),
				#('sent', 		'Presupuesto enviado'),
				('sale', 		'Facturado'),
				('done', 		'Completo'),
				('cancel', 	'Cancelado'),
			]




_payment_method_list = [

		#('none','Ninguno'), 

		('cash','Efectivo'), 
		
		('cuota_perfecta','Cuota perfecta'), 
		
		('debit_visa','Débito - Visa'), 
		
		('debit_master','Débito - Master'), 
		
		('credit_visa','Crédito - Visa'), 
		
		('credit_master','Crédito - Master'), 
		
		('diners','Diners'), 
		
		('american_express','American Express'), 

		#('',''), 
	]





_sale_docs_list = [

		#('none','Ninguno'), 

		('receipt','Boleta'), 

		('invoice','Factura'), 

		('advertisement','Canje publicidad'), 


		#('sale_note','Nota de venta'), 
		('sale_note','Canje (nv)'), 


		('ticket_receipt','Ticket boleta'), 

		('ticket_invoice','Ticket factura'), 

		#('',''), 

	]
