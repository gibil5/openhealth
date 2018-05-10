# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime


_cuentab = {
				'service':			'704110001', 
				'product': 			'701101001', 
				'consu': 			'701101001', 
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








#------------------------------------------------ Correct Time ---------------------------------------------------

def correct_time(self, date, delta):

	#print
	#print 'Correct'
	#print date 

	if date != False: 

		#1876-10-10 00:00:00
		year = int(date.split('-')[0])
		#print year 

		if year >= 1900:

			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
			DATETIME_FORMAT_sp = "%d/%m/%Y %H:%M"

			date_field1 = datetime.datetime.strptime(date, DATETIME_FORMAT)

			#date_corr = date_field1 + datetime.timedelta(hours=+5,minutes=0)
			date_corr = date_field1 + datetime.timedelta(hours=delta,minutes=0)

			date_corr_sp = date_corr.strftime(DATETIME_FORMAT_sp)

			#return date_corr
			return date_corr, date_corr_sp








# ----------------------------------------------------------- Get Net and Tax ------------------------------------------------------

@api.multi
def get_net_tax(self, amount):

	x = amount / 1.18
	net = float("{0:.2f}".format(x))

	x = amount * 0.18
	tax = float("{0:.2f}".format(x))

	return net, tax 



