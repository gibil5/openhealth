# 26 sep 2019




# ----------------------------------------------------------- Testing Booleans --------------------

	# Create Flags

	# Sessions
	ses_create = fields.Boolean(
			string="Ses",
			default=False,
		)

	# Controls
	con_create = fields.Boolean(
			string="Con",
			default=False,
		)



	# Laser
	co2_create = fields.Boolean(
			string="Co2",
			default=False,
		)

	exc_create = fields.Boolean(
			string="Exc",
			default=False,
		)

	ipl_create = fields.Boolean(
			string="Ipl",
			default=False,
		)

	ndy_create = fields.Boolean(
			string="Ndyag",
			default=False,
		)

	qui_create = fields.Boolean(
			string="Quick",
			default=False,
		)

	# Medical
	med_create = fields.Boolean(
			string="Med",
			default=False,
		)

	# Cosmeto
	cos_create = fields.Boolean(
			string="Cos",
			default=False,
		)

	# Vip
	vip_create = fields.Boolean(
			string="Vip",
			default=False,
		)

	# Product
	product_create = fields.Boolean(
			string="Product",
			default=False,
		)






# ----------------------------------------------------------- Creates - Manual, Process and Testing ---------------------------------

# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_tst(self):

		# Init
		target = 'consultation'

		# Create
		order = cre.create_order(self, target)

		return order


# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con(self):

		# Init
		target = 'consultation'

		# Create
		order = cre.create_order(self, target)

		# Open
		return {
				# Created
				'res_id': order.id,
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action
				'res_model': 'sale.order',
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
				'context': {}
			}
	# create_order_con


# -----------------------------------------------------------  Create Order Pro  ------------------
	@api.multi
	def create_order_pro(self):

		target = 'procedure'

		order = cre.create_order(self, target)

		return {
				# Created
				'res_id': order.id,
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action
				'res_model': 'sale.order',
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
				'context': {}
			}
	# create_order_pro


# ----------------------------------------------------------- Create Procedure Manual  ------------
	@api.multi
	def create_procedure_man(self):
		#print
		#print 'Create Procedure - Manual'

		# Loop - Create Procedures
		ret = 0
		for order in self.order_pro_ids:

			if order.state == 'sale':

				# Update
				order.x_procedure_created = True

				# Loop
				for line in order.order_line:

					# Init
					date_app = order.date_order
					product_id = line.product_id

					# Search
					product_template = self.env['product.template'].search([
																				('x_name_short', '=', product_id.x_name_short),
												])

					subtype = product_template.x_treatment

					ret = cre.create_procedure_go(self, date_app, subtype, product_id.id)




# ----------------------------------------------------------- Create Controls  --------------------
	# Create Controls
	@api.multi
	def create_controls(self):
		#print
		#print 'Create Controls'
		control_date = self.start_date
		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id
		chief_complaint = self.chief_complaint

		# Create Control
		control = self.control_ids.create({
											'evaluation_start_date':control_date,
											'first_date':control_date,
											'patient':patient_id,
											'doctor':doctor_id,
											'chief_complaint':chief_complaint,
											'treatment': treatment_id,

											#'appointment': appointment_id,
											#'product':product_id,
											#'procedure':procedure_id,
									})
	# create_controls




# ----------------------------------------------------- Create Consultation -----------------------
	# Create Consultation
	@api.multi
	def create_consultation(self):
		print()
		print('OH - Create Consultation')


		# Init vars
		patient_id = self.patient.id
		treatment_id = self.id
		chief_complaint = self.chief_complaint


		# Doctor
		doctor = user.get_actual_doctor(self)
		doctor_id = doctor.id

		if doctor_id == False:
			doctor_id = self.physician.id


		# Date
		GMT = time_funcs.Zone(0, False, 'GMT')
		#evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")



		# Apointment
		#if False:
		#	appointment = self.env['oeh.medical.appointment'].search([
		#																('patient', '=', self.patient.name),
		#																('doctor', '=', self.physician.name),
		#																('x_type', '=', 'consultation'),
		#														],
		#														order='appointment_date desc', limit=1)
		#	appointment_id = appointment.id
		
		#appointment_id = False



		# Search
		consultation = self.env['openhealth.consultation'].search([
																		('treatment', '=', self.id),
																],
																#order='appointment_date desc',
																limit=1,)
		# Create if it does not exist
		if consultation.name == False:

			# Change App state
			#if False:
			#	if appointment.name != False:
			#		appointment.state = 'Scheduled'


			# Consultation
			consultation = self.env['openhealth.consultation'].create({
																		'patient': patient_id,
																		'treatment': treatment_id,
																		'evaluation_start_date': evaluation_start_date,
																		'chief_complaint': chief_complaint,
																		#'appointment': appointment_id,
																		'doctor': doctor_id,
													})
			consultation_id = consultation.id


			# Update
			#if False:
			#	rec_set = self.env['oeh.medical.appointment'].browse([
			#															appointment_id
			#														])
			#	ret = rec_set.write({
			#							'consultation': consultation_id,
			#						})



		consultation_id = consultation.id

		# Update Patient
		#consultation.update_patient()

		return {

			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action
			'res_model': 'openhealth.consultation',
			'res_id': consultation_id,
			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#'view_id': 'oeh_medical_evaluation_view',
			#'view_id': 'oehealth.oeh_medical_evaluation_view',
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
					},
			'context':   {
							'search_default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							'default_treatment': treatment_id,
							'default_evaluation_start_date': evaluation_start_date,
							'default_chief_complaint': chief_complaint,
							#'default_appointment': appointment_id,
			}
		}
	# create_consultation






