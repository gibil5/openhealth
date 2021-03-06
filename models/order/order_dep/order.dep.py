# 6 dec 2020 

# ----------------------------------------------------------- Dep ? -------
	# Check Ruc
	#@api.constrains('x_ruc')
	#def _check_x_ruc(self):
	#	if self.x_type in ['ticket_invoice', 'invoice']:
	#		chk_patient.check_x_ruc(self)

	# Check Id doc - Use Chk Patient
	#@api.constrains('x_id_doc')
	#def _check_x_id_doc(self):
	#	if self.x_type in ['ticket_receipt', 'receipt']:
	#		chk_patient.check_x_id_doc(self)



# 8 Aug 2020 


# ----------------------------------------------------------- Test Validation --------------------------------
	#@api.multi
	#def test_validation(self):
	#	"""
	#	Test Validation
	#	"""
	#	print('')
	#	print('Test Validation')
	#	self.validate_and_confirm()

# ----------------------------------------------------------- Test Payment method --------------------------------
	#@api.multi
	#def test_pm(self):
	#	"""
	#	Test Payment method
	#	"""
	#	print('')
	#	print('test_pm')
	#	self.create_payment_method()

# ----------------------------------------------------------- Test Ticket --------------------------------
	#@api.multi
	#def test_ticket(self):
	#	"""
	#	Test Ticket
	#	"""
	#	print('')
	#	print('Test Ticket')
	#	name = 'openhealth.report_ticket_receipt_electronic'
	#	action = self.env['report'].get_action(self, name)
	#	return action

# ----------------------------------------------------------- Test QR --------------------------------
	#@api.multi
	#def test_qr(self):
	#	"""
	#	Test QR
	#	"""
	#	print()
	#	print('order - test_qr')
		# Create loosely coupled object
	#	h = self.get_hash_for_qr()
	#	qr_obj = qr.QR(h)
		# Get data
	#	print(qr_obj.get_name())
	#	print(qr_obj.get_img_str())
		#qr_obj.print_obj()


# ----------------------------------------------------------- Test Payment method --------------------------------
	#@api.multi
	#def test_serial_number(self):
	#	"""
	#	Test Serial Number
	#	"""
	#	print('')
	#	print('test_serial_number')
	#	self.make_serial_number()




def set_procedure_created(self, value=True):
	"""
	Set Procedure Created
	Used by: Treatment and Order
	"""
	print()
	print('order - set_procedure_created')
	self.x_procedure_created = value


	# Date Date
	#x_date_order_date = fields.Date(
	#	'Fecha',
	#)


	# Check payment method
	#@api.multi
	#def check_payment_method(self):
	#	"""
	#	Check Payment method
	#	"""
		#print
		#print 'Check Payment Method'
	#	pm_total = 0
	#	for pm in self.x_payment_method.pm_line_ids:
	#		pm_total = pm_total + pm.subtotal
	#	self.x_pm_total = pm_total


# ----------------------------------------------------------- Pricelist  -------------------------------
	# Default
	def _get_default_pricelist(self):
		print()
		print('Default Pricelist')
		# Search
		pricelist = self.env['product.pricelist'].search([
												#('active', 'in', [True]),
												],
												#order='x_serial_nr asc',
												limit=1,
											)
		print(pricelist)
		print(pricelist.name)
		return pricelist





# 1 Aug 2020 
from openerp.addons.openhealth.models.emr import pl_creates

# ----------------------------------------------------------- Setters ----------------------------

	def create_procedure_man(self, treatment):
		"""
		Create Procedure Man - In prog
		Used by: Treatment
		"""
		# Update Order
		#self.set_procedure_created(True)
		self.set_procedure_created()

		# Loop
		for line in self.order_line:
			print(line.product_id)
			if line.product_id.is_procedure():
				product_product = line.product_id

				# Create
				#pl_creates.create_procedure_go(self, product_product)
				pl_creates.create_procedure_go(treatment, product_product)


	#def set_procedure_created(self, value):
	def set_procedure_created(self, value=True):
		"""
		Set Procedure Created
		Used by: Treatment and Order
		"""
		print()
		print('order - set_procedure_created')
		self.x_procedure_created = value


	#def is_procedure_created(self):
	def proc_is_not_created_and_state_is_sale(self):
		"""
		Used by: Treatment
		"""
		print()
		print('order - proc_is_not_created_and_state_is_sale')
		#return self.x_procedure_created
		return not self.x_procedure_created and self.state == 'sale'







