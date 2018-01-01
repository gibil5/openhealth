


# 16 Jun 2017


# ----------------------------------------------------------- Button - Reseve Machine  ------------------------------------------------------

	@api.multi 
	def reserve_machine_old(self):

		#print 'jx'
		#print 'Reserve Machine - Old'

		#self.x_machine = 'laser_co2_1'


		
		# Create Machine
		appointment_date = 	self.x_appointment_date
		doctor_name = 		self.x_doctor.name
		doctor_id = 		self.x_doctor.id
		patient_id = 		self.patient.id
		treatment_id = 		self.treatment.id
		duration = 			self.x_duration


		x_machine_old = 	self.x_machine




		#start_machine = 	self.x_machine
		start_machine = 	self.x_machine_req





		# New 
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration)
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		x_machine = mac_funcs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		

		


		self.x_machine = x_machine 
		self.x_appointment.x_machine = x_machine





		# If Sucess create Machine Appointment
		if x_machine != False:


			# Create Appointment - Machine 
			app = self.env['oeh.medical.appointment'].create(
															{
																'appointment_date': appointment_date,

																'patient': 		patient_id,																	

																'x_type': 		'procedure',

																'duration': 	duration,
																																
																'x_create_procedure_automatic': False, 

																'x_machine': 	x_machine,



							                    				#'x_target': 	'machine',
							                    				'x_target': 	self.x_target,


																'doctor': 		doctor_id,

																'treatment': 	treatment_id, 
															}
															)



			if app != False:

				# Unlink Old 
				rec_set = self.env['oeh.medical.appointment'].search([
																			('appointment_date', 'like', appointment_date), 
																			('doctor', '=', doctor_name), 
																			('x_machine', '=', x_machine_old),

																			('patient', '=', self.patient.name), 
																	])
				ret = rec_set.unlink()
				#print "ret: ", ret




		else:
			#print 'Error !'	
			#print 			


			return {	'warning': 	{'title': "Error: Colisión !",
						'message': 	'La sala ya está reservada.',   
			#' + start + ' - ' + end + '.',
						}}

	# reserve_machine




# 29 Aug 2017


	@api.multi 
	def action_confirm_deprecated(self):

		#print 
		#print 'jx'
		#print 'Action confirm - Over ridden'
		 
		#Write your logic here


		# Validate 
		#if self.x_machine != False:

		#print 'x_doctor.name: ', self.x_doctor.name
		#print 'x_machine', self.x_machine
		#print 'x_state', self.x_state



		#if self.x_doctor.name != False   and   self.x_machine == False:
		#if self.x_doctor.name != False   and   self.x_machine == False	 and 	self.x_machine_req != 'consultation':

		if self.x_treatment == 'laser_co2'   and   self.x_machine == False:
			#print 'Warning: Sala no Reservada !'
			tra = 1 
		else:
			#print 'Success !!!'

			#self.x_state = 'sale'
			#self.x_confirmed = True 


			#if self.x_family == 'consultation': 
			if self.x_family == 'consultation'	or 	self.x_family == 'procedure': 
				self.x_appointment.state = 'Scheduled'

				#self.state = 'confirmed'


			# State is changed here ! 
			res = super(sale_order, self).action_confirm()
			
			#self.state = 'confirmed'

		#else: 
			
		#res = super(sale_order, self).action_confirm()
		#Write your logic here
		
		#print
	# action_confirm
	






# Ooor

	#name = fields.Char(
	#		string="Presupuesto #"
	#	)

	# Test 
	#test = fields.Char(
	#	)

	# Type
	#x_type = fields.Selection(
	#		selection = ord_vars._owner_type_list, 
	#		string='Tipo', 
	#	)










# User by Doctor 
	# Doctor 
	#_dic_docuser = {
	#					'Dr. Medico': 		'Medico', 
	#					'Dr. Chavarri': 	'Fernando Chavarri', 
	#					'Dr. Canales': 		'Paul Canales', 
	#					'Dr. Escudero':		'Carlos Escudero', 
	#					'Dr. Gonzales':		'Leo Gonzales', 
	#					'Dr. Vasquez':		'Javier Vasquez', 
	#					'Dr. Alarcon': 		'Guillermo Alarcon', 
	#					'Dr. Monteverde':	'Piero Monteverde', 
	#					'Dr. Mendez':		'Carlos Mendez', 
	#					'Dra. Acosta':		' Desiree Acosta', 
	#					'Dra. Pedemonte':	'Maria Luisa Pedemonte', 
	#					'Eulalia':			'Eulalia Ruiz', 
	#				}
	
	#@api.onchange('x_doctor')	
	#def _onchange_x_doctor(self):
	#	user_name = self._dic_docuser[self.x_doctor.name]
	#	self.user_id = self.env['res.users'].search([('name', '=', user_name)]).id 


	#user_id = fields.Many2one('res.users', string='Salesperson', index=True, track_visibility='onchange', default=lambda self: self.env.user)

	#@api.multi
	#@api.depends('x_doctor')
	#def _compute_user_id(self):
	#	for record in self:
	#		if record.x_doctor.name != False:
	#			user_name = record._dic_docuser[record.x_doctor.name]
	#			record.user_id = record.env['res.users'].search([('name', '=', user_name)]).id 










