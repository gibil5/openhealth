# 4 Dec 2019

# ----------------------------------------------------------- Make SN - BUtton ----------------------
	# Make Serial Number
	@api.multi
	def make_serial_number(self):


		# Get Order
		order = self.env['sale.order'].search([
													('x_electronic', '=', True),
													('x_type', '=', self.x_type),
													('state', 'in', ['sale', 'cancel']),
												],
											
											#order='x_counter_value desc',		# Deprecated. Too unstable for Tacna !
											order='date_order desc',
											
											limit=1,
										)
		#print(order)
		#print(order.x_counter_value)


		# Update Counter
		self.x_counter_value = order.x_counter_value + 1
		#print(self.x_counter_value)





# ----------------------------------------------------------- Autofill - Dep ----------------------------
	# Autofill
	x_autofill = fields.Boolean(
			string="Autofill",
			default=False,
		)

	# Autofill
	@api.onchange('x_autofill')
	def _onchange_x_autofill(self):
		if self.x_autofill:
			self.autofill()


	def autofill(self):
		"""
		Autofill Order
		For Testing
		"""

		#self.sex = 'Male'

		# Patient
		patient = self.env['oeh.medical.patient'].search([
															('name', 'in', ["REVILLA RONDON JOSE JAVIER"]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		print(patient.name)


		# Doctor
		doctor = self.env['oeh.medical.physician'].search([
															('name', 'in', ["Dr. Chavarri"]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		print(doctor.name)


		# Treatment
		treatment = self.env['openhealth.treatment'].search([
															('patient', 'in', ["REVILLA RONDON JOSE JAVIER"]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		print(treatment.name)

		# Fill
		self.patient = patient
		self.x_doctor = doctor
		self.treatment = treatment

	# autofill




# ----------------------------------------------------------- Quick Sale - Dep -------------------------------

	@api.multi
	def quick_sale_service(self):
		"""
		Quick Sale Service
		To accelerate Testing
		"""
		print()
		print('Quick Sale Service')

		#self.order_line.create

		# Product
		name = "LASER CO2 FRACCIONAL - Todo Rostro - Rejuvenecimiento - Grado 1 - 1 sesion"
		product = self.env['product.product'].search([
															('name', 'in', [name]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		print(product.name)


		# Line
		line = self.order_line.create({
											'product_id': product.id,
											'product_uom_qty': 1,
											'order_id': self.id,
										})
		print(line.product_id.name)

		# Pay
		if self.state in ['draft']:
			self.pay_myself()







# ----------------------------------------------------------- Ticket - Get Table Lines - Format ----------------

	# Format Line
	def format_line(self, tag, value):
		"""
		Abstraction. 
		Used by tickets.
		Contains the formatting rules. For all entries. 
		Does not use Bootstrap classed. Is much more robust than the previous approach. 
		Allows for easy font size config. 
		"""

		#value = str(value)

		# Init
		_size_font = '2'


		# Items header
		if tag in ['items'] and value in ['header']:

			line = 	"<tr>\
						<td>\
							<font size='2'>\
								<b>Desc</b>\
							</font>\
						</td>\
						<td>\
							<font size='2'>\
								<b>Cnt</b>\
							</font>\
						</td>\
						<td>\
							<font size='2'>\
								<b>PUnit</b>\
							</font>\
						</td>\
						<td>\
							<font size='2'>\
								<b>Total</b>\
							</font>\
						</td>\
					</tr>"


		# Formatted line
		else:

			line = "<tr>\
						<td>\
							<font size='" + _size_font +"'>\
								<b>" + tag + "</b>\
							</font>\
						</td>\
						<td>\
							<font size='" + _size_font + " '>"\
								+ value + "</font></td></tr>"


		return line 



	# Format Line
	def format_line_lean(self, tag, value):
		"""
		Abstraction. 
		Contains the formatting rules. For all entries. 
		Lean version (not bold)
		"""

		#value = str(value)

		line = "<tr>\
					<td>\
						<font size='2'>" + tag + "</font>\
					</td>\
					<td>\
						<font size='2'>" + value + "</font>\
					</td>\
				</tr>"

		return line 





# ----------------------------------------------------------- Credit Notes - Getters ----------------

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





# ----------------------------------------------------------- Ticket - Get Items Lines  ----------------

	# Patient Name 
	def get_order_lines_header(self):
		print()
		print('Get Order Lines Header')

		line = 	"<tr>\
					<td>\
						<font size='2'>\
							<b>Desc</b>\
						</font>\
					</td>\
					<td>\
						<font size='2'>\
							<b>Cnt</b>\
						</font>\
					</td>\
					<td>\
						<font size='2'>\
							<b>PUnit</b>\
						</font>\
					</td>\
					<td>\
						<font size='2'>\
							<b>Total</b>\
						</font>\
					</td>\
				</tr>"

		#print(line)
		return line





# ----------------------------------------------------------- Ticket - Get Table Lines - Words ----------------

	# Ticket Total Words Header
	def get_ticket_total_words_header(self):

		tag = 'Son:'
		value = ''

		line = self.format_line(tag, value)

		#print(line)
		return line



	# Ticket Total Words Soles
	def get_ticket_total_words_soles(self):

		tag = ''
		value = str(self.get_total_in_words())

		line = self.format_line(tag, value)

		#print(line)
		return line



	# Ticket Total Words Cents
	def get_ticket_total_words_cents(self):

		tag = ''
		value = str(self.get_total_cents())

		line = self.format_line(tag, value)

		#print(line)
		return line



	# Ticket Total Words Footer
	def get_ticket_total_words_footer(self):

		tag = ''
		value = 'Soles'

		line = self.format_line(tag, value)

		#print(line)
		return line








# ----------------------------------------------------------- Ticket - Get Table Lines - Totals ----------------

	# Ticket Total Net 
	def get_ticket_total_net_line(self):

		tag = 'OP. GRAVADAS S/.'
		value = str(self.get_total_net())

		line = self.format_line_lean(tag, value)

		#print(line)
		return line



	# Ticket Total Free
	def get_ticket_total_free_line(self):

		tag = 'OP. GRATUITAS S/.'
		value = '0'

		line = self.format_line_lean(tag, value)

		#print(line)
		return line




	# Ticket Total Exonerated 
	def get_ticket_total_exonerated_line(self):

		tag = 'OP. EXONERADAS S/.'
		value = '0'

		line = self.format_line_lean(tag, value)

		#print(line)
		return line



	# Ticket Total Unaffected 
	def get_ticket_total_unaffected_line(self):

		tag = 'OP. INAFECTAS S/.'
		value = '0'

		line = self.format_line_lean(tag, value)

		#print(line)
		return line



	# Ticket Total Tax 
	def get_ticket_total_tax_line(self):

		tag = 'I.G.V. 18% S/.'
		value = str(self.get_total_tax())

		line = self.format_line_lean(tag, value)

		#print(line)
		return line



	# Ticket Total
	def get_ticket_total_line(self):

		tag = 'TOTAL S/.'
		value = str(self.get_amount_total())

		line = self.format_line_lean(tag, value)

		#print(line)
		return line




# ----------------------------------------------------------- Ticket - Sale  ----------------

	# Ticket Date
	def get_ticket_date_line(self):
		print()
		print('Get Ticket Date Line')

		tag = 'Fecha:'
		value = self.get_date_corrected()

		line = self.format_line(tag, value )

		#print(line)
		return line


	# Ticket Number
	def get_ticket_number_line(self):
		print()
		print('Get Ticket Number Line')

		tag = 'Ticket:'
		value = self.x_serial_nr

		line = self.format_line(tag, value )

		#print(line)
		return line






# ----------------------------------------------------------- Ticket - Receipt ----------------

	# Patient Name 
	def get_patient_name_line(self):
		print()
		print('Get Patient Name Line')

		tag = 'Cliente:'
		value = self.patient.name

		#line = self.format_line('Cliente:', self.patient.name )
		line = self.format_line(tag, value )

		#print(line)
		return line



	# Patient Dni
	def get_patient_dni_line(self):
		#print()
		#print('Get Patient Dni Line')

		line = self.format_line('DNI:', self.x_id_doc )

		#print(line)
		return line



	# Patient Address
	def get_patient_address_line(self):
		print()
		print('Get Patient Address Line')

		line = self.format_line('Direccion:', self.get_patient_address() )

		#print(line)
		return line



# ----------------------------------------------------------- Ticket - Invoice ----------------

	# Patient Name 
	def get_patient_firm_line(self):
		print()
		print('Get Patient Firm Line')

		line = self.format_line('Razon social::', self.patient.x_firm )

		#print(line)
		return line



	# Patient Ruc
	def get_patient_ruc_line(self):
		print()
		print('Get Patient Firm Line')

		line = self.format_line('RUC::', self.x_ruc )

		#print(line)
		return line



	# Patient Firm Address
	def get_patient_firm_address_line(self):
		print()
		print('Get Patient Firm Address Line')

		line = self.format_line('Direccion::', self.get_firm_address() )

		#print(line)
		return line





# ----------------------------------------------------------- Ticket Get Raw Line ----------------
	# Raw Line
	def get_ticket_raw_line_dep(self, argument):
		"""
		Abstraction. 
		Used by tickets.
		Can be used by all entries. 
		Types:
			- Receipt, 
			- Invoice, 
			- Credit note. 
		"""

		print()
		print('Get Ticket Raw Line')

		print(argument)

		line = 'empty'


		# Credit note
		if argument in ['date_credit_note']:
			tag = 'Fecha:'
			value = self.get_date_corrected()

		elif argument in ['denomination_credit_note_owner']:
			tag = 'Denominacion:'
			value = self.x_credit_note_owner.x_serial_nr

		elif argument in ['date_credit_note_owner']:
			tag = 'Fecha de emision:'
			value = self.x_credit_note_owner.get_date_corrected()

		elif argument in ['reason_credit_note']:
			tag = 'Motivo:'
			value = self.get_credit_note_type()



		# Receipt


		# Invoice



		else:
			print('This should not happen !')


		line = self.format_line(tag, value)


		#print(line)
		return line












# 23 Nov 2019

# Serial nr


# Credit note

		# State
		#state = 'credit_note'

		# Counter
		#counter_value = user.get_counter_value(self, self.x_type, state)

		# Serial Nr
		#serial_nr = user.get_serial_nr(self.x_type, counter_value, state)



		# Init
		x_type = self.x_type
		#state = 'credit_note'

		# Create Object
		snr_obj = snr.SerialNumber(self, x_type, state)

		# Get data
		serial_nr = snr_obj.get_serial_number()
		counter_value = snr_obj.get_counter()
		#print(serial_nr)



# Sale 
		# Init
		#x_type = self.x_type
		#state = self.state

		# Create Object
		#snr_obj = snr.SerialNumber(self, x_type, state)

		# Get data
		#serial_nr = snr_obj.get_serial_number()
		#counter_value = snr_obj.get_counter()
		#print(serial_nr)

		# Update the Database
		#self.write({
		#				'x_serial_nr': serial_nr,
		#				'x_counter_value': counter_value,
		#		})




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
