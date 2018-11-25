# -*- coding: utf-8 -*-
#
# 	payment method line
# 
# 	Created: 				2016
# 	Last mod: 				28 Aug 2018
#
from openerp import models, fields, api
import pm_vars
import account_funcs as acc_funcs
class payment_method_line(models.Model):	
	_name = 'openhealth.payment_method_line'
	_order = 'date_time asc'



# ----------------------------------------------------------- Init ------------------------------------------------------
	# Init 
	#def __init__(self, pool, cr): 
	#	print 
	#	print 'Init'
		#print self 
		#print pool
		#print cr 


# ----------------------------------------------------------- Important ------------------------------------------------------
	# Subtotal 
	subtotal = fields.Float(
			string = 'Subtotal', 
			#default=self.balance, 
			required=True, 
		)




# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Payment Method
	payment_method = fields.Many2one(
			'openhealth.payment_method',
			ondelete='cascade', 
			required=False, 			
		)

	# Account - Contabilidad  
	account_id = fields.Many2one(
			'openhealth.account.contasis',
			ondelete='cascade', 
		)


# ----------------------------------------------------------- Meta ------------------------------------------------------

	# Date 
	date_char = fields.Char(
			string="Fecha", 
		)

	# Time 
	time_char = fields.Char(
			string="Hora", 
		)



	# State 
	state = fields.Selection(
			selection = pm_vars._state_list, 
			string="Estado", 
		)



	# Document 
	document = fields.Char(
			string="Documento", 
		)

	document_type = fields.Char(
			string="Tipo Doc", 
		)



	# Other 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Nombre", 
		)

	serial_nr = fields.Char(
			string="Nr. de serie", 
		)

	x_type = fields.Selection(
			[	('receipt', 			'Boleta'),
				('invoice', 			'Factura'),
				('advertisement', 		'Canje Publicidad'),
				('sale_note', 			'Canje NV'),
				('ticket_receipt', 		'Ticket Boleta'),
				('ticket_invoice', 		'Ticket Factura'),	], 
			string='Tipo', 
		)

	date_time = fields.Datetime(
			#string="Fecha", 
			string="Fecha y Hora", 
		)


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name 
	name = fields.Char( 
			string="#", 
			required=True, 
		)

	# Method
	method = fields.Selection(
			selection = pm_vars._payment_method_list,
			string="Forma de Pago", 
			default="cash", 
			required=True, 
		)


	# Currency 
	currency = fields.Char(
			string="Moneda", 
			default="S/.", 
		)

	# Vspace 
	vspace = fields.Char(
			' ', 
			readonly=True
			)



# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  
		#print
		#print 'PM Line - Update'

		# Dates 
		date_time_corr, date_time_str = acc_funcs.correct_time(self,self.date_time, -5)

		self.date_char = date_time_str.split()[0]
		self.time_char = date_time_str.split()[1]

	# update_fields

