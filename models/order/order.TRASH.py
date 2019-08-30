# 29 Aug 2019 - Update Counter
# Deprecated ?


# ---------------------------------------------- Update Counter -----------------------------------
	# Update Counter
	@api.multi
	def update_counter(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Counter')
		#print(self.x_counter_value)
		#print(self.x_serial_nr)

		counter_value = self.x_counter_value		
		state = self.state
		serial_nr = user.get_serial_nr(self.x_type, counter_value, state)

		#print(serial_nr)

		if self.x_serial_nr != serial_nr:
			print('Gotcha !')
			counter = user.get_counter_from_serial_nr(self.x_serial_nr)
			#print(counter)
			self.x_counter_value = counter








# 29 Aug 2019 - Update Legacy
# Deprecated !


	# Update Legacy Jan
	@api.multi
	def update_legacy_jan(self):
		"""
		high level support for doing this and that.
		"""
		orders = self.env['sale.order'].search([
																('date_order', '>=', '2018-01-01'),
																('date_order', '<', '2018-02-01'),
													],
																order='date_order asc',
																#limit=1000,
												)
		for order in orders:
			order.update_legacy()


	# Update Legacy Fev
	@api.multi
	def update_legacy_fev(self):
		"""
		high level support for doing this and that.
		"""

		orders = self.env['sale.order'].search([
																('date_order', '>=', '2018-02-01'),
																('date_order', '<', '2018-03-01'),
													],
																order='date_order asc',
																#limit=1000,
												)
		for order in orders:
			order.update_legacy()



	# Update Legacy Mar
	@api.multi
	def update_legacy_mar(self):
		"""
		high level support for doing this and that.
		"""
		orders = self.env['sale.order'].search([
																('date_order', '>=', '2018-03-01'),
																('date_order', '<', '2018-03-06'),
													],
																order='date_order asc',
																#limit=1000,
												)
		for order in orders:
			order.update_legacy()
	# update_type_legacy_mar


	# Update Legacy
	#@api.multi
	#def update_legacy(self):
	#	"""
	#	high level support for doing this and that.
	#	"""
	#	self.x_legacy = True







# 29 Aug 2019 - Update Descriptors All
# Deprecated !

# ----------------------------------------------------------- Update Descriptors ------------------

	# For batch
	@api.multi
	def update_descriptors_all(self):
		"""
		high level support for doing this and that.
		"""
		orders = self.env['sale.order'].search([
													('state', '=', 'sale'),
											],
												order='date_order desc',
												#limit=2000,
												limit=300,
											)
		#print orders
		for order in orders:
			order.update_descriptors()







# 29 Aug 2019 - Update Month Day All
# Deprecated !

	# Update Day Month - All
	@api.multi
	def update_day_month_all(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Day Month - All')
		orders = self.env['sale.order'].search([
																('date_order', '>=', '2018-01-01'),
													],
																order='date_order asc',
																#limit=1000,
												)
		for order in orders:
			if order.x_day_order in [False] and order.x_month_order in [False]:
				order.update_day_month()









# 29 Aug 2019 - Print Ticket Old
# Deprecated !

	# Print Ticket - Deprecated !
	@api.multi
	def print_ticket(self):
		"""
		high level support for doing this and that.
		"""
		if self.x_type == 'ticket_receipt':
			name = 'openhealth.report_ticket_receipt_nex_view'
			return self.env['report'].get_action(self, name)
		elif self.x_type == 'ticket_invoice':
			name = 'openhealth.report_ticket_invoice_nex_view'
			return self.env['report'].get_action(self, name)









# 29 Aug 2019 - Testing
# Deprecated !

	# Test Case
	x_test_case = fields.Char()


	# Test
	@api.multi
	def test(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Order - Test - Interface'
		test_order.test(self)


	def test_actions(self):
		"""
		high level support for doing this and that.
		"""
		print('')
		print('Test Actions')
		self.print_ticket_electronic()
		self.correct_pm()
		self.create_credit_note()
		self.cancel_order()
		self.activate_order()


	def test_computes(self):
		"""
		high level support for doing this and that.
		"""
		print('')
		print('Test Computes')

		print(self.x_type_code)
		print(self.nr_lines)
		print(self.x_partner_vip)
		#print(self.x_total_in_words)
		#print(self.x_total_cents)
		#print(self.x_total_net)
		#print(self.x_total_tax)
		#print(self.x_my_company)
		#print(self.x_date_order_corr)
		#print(self.x_amount_total)
		#print(self.)








# 29 Aug 2019 - Automatec Actions - Called by Appointment
# Highly Deprecated !!!


# ----------------------------------------------------------- Automatic - Highly Deprecated !!! ---------------------------

	# Get Control Date Auto
	#@api.multi
	#def get_date_order_auto(self, date):
	#	"""
	#	Get Date Order Auto
	#	Used by Automated Actions - Appointments
	#	"""
	#	print()
	#	print('Get Date Order Auto')
	#	print('Do Nothing')
	#
	#	#print(date)
	#
	#	if date not in [False]:
	#		date_format = "%Y-%m-%d %H:%M:%S"
	#		date_dt = datetime.datetime.strptime(date, date_format) + datetime.timedelta(hours=-5, minutes=0)
	#		date_str = date_dt.strftime(date_format)
	#	else:
	#		date_str = False
	#
	#	return date_str








# 29 Aug 2019 - Confirm

	@api.multi
	def action_confirm_nex(self):

		# Call the Parent Procedure - Highly Deprecated. Generates Procurement and Stock  !!!
		#super(sale_order, self).action_confirm()




# 29 Aug 2019 - Computes

	# Total in Words
	#x_total_in_words = fields.Char(
	#		"",
			#compute='_compute_x_total_in_words',
	#	)

	# Total in cents
	#x_total_cents = fields.Integer(
	#		"Céntimos",
			#compute='_compute_x_total_cents',
	#	)


	# Date corrected
	#x_date_order_corr = fields.Char(
	#		string='Order Date Corr',
			#compute="_compute_date_order_corr",
	#	)




# 29 Aug 2019 - Getters


# ----------------------------------------------------------- Ticket - Getters ----------------

	# Company

	def get_company_name(self):
		"""
		Used by Print Ticket.
		"""
		company_name = 'SERVICIOS MÉDICOS ESTÉTICOS S.A.C'
		return company_name


	def get_company_address(self):
		"""
		Used by Print Ticket.
		"""
		company_address = 'Av. La Merced 161 Miraflores - Lima'
		return company_address


	def get_company_phone(self):
		"""
		Used by Print Ticket.
		"""
		company_phone = 'Teléfono: (051) 321 2394'
		return company_phone


	def get_company_ruc(self):
		"""
		Used by Print Ticket.
		"""
		company_ruc = 'R.U.C.: 20523424221'
		return company_ruc


	def get_title(self):
		"""
		Used by Print Ticket.
		"""
		return self.x_title


	def get_serial_nr(self):
		"""
		Used by Print Ticket.
		"""
		return self.x_serial_nr



	def get_warning(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Get Warning')
		#return self.x_my_company.x_warning
		return False


	def get_website(self):
		"""
		high level support for doing this and that.
		"""
		#return self.x_my_company.website
		return False


	def get_email(self):
		"""
		high level support for doing this and that.
		"""
		#return self.x_my_company.email
		return False



# ----------------------------------------------------------- Electronic - Getters ----------------

	#def get_patient_address(self):
	#	"""
	#	high level support for doing this and that.
	#	"""
		#print
		#print 'Get Patient Address'
	#	return self.partner_id.x_address


	#def get_firm_address(self):
	#	"""
	#	high level support for doing this and that.
	#	"""
	#	return self.partner_id.x_address



	def get_credit_note_type(self):
		"""
		Used by Print Ticket.
		"""
		_dic_cn = {
					'cancel': 					'Anulación de la operación.',
					'cancel_error_ruc': 		'Anulación por error en el RUC.',
					'correct_error_desc': 		'Corrección por error en la descripción.',
					'discount': 				'Descuento global.',
					'discount_item': 			'Descuento por item.',
					'return': 					'Devolución total.',
					'return_item': 				'Devolución por item.',
					'bonus': 					'Bonificación.',
					'value_drop': 				'Disminución en el valor.',
					'other': 					'Otros.',
					False: 						'',
		}
		return _dic_cn[self.x_credit_note_type]


	def get_credit_note_owner_amount(self):
		"""
		Used by Print Ticket.
		"""
		return self.x_credit_note_owner_amount












# 28 Aug 2019
# App is Highly Deprecated !
# My Company also
# 


		# Manage Exception
		try:
			configurator.ensure_one()

		except:
			msg = "ERROR: Record Must be One."
			class_name = type(configurator).__name__
			#obj_name = counter.name
			#msg =  msg + '\n' + class_name + '\n' + obj_name
			#msg =  msg 
			msg =  msg + '\n' + class_name

			raise UserError(_(msg))




# ----------------------------------------------------------- Appointments - Dep !!! -----------------

	# Update Appointment in Treatment
	#@api.multi
	#def update_appointment(self):
	#	"""
	#	high level support for doing this and that.
	#	"""
	#	if self.x_family == 'consultation':
	#		for app in self.treatment.appointment_ids:
	#			if app.x_type == 'consultation':
	#				app.state = 'Scheduled'
	#	if self.x_family == 'procedure':
	#		for app in self.treatment.appointment_ids:
	#			if app.x_type == 'procedure':
	#				app.state = 'Scheduled'




# ----------------------------------------------------------- Dep ! -------------------------

	# My company
	#x_my_company = fields.Many2one(
	#		'res.partner',
	#		string="Mi compañía",
	#		domain=[
	#					('company_type', '=', 'company'),
	#				],

	#		compute="_compute_x_my_company",
	#	)

	#@api.multi
	#def _compute_x_my_company(self):
	#	for record in self:
	#			com = self.env['res.partner'].search([
	#														('x_my_company', '=', True),
	#												],
	#												order='date desc',
	#												limit=1,
	#				)
	#			record.x_my_company = com







	def action_confirm_nex(self):


		#if self.x_serial_nr != '' and self.x_admin_mode == False:
			# Prefix
			#prefix = ord_vars._dic_prefix[self.x_type]

			# Padding
			#padding = ord_vars._dic_padding[self.x_type]

			# Serial Nr
			#self.x_serial_nr = prefix + self.x_separator + str(self.x_counter_value).zfill(padding)

			#self.x_counter_value = user.get_counter_value(self)

			#self.x_serial_nr = user.get_serial_nr(self.x_type, self.x_counter_value)


		#res = super(sale_order, self).action_confirm()




# ----------------------------------------------------- Product Selector - Dep --------------------------

	@api.multi
	def open_product_selector_product(self):
		"""
		high level support for doing this and that.
		"""
		return self.open_product_selector('product')


	@api.multi
	def open_product_selector_service(self):
		"""
		high level support for doing this and that.
		"""
		return self.open_product_selector('service')


	# Buttons  - Agregar Producto Servicio
	@api.multi
	def open_product_selector(self, x_type):
		"""
		high level support for doing this and that.
		"""

		# Init Vars
		order_id = self.id
		res_id = False

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Orderline Selector Current',
				'view_type': 'form',
				'view_mode': 'form',
				#'target': 'current',
				'target': 'new',

				'res_id': res_id,

				#'res_model': 'sale.order.line',
				'res_model': 'openhealth.product.selector',
				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
								'form':{'action_buttons': False, 'options': {'mode': 'edit'}}
							},
				'context': {
								'default_order_id': order_id,
								'default_x_type': x_type,
					}}
	# open_product_selector