# ----------------------------------------------------------- Partner - Create Order - Fields - Dep ? ---------------------------

	# Partner
	partner_id = fields.Many2one(
			'res.partner',
			string="Cliente",

			compute='_compute_partner_id',
		)

	#@api.multi
	@api.depends('patient')
	def _compute_partner_id(self):
		for record in self:
			partner = record.env['res.partner'].search([
															('name', 'like', record.patient.name),
														],
														#order='appointment_date desc',
														limit=1,)
			record.partner_id = partner



# ----------------------------------------------------------- Create Service (Recommendation) -----

	# Create Service
	@api.multi
	def create_service(self):
		#print
		#print 'Create Service'

		# Init
		res_id = self.id
		res_model = 'openhealth.treatment'
		view_id = self.env.ref('openhealth.treatment_2_form_view').id
		#print view_id

		# Open
		return {
			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',
			# Window action
			'priority': 1,
			'res_id': res_id,
			'res_model': res_model,
			#'view_id': view_id,
			# Views
			#"views": [[False, "form"]],


			"views": [[view_id, "form"]],


			'view_mode': 'form',
			'target': 'current',
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': False, }
					},
			'context': {
						#'default_treatment': treatment_id,
					}
		}
	# create_service





# Create Services - Dep

# ----------------------------------------------------------- All Services - Dep ! ------------------------
	# Product
	@api.multi
	def create_service_product(self):
		#ret = reco_funcs.create_service_product(self)
		return 0

	# Co2
	@api.multi
	def create_service_co2(self):
		#ret = reco_funcs.create_service_co2(self)
		return 0

	# Quick
	@api.multi
	def create_service_quick(self):
		#ret = reco_funcs.create_service_quick(self)
		return 0

	# Excilite
	@api.multi
	def create_service_excilite(self):
		#ret = reco_funcs.create_service_excilite(self)
		return 0

	# Ipl
	@api.multi
	def create_service_ipl(self):
		#ret = reco_funcs.create_service_ipl(self)
		return 0

	# Ndyag
	@api.multi
	def create_service_ndyag(self):
		#ret = reco_funcs.create_service_ndyag(self)
		return 0

	# Medical
	@api.multi
	def create_service_medical(self):
		#ret = reco_funcs.create_service_medical(self)
		return 0

	# Cosmetology
	@api.multi
	def create_service_cosmetology(self):
		#ret = reco_funcs.create_service_cosmetology(self)
		return 0




# ----------------------------------------------------------- Reload - Dep ! ------------------------------

	# Reload
	@api.multi
	def reload(self):
		#print
		#print 'Reload'
		return {
				'type': 'ir.actions.client',
				'tag': 'reload',
		}


# ----------------------------------------------------------- Optimization - Dep ! ------------------------
	delta_1 = fields.Float(
			'Delta 1',
		)

	delta_2 = fields.Float(
			'Delta 2',
		)




# ----------------------------------------------------------- Test - Dep ? --------------------------------

	# Electronic
	#electronic_order = fields.One2many(
	#		'openhealth.electronic.order',
	#		'treatment_id',
	#	)








# ----------------------------------------------------------- Dep !!! ------------------------
	# Appointments
	#appointment_ids = fields.One2many(
	#		'oeh.medical.appointment',
	#		'treatment',
	#		string="Citas",
	#	)

	# Reservations
	#reservation_ids = fields.One2many(
	#		'oeh.medical.appointment',
	#		'treatment',
	#		string="Reserva de sala",
	#		domain=[
						#('x_machine', '!=', 'false'),
	#				],
	#		)


	# Appointments
	#nr_appointments = fields.Integer(
	#		string="Citas",
	#		compute="_compute_nr_appointments",
	#)
	#@api.multi
	#def _compute_nr_appointments(self):
	#	for record in self:
	#		record.nr_appointments = self.env['oeh.medical.appointment'].search_count([
	#																					('treatment', '=', record.id),
	#																					#('x_target', '=', 'doctor'),
	#																])








