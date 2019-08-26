# -*- coding: utf-8 -*-
"""
		lib_qr.py

		Created: 			02 Nov 2018
		Last up: 	 		02 Nov 2018
"""
import datetime
import base64
import cStringIO
import qrcode




#------------------------------------------------ Get QR Data -------------------------------------
# Get QR Data
def get_qr_data(self):
	"""
	high level support for doing this and that.
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


	ruc_company = self.x_my_company.x_ruc

	type_code = _dic_type_code[self.x_type]

	series = self.x_serial_nr.split('-')[0]

	number = self.x_serial_nr.split('-')[1]

	igv = str(self.x_total_tax)

	total = str(self.amount_total)


	date_format = "%Y-%m-%d %H:%M:%S"
	date_format_pe = "%d/%m/%Y"
	date = (datetime.datetime.strptime(self.date_order, date_format) - datetime.timedelta(hours=5)).strftime(date_format_pe)


	type_doc = ''
	doc = ''

	if self.x_type in ['ticket_receipt', 'credit_note']:
		if self.x_id_doc_type not in [False] and self.x_id_doc not in [False, '']:
			type_doc = _dic_type_doc[self.x_id_doc_type]
			doc = self.x_id_doc

	elif self.x_type in ['ticket_invoice']:
		if self.x_ruc not in [False, '']:
			type_doc = '6'
			doc = self.x_ruc


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

	buffer = cStringIO.StringIO()

	img.save(buffer, format="PNG")

	img_str = base64.b64encode(buffer.getvalue())


	return img_str, name

# get_qr_img
