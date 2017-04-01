# -*- coding: utf-8 -*-
#
# 	Sale document 
# 
#

from openerp import models, fields, api


class SaleDocument(models.Model):
	
	_name = 'openhealth.sale_document'

	#_inherit='sale.order'




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







	receipt = fields.Many2one(
			'openhealth.receipt',
			string = "Boleta", 			
			#required=True, 
		)


	invoice = fields.Many2one(
			'openhealth.invoice',
			string = "Factura", 			
			#required=True, 
		)


	advertisement = fields.Many2one(
			'openhealth.advertisement',
			string = "Canje publicidad", 			
			#required=True, 
		)


	sale_note = fields.Many2one(
			'openhealth.sale_note',
			string = "Nota de venta", 			
			#required=True, 
		)


	ticket_receipt = fields.Many2one(
			'openhealth.ticket_receipt',
			string = "Ticket Boleta", 			
			#required=True, 
		)


	ticket_invoice = fields.Many2one(
			'openhealth.ticket_invoice',
			string = "Ticket Factura", 			
			#required=True, 
		)







# ---------------------------------------------- Create Receipt --------------------------------------------------------
	@api.multi 
	def create_receipt(self):
		print 
		print 'Create Receipt'


		# Search 
		receipt_id = self.env['openhealth.receipt'].search([('order','=',self.order.id),]).id



		# Create 
		if receipt_id == False:

			receipt = self.env['openhealth.receipt'].create({
																'order': self.order.id,

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
							'default_order': self.order.id,

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
		invoice_id = self.env['openhealth.invoice'].search([('order','=',self.order.id),]).id

		# Create 
		if invoice_id == False:

			invoice = self.env['openhealth.invoice'].create({
																'order': self.order.id,

																'total': self.total, 
																
																'ruc': self.ruc,	

																'partner': self.partner.id,	
													})
			invoice_id = invoice.id 



		self.x_invoice = invoice_id


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
							'default_order': self.order.id,
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
		advertisement_id = self.env['openhealth.advertisement'].search([('order','=',self.order.id),]).id

		# Create 
		if advertisement_id == False:

			advertisement = self.env['openhealth.advertisement'].create({
																'order': self.order.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			advertisement_id = advertisement.id 


		self.x_advertisement = advertisement_id


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
							'default_order': self.order.id,

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
		sale_note_id = self.env['openhealth.sale_note'].search([('order','=',self.order.id),]).id

		# Create 
		if sale_note_id == False:

			sale_note = self.env['openhealth.sale_note'].create({
																'order': self.order.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			sale_note_id = sale_note.id 



		self.x_sale_note = sale_note_id


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
							'default_order': self.order.id,

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
		ticket_receipt_id = self.env['openhealth.ticket_receipt'].search([('order','=',self.order.id),]).id

		# Create 
		if ticket_receipt_id == False:

			ticket_receipt = self.env['openhealth.ticket_receipt'].create({
																'order': self.order.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			ticket_receipt_id = ticket_receipt.id 



		self.x_ticket_receipt = ticket_receipt_id


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
							'default_order': self.order.id,
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
		ticket_invoice_id = self.env['openhealth.ticket_invoice'].search([('order','=',self.order.id),]).id

		# Create 
		if ticket_invoice_id == False:

			ticket_invoice = self.env['openhealth.ticket_invoice'].create({
																'order': self.order.id,

																'total': self.total, 

																'partner': self.partner.id,	
													})
			ticket_invoice_id = ticket_invoice.id 



		self.x_ticket_invoice = ticket_invoice_id


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
							'default_order': self.order.id,

							'default_total': self.total,

							'default_partner': self.partner.id,
							}
				}

	# create_ticket_invoice






