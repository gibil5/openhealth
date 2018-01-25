# -*- coding: utf-8 -*-
#
# 	Sale proof 
# 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from openerp import models, fields, api
from num2words import num2words


class SaleProof(models.Model):
	
	_name = 'openhealth.sale_proof'





# ----------------------------------------------------------- Important ------------------------------------------------------



	# Prefix 
	#prefix = fields.Char(
	#		string="Prefijo", 
	#	)




	# Serial Number 
	serial_nr = fields.Char(
			string="Nr de Serie", 

			readonly=True, 
		)



	# Counter 
	counter = fields.Many2one(

			'openhealth.counter',
			
			string="Counter",

			#required=True, 
			required=False, 
			
			compute="_compute_counter",
		)


	@api.multi
	#@api.depends('saledoc')

	def _compute_counter(self):

		for record in self:
		
			record.counter = self.env['openhealth.counter'].search([('name', 'like', record.family)])










# ----------------------------------------------------------- Vars Primitives ------------------------------------------------------
	

	vspace = fields.Char(
			' ', 
			readonly=True
			)


	# Family 
	family = fields.Selection(
		
			[	
				('receipt', 		'Recibo'),
				('invoice', 		'Factura'),
				
				('ticket_receipt', 	'Ticket Recibo'),
				('ticket_invoice', 	'Ticket Factura'),

				('advertisement', 	'Canje Publicidad'),
				('sale_note', 		'Canje NV'),
			], 

		)












# ----------------------------------------------------------- Vars Required ------------------------------------------------------






	# Date created 
	date_created = fields.Datetime(
			string="Fecha", 

			default = fields.Date.today,

			#readonly=True,
			required=True, 
			)


	# Partner 
	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 			
			required=True, 
		)


	# Total 
	total = fields.Float(
			string = 'Total S/.', 
			required=True, 
		)


	# Name 
	name = fields.Char(
			string="", 

			required=True, 
		)





# ----------------------------------------------------------- Vars NOT Required ------------------------------------------------------


	payment_method = fields.Many2one('openhealth.payment_method',
			ondelete='cascade', 
			string="Payment method",

			#required=True, 
			required=False, 
			)


	order = fields.Many2one(
			'sale.order',
			"Presupuesto",
			ondelete='cascade', 
			
			#required=True, 
			required=False, 
		)



	ruc = fields.Char(
			string="RUC", 
				
			required=False, 
			#required=True, 
		)

	address = fields.Char(
			'Dirección', 
			required=False, 
	)

	company = fields.Char(
			'Razón social', 
			required=False, 
	)






# ----------------------------------------------------------- Actions ------------------------------------------------------


	# Open Order
	@api.multi 
	def open_order(self):
		#print 
		#print 'Open order'



		self.order.name = self.name 

		self.order.state = 'sale' 



		ret = self.order.open_myself()

		return ret 
	# open_order





	# Confirm
	@api.multi 
	def confirm(self):

		print 'jx'
		print 'Confirm'

		ret = 0 
		return ret 


