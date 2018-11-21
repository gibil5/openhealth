
	# Two - Unit - Appointment
	@api.multi 
	def test_case_two(self):
		print 
		print 'Test Case - Two'
		if self.patient.x_test: 
			tst.test_appointment(self)


	# Three - Reset 
	@api.multi 
	def test_case_reset(self):
		#print 
		#print 'Test Case - Reset'
		if self.patient.x_test: 
			#print 'Is a Tester'
			tst.reset_treatment(self)
		else: 
			print 'Not a Tester'

	# Four - Reload
	@api.multi 
	def test_case_reload(self):
		#print 
		#print 'Test Case - Reload'
		self.reload()




# ----------------------------------------------------------- Test Integration Objects ------------
	# Objects - Integration
	@api.multi 
	def test_case_objs(self):
		"""
		Integration Test of an Object.
		"""
		print
		print 'Test Case - Obj'
		
		if self.patient.x_test: 

			# Init 
			patient_id = self.patient.id
			doctor_id = self.physician.id
			treatment_id = self.id 
			partner_id = self.partner_id.id			
			pl_id = self.patient.property_product_pricelist.id   	# Pricelist 
			caller = self 											# Caller 

			# Objects 
			order = 	lib_obj.Object(	caller, 'order', 	'sale.order', 			patient_id, partner_id, doctor_id, 	treatment_id, 	pl_id)
			patient = 	lib_obj.Object(	caller, 'patient', 	'oeh.medical.patient', 	False, 		False, 		doctor_id, 	False, 			False)


			# All  
			objs = [
						order, 
						patient, 
				]

			# Test  
			for obj in objs: 
				obj.test()
			print 

			# Print 
			for obj in objs: 
				print obj

	# test_case_objs






# ----------------------------------------------------------- Test Integration - Order ------------
	#  Objects - Integration
	@api.multi 
	def test_case_order(self):
		"""
		Integration Test of the Sale Order Class.
		"""
		print
		print 'Test Case - Order'
		if self.patient.x_test: 

			# Init
			patient_id = self.patient.id
			doctor_id = self.physician.id
			treatment_id = self.id
			partner_id = self.partner_id.id
			pl_id = self.patient.property_product_pricelist.id   	# Pricelist
			caller = self 											# Caller


			# Objects
			order = lib_obj.Object(caller, 'order', 'sale.order', patient_id, partner_id, doctor_id, treatment_id, pl_id)


			# All  
			objs = [
						order, 
				]

			# Test  
			for obj in objs: 
				obj.test()

			# Print
			for obj in objs:
				print obj
	# test_case_order




# ----------------------------------------------------------- Testing - Consu ------------------------------------------------------
	# Consu
	@api.multi 
	def test_case_consu(self):
		print
		print 'Test Case - Consu'

		# Init 


		# Search 
		products = self.env['product.template'].search([
															#('type','in', ['consu']),
															('sale_ok','not in', ['True']),
														],
													#order='name asc',
													#limit=1,
													#limit=10,
													#limit=100,
													#limit=120,
												)

		count = self.env['product.template'].search_count([
															#('type','in', ['consu']),
															('sale_ok','not in', ['True']),
													])


		print 'Products: \t', products
		print 
		print 'Count: \t', count 
		print 


		# Not Sale Ok Must be Consu !
		# Consu Must be Inactive !
		for product in products: 
			print product.name 
			print product.sale_ok

			if product.sale_ok == False: 
				product.type = 'consu'

			if product.type == 'consu': 
				product.active = False

			print product.type 
			print product.active 


			print 






