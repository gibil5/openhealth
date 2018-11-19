# -*- coding: utf-8 -*-



_dic_prefix_cn = {
					'ticket_receipt': 	'BC01',
					'ticket_invoice': 	'FC01',

					'receipt': 			'C01',
					'invoice': 			'C01',
					'sale_note': 		'C01',
					'advertisement': 	'C01',
}

_dic_prefix = {
					'ticket_receipt': 	'B001',
					'ticket_invoice': 	'F001',

					'receipt': 			'001',
					'invoice': 			'001',
					'sale_note': 		'001',
					'advertisement': 	'001',
}

_dic_padding = {
					'ticket_receipt': 	8,
					'ticket_invoice': 	8,

					'receipt': 			6,
					'invoice': 			6,
					'sale_note': 		10, 
					'advertisement': 	10, 
}




#------------------------------------------------ Getters -----------------------------------------

def get_prefix(x_type):
	"""
	high level support for doing this and that.
	"""
	return _dic_prefix[x_type]



def get_prefix_cn(x_type):
	"""
	high level support for doing this and that.
	"""
	return _dic_prefix_cn[x_type]



def get_padding(x_type):
	"""
	high level support for doing this and that.
	"""
	return _dic_padding[x_type]







#------------------------------------------------ Not Protected -----------------------------------

# State - Current !!
_state_list = [

				#('draft', 		'Quotation'),
				#('sent', 		'Quotation Sent'),
				#('sale', 		'Sale Order'),
				#('done', 		'Done'),
				#('cancel', 	'Cancelled'),

				('draft', 		'Presupuesto'),
				('sent', 		'Generado'),			
				('validated', 	'Validado'),			
				('sale', 		'Pagado'),				
				('done', 		'Completo'),
				('cancel', 		'Anulado'),
				('credit_note', 'Nota de Credito'),
			]



_dic_tc_type = {
					'ticket_invoice': 	'ticket_invoice',	
					'ticket_receipt': 	'ticket_receipt',
					'invoice': 			'invoice',	
					'receipt': 			'receipt',

					'ticket_invoice_cancel': 	'ticket_invoice',	
					'ticket_receipt_cancel': 	'ticket_receipt',
					'invoice_cancel': 			'invoice_cancel',	
					'receipt_cancel': 			'receipt_cancel',
}


_dic_type_code = {
					'ticket_invoice': 	'01',	
					'ticket_receipt': 	'03',

					#'invoice': 		'01',
					#'receipt': 		'03',
					'invoice': 			'11',		# Not Sunat Compliant !
					'receipt': 			'13',		# Not Sunat Compliant !

					'advertisement': 	'14',
					'sale_note': 		'15',
}


# Legacy 
_dic_type_leg = {

						'BOL' : 'receipt', 		
						'FAC' : 'invoice', 		
						'TKB' : 	'ticket_receipt', 		
						'TKF' : 	'ticket_invoice', 
						'advertisement' : 	'advertisement', 		
						'CE' : 		'sale_note', 		
						False: False, 
			}
