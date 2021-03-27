# -*- coding: utf-8 -*-


# Id Doc type
_doc_type = {
				'other':			'0',
				'foreign_card':		'4',
				'passport':			'7',

				#'ptp':				'1', 		# Verify
				'ptp':				'0', 		# Verified

				#'dni':				'2', 		# Verify
				'dni':				'1', 		# Verified

				False: 			False,
}


# account_line 
_cuentab = {
				'service':			'704110001', 
				'product': 			'701101001', 
				'consu': 			'701101001', 
}

def get_cuentab(product_type):
	print()
	print('acc_vars - Get Cuentab')
	#print(product_type)
	return _cuentab[product_type]






#_h_type = {
_sale_type = {
				#'ticket_invoice': 	'12',
				#'ticket_receipt': 	'12',
				'ticket_invoice': 	'01',
				'ticket_receipt': 	'03',

				'invoice':			'01',
				'receipt': 			'03',
				'advertisement': 	'14',
				'sale_note': 		'15',
				False: 			False, 
}