# 17 Sep 2019
#
# All Testing is now done by Pricelist


from . import test_foo
from . import test_treatment


# ----------------------------------------------------------- Test Flags --------------------------

	# Clear All
	@api.multi
	def clear_all(self):
		test_treatment.clear_all(self)

	# Set All
	@api.multi
	def set_all(self):
		test_treatment.set_all(self)



# ----------------------------------------------------------- Test Libs --------------------
	@api.multi
	def test_libs(self):
		"""
		Test Libraries
		"""

		print()
		print('Test Libs')


		# Product (Generated Names)
		lib = test_foo.LibGen()
		lib.test()
		print(lib)


		# Export TXT
		#self.electronic_order.unlink()
		#for order in self.order_ids:
		#	electronic_order = cre.create_order_electronic(self, order)
		#	lib = test_foo.LibExp(electronic_order)
		#	lib.test()
		#	print(lib)


		# Check Patient
		lib = test_foo.LibChkPatient(self.patient)
		lib.test()
		print(lib)


		# Products
		lib = test_foo.Products(self)
		lib.test()
		print(lib)


		# Reports
		lib = test_foo.Reports(self)
		lib.test()
		print(lib)


		# Patients
		lib = test_foo.Patients(self)
		lib.test()
		print(lib)


		# Payments
		lib = test_foo.Payments(self)
		lib.test()
		print(lib)

	# test_libs

# ----------------------------------------------------------- Test - Computes ---------------------
	def test_computes(self):
		print()
		print('Treatment - Computes')
		#t0 = timer()
		print(self.name)
		print(self.state)
		print(self.progress)
		print(self.vip)
		print(self.pricelist_id)
		print(self.patient_sex)
		print(self.patient_age)
		print(self.patient_city)
		print(self.x_vip_inprog)
		print(self.consultation_progress)
		#print(self.nr_appointments)
		print(self.nr_consultations)
		print(self.nr_budgets_cons)
		print(self.nr_invoices_cons)
		print(self.nr_services)
		print(self.nr_services_co2)
		print(self.nr_services_excilite)
		print(self.nr_services_ipl)
		print(self.nr_services_ndyag)
		print(self.nr_services_quick)
		print(self.nr_services_medical)
		print(self.nr_services_cosmetology)
		print(self.nr_services_vip)
		print(self.nr_services_product)
		print(self.nr_controls)
		print(self.nr_sessions)
		print(self.nr_procedures)
		#t1 = timer()
		#self.delta_1 = t1 - t0
		#print self.delta_1
	# test_computes



# ----------------------------------------------------------- Test Create Recos --------------------------------
	# Test
	def test_create_recos(self):
		#print
		#print 'Treatment - Test'
		ret = self.create_service_product()
		ret = self.create_service_co2()
		ret = self.create_service_excilite()
		ret = self.create_service_ipl()
		ret = self.create_service_ndyag()
		ret = self.create_service_quick()
		ret = self.create_service_medical()
		ret = self.create_service_cosmetology()
	# test_create_recos



# ----------------------------------------------------------- Test Integration --------------------
	@api.multi
	def test_integration(self):
		"""
		Integration Test of the Treatment Class.
		"""
		print()
		print('Test Integration')
		if self.patient.x_test:

			# Reset
			test_treatment.reset_treatment(self)

			# Test Integration
			test_treatment.test_integration_treatment(self)


# ----------------------------------------------------------- Test Reset --------------------------
	@api.multi
	def test_reset(self):
		print()
		print('Test Case - Reset')
		if self.patient.x_test:
			test_treatment.reset_treatment(self)


# ----------------------------------------------------------- Test --------------------------------
	# Test
	@api.multi
	def test(self):
		print()
		print('Treatment - Test')		
		if self.patient.x_test:
			self.test_reset()
			self.test_integration()
			self.test_create_recos()
			self.test_computes()
			#self.test_libs()








# 17 Sep 2019
#
# Update ?

# ----------------------------------------------------------- Update ------------------------------
	# Flag
	flag = fields.Boolean(
			'Flag',
		)

	# Update
	@api.multi
	def update(self):
		#print
		#print 'Update'
		self.flag = not self.flag
	# update










