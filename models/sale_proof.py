# -*- coding: utf-8 -*-
#
# 	Sale proof 
# 
#


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from openerp import models, fields, api

from num2words import num2words



class SaleProof(models.Model):
	
	_name = 'openhealth.sale_proof'



	name = fields.Char(
			string="", 
			required=True, 

			)




# Other 

	serial_nr = fields.Char(
		)

	authorization = fields.Char(
		)






# My Company


	# Firm
	my_firm = fields.Char(
			"Razon social",

			compute='_compute_my_firm', 
		)

	@api.multi
	#@api.depends('')
	def _compute_my_firm(self):
		for record in self:
			record.my_firm = record.order.x_my_company.x_firm




	# Ruc
	my_ruc = fields.Char(

			"Ruc",
			compute='_compute_my_ruc', 
		)

	@api.multi
	#@api.depends('')
	def _compute_my_ruc(self):
		for record in self:
			record.my_ruc = record.order.x_my_company.x_ruc




	# Phone 
	my_phone = fields.Char(

			"Teléfono",
			compute='_compute_my_phone', 
		)

	@api.multi
	#@api.depends('')
	def _compute_my_phone(self):
		for record in self:
			record.my_phone = record.order.x_my_company.phone





	# Address
	my_address = fields.Char(

			"Dirección",
			compute='_compute_my_address', 
		)

	@api.multi
	#@api.depends('')
	def _compute_my_address(self):
		for record in self:

			com = record.order.x_my_company

			record.my_address = com.street + ' - ' + com.street2 + ' - ' + com.city






# Customer 




	# Name
	par_name = fields.Char(

			"Nombre",
			compute='_compute_par_name', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_name(self):
		for record in self:

			par = record.order.partner_id

			record.par_name = par.name







	# DNI
	par_dni = fields.Char(

			"DNI",
			compute='_compute_par_dni', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_dni(self):
		for record in self:
			record.par_dni = record.order.partner_id.x_dni





	# Address
	par_address = fields.Char(

			"Dirección",
			compute='_compute_par_address', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_address(self):
		for record in self:

			par = record.order.partner_id

			record.par_address = par.street + ' - ' + par.street2 + ' - ' + par.city





	# Ruc
	par_ruc = fields.Char(

			"Ruc",
			compute='_compute_par_ruc', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_ruc(self):
		for record in self:

			par = record.order.partner_id

			record.par_ruc = par.x_ruc





	# Firm
	par_firm = fields.Char(
			"Razon social",

			compute='_compute_par_firm', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_firm(self):
		for record in self:

			par = record.order.partner_id

			record.par_firm = par.x_firm













# Sale

	# Order lines 
	order_line = field_One2many=fields.One2many(

			'sale.order.line',
			'order_id',
			'Order line',

			compute='_compute_order_line', 			
	)

	@api.multi
	#@api.depends('')
	def _compute_order_line(self):
		for record in self:
			record.order_line = record.order.order_line





	# Order lines text 
	order_line_txt = field_One2many=fields.Text(

			'Order Lines Text',

			#default = '', 
			compute='_compute_order_line_txt', 			
	)

	@api.multi
	#@api.depends('')
	def _compute_order_line_txt(self):
		for record in self:

			print 'jx'
			print 'Compute order line txt'

			txt = 'Descripción\tCNT\tP. UNIT.\tSubtotal\n'

			for line in record.order_line: 
				print line
				print line.name 

				#txt = txt + line.name + '\t' + line.product_uom_qty + '\t' + line.price_unit + '\t' + line.price_subtotal + '\n'
				txt = txt + line.name + '\t' + str(line.product_uom_qty) + '\t' + str(line.price_unit) + '\t' + str(line.price_subtotal) + '\n'

				#txt = txt + line.name + '\n'
				#txt = txt + line.name 
				#txt = txt + line.name + '\n'


			record.order_line_txt = txt





	cr = fields.Char(
			default='-------------------------------------------------------', 
		)






	# Ruc
	total_in_words = fields.Char(

			"",
			compute='_compute_total_in_words', 
		)

	@api.multi
	#@api.depends('')
	def _compute_total_in_words(self):
		for record in self:

			#words = record.total
			words = num2words(record.total, lang='es')

			record.total_in_words = words.title() + ' Soles'









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
			string = 'Total S/.', 
			required=True, 
		)












