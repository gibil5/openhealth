# -*- coding: utf-8 -*-
"""
		lib_qr.py

		Created: 			02 Nov 2018
		Last up: 	 		23 Jul 2020
"""
import datetime
import base64

#import cStringIO
from io import StringIO ## for Python 3

import qrcode

#------------------------------------------------ Get QR Data -------------------------------------
# Get QR Data
def get_qr_data(self):
	"""
	Encapsulates the Business Logic for:
	QR creation for:
		- Ticket Receipts, 
		- Ticket Invoices, 
		- Credit Notes.
	"""
	#print
	#print 'Get QR Data'

	# Init
	_dic_type_code = {
						'ticket_receipt': '03',
						'ticket_invoice': '01',
						'credit_note': '07',
						#'debit_note': '08',
	}

	_dic_type_doc = {
						'dni': 		'1',
						'ruc': 		'6',
						'other': 	'0',
						'ptp': 		'0',
						'passport': 	'7',
						'foreign_card': '4',
						'foreigner_card': '4',		# Old format
	}



	ruc_company = self.ruc_company

	type_code = _dic_type_code[self.x_type]

	series = self.serial_nr.split('-')[0]

	number = self.serial_nr.split('-')[1]

	igv = str(self.total_tax)

	total = str(self.amount_total)


	date_format = "%Y-%m-%d %H:%M:%S"
	date_format_pe = "%d/%m/%Y"

	#date = (datetime.datetime.strptime(self.date_order, date_format) - datetime.timedelta(hours=5)).strftime(date_format_pe)
	date = (datetime.datetime.strptime(self.date, date_format) - datetime.timedelta(hours=5)).strftime(date_format_pe)


	type_doc = ''
	doc = ''


	# Receipt
	if self.x_type in ['ticket_receipt', 'credit_note']:
		if self.receptor_id_doc_type not in [False] and self.receptor_id_doc not in [False, '']:
			type_doc = _dic_type_doc[self.receptor_id_doc_type]
			doc = self.receptor_id_doc


	# Invoice
	elif self.x_type in ['ticket_invoice',]:
		if self.receptor_ruc not in [False, '']:
			type_doc = '6'
			doc = self.receptor_ruc

	# Other
	else:
		print('This should not happen !')

	se = '|'

	qr_data = ruc_company + se + type_code + se + series + se + number + se + igv + se + total + se + date + se + type_doc + se + doc

	return qr_data

# get_qr_data



#------------------------------------------------ Get QR Img -------------------------------------
# Get QR Img
def get_qr_img(qr_data):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get QR Img'


	qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4, )

	name = qr_data + '.png'

	qr.add_data(qr_data) #you can put here any attribute SKU in my case

	qr.make(fit=True)

	img = qr.make_image()

	#buffer = cStringIO.StringIO()
	buffer = io.StringIO()

	img.save(buffer, format="PNG")

	img_str = base64.b64encode(buffer.getvalue())


	return img_str, name

# get_qr_img
