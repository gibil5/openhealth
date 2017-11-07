# -*- coding: utf-8 -*-
#
# 	Sale proof 
# 
#

from openerp import models, fields, api


class SaleProof(models.Model):
	
	_name = 'openhealth.sale_proof'



	name = fields.Char(
			string="", 
			required=True, 

			)






	# Print
	@api.multi 
	def print_ticket(self):

		print 'jx'
		print 'Print Ticket'

		ret = 0 
		return ret 



	# Confirm
	@api.multi 
	def confirm(self):

		print 'jx'
		print 'Confirm'

		ret = 0 
		return ret 









	#family = fields.Char(
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







	ruc = fields.Char(
			string="RUC", 	
			#required=True, 
		)

	address = fields.Char(
			'Dirección', 
	)

	company = fields.Char(
			'Razón social', 
	)











	vspace = fields.Char(
			' ', 
			readonly=True
			)


	counter = fields.Many2one('openhealth.counter',
			#ondelete='cascade', 
			string="Counter",
			required=True, 

			compute="_compute_counter",
			)

	@api.multi
	#@api.depends('saledoc')

	def _compute_counter(self):
		for record in self:
			record.counter = self.env['openhealth.counter'].search([('name', 'like', record.family)])







	# Counter
	#counter = fields.Char(
	#		string="Counter", 
	#		default="0", 
	#		required=True, 
	#	)

	# Code
	#code = fields.Char(
	#		string="Code", 
	#		default="x", 
	#		required=True, 
	#	)





	# Date created 
	date_created = fields.Datetime(
			string="Fecha", 

			default = fields.Date.today,

			#readonly=True,
			required=True, 
			)













	# Open Order
	@api.multi 
	def open_order(self):
		#print 
		#print 'Open order'
		self.order.name = self.name 

		ret = self.order.open_myself()

		return ret 
	# open_order




	# Open Payment Method
	@api.multi 
	def open_pm(self):
		#print 
		#print 'Open Payment method'
		ret = self.payment_method.open_myself()
		return ret 
	# open_order







	payment_method = fields.Many2one('openhealth.payment_method',
			ondelete='cascade', 
			string="Payment method",

			#required=True, 
			required=False, 
			)

	#sale_document = fields.Many2one('openhealth.sale_document',
	#		ondelete='cascade', 
	#		string="Sale document",
	#		)

	order = fields.Many2one(
			'sale.order',

			string="Presupuesto",
			
			ondelete='cascade', 
			
			#required=True, 
			required=False, 
		)



	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 			
			required=True, 
		)

	total = fields.Float(
			string = 'Total', 
			required=True, 
		)