# ----------------------------------------------------------- Testing - Products ------------------------------------------------------
	# Prods
	@api.multi 
	def test_case_products(self):
		print
		print 'Test Case - Products'

		# Init 
		se = ' - '
		eol = 'x'

		#families = ['cosmetology']
		#treatments = ['laser_excilite', 'laser_ipl']
		#treatments = ['laser_excilite']
		#treatments = ['laser_ipl']
		#treatments = ['laser_ndyag']


		treatments = ['laser_quick']


		# Search 
		products = self.env['product.template'].search([
															('type','in', ['service']),

															('x_treatment','in', treatments),

															#('x_family','in', families),
														],
													#order='name asc',
													#limit=1,
													#limit=10,
													limit=100,
													#limit=120,
												)
		print products
		print 

		# Products 
		for product in products: 


			# Quick 
			if product.x_treatment in ['laser_quick']: 			# Standardize Shortname
				#print 'Quick'

				# Array Short Name
				arr_sho = product.x_name_short.split('_')

				# Array Name
				arr_nam = product.name.split('-')


				# Correct the Name 
				if len(arr_nam) == 4: 			# To avoid repetition 

					name = product.name
					name_old = name 

					for tup in [ 
									('1', '5 min - 1'), 
									('2', '15 min - 1'), 
									('3', '30 min - 1'), 
									('4', '45 min - 1'), 
								]: 

						old = tup[0]
						new = tup[1]
						#print old 
						#print new 

						name = name.replace(old, new)

					print name_old
					print name
					print 


					# Change 
					product.name = name





				# Correct the Short Name 
				if len(arr_sho) == 4: 			# To avoid repetition 

					short = product.x_name_short
					short_old = short 

					#print short

					for tup in [ 
									#('quick', 'qui'), 
									#('face_all_hands', 'faa-han'), ('face_all_neck', 'faa-nec'), ('neck_hands', 'nec-han'), 
									#('body_local', 'bol'), ('face_local', 'fal'), ('face_all', 'faa'), 
									#('hands', 'han'), ('neck', 'nec'), ('cheekbones', 'che'), 
									#('rejuvenation', 'rej'), ('acne_sequels', 'acs'), ('scar', 'sca'), 
									#('mole', 'mol'), ('stains', 'sta'), ('keratosis', 'ker'), ('cyst', 'cys'),
									#('tatoo', 'tat'), ('wart', 'war'), 

									('1', '5m_one'), 
									('2', '15m_one'), 
									('3', '30m_one'), 
									('4', '45m_one'), 
								]: 
						
						old = tup[0]
						new = tup[1]
						#print old 
						#print new 

						short = short.replace(old, new)

					
					print short_old
					print short
					print 

					# Change  
					product.x_name_short = short 




			# Exc, Ipl, Ndyag 
			elif product.x_treatment in ['laser_excilite', 'laser_ipl', 'laser_ndyag']: 		# Swap Sessions and Time 
				print 'Exc, Ipl or Ndy'
				name = product.name 
				arr = name.split(' - ')
				tre = arr[0]
				zone = arr[1]
				patho = arr[2]
				sess = arr[3]
				time = arr[4]

				print tre 
				print zone 
				print patho 
				print sess
				print time 

				if sess in ['1', '6', '12']: 
					print 'Gotcha'
					print product 
					print product.name + eol
					name = tre + se + zone + se + patho + se + time + se + sess  
					product.name = name 
					print product.name + eol
				print 



# ----------------------------------------------------------- Testing - Coder ------------------------------------------------------
	# Coder
	@api.multi 
	def test_case_coder(self):
		print
		print 'Test Case - Coder'


		# Search 
		products = self.env['product.template'].search([
															#('type','in', ['product']),
															('type','in', ['service']),
															('x_treatment','in', ['laser_co2']),
														],
													#order='appointment_date desc',
													#limit=1,
													limit=101,
													)
		print products
		print 


		# Products 
		for product in products: 
		
			if product.x_coder.name == False: 			# Does not have a Coder 

				#name = product.name 
				name = product.name[:-4]

				print product 
				print product.name
				print name + '_eol'
				

				# Search 
				coder = self.env['openhealth.coder'].search([
																('name','in', [name]),
															],
														#order='appointment_date desc',
														limit=1,
														)


				
				if coder.name != False: 			# There is a Coder with this Name 
					
					print 'Gotcha !'
					print coder 			

					product.name = name 

					product.x_coder = coder 
					product.x_code = coder.code
					coder.product = product 


				else:
					product.x_coder = False


				print 




# ----------------------------------------------------------- Testing - Export ------------------------------------------------------
	# Export 
	@api.multi 
	def test_case_export(self):
		print
		print 'Test Case - Export'
		
		if self.patient.x_test: 


			# Search 
			mgt = self.env['openhealth.management'].search([
																('name','=', 'Hoy'),
														],
														#order='appointment_date desc',
														limit=1,)

			# Update
			mgt.update_electronic()


			# Export
			export.export_txt(mgt.electronic_order)




