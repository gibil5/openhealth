



# 5 April 2018

		# Generate Saledoc Code - Deprecated !!!
		#pre = {
		#		'receipt':	'BO-1-', 
		#		'invoice':	'FA-1-', 
		#		'advertisement':	'CP-1-', 
		#		'sale_note':		'CN-1-', 
		#		'ticket_receipt':	'TKB-1-', 
		#		'ticket_invoice':	'TKF-1-', 
		#}


		#counter = self.env['openhealth.counter'].search([('name', '=', self.saledoc)])

		#out = False 

		#while not out:

		#	ctr = counter.value
		#	name = pre[self.saledoc] + str(ctr).rjust(4, '0')
		#	model = ord_vars._dic_model[self.saledoc]
		#	count = self.env[model].search_count([
		#											('name','=', name),
		#									]) 
		#	if count == 0:
		#		out = True
		#	else:
		#		counter.increase()

		#self.saledoc_code = name















	# Receipt
	receipt = fields.Many2one(
			'openhealth.receipt',
			string = "Boleta", 			
			#ondelete='cascade', 

			compute="_compute_receipt",
		)

	@api.multi
	#@api.depends('saledoc')

	def _compute_receipt(self):
		for record in self:
			record.receipt = record.env['openhealth.receipt'].search([('payment_method', '=', record.id),])

	




	# Invoice
	invoice = fields.Many2one(
			'openhealth.invoice',
			string = "Factura", 			
			#ondelete='cascade', 

			compute="_compute_invoice",
		)

	@api.multi
	#@api.depends('saledoc')

	def _compute_invoice(self):
		for record in self:
			record.invoice = record.env['openhealth.invoice'].search([('payment_method', '=', record.id),])






	# Ticket Receipt
	ticket_receipt = fields.Many2one(
			'openhealth.ticket_receipt',
			string = "Ticket Boleta", 			
			#ondelete='cascade', 

			compute="_compute_ticket_receipt",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_ticket_receipt(self):
		for record in self:
			record.ticket_receipt = record.env['openhealth.ticket_receipt'].search([('payment_method', '=', record.id),])





	# Ticket Invoice
	ticket_invoice = fields.Many2one(
			'openhealth.ticket_invoice',
			string = "Ticket Factura", 			
			#ondelete='cascade', 

			compute="_compute_ticket_invoice",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_ticket_invoice(self):
		for record in self:
			record.ticket_invoice = record.env['openhealth.ticket_invoice'].search([('payment_method', '=', record.id),])







	# Advertisement
	advertisement = fields.Many2one(
			'openhealth.advertisement',
			string = "Canje publicidad", 			
			#ondelete='cascade', 

			compute="_compute_advertisement",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_advertisement(self):
		for record in self:
			record.advertisement = record.env['openhealth.advertisement'].search([('payment_method', '=', record.id),])







	# Sale note 
	sale_note = fields.Many2one(
			'openhealth.sale_note',
			string = "Nota de venta", 			
			#ondelete='cascade', 

			compute="_compute_sale_note",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_sale_note(self):
		for record in self:
			record.sale_note = record.env['openhealth.sale_note'].search([('payment_method', '=', record.id),])








	# Order name 
	@api.multi 
	def order_name(self):
		#print
		#print 'jx'
		
		#print self.invoice.name 
		#print self.receipt.name 
		#print self.advertisement.name 
		#print self.ticket_invoice.name 
		#print self.ticket_receipt.name


		if self.invoice.name != False:
			self.order.name = self.invoice.name

		if self.receipt.name != False:
			self.order.name = self.receipt.name
	
		if self.advertisement.name != False:
			self.order.name = self.advertisement.name

		if self.sale_note.name != False:
			self.order.name = self.sale_note.name

		if self.ticket_invoice.name != False:
			self.order.name = self.ticket_invoice.name

		if self.ticket_receipt.name != False:
			self.order.name = self.ticket_receipt.name

		#print self.order.name 
		#print 










	# Saledoc Code 
	saledoc_code = fields.Char(
			string="No", 
			readonly=False, 
			#compute="_compute_saledoc_code",

			#states=READONLY_STATES, 
		)








	# Create Sale Proof
	@api.multi 
	def create_saleproof(self):

		print 'jx'
		print 'Create Sale Proof'


		# Search in the Model dic
		model = ord_vars._dic_model[self.saledoc]
		print model 



		#serial_nr = 'x'



		# The model is valid 
		if model != False: 


			# Search it exists 
			proof = self.env[model].search([
												('payment_method', '=', self.id),
											])

			# Create 
			if proof.id == False:
				print 'create'


				count = self.env[model].search_count([('name','=', self.saledoc_code),])
				print count
				print 

				#if count != 0: 
				if count == 0: 

					print 'GO CREATE'
	
					proof = self.env[model].create({
														'name': self.saledoc_code,

														'payment_method': self.id,

														'order': self.order.id,
														
														'partner': self.partner.id,
																
														'total': self.total,
														
														'date_created': self.date_created,



														#'serial_nr': serial_nr,
												})


			proof_id = proof.id 
			print 
			print proof
			print 
			print self.saledoc_code
			print self.id
			print self.order
			print self.partner
			print self.total
			print self.date_created
			print






			# Sale doc code 
			if self.saledoc == 'ticket_receipt': 
				self.saledoc_code = self.ticket_receipt.serial_nr

			elif self.saledoc == 'ticket_invoice': 
				self.saledoc_code = self.ticket_invoice.serial_nr



			elif self.saledoc == 'invoice': 
				self.saledoc_code = self.invoice.serial_nr

			elif self.saledoc == 'receipt': 
				self.saledoc_code = self.receipt.serial_nr




			elif self.saledoc == 'advertisement': 
				self.saledoc_code = self.advertisement.serial_nr

			elif self.saledoc == 'sale_note': 
				self.saledoc_code = self.sale_note.serial_nr







			# Action confirm ?



			# Open Order 
			self.confirmed = True 
			ret = self.order.open_myself()




			#return {}
			return ret 

	# create_saleproof







	def _compute_state(self):


			#if	record.env['openhealth.receipt'].search_count([('payment_method','=', record.id),])			or \
			#	record.env['openhealth.invoice'].search_count([('payment_method','=', record.id),])			or \
			#	record.env['openhealth.advertisement'].search_count([('payment_method','=', record.id),])	or \
			#	record.env['openhealth.sale_note'].search_count([('payment_method','=', record.id),])		or \
			#	record.env['openhealth.ticket_receipt'].search_count([('payment_method','=', record.id),])	or \
			#	record.env['openhealth.ticket_invoice'].search_count([('payment_method','=', record.id),]):
				
			#	record.state = 'generated'









	# On change - Balance
	#@api.onchange('balance')
	
	#def _onchange_balance(self):
		
		#print 'Onchange Balance'

		#if self.balance == 0.0:
	#	if self.total == self.pm_total:
			#print 'Gotcha'
	#		self.state = 'done'
			#print self.state  


	# Open Order
	#@api.multi 
	#def open_order(self):
	#	self.confirmed = True 
	#	ret = self.order.open_myself()
	#	return ret 
	# open_order







	# Create 
	@api.model
	def create(self,vals):


		#order = vals['order']
		#nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', order),]) 
		#name = 'MP-' + str(nr_pm + 1)
		#vals['name'] = name




		#total = vals['total']






	# Open Myself
	@api.multi 
	def open_myself(self):
		payment_method_id = self.id  

		return {
				# Mandatory 
				'type': 'ir.actions.act_window',
				'name': 'Open payment method Current',

				# Window action 
				'res_model': 'openhealth.payment_method',
				'res_id': payment_method_id,

				# Views 
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',

				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False, 

				'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
				},			

				'context':   {}
			}
	# open_myself








	# Total Paid
	#pm_total = fields.Float(
	#		string = 'Total pagado', 
	#		required=True, 
	#		default=0, 

	#		compute="_compute_pm_total",
	#	)

	#@api.multi
	#@api.depends('total', 'pm_total')
	#def _compute_pm_total(self):
	#	for record in self:

	#		pm_total = 0

	#		for line in record.pm_line_ids:
	#			s = line.subtotal
	#			pm_total = pm_total + s

	#		record.pm_total = record.pm_total + pm_total





# 14 Jun 2018 

		# Generate Name
		#pre = {
		#		'receipt':	'BO-1-', 
		#		'invoice':	'FA-1-', 
		#		'advertisement':	'CP-1-', 
		#		'sale_note':		'CN-1-', 
		#		'ticket_receipt':	'TKB-1-', 
		#		'ticket_invoice':	'TKF-1-', 
		#}
		#counter = self.env['openhealth.counter'].search([('name', '=', self.saledoc)])
		#name = pre[self.saledoc] + str(counter.value).rjust(4, '0')
		#self.saledoc_code = name
