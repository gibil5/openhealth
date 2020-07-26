# -*- coding: utf-8 -*-
"""
	Order Funcs
	Encapsulate Order Business Rules

	Created: 			 4 Dec 2019
	Last up: 	 		24 Jul 2020
"""
from __future__ import print_function
import datetime

# ----------------------------------------------------------- Ticket - Get Raw Line - Aux ----------------
def get_date_corrected(date_order):
	"""
	Used by:
		- Get Ticket Raw
	"""
	print()
	print('Get Date Corrected')
	DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	date_field1 = datetime.datetime.strptime(date_order, DATETIME_FORMAT)
	date_field2 = date_field1 + datetime.timedelta(hours=-5, minutes=0)
	DATETIME_FORMAT_2 = "%d-%m-%Y %H:%M:%S"
	date_corrected = date_field2.strftime(DATETIME_FORMAT_2)
	return date_corrected

# ----------------------------------------------------------- Ticket - Get Raw Line - Aux ----------------
def get_credit_note_type(self):
	"""
	Used by:  
		- Get Ticket Raw
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

