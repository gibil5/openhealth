

# 12 June 2017

		#if self.saledoc  == 'receipt':
		#	counter = self.env['openhealth.counter'].search([('name', 'like', 'receipt')])
		#	ctr = counter.value
		#	name = 'BO-1-' + str(ctr).rjust(4, '0')

		#if self.saledoc  == 'invoice':
		#	counter = self.env['openhealth.counter'].search([('name', 'like', 'invoice')])
		#	ctr = counter.value
		#	name = 'FA-1-' + str(ctr).rjust(4, '0')

		#if self.saledoc  == 'advertisement':
		#	pre = 'CA-'

		#if self.saledoc  == 'sale_note':
		#	pre = 'NV-'
			
		#if self.saledoc  == 'ticket_receipt':
		#	pre = 'TB-'
			
		#if self.saledoc  == 'ticket_invoice':
		#	pre = 'TF-'

		#if self.saledoc  == 'none':
		#	pre = 'NO-'



	# Consistency 

	#subtotal = fields.Float(
	#		string = 'Sub-total', 
	#		required=True, 
	#	)

	#method = fields.Selection(
	#		string="Medio", 
	#		selection = ord_vars._payment_method_list, 			
	#		required=True, 
	#	)





	#@api.multi
	@api.depends('saledoc')

	def _compute_saledoc_code(self):
		for record in self:

			receipt_ctr = '00001'

			pre = 'x'

			if record.saledoc  == 'receipt':
				pre = 'BO-'


			if record.saledoc  == 'invoice':
				pre = 'FA-'

			if record.saledoc  == 'advertisement':
				pre = 'CA-'

			if record.saledoc  == 'sale_note':
				pre = 'NV-'
			
			if record.saledoc  == 'ticket_receipt':
				pre = 'TB-'
			
			if record.saledoc  == 'ticket_invoice':
				pre = 'TF-'

			if record.saledoc  == 'none':
				pre = 'NO-'

			if pre != 'x':
				code = receipt_ctr
				record.saledoc_code = pre + code


			#counter = self.env['openhealth.counter'].search([('name', 'like', record.saledoc)])
			#ctr = counter.value
			#name = pre[record.saledoc] + str(ctr).rjust(4, '0')










	#_saledoc_list = [

	#			('receipt', 			'Boleta'),
	#			('invoice', 			'Factura'),
	#			('advertisement', 		'Canje Publicidad'),
	#			('sale_note', 			'Canje NV'),
	#			('ticket_receipt', 		'Ticket Boleta'),
	#			('ticket_invoice', 		'Ticket Factura'),
	#		]





	# Create Saledoc
	#@api.multi 
	#def create_saledoc(self):
	#	print 'Create Saledoc'
	#	ret = ''
	#	if self.saledoc == 'receipt':
	#		ret = self.create_receipt()
	#	elif self.saledoc == 'invoice':
	#		ret = self.create_invoice()
	#	return ret 







	# Create Receipt
	@api.multi 
	def create_receipt(self):
		print 
		print 'Create Receipt'

		# Search 
		receipt = self.env['openhealth.receipt'].search([
																('payment_method', '=', self.id),
															])

		# Create 
		if receipt.id == False:

			count = self.env['openhealth.receipt'].search_count([
																	('name','=', self.saledoc_code),
															])
			if count != 0: 
				receipt = self.env['openhealth.receipt'].create({
																'payment_method': self.id,
																'partner': self.partner.id,
																'total': self.total,
																'date_created': self.date_created,
																'order': self.order.id,

																'name': self.saledoc_code,
														})


		receipt_id = receipt.id 



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
							'default_payment_method': self.id,
							'default_total': self.total,
							'default_partner': self.partner.id,
							'default_date_created': self.date_created,
							'default_order': self.order.id,

							'default_name': self.saledoc_code,
							}
				}

	# create_receipt	
