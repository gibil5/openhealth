

# 3 Nov 2017


	state = fields.Selection(
		[
			#('draft', 'Draft PO'),
			('draft', 'Borrador'),
			
			#('sent', 'RFQ Sent'),
			('sent', 'Enviado'),


			#('to approve', 'To Approve'),
			('to approve', 'Validar'),


			#('purchase', 'Purchase Order'),
			('purchase', 'Orden de C/S'),

			

			('bill_ready', 'Factura lista'),
			('bill_paid', 'Factura pagada'),
			('product_received', 'Producto recibido'),




			#('cancel', 'Cancelled')
			('cancel', 'Cancelado'), 

			#('done', 'Done'),
			('done', 'Completo'),
			#('done', 'Cotizado'),
		], 
		string='Status', 
		readonly=True, 
		index=True, 
		copy=False, 
		default='draft', 
		track_visibility='onchange'
	)








	#x_type = fields.Selection(

	#	[	
	#		('rfq', 	'Demanda de Cotización'),
	#		('po', 		'Orden de C/S'),
	#	], 
			
	#	string='Tipo', 

	#	required=False, 
	#)
