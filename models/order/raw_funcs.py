# -*- coding: utf-8 -*-
"""
	Order Funcs
	Encapsulate Order Business Rules

	Created: 			4 Dec 2019
	Last up: 	 		Id.
"""
from __future__ import print_function
#from openerp.addons.openhealth.models.libs import lib
#from . import ord_vars
#from openerp import _
#from openerp.exceptions import Warning as OrderError



# ----------------------------------------------------------- Ticket - Get Raw Line - Aux ----------------
def get_credit_note_type(self):
	"""
	Used by Print Ticket.
	"""
	_dic_cn = {
				'cancel': 					'Anulación de la operación.',
				'cancel_error_ruc': 		'Anulación por error en el RUC.',
				'correct_error_desc': 		'Corrección por error en la descripción.',
				'discount': 				'Descuento global.',
				'discount_item': 			'Descuento por item.',
				'return': 					'Devolución total.',
				'return_item': 				'Devolución por item.',
				'bonus': 					'Bonificación.',
				'value_drop': 				'Disminución en el valor.',
				'other': 					'Otros.',
				False: 						'',
	}

	return _dic_cn[self.x_credit_note_type]


# ----------------------------------------------------------- Ticket - Get Raw Line ----------------
# Raw Line
def get_ticket_raw_line(self, argument):
	"""
	Abstraction. 
	Used by tickets.
	Can be used by all entries. 
	Types:
		- Receipt, 
		- Invoice, 
		- Credit note. 
	"""

	print()
	print('OFuncs - Get Ticket Raw Line')

	print(argument)

	line = 'empty'

	bold = True



	# Credit note
	if argument in ['date_credit_note']:
		tag = 'Fecha:'
		value = self.get_date_corrected()

	elif argument in ['denomination_credit_note_owner']:
		tag = 'Denominacion:'
		value = self.x_credit_note_owner.x_serial_nr

	elif argument in ['date_credit_note_owner']:
		tag = 'Fecha de emision:'
		value = self.x_credit_note_owner.get_date_corrected()

	elif argument in ['reason_credit_note']:
		tag = 'Motivo:'
		#value = self.get_credit_note_type()
		value = get_credit_note_type(self)




	# Receipt
	elif argument in ['receipt_patient_name']:
		tag = 'Cliente:'
		value = self.patient.name

	elif argument in ['receipt_patient_dni']:
		tag = 'DNI:'
		value = self.x_id_doc

	elif argument in ['receipt_patient_address']:
		tag = 'Direccion:'
		value = self.get_patient_address()




	# Invoice
	elif argument in ['invoice_firm_name']:
		tag = 'Razon social:'
		value = self.patient.x_firm

	elif argument in ['invoice_patient_ruc']:
		tag = 'RUC:'
		value = self.x_ruc

	elif argument in ['invoice_firm_address']:
		tag = 'Direccion:'
		value = self.get_firm_address()




	# Sale - Not Credit Note
	elif argument in ['sale_date']:
		tag = 'Fecha:'
		value = self.get_date_corrected()

	elif argument in ['sale_serial_number']:
		tag = 'Ticket:'
		value = self.x_serial_nr




	# Totals
	elif argument in ['totals_net']:
		tag = 'OP. GRAVADAS S/.'
		value = str(self.get_total_net())
		bold = False

	elif argument in ['totals_free']:
		tag = 'OP. GRATUITAS S/.'
		value = '0'
		bold = False

	elif argument in ['totals_exonerated']:
		tag = 'OP. EXONERADAS S/.'
		value = '0'
		bold = False



	elif argument in ['totals_unaffected']:
		tag = 'OP. INAFECTAS S/.'
		value = '0'
		bold = False

	elif argument in ['totals_tax']:
		tag = 'I.G.V. 18% S/.'
		value = str(self.get_total_tax())
		bold = False

	elif argument in ['totals_total']:
		tag = 'TOTAL S/.'
		value = str(self.get_amount_total())
		bold = False




	# Words
	elif argument in ['words_header']:
		tag = 'Son:'
		value = ''

	elif argument in ['words_soles']:
		tag = ''
		value = str(self.get_total_in_words())

	elif argument in ['words_cents']:
		tag = ''
		value = str(self.get_total_cents())

	elif argument in ['words_footer']:
		tag = ''
		value = 'Soles'




	# Items
	elif argument in ['items_header']:
		tag = 'items'
		value = 'header'





	# Else
	else:
		print('This should not happen !')


	# Go
	if bold:
		line = self.format_line(tag, value)

	else:
		line = self.format_line_lean(tag, value)



	#print(line)
	return line




