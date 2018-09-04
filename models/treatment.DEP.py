

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




