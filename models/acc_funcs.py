# -*- coding: utf-8 -*-

from openerp import models, fields, api



_cuentab = {
				'service':			'704110001', 
				'product': 			'701101001', 
		}




_doc_type = {

			'other':			'0', 
			'foreigner_card':	'4', 
			'passport':			'7', 

			False: 			False, 
}


_h_type = {

			'invoice':			'01', 
			'receipt': 			'03', 

			'ticket_receipt': 	'12', 
			'ticket_invoice': 	'12', 

			'advertisement': 	'14', 
			'sale_note': 		'15', 

			False: 			False, 
	}




# ----------------------------------------------------------- Get Net and Tax ------------------------------------------------------

@api.multi
def get_net_tax(self, amount):

	x = amount / 1.18
	net = float("{0:.2f}".format(x))

	x = amount * 0.18
	tax = float("{0:.2f}".format(x))

	return net, tax 