# 6 Sep 2019
#
# Duplication !


	x_test_scenario = fields.Selection(
			[
				('co2', 'Co2'),
				('exc', 'Exc'),
				('quick', 'Quick'),
				('ipl', 'Ipl'),
				('ndyag', 'Ndyag'),

				('all', 'All'),
			],
			string="Scenarios",
		)







# 27 Aug 2019
# Appointment is Highly Deprecated !
#




# ----------------------------------------------------------- Create Appointment  -----------------

	# Create Appointment Consultation
	@api.multi
	def create_appointment_consultation(self):

		# Consultation
		x_type = 'consultation'
		subtype = 'consultation'
		state = 'pre_scheduled'

		self.create_appointment_nex(x_type, subtype, state)

	# create_appointment_consultation




	# Create Appointment Nex
	@api.multi
	#def create_appointment_nex(self):
	def create_appointment_nex(self, x_type, subtype, state):
		#print
		#print 'Create Appointment'


		# Init
		doctor_name = self.physician.name



		# Consultation, Procedure
		if x_type in ['consultation', 'procedure']: 	# Appointment is Today. With time. So check for availability.


			# Get Next Slot - Real Time version
			appointment_date = lib.get_next_slot(self)						# Get Next Slot
			#print appointment_date


			if appointment_date != False:


				# Init
				states = False
				duration = 0.5



				# Check and Push
				#appointment_date_str = procedure_funcs.check_and_push(self, appointment_date, duration, x_type, doctor_name, states)
				#appointment_date_str = user.check_and_push(self, appointment_date, duration, x_type, doctor_name, states)
				appointment_date_str = user.check_and_push(self, appointment_date, duration, doctor_name, states)
				#print appointment_date_str



				# Create
				#print 'Create'
				#appointment = self.env['oeh.medical.appointment'].create({
				appointment = self.appointment_ids.create({
																			'appointment_date': appointment_date_str,
																			'patient':			self.patient.id,
																			'doctor':			self.physician.id,

																			#'state': 			'pre_scheduled',
																			#'x_type': 			'consultation',
																			#'x_subtype': 		'consultation',

																			'state': 			state,
																			'x_type': 			x_type,
																			'x_subtype': 		subtype,

																			'treatment':	self.id,
																	})
				#print appointment



		# Session, Control
		else: 	# Appointment is not Today. Without time.

			#print 'Appointment not Today'


			# Init
			if x_type == 'control':
				duration = 0.25
				state = 'pre_scheduled_control'
				states = ['pre_scheduled_control']
			else:
				duration = 0.5
				state = 'pre_scheduled_session'
				states = ['pre_scheduled_session']
				#state = 'pre_scheduled_control'
				#states = ['pre_scheduled_control']




			# Control
			nr_days = 0
			#nr_days = 1


			#start_date = self.start_date
			start_date = datetime.datetime.now() + datetime.timedelta(hours=-5, minutes=0)
			#date_2_format = "%Y-%m-%d"
			date_format = "%Y-%m-%d %H:%M:%S"
			start_date_str = start_date.strftime(date_format)




			# Control date
			#appointment_date = procedure_funcs.get_next_date(self, start_date_str, nr_days)
			appointment_date = lib.get_next_date(self, start_date_str, nr_days)

			#print appointment_date


			# Cut Time out
			appointment_date_str = appointment_date.strftime("%Y-%m-%d")
			appointment_date_str = appointment_date_str + ' 14:00:00'			# 09:00:00
			#print appointment_date_str



			# Check and Push
			#appointment_date_str = procedure_funcs.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)
			#appointment_date_str = user.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)
			appointment_date_str = user.check_and_push(self, appointment_date_str, duration, doctor_name, states)



			# Create
			appointment = self.env['oeh.medical.appointment'].create({
																			'appointment_date': appointment_date_str,
																			'patient':			self.patient.id,
																			'doctor':			self.physician.id,
																			'duration': duration,

																			#'x_create_procedure_automatic': False,
																			#'x_chief_complaint': chief_complaint,
																			#'x_target': 'doctor',

																			'state': state,
																			'x_type': x_type,
																			'x_subtype': subtype,

																			'treatment':	self.id,
																	})
	# create_appointment_nex





# ----------------------------------------------------------- Update Apps  ------------------------

	# Update Appointments
	@api.multi
	def update_appointments(self):

		#print
		#print 'Update Appointments'

		# Consultations
		for consultation in self.consultation_ids:
			if consultation.appointment.appointment_date != False: 
				consultation.evaluation_start_date = consultation.appointment.appointment_date

		# Sessions
		for session in self.session_ids:
			if session.appointment.appointment_date != False:
				session.evaluation_start_date = session.appointment.appointment_date

	# update_appointments