# 6 Oct 2017


	#partner_invoice_id = fields.Many2one('res.partner', string='Invoice Address', readonly=True, 
	#	required=True, 
		#required=False, 
	#	states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Invoice address for current sales order.")

	#partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address', readonly=True, 
	#	required=True, 
		#required=False, 
	#	states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Delivery address for current sales order.")





	# Pricelist
	#@api.multi 
	#def _get_default_pl(self):
	#	pl = self.env['product.pricelist'].search([('name', '=', 'Public Pricelist')]).id 
	#	pl = 1 
	#	return pl

	#pricelist_id = fields.Many2one(
	#	'product.pricelist', 
	#	default=lambda self: self._get_default_pl(),
	#	string='Pricelist', required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Pricelist for current sales order.")


	#pricelist_id = fields.Many2one('product.pricelist', string='Pricelist', required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Pricelist for current sales order.")




	# For Debugging purposes 
	@api.multi
	@api.onchange('partner_id')
	def onchange_partner_id(self):
		print 'jx'
		print 'onchange_partner_id'
		print self.partner_id
		print 

		"""
		Update the following fields when the partner is changed:
		- Pricelist
		- Payment term
		- Invoice address
		- Delivery address
		"""
		if not self.partner_id:

			print 'jx 2'

			self.update({
				'partner_invoice_id': False,
				'partner_shipping_id': False,
				'payment_term_id': False,
				'fiscal_position_id': False,
			})
			return



		addr = self.partner_id.address_get(['delivery', 'invoice'])


		print 'jx 3'
		print addr 
		print 'jx 4'
		print self.partner_id.property_payment_term_id
		print 'jx 5'
		print self.partner_id.property_product_pricelist.id
		print 'jx 6'
		print self.partner_id.property_product_pricelist
		print 'jx 7'


		values = {
			'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
			'payment_term_id': self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
			'partner_invoice_id': addr['invoice'],
			'partner_shipping_id': addr['delivery'],
		}

		print 'jx 10'

		if self.env.user.company_id.sale_note:
			values['note'] = self.with_context(lang=self.partner_id.lang).env.user.company_id.sale_note

		if self.partner_id.user_id:
			values['user_id'] = self.partner_id.user_id.id
		if self.partner_id.team_id:
			values['team_id'] = self.partner_id.team_id.id
		self.update(values)



# 20 Nov 2017

			#name = record.name
			#pre = name.split('-')[0]

			#if pre == 'BO' or  pre == 'BOL':
			#	record.x_type = 'receipt'

			#elif pre == 'FA':
			#	record.x_type = 'invoice'

			#elif pre == 'CP':
			#	record.x_type = 'advertisement'

			#elif pre == 'CN':
			#	record.x_type = 'sale_note'
			
			#elif pre == 'TKB':
			#	record.x_type = 'ticket_receipt'
			
			#elif pre == 'TKF':
			#	record.x_type = 'ticket_invoice'

			#else:
			#	print 'jx'
			#	print 'This should not happen'
			#	print pre 
			#	print 





	#order_day = fields.Char(	
	#		'Day', 
	#		default = lambda *a: str(date_order.strftime('%d')),
	#	)








#'task_date_from':fields.function(lambda *a,**k:{}, method=True, type='date',string="Task date from"),
#'task_date_to':fields.function(lambda *a,**k:{}, method=True, type='date',string="Task date to"),

	#task_date_from = fields.Date(
	#	default = lambda *a,#**k:{}, 
		#method=True, 
		#type='date', 
	#	string="Task date from", 
	#)

	#task_date_to = fields.Date(
	#	default=lambda *a,#**k:{}, 
		#method=True, 
	#	string="Task date to"
	#)





# 31 Dec 

	@api.depends('order_line.price_total')
	def _amount_all(self):
		"""
		Compute the total amounts of the SO.
		"""
		for order in self:
			amount_untaxed = amount_tax = 0.0
			for line in order.order_line:


				#amount_untaxed += line.price_subtotal
				amount_untaxed += 5
				#amount_untaxed += line.x_price_subtotal
				

				# FORWARDPORT UP TO 10.0
				if order.company_id.tax_calculation_rounding_method == 'round_globally':
					price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
					taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
					amount_tax += sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
				else:
					amount_tax += line.price_tax
			order.update({
				'amount_untaxed': order.pricelist_id.currency_id.round(amount_untaxed),
				'amount_tax': order.pricelist_id.currency_id.round(amount_tax),
				'amount_total': amount_untaxed + amount_tax,
			})









