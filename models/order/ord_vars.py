# -*- coding: utf-8 -*-
"""
	Ord Vars

	Created: 			26 Aug 2016
	Last up: 			 5 dec 2020
"""

# Id Doc Type
_id_doc_type_list = [
					('dni', 			'DNI'),
					('passport', 		'Pasaporte'),
					('foreign_card', 	'CE'),
					('ptp', 			'PTP'),
					('other', 			'Otro'),
					
					# Dep
					('foreigner_card', 	'CE - Antiguo'),
]


_year_order_list = [
					('2020', 		'2020'),
					('2019', 		'2019'),
					('2018', 		'2018'),
					('2017', 		'2017'),
					('2016', 		'2016'),
]


_month_order_list = [
					('01', 		'ENE'),
					('02', 		'FEB'),
					('03', 		'MAR'),
					('04', 		'ABR'),
					('05', 		'MAY'),
					('06', 		'JUN'),
					('07', 		'JUL'),
					('08', 		'AGO'),
					('09', 		'SET'),
					('10', 		'OCT'),
					('11', 		'NOV'),
					('12', 		'DIC'),
]


_day_order_list = [

					('01', 		'01'),
					('02', 		'02'),
					('03', 		'03'),
					('04', 		'04'),
					('05', 		'05'),
					('06', 		'06'),
					('07', 		'07'),
					('08', 		'08'),
					('09', 		'09'),
					('10', 		'10'),

					('11', 		'11'),
					('12', 		'12'),
					('13', 		'13'),
					('14', 		'14'),
					('15', 		'15'),
					('16', 		'16'),
					('17', 		'17'),
					('18', 		'18'),
					('19', 		'19'),
					('20', 		'20'),

					('21', 		'21'),
					('22', 		'22'),
					('23', 		'23'),
					('24', 		'24'),
					('25', 		'25'),
					('26', 		'26'),
					('27', 		'27'),
					('28', 		'28'),
					('29', 		'29'),
					('30', 		'30'),

					('31', 		'31'),
]









# Order State
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




_dic_credit_note = {
					'cancel': 				'cancel',
					'cancel_error_ruc': 	'cancel_error',
					'correct_error_desc': 	'correction',
					
					'discount': 			'discount',
					'discount_item': 		'discount_item',
					
					'return': 				'return',
					'return_item': 			'return_item',

					'bonus': 				'bonus',
					'value_drop': 			'value_drop',
					'other': 				'other',
}


_weekday_list = [
					('monday', 			'Lunes'),
					('tuesday', 		'Martes'),
					('wednesday', 		'Miercoles'),
					('thursday', 		'Jueves'),
					('friday', 			'Viernes'),
					('saturday', 		'Sabado'),
					('sunday', 			'Domingo'),
]


_dic_weekday = {
					0: 	'monday',
					1: 	'tuesday',
					2: 	'wednesday',
					3: 	'thursday',
					4: 	'friday',
					5: 	'saturday',
					6: 	'sunday',
}








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
	Get Prefix
	"""
	return _dic_prefix[x_type]


def get_prefix_cn(x_type):
	"""
	Get Prefix Credit Note
	"""
	return _dic_prefix_cn[x_type]


def get_padding(x_type):
	"""
	Get Padding
	"""
	return _dic_padding[x_type]







#------------------------------------------------ Not Protected -----------------------------------

_credit_note_type_list = [
							('cancel', 					'01 - Anulación de la operación'),
							('cancel_error_ruc', 		'02 - Anulación por error en el RUC'),
							('correct_error_desc', 		'03 - Corrección por error en la descripción'),
							('discount', 				'04 - Descuento global'),
							('discount_item', 			'05 - Descuento por item'),
							('return', 					'06 - Devolución total'),
							('return_item', 			'07 - Devolución por item'),
							('bonus', 					'08 - Bonificación'),
							('value_drop', 				'09 - Disminución en el valor'),
							('other', 					'10 - Otros'),
]


_dic_type_code = {
					'ticket_invoice': 	'01',	
					'ticket_receipt': 	'03',
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


