# -*- coding: utf-8 -*-
#
# 	Account Line
# 
# Created: 				18 April 2018
#
#

from openerp import models, fields, api

import datetime

#import resap_funcs



class AccountLine(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.account.line'
	
	#_order = 'serial_nr asc'
	_order = 'date_time asc'



# ----------------------------------------------------------- Relational ------------------------------------------------------

	account_id = fields.Many2one(

			'openhealth.account.contasis'

		)





# ----------------------------------------------------------- Primitives ------------------------------------------------------

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
			
			#required=False,
		)

	document = fields.Char(
			string="Documento", 
		)



	date = fields.Date(
		)

	date_time = fields.Datetime(
			string="Fecha", 
		)



	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Nombre", 
		)




	amount = fields.Float(
			string="Total", 
		)

	amount_net = fields.Float(
			string="Neto", 
		)

	amount_tax = fields.Float(
			string="Impuesto", 
		)




