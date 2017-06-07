# -*- coding: utf-8 -*-
#
# 	Sale document 
# 
#

from openerp import models, fields, api

import ord_vars



class SaleDocument(models.Model):
	
	_name = 'openhealth.sale_document'

	#_inherit='sale.order'



	code = fields.Char(
			string='Código',

			compute='_compute_code', 
		)

	#@api.depends()
	@api.multi

	def _compute_code(self):
		for record in self:

			if record.receipt != False :
				record.code = record.receipt.name

			elif record.invoice != False:
				record.code = record.invoice.name

			elif record.advertisement != False:
				record.code = record.advertisement.name

			elif record.sale_note != False:
				record.code = record.sale_note.name

			elif record.ticket_receipt != False:
				record.code = record.ticket_receipt.name

			elif record.ticket_invoice != False:
				record.code = record.ticket_invoice.name





	# Type 
	x_type = fields.Selection(

			selection = ord_vars._sale_doc_type_list, 

			string='Tipo',

			compute='_compute_x_type', 
		)


	#@api.depends()
	@api.multi

	def _compute_x_type(self):

		print 
		print 'Compute x type'



		for record in self:


			print record.name
			print record.receipt.name
			print record.ticket_receipt.name

			print 

			if record.receipt.name != False :
				record.x_type = 'receipt'

			elif record.invoice.name != False:
				record.x_type = 'invoice'

			elif record.advertisement.name != False:
				record.x_type = 'advertisement'

			elif record.sale_note.name != False:
				record.x_type = 'sale_note'

			elif record.ticket_receipt.name != False:
				record.x_type = 'ticket_receipt'

			elif record.ticket_invoice.name != False:
				record.x_type = 'ticket_invoice'









	name = fields.Char(
			string="Comprobante #", 
			required=True, 
			compute='_compute_name', 
		)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'CP-' + str(record.id) 



	vspace = fields.Char(
			' ', 
			readonly=True
			)

	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 			
			required=True, 
		)

	total = fields.Float(
			string = 'Total', 
		)

	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			required=True, 
		)

	ruc = fields.Char(
			string="RUC", 	
			#required=True, 
		)










	#consultation_ids = fields.One2many(
	#		'openhealth.consultation', 
	#		'treatment', 

	#		string = "Consultas", 
	#		)





	#receipt = fields.One2many(
	receipt = fields.Many2one(
			'openhealth.receipt',
			#'sale_document', 

			string = "Boleta", 			

			#ondelete='cascade', 
		)





	#invoice = fields.One2many(
	invoice = fields.Many2one(
			'openhealth.invoice',
			#'sale_document', 

			string = "Factura", 			

			#ondelete='cascade', 
		)


	#advertisement = fields.One2many(
	advertisement = fields.Many2one(
			'openhealth.advertisement',
			#'sale_document', 

			string = "Canje publicidad", 			

			#ondelete='cascade', 
		)


	#sale_note = fields.One2many(
	sale_note = fields.Many2one(
			'openhealth.sale_note',
			#'sale_document', 

			string = "Nota de venta", 			

			#ondelete='cascade', 
		)


	#ticket_receipt = fields.One2many(
	ticket_receipt = fields.Many2one(
			'openhealth.ticket_receipt',
			#'sale_document', 

			string = "Ticket Boleta", 			

			#ondelete='cascade', 
		)


	#ticket_invoice = fields.One2many(
	ticket_invoice = fields.Many2one(
			'openhealth.ticket_invoice',
			#'sale_document', 

			string = "Ticket Factura", 			

			#ondelete='cascade', 
		)












	# Number of receipts 
	nr_receipts = fields.Integer(
			compute="_compute_nr_receipts",
	)
	@api.multi
	def _compute_nr_receipts(self):
		for record in self:
			record.nr_receipts=self.env['openhealth.receipt'].search_count([

																				('sale_document','=', record.id),
				
																		]) 

	# Number of invoices 
	nr_invoices = fields.Integer(
			compute="_compute_nr_invoices",
	)
	@api.multi
	def _compute_nr_invoices(self):
		for record in self:
			record.nr_invoices=self.env['openhealth.invoice'].search_count([

																				('sale_document','=', record.id),
				


																		]) 


	# Number of advertisements 
	nr_advertisements = fields.Integer(
			compute="_compute_nr_advertisements",
	)
	@api.multi
	def _compute_nr_advertisements(self):
		for record in self:
			record.nr_advertisements=self.env['openhealth.advertisement'].search_count([

																				('sale_document','=', record.id),
				
																		]) 

	# Number of sale_notes 
	nr_sale_notes = fields.Integer(
			compute="_compute_nr_sale_notes",
	)
	@api.multi
	def _compute_nr_sale_notes(self):
		for record in self:
			record.nr_sale_notes=self.env['openhealth.sale_note'].search_count([

																				('sale_document','=', record.id),
				
																		]) 



	# Number of ticket_invoices 
	nr_ticket_invoices = fields.Integer(
			compute="_compute_nr_ticket_invoices",
	)
	@api.multi
	def _compute_nr_ticket_invoices(self):
		for record in self:
			record.nr_ticket_invoices=self.env['openhealth.ticket_invoice'].search_count([

																				('sale_document','=', record.id),
				
																		]) 

	# Number of ticket_receipts 
	nr_ticket_receipts = fields.Integer(
			compute="_compute_nr_ticket_receipts",
	)
	@api.multi
	def _compute_nr_ticket_receipts(self):
		for record in self:
			record.nr_ticket_receipts=self.env['openhealth.ticket_receipt'].search_count([

																				('sale_document','=', record.id),
				
																		]) 





	nr_proofs = fields.Integer(
			string='Nr Proofs',	
			default=0, 
			compute="_compute_nr_proofs",
	)


	@api.multi
	#@api.depends('state')

	def _compute_nr_proofs(self):
		for record in self:

			record.nr_proofs = 	record.nr_receipts + record.nr_invoices + record.nr_advertisements + \
								record.nr_sale_notes + record.nr_ticket_receipts + record.nr_ticket_invoices