# ----------------------------------------------------------- Testing - Containers ------------------------------------------------------

	container = fields.Many2one(
			'openhealth.container', 
		)


	x_object = fields.Many2one(
			lib_obj.Object, 
		)




# ----------------------------------------------------------- Testing - Patient - Test ------------------------------------------------------
	#  Objects - Integration
	@api.multi 
	def test_case_container(self):
		print
		print 'Test - Container'
		#print self 

		# Create 
		self.container = self.env['openhealth.container'].create({
																	'name': 'Tester',
												})

		# Init 
		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id 
		partner_id = self.partner_id.id			
		#pl_id = self.patient.property_product_pricelist.id   	# Pricelist 

		# Init Container
		#pat_array = self.container.my_init(self.patient, self.partner_id, self.physician, self.id)
		self.container.my_init(self.patient, self.partner_id, self.physician, self.id)


		#simple = lib_obj.Simple('My Name')
		#print simple
		#print simple.whoami()
		#print 'mark 1'
		#print 


		#print 'mark 2'
		#print self.container



		# Init 
		#patient_id = self.patient.id
		#doctor_id = self.physician.id
		#treatment_id = self.id 
		#partner_id = self.partner_id.id			
		#pl_id = self.patient.property_product_pricelist.id   	# Pricelist 

		# Init Container
		#pat_array = self.container.my_init(self.patient, self.partner_id, self.physician, self.id)


		#print pat_array
		#print self.container.patient_ids
		#print 'mark 3'
		#print 

	# test_case_patients_order



# ----------------------------------------------------------- Testing - Patient - Create ------------------------------------------------------
	#  Objects - Integration
	@api.multi 
	def test_case_patients(self):
		print
		print 'Test Case - Patient'
		
		if self.patient.x_test: 

			# Init 
			patient_id = self.patient.id
			doctor_id = self.physician.id
			treatment_id = self.id 
			partner_id = self.partner_id.id			
			pl_id = self.patient.property_product_pricelist.id   	# Pricelist 
			caller = self 											# Caller 



			# Init 
			patient = lib_obj.Object(	caller, 'patient', 	'oeh.medical.patient', 	False, 		False, 		doctor_id, 	False, 			False)
			
			#self.x_object = lib_obj.Object(	caller, 'patient', 	'oeh.medical.patient', 	False, 		False, 		doctor_id, 	False, 			False)
			#self.container.obj = lib_obj.Object(	caller, 'patient', 	'oeh.medical.patient', 	False, 		False, 		doctor_id, 	False, 			False)




			# Print 
			print 
			print 'Print'
			print patient 
			#print self.x_object

			print 
			print 'Who'
			print patient.whoami()
			#print self.x_object.whoami()



			# All  
			#obj_arr = [
						#patient, 
						#self.x_object, 
			#		]

			# Test  
			#for obj in obj_arr: 
			#	print 
				#obj.test()
			#print 

			#print 
			#print 'Print'
			#for obj in obj_arr: 
			#	print obj



	# test_case_patient









# ----------------------------------------------------------- State ------------------------------------------------------
	@api.multi
	#@api.depends('consultation_ids')
	def _compute_state(self):
		for record in self:

			# Init 
			state = 'empty'


			if record.nr_appointments > 0:
				state = 'appointment'

			if record.nr_budgets_cons > 0:
				state = 'budget_consultation'

			if record.nr_invoices_cons > 0:
				state = 'invoice_consultation'

			if record.consultation_progress == 100:
				state = 'consultation'

			if record.nr_services > 0:
				state = 'service'

			if record.nr_budgets_pro > 0:
				state = 'budget_procedure'

			if record.nr_invoices_pro > 0:
				state = 'invoice_procedure'

			if record.nr_procedures > 0:
				state = 'procedure'

			if record.nr_sessions > 0:
				state = 'sessions'

			if record.nr_controls > 0:
				state = 'controls'

			if record.treatment_closed:
				state = 'done'


			record.state = state
	# _compute_state






# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	
	# Orders 
	#nr_orders = fields.Integer(
	#		string="Presupuestos",

	#		compute="_compute_nr_orders",
	#)
	#@api.multi
	#def _compute_nr_orders(self):
	#	for record in self:
	#		ctr = 0 			
	#		for c in record.consultation_ids:
	#			for o in c.order:
	#				ctr = ctr + 1
	#		record.nr_orders = ctr





# ----------------------------------------------------------- Recommendation - Deprecated ------------------------------------------------------

	#recommendation_ids = fields.One2many(
	#		'openhealth.recommendation', 
	#		'treatment', 
	#		string = "Recomendaciones", 
	#	)

	#recommendation = fields.Many2one(
	#		'openhealth.recommendation', 
	#		string = "Recomendacion", 
	#	)


# ----------------------------------------------------------- Create Service - Dep ------------------------------------------------------
	# Create Service 
	@api.multi
	def create_service_dep(self):

		#print 
		#print 'Open Service Selector'

		treatment_id = self.id

 		if self.recommendation.name == False: 
 			#print 'Create'
			self.recommendation = self.env['openhealth.recommendation'].create({
																					'treatment': 	self.id, 	
				})
		
		res_id = self.recommendation.id 

		return {
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action 

			'res_id': res_id,
			'res_model': 'openhealth.recommendation',
			
			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 
			'flags': {
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': False, }
					},			
			'context': {
							'default_treatment': treatment_id,					
					}
		}
	# create_service




# ----------------------------------------------------------- Tmp  ------------------------------------------------------

	#nr_quick_hands = fields.Char()
	#nr_quick_body_local = fields.Char()
	#nr_quick_face_local = fields.Char()
	#nr_quick_cheekbones = fields.Char()
	#nr_quick_face_all = fields.Char()
	#nr_quick_face_all_hands = fields.Char()
	#nr_quick_face_all_neck = fields.Char()
	#nr_quick_neck = fields.Char()
	#nr_quick_neck_hands = fields.Char()



