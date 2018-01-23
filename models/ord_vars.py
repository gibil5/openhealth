# -*- coding: utf-8 -*-





# State - Current !!
_state_list = [

				#('draft', 		'Quotation'),
				#('sent', 		'Quotation Sent'),
				#('sale', 		'Sale Order'),
				#('done', 		'Done'),
				#('cancel', 	'Cancelled'),

				#('draft', 		'Presupuesto'),
				#('sent', 		'Pagado'),
				#('sale', 		'Facturado'),				
				#('done', 		'Completo'),
				#('cancel', 		'Anulado'),




				('draft', 		'Presupuesto'),

				#('sent', 		'Pagado'),
				('sent', 		'Generado'),

				#('sale', 		'Facturado'),				
				('sale', 		'Pagado'),				




				('printed', 	'Impreso'),
				('done', 		'Completo'),
				('cancel', 		'Anulado'),

			]











_counter_type_list = [

						('emr', 				'Historias'),


						('receipt', 			'Boleta'),
						('invoice', 			'Factura'),
						('advertisement', 		'Canje Publicidad'),
						('sale_note', 			'Canje NV'),
						('ticket_receipt', 		'Ticket Boleta'),
						('ticket_invoice', 		'Ticket Factura'),

						('vip', 				'Tarjeta VIP'),

						#('', 			''),
		]











_sale_doc_type_list = [

						('ticket_receipt', 		'Ticket Boleta'),
						('ticket_invoice', 		'Ticket Factura'),

						('receipt', 			'Boleta'),
						('invoice', 			'Factura'),

						('advertisement', 		'Canje Publicidad'),
						('sale_note', 			'Canje NV'),
						

						#('', 			''),
		]









_owner_type_list = [
						('product', 			'Product'),
						('service', 			'Servicio'),
		]










_dic_model = {

						'receipt' : 'openhealth.receipt', 		
						'invoice' : 'openhealth.invoice', 		

						'advertisement' : 	'openhealth.advertisement', 		
						'sale_note' : 		'openhealth.sale_note', 		

						'ticket_receipt' : 	'openhealth.ticket_receipt', 		
						'ticket_invoice' : 	'openhealth.ticket_invoice', 		

						False :	False, 
			}








# Deprecated ?
#_x_state_list = [
#				('draft', 			'Presupuesto'),
#				('payment', 		'Pagado'),
				#('proof', 		    'Comprobante'),
				#('machine', 		'Reservación de Sala'),
				#('sale', 			'Venta'),
#				('sale', 			'Confirmado'),
				#('confirmed', 		'Confirmado'),
				#('invoice', 		'Facturado'),
#				('done', 			'Completo'),
#				('printed', 		'Impreso'),
#				('cancel', 			'Cancelado'),
#]








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