# ---------------------------------------------- Create Receipt --------------------------------------------------------
	@api.multi 
	def create_receipt(self):
		print 
		print 'Create Receipt'

		# Search 
		receipt_id = self.env['openhealth.receipt'].search([
																#('order','=',self.order.id),
																('sale_document','=',self.id),
															]).id

		# Create 
		if receipt_id == False:

			receipt = self.env['openhealth.receipt'].create({
																'sale_document': self.id,
																#'order': self.order.id,
																'total': self.total, 
																'partner': self.partner.id,				
													})
			receipt_id = receipt.id 


		self.receipt = receipt_id

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Receipt Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',

				'res_model': 'openhealth.receipt',				
				'res_id': receipt_id,

				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_sale_document': self.id,
							#'default_order': self.order.id,
							'default_total': self.total,
							'default_partner': self.partner.id,
							}
				}

	# create_receipt





# ---------------------------------------------- Create Invoice --------------------------------------------------------
	@api.multi 
	def create_invoice(self):
		print 
		print 'Create Invoice'


		# Search 
		invoice_id = self.env['openhealth.invoice'].search([
																#('order','=',self.order.id),
																('sale_document','=',self.id),

																]).id

		# Create 
		if invoice_id == False:

			invoice = self.env['openhealth.invoice'].create({
																'sale_document': self.id,

																'total': self.total, 
																
																'ruc': self.ruc,	

																'partner': self.partner.id,	
													})
			invoice_id = invoice.id 



		self.invoice = invoice_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New invoice Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.invoice',				
				'res_id': invoice_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_sale_document': self.id,

							'default_total': self.total,
							'default_ruc': self.ruc,
							'default_partner': self.partner.id,
							}
				}

	# create_invoice





# ---------------------------------------------- Create advertisement --------------------------------------------------------
	@api.multi 
	def create_advertisement(self):
		print 
		print 'Create advertisement'


		# Search 
		advertisement_id = self.env['openhealth.advertisement'].search([	
																			#('order','=',self.order.id),
																			('sale_document','=',self.id),
																		]).id

		# Create 
		if advertisement_id == False:

			advertisement = self.env['openhealth.advertisement'].create({
																'sale_document': self.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			advertisement_id = advertisement.id 


		self.advertisement = advertisement_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New advertisement Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.advertisement',				
				'res_id': advertisement_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_sale_document': self.id,

							'default_total': self.total,
							'default_partner': self.partner.id,
							}
				}

	# create_advertisement






# ---------------------------------------------- Create Sale Note --------------------------------------------------------
	@api.multi 
	def create_sale_note(self):
		print 
		print 'Create Sale Note'



		# Search 
		sale_note_id = self.env['openhealth.sale_note'].search([
																	#('order','=',self.order.id),
																	('sale_document','=',self.id),

																	]).id

		# Create 
		if sale_note_id == False:

			sale_note = self.env['openhealth.sale_note'].create({
																'sale_document': self.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			sale_note_id = sale_note.id 



		self.sale_note = sale_note_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New sale_note Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.sale_note',				
				'res_id': sale_note_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_sale_document': self.id,

							'default_total': self.total,
							'default_partner': self.partner.id,
							}
				}

	# create_sale_note









# ---------------------------------------------- Create Ticket Receipt  --------------------------------------------------------
	@api.multi 
	def create_ticket_receipt(self):
		print 
		print 'Create Ticekt Receipt'

		# Search 
		ticket_receipt_id = self.env['openhealth.ticket_receipt'].search([
																			#('order','=',self.order.id),
																			('sale_document','=',self.id),
																			]).id

		# Create 
		if ticket_receipt_id == False:

			ticket_receipt = self.env['openhealth.ticket_receipt'].create({
																'sale_document': self.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			ticket_receipt_id = ticket_receipt.id 



		self.ticket_receipt = ticket_receipt_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New ticket_receipt Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.ticket_receipt',				
				'res_id': ticket_receipt_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_sale_document': self.id,

							'default_total': self.total,
							'default_partner': self.partner.id,
							}
				}

	# create_ticket_receipt








# ---------------------------------------------- Create Ticket Invoice --------------------------------------------------------
	@api.multi 
	def create_ticket_invoice(self):
		print 
		print 'Create Ticket Invoice'


		# Search 
		ticket_invoice_id = self.env['openhealth.ticket_invoice'].search([
																			#('order','=',self.order.id),
																			('sale_document','=',self.id),
																		]).id

		# Create 
		if ticket_invoice_id == False:

			ticket_invoice = self.env['openhealth.ticket_invoice'].create({
																'sale_document': self.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			ticket_invoice_id = ticket_invoice.id 



		self.ticket_invoice = ticket_invoice_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New ticket_invoice Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.ticket_invoice',				
				'res_id': ticket_invoice_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_sale_document': self.id,

							'default_total': self.total,
							'default_partner': self.partner.id,
							}
				}

	# create_ticket_invoice