# ----------------------------------------------------------- Quick Nr Ofs ------------------------------------------------------

	# Quick Hands
	nr_quick_hands = fields.Integer(
			string='Manos', 
			default=11, 

			compute='_compute_nr_quick_hands', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_hands(self):
		for record in self:
			record.nr_quick_hands = record.patient.x_nr_quick_hands



	# Quick Body Local
	nr_quick_body_local = fields.Integer(
			string='Localizado Cuerpo', 
			default=11, 

			compute='_compute_nr_quick_body_local', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_body_local(self):
		for record in self:
			record.nr_quick_body_local = record.patient.x_nr_quick_body_local


	# Quick Face Local
	nr_quick_face_local = fields.Integer(
			string='Localizado Rostro', 
			default=11, 

			compute='_compute_nr_quick_face_local', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_face_local(self):
		for record in self:
			record.nr_quick_face_local = record.patient.x_nr_quick_face_local



	# Quick cheekbones
	nr_quick_cheekbones = fields.Integer(
			string='Pómulos', 
			default=11, 

			compute='_compute_nr_quick_cheekbones', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_cheekbones(self):
		for record in self:
			record.nr_quick_cheekbones = record.patient.x_nr_quick_cheekbones


	# Quick face_all
	nr_quick_face_all = fields.Integer(
			string='Todo Rostro', 
			default=11, 

			compute='_compute_nr_quick_face_all', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_face_all(self):
		for record in self:
			record.nr_quick_face_all = record.patient.x_nr_quick_face_all



	# Quick face_all_hands
	nr_quick_face_all_hands = fields.Integer(
			string='Todo Rostro Manos', 
			default=11, 

			compute='_compute_nr_quick_face_all_hands', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_face_all_hands(self):
		for record in self:
			record.nr_quick_face_all_hands = record.patient.x_nr_quick_face_all_hands



	# Quick face_all_neck
	nr_quick_face_all_neck = fields.Integer(
			string='Todo Rostro Cuello', 
			default=11, 

			compute='_compute_nr_quick_face_all_neck', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_nr_quick_face_all_neck(self):
		for record in self:
			record.nr_quick_face_all_neck = record.patient.x_nr_quick_face_all_neck



	# Quick neck
	nr_quick_neck = fields.Integer(
			string='Cuello', 
			default=11, 

			compute='_compute_nr_quick_neck', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_nr_quick_neck(self):
		for record in self:
			record.nr_quick_neck = record.patient.x_nr_quick_neck



	# Quick neck_hands
	nr_quick_neck_hands = fields.Integer(
			string='Cuello Manos', 
			default=11, 

			compute='_compute_nr_quick_neck_hands', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_nr_quick_neck_hands(self):
		for record in self:
			record.nr_quick_neck_hands = record.patient.x_nr_quick_neck_hands





	



# ----------------------------------------------------------- Constants ------------------------------------------------------

	# States 
	READONLY_STATES = {
		'empty': 		[('readonly', False)], 
		#'done': 		[('readonly', True)], 	
	}


	READONLY_STATES = {
		#'purchase': [('readonly', True)],
		#'cancel': [('readonly', True)],
		'done': 	[('readonly', True)],
		#'service': 	[('readonly', True)],
	}


# ----------------------------------------------------------- Vars ------------------------------------------------------


	# User 
	user_id = fields.Many2one(
			'res.users', 
			string='Salesperson', 
			index=True, 
			track_visibility='onchange', 
			default=lambda self: self.env.user, 
			readonly=True, 
			states=READONLY_STATES, 
		)





	# Order 
	#order = fields.One2many(
	#		'sale.order',
	#		'treatment', 
	#		)

	# Quotations 
	#quotation_ids = fields.One2many(
	#		'sale.order',			 
	#		'treatment', 			
	#		string="Presupuestos",
	#		domain = [
						#('state', '=', 'pre-draft'),
						#('state', 'in', ['draft', 'sent', 'sale', 'done'])
						#('x_family', '=', 'private'),
	#				],
	#		)

	# Sales 
	#sale_ids = fields.One2many(
	#		'sale.order',			 
	#		'treatment', 
	#		string="Ventas",
	#		domain = [
						#('state', '=', 'sale'),
	#					('state', 'in', ['sale', 'done'])
	#				],
	#		)




# ----------------------------------------------------------- Duplications ------------------------------------------------------
	# Nr Procedures 
	#nr_procedures = fields.Integer(
	#		default = 0, 

	#		compute='_compute_nr_procedures', 
	#	)

	#@api.depends('procedure_ids')
	#def _compute_nr_procedures(self):
	#	for record in self:
	#		sub_total = 0 
	#		for co in record.procedure_ids:   
	#			sub_total = sub_total + 1  
	#		record.nr_procedures = sub_total  

	# Consultations 
	#nr_consultations = fields.Integer(
	#		default = 0, 

	#		compute='_compute_nr_consultations', 
	#	)

	#@api.depends('consultation_ids')
	#def _compute_nr_consultations(self):
	#	for record in self:
	#		sub_total = 0 
	#		for co in record.consultation_ids:   
	#			sub_total = sub_total + 1  
	#		record.nr_consultations = sub_total  

	# Number of appointments
	#nr_appointments = fields.Integer(
	#			string="Citas",
				
	#			compute="_compute_nr_appointments",
	#)

	#@api.multi
	#def _compute_nr_appointments(self):
	#	for record in self:
	#		ctr = 0 
	#		for c in record.appointment_ids:
	#			ctr = ctr + 1		
	#		record.nr_appointments = ctr



# ----------------------------------------------------------- Actions ------------------------------------------------------
	
	# Update App 
	@api.multi
	def update_appointment(self, appointment_id, procedure_id, x_type):
		ret = treatment_funcs.update_appointment_go(self, appointment_id, procedure_id, x_type)

	# Clean procedures
	@api.multi
	def clean_procedures(self):
		self.procedure_ids.unlink()

			


# ----------------------------------------------------------- Alta ------------------------------------------------------

	# End 
	end_date = fields.Date(
			string="Fecha fin", 
			default = False, 
		)


	# Today 
	today_date = fields.Date(
			string="Fecha hoy", 
			default = fields.Date.today, 

			compute='_compute_today_date', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_today_date(self):
		for record in self:
			#record.today_date = datetime.today().strftime("%m/%d/%Y")
			record.today_date = datetime.today().strftime('%Y-%m-%d')



	# Duration 
	duration = fields.Integer(
			#string="Días", 
			default = 0,

			#compute='_compute_duration', 
		)


	@api.multi
	#@api.depends('start_date', 'end_date')

	def _compute_duration(self):
		print 
		print 'jx'
		print 'Compute Duration'
		for record in self:
			print record.start_date
			print record.today_date
			print 
			date_format = "%Y-%m-%d"
			a = datetime.strptime(record.start_date, date_format)
			b = datetime.strptime(record.today_date, date_format)
			
			#if record.treatment_open:
			#if not record.treatment_closed:
			#	if record.today_date != False: 
			#		b = datetime.strptime(record.today_date, date_format)
			#else:
			#if record.treatment_closed:
			#	if record.end_date != False: 
			#		b = datetime.strptime(record.end_date, date_format)

			delta = b - a
			record.duration = delta.days + 1 






# ----------------------------------------------------------- Resets ------------------------------------------------------

	# Reset Half
	@api.multi 
	def reset_half(self):

		print 'jx'
		print 'Reset Half'

		# Unlinks
		self.service_quick_ids.unlink()
		self.service_vip_ids.unlink()
		self.service_co2_ids.unlink()
		self.service_excilite_ids.unlink()
		self.service_ipl_ids.unlink()
		self.service_ndyag_ids.unlink()
		self.service_medical_ids.unlink()				
		self.procedure_ids.unlink()
		self.session_ids.unlink()
		self.control_ids.unlink()
		#self.consultation_ids.unlink()
		#self.appointment_ids.unlink()

		# Alta 
		self.treatment_closed = False

		# Add procedures 
		self.add_procedures = False

		# Orders 
		for order in self.order_ids:			
			if order.x_family != 'consultation':
				order.remove_myself()

		# Numbers 
		self.nr_invoices_pro = 0 
	# reset_half


	# Reset Quick 
	@api.multi 
	def reset_quick(self):

		# Services 
		self.service_quick_ids.unlink()

		# Orders 
		for order in self.order_ids:
			if order.x_machine_req == 'laser_quick': 
				order.remove_myself()

	# Reset 
	@api.multi 
	def reset(self):

		# Unlinks
		self.service_quick_ids.unlink()
		self.service_vip_ids.unlink()
		self.service_co2_ids.unlink()
		self.service_excilite_ids.unlink()
		self.service_ipl_ids.unlink()
		self.service_ndyag_ids.unlink()
		self.service_medical_ids.unlink()
		self.consultation_ids.unlink()
		self.procedure_ids.unlink()
		self.session_ids.unlink()
		self.control_ids.unlink()
		self.appointment_ids.unlink()

		# Numbers 
		self.nr_invoices_cons = 0 
		self.nr_invoices_pro = 0 

		# Orders 
		for order in self.order_ids:
			order.remove_myself()

		# Alta 
		self.treatment_closed = False

		# Important
		self.patient.x_nothing = 'Nothing'

		# Add Procs 
		self.add_procedures = False 
	# reset









	# ----------------------------------------------------------- Buttons - Create - Deprecated ? ------------------------------------------------------

	@api.multi 
	def create_sessions(self):
		procedure = self.env['openhealth.procedure'].search([('treatment','=', self.id)]) 
		procedure_id = procedure.id
		return {
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Procedure Current',
			# Window action 
			'res_model': 'openhealth.procedure',
			'res_id': procedure_id,
			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			#'target': 'new',
			'target': 'current',
			'context':   {}
		}
	# create_session

	@api.multi 
	def create_controls(self):
		procedure = self.env['openhealth.procedure'].search([('treatment','=', self.id)]) 
		procedure_id = procedure.id
		return {
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Procedure Current',
			# Window action 
			'res_model': 'openhealth.procedure',
			'res_id': procedure_id,
			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			#'target': 'new',
			'target': 'current',
			'context':   {}
		}
	# create_controls













# ----------------------------------------------------------- Button - Create Budget  ------------------------------------------------------

	@api.multi 
	def create_budget(self):

		#print 'jx'
		#print 'Create Budget'


		consultation = self.env['openhealth.consultation'].search([('treatment','=', self.id)]) 
		consultation_id = consultation.id


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
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 

			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			


			#'context':   {
			#	'search_default_treatment': treatment_id,

			#	'default_patient': patient_id,
			#	'default_doctor': doctor_id,
			#	'default_treatment': treatment_id,				
			#	'default_evaluation_start_date': evaluation_start_date,
			#	'default_chief_complaint': chief_complaint,
			#	'default_appointment': appointment_id,
			#}
		}


	# create_budget 










# ----------------------------------------------------------- Button - Create New Procedure ------------------------------------------------------

	@api.multi
	def create_new_procedure(self):

		print 
		print 'jx'
		print 'Create New Procedure'


		#if self.nr_invoices_pro > 0:
		#	ret = treatment_funcs.create_procedure_go(self)


		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id 
		chief_complaint = self.chief_complaint
		evaluation_start_date = self.start_date


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Procedure Current',


			# Window action 
			'res_model': 'openhealth.procedure',
			#'res_id': order.id,


			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			'target': 'current',


			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 

			'flags': {
						#'form': {'action_buttons': True, }
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
				},			


			'context': {

						'default_patient': patient_id,
						'default_doctor': doctor_id,
						'default_treatment': treatment_id,				
						'default_chief_complaint': chief_complaint,


						'default_evaluation_start_date': evaluation_start_date,
				}
		}

	# create_new_procedure 




	# ----------------------------------------------------------- Button - Create Invoice  ------------------------------------------------------

	#@api.multi 
	#def create_invoice(self):			# Do Nothing  
		#print 'jx'
		#print 'Create Invoice'
	# create_invoice 





# ----------------------------------------------------------- Buttons ------------------------------------------------------

	# Treatment - EDIT 
	# --------------------

	@api.multi
	def open_line_current(self):  
		treatment_id = self.id 
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Treatment Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				#'res_model': 'openhealth.consultation',
				'res_id': treatment_id,
				'target': 'current',
				#'target': 'inline'.
				'flags': {
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
						},

				'context': {}
		}



	# ----------------------------------------------------- Open Appointment ------------------------------------------------------------

	# Open Appointment
	# -----------------
	@api.multi
	def open_appointment(self):  

		#print 
		#print 'open appointment'

		owner_id = self.id 
		patient_id = self.patient.id
		doctor_id = self.physician.id
		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#appointment_date = '2016-12-23 09:00:00'

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Appointment', 				
				'view_type': 'form',
				#'view_mode': 'form',			
				'view_mode': 'calendar',			
				'target': 'current',
				'res_model': 'oeh.medical.appointment',				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},
				'context': {
							'default_treatment': owner_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							#'default_x_type': owner_type,
							'default_appointment_date': appointment_date,
							}
				}





	# ----------------------------------------------------- Open Evaluation ------------------------------------------------------------
	# BUTTONS with Context
	# ----------------------

	# Button - Evaluation  
	# ----------------------
	@api.multi
	def open_evaluation_current(self):  

		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Evaluation Current',

			# Window action 
			'res_model': 'oeh.medical.evaluation',

			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			#'target': 'new',
			'target': 'current',

			'context':   {
				'search_default_treatment': treatment_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_treatment_id': treatment_id,
			}
		}




# ----------------------------------------------------------- CRUD - Write - Deprecated !!! ------------------------------------------------------

	# WTF is this ? 
	@api.multi
	def write_jx(self,vals):

		print 
		print 'CRUD - Treatment - Write'

		#Write your logic here
		res = super(Treatment, self).write(vals)
		#Write your logic here


		app_c = self.env['oeh.medical.appointment'].search([
															('patient', '=', self.patient.name), 
															('x_type', '=', 'consultation'),
															('doctor', '=', self.physician.name), 
														],
														order='appointment_date desc',
														limit=1,
													)
		app_p = self.env['oeh.medical.appointment'].search([
															('patient', '=', self.patient.name), 
															('x_type', '=', 'procedure'),
															('doctor', '=', self.physician.name), 
														],
														order='appointment_date desc',
														limit=1,
													)
		if app_c.id != False:
			if app_c.treatment.name == False: 	
				app_c.treatment = self.id 
				
		if app_p.id != False:
			if app_p.treatment.name == False: 
				app_p.treatment = self.id 

		return res
	# CRUD 




#from . import pat_vars
#from . import treatment_vars
#from datetime import tzinfo