# 26 Jul 2020 

	# Partner Vip - OK
	x_partner_vip = fields.Boolean(
			'Vip',
			default=False,
			compute="_compute_partner_vip",
		)

	@api.multi
	def _compute_partner_vip(self):
		for record in self:
			record.x_partner_vip = False
			#count = self.env['openhealth.card'].search_count([
			#													('patient_name', '=', record.partner_id.name),
			#											])
			#if count == 0:
			#	record.x_partner_vip = False
			#else:
			#	record.x_partner_vip = True


# --------------------------------- Price List - Computes ----------------------
	# Price List
	pl_price_list = fields.Char(
			string="Pl - Price List",
			compute='_compute_pl_price_list',
		)
	@api.multi
	def _compute_pl_price_list(self):
		for record in self:
			price_list = ''
			for line in record.order_line:
				price_list = line.get_price_list()
			record.pl_price_list = price_list


	# Check Serial Nr
	@api.constrains('x_serial_nr')
	def _check_x_serial_nr(self):
		chk_order.check_serial_nr(self)


		options = {
			0 : zero,
			1 : sqr,
			4 : sqr,
			9 : sqr,
			2 : even,
			3 : prime,
			5 : prime,
			7 : prime,
		}

		#options = {
		#	'totals_net' : ('OP. GRAVADAS S/.', str(self.get_total_net())),
		#	'totals_free' : ('OP. GRATUITAS S/.', '0'),
		#	'totals_exonerated' : ('OP. EXONERADAS S/.', '0'),
		#	'totals_unaffected' : (),
		#	'totals_tax' : (),
		#	'totals_total' : (),
		#	'warning' : (),
		#	'website' : (),
		#	'email' : (),
		#}
		#return options[tag]


	def get_raw_line(self, argument):

		# Totals
		if argument in ['totals_net']:
			tag = 'OP. GRAVADAS S/.'
			value = str(self.get_total_net())

		elif argument in ['totals_free']:
			tag = 'OP. GRATUITAS S/.'
			value = '0'

		elif argument in ['totals_exonerated']:
			tag = 'OP. EXONERADAS S/.'
			value = '0'




	def get_company(self, item):

		if item == 'name':
			ret = self.configurator.company_name
		elif item == 'ruc':
			ret = self.configurator.ticket_company_ruc
		elif item == 'address':
			ret = self.configurator.ticket_company_address

		elif item == 'phone':
			ret = self.configurator.company_phone
		elif item == 'note':
			ret = self.configurator.ticket_note
		elif item == 'description':
			ret = self.configurator.ticket_description

		elif item == 'warning':
			ret = self.configurator.ticket_warning
		elif item == 'website':
			ret = self.configurator.company_website
		elif item == 'email':
			ret = self.configurator.company_email

		return ret



# ----------------------------------------------------------- Correct -----------------------------
	# Correct payment method
	@api.multi
	def correct_pm(self):
		"""
		Correct payment method
		"""
		if self.x_payment_method.name == False:
			self.x_payment_method = self.env['openhealth.payment_method'].create({
																					'order': 	self.id,
																					'partner':	self.partner_id.id,
																					'total':	self.amount_total,
																			})
		res_id = self.x_payment_method.id

		return {
			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Payment Method Current',
			# Window action
			'res_id': res_id,
			'res_model': 'openhealth.payment_method',
			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
						#'form': {'action_buttons': False, }
					},
			'context': {}
		}
	# correct_pm






# 25 Jul 2D2020

# ----------------------------------------------------------- Constraints - Sql -------------------
	# Uniqueness constraints for:
	# Serial Number
	_sql_constraints = [
				#('x_serial_nr','unique(x_serial_nr)', 'SQL Warning: x_serial_nr must be unique !'),
				('x_serial_nr', 'Check(1=1)', 'SQL Warning: x_serial_nr must be unique !'),
			]

	@api.multi
	def fix_treatment_month(self):
		"""
		Fix Treatment Month
		"""
		print()
		print('Fix Treatment Month')


	@api.multi
	def fix_treatment_all(self):
		"""
		Fix Treatment All
		"""
		print()
		print('Fix Treatment All')





# 24 Jul 2020

"""
Sale Class - Inherited from the medical Module OeHealth.
Has the Business Logic of the Clinic.
This is only a Data Model. Must NOT contain Business Rules.
All BRs should be in Classes and Libraries.
"""



# ------------------------------- Used by - Print Ticket - Header and Footer ---
	def get_title(self):
		return self.x_title

	def get_serial_nr(self):
		return self.x_serial_nr

	def get_firm_address(self):
		return self.patient.x_firm_address

	def get_patient_address(self):
		return self.patient.x_address

	def get_note(self):
		if self.pl_transfer_free:
			note = 'TRANSFERENCIA A TITULO GRATUITO'
		else:
			if self.x_type in ['ticket_receipt']:
				note = 'Representación impresa de la BOLETA DE VENTA ELECTRONICA.'
			elif self.x_type in ['ticket_invoice']:
				note = 'Representación impresa de la FACTURA DE VENTA ELECTRONICA.'
			else:
				note = ''
		return note

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_raw_line(self, argument):
		"""
		Just a stub.
		"""
		line = raw_funcs.get_ticket_raw_line(self, argument)
		return line


# ----------------------------------------------------------- Ticket - Header - Getters ----------------

	# Company Address
	def get_company_name(self):
		company_name = self.configurator.company_name
		return company_name

	# Company Address
	def get_company_address(self):
		company_address = self.configurator.ticket_company_address
		return company_address

	# Company Address
	def get_company_phone(self):
		company_phone = self.configurator.company_phone
		return company_phone

	# Company Address
	def get_company_ruc(self):
		company_ruc = self.configurator.ticket_company_ruc
		return company_ruc

# ----------------------------------------------------------- Ticket - Footer - Getters ----------------

	# Description
	def get_description(self):
		description = self.configurator.ticket_description
		return description

	# Warning
	def get_warning(self):
		warning = self.configurator.ticket_warning
		return warning

	# Website
	def get_website(self):
		website = self.configurator.website
		return website

	# Email
	def get_email(self):
		email = self.configurator.email
		return email

# ----------------------------------------------------------- Print Ticket - Amounts -------------------------------

	def get_amount_total(self):
		"""
		Used by Print Ticket.
		Is zero if Transfer Free.
		"""
		#print()
		#print('Get Amount Total')
		if self.pl_transfer_free:
			total = 0
		else:
			total = tick_funcs.get_total(self)
		return total

	def get_total_net(self):
		"""
		Used by Print Ticket.
		Is zero if Transfer Free.
		"""
		#print()
		#print('Get Total Net')

		if self.pl_transfer_free:
			self.x_total_net = 0

		else:
			self.x_total_net =  tick_funcs.get_net(self)

		return self.x_total_net



	def get_total_tax(self):
		"""
		Used by Print Ticket.
		Is zero if Transfer Free.
		"""
		#print()
		#print('Get Total Tax')

		if self.pl_transfer_free:
			self.x_total_tax = 0

		else:
			self.x_total_tax = tick_funcs.get_tax(self)

		return self.x_total_tax



	def get_total_in_words(self):
		"""
		Used by Print Ticket.
		"""
		#print()
		#print('Get Total Words')

		if self.pl_transfer_free:
			words = 'Cero'

		else:
			words = tick_funcs.get_words(self)

		#return tick_funcs.get_words(self)
		return words



	def get_total_cents(self):
		"""
		Used by Print Ticket.
		"""
		#print()
		#print('Get Total Cents')

		if self.pl_transfer_free:
			cents = '0.0'

		else:
			cents = tick_funcs.get_cents(self)

		#return tick_funcs.get_cents(self)
		return cents



# ----------------------------------------------------------- Configurator -------------------------
	#def _get_default_configurator(self):
	#	print()
	#	print('Default Configurator')
		# Search
	#	configurator = self.env['openhealth.configurator.emr'].search([
												#('active', 'in', [True]),
	#											],
												#order='x_serial_nr asc',
	#											limit=1,
	#										)
	#	return configurator

	#configurator = fields.Many2one(
	#		'openhealth.configurator.emr',
	#		string="Config",
	#		readonly=True,

			#required=True,
	#		required=False,
			#default=_get_default_configurator,
	#	)
