

# 3 Oct 2017





# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):



		print 
		print 'CRUD - Treatment - Create'
		print 
		print vals



		print 'patient', self.patient.name
		print 'physicien', self.physician.name 


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

		print 'id', self.id

		print app_c 
		if app_c.id != False:
			app_c.treatment = self.id 
			print 'c id', app_c.id
			print 'treatment', app_c.treatment 


		print app_p 
		if app_p.id != False:
			app_p.treatment = self.id 
			print 'p id', app_p.id
			print 'treatment', app_p.treatment 






		# Put your logic here 
		res = super(Treatment, self).create(vals)
		# Put your logic here 

		return res

	# CRUD 










# 30 Dec 2017

	# Open 
	#treatment_open = fields.Boolean(
	#		string="Abierto",
	#		default=True,
	#)




# 28 Jun 2018


	#evaluation_ids = fields.One2many(
	#		'oeh.medical.evaluation', 
	#		'treatment_id', 
	#		string = "Evaluaciones", 
	#		)

	
	#nr_evaluations = fields.Integer(
	#		compute='_compute_nr_evaluations', 
	#		string='Nr. evaluaciones', 
	#		default = 0, 
	#		)

	#@api.depends('evaluation_ids')
	#def _compute_nr_evaluations(self):
	#	for record in self:
	#		sub_total = 0 
	#		for se in record.evaluation_ids:   
	#			sub_total = sub_total + 1  
	#		record.nr_evaluations= sub_total  


	# Update  
	#@api.multi 
	#def update_patient(self):
	#	print 
		#print 'Update Patient - Treatment'
		#self.patient_sex = self.patient.sex[0]
		#self.patient_age =  self.patient.age.split()[0]
		#self.patient_city = self.patient.city.title()
		#for consultation in self.consultation_ids: 
		#	consultation.update_patient()


	# Family 
	#x_family = fields.Selection(
	#		selection = [
	#						('product','Producto'), 
	#						('consultation','Consulta'), 
	#						('procedure','Procedimiento'), 
	#						('cosmetology','Cosmiatría'), 
	#		], 
	#		string = "Tipo",
	#	)




	#name = fields.Char(
			#string="Treatment #", 
	#		string="Tratamiento #", 
	#		required=True, 
	#		compute='_compute_name', 
	#		default='.'
	#		)

	# Number of services
	#nr_services = fields.Integer(
	#		compute='_compute_nr_services', 
			#string='Number of services', 
	#		string='Nr servicios', 
	#		default = 0, 
	#		)

	#@api.depends('service_ids')
	#def _compute_nr_services(self):
	#	for record in self:
	#		sub_total = 0 
	#		for se in record.service_ids:   
				#print se.price
	#			sub_total = sub_total + 1  
	#		record.nr_services= sub_total  
			#record.nr_services = record.service_ids.count 

	#@api.multi
	#@api.depends('service_ids')

	#def _compute_price_total(self):
	#	for record in self:
	#		sub_total = 0.0 
	#		for se in record.service_ids:   
	#			#print se.price
	#			sub_total = sub_total + se.price 
	#		record.price_total = sub_total  




	#@api.multi
	#@api.depends('start_date', 'end_date')
	#def _compute_end_date(self):
	#	for record in self:
	#		if not record.treatment_closed:
	#			record.end_date = False
	#		else:
	#			record.end_date = record.today_date


	#@api.onchange('treatment_closed')
	#def _onchange_treatment_closed(self):
	#	print 'jx'
	#	print 'On Change Treatment Closed'
	#	print self.treatment_closed
	#	print self.today_date
	#	print self.end_date
	#	if self.treatment_closed: 		
			#self.end_date = self.today_date
			#self.end_date = datetime.today().strftime('%Y-%m-%d')
	#		self.end_date = datetime.today()


	# Controls 
	# ---------
	#control_ids = fields.One2many(
			#'oeh.medical.evaluation', 
	#		'openhealth.control', 

	#		'treatment_id', 
	#		string = "Controles", 
	#		)




# 4 Jul 2018 

# ----------------------------------------------------------- Testing ------------------------------------------------------

	# Test  
	@api.multi 
	def test(self):

		print 
		print 'Testing'
		# Date 
		GMT = time_funcs.Zone(0,False,'GMT')
		#self.start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		self.start_date = datetime.now(GMT).strftime("%Y-%m-%d")

		
		# Init 
		patient_id = self.patient.id
		doctor_id = self.physician.id
		duration = 0.5
		state = 'pre_scheduled'
		x_type = 'consultation'

		#x_create_procedure_automatic = True
		x_create_procedure_automatic = False
		
		treatment_id = self.id 

		#appointment_date = self.start_date
		appointment_date = self.start_date + ' 14:00:00'			# 09:00:00


		# Appointment 
		#appointment = self.create_appointment(appointment_date, patient_id, doctor_id, duration, state, x_type, x_create_procedure_automatic, treatment_id)


		# Create
		#appointment = self.env['oeh.medical.appointment'].create({
		#appointment = self.appointment_ids.create({
		#															'appointment_date': appointment_date,
		#															'patient': patient_id,	
		#															'doctor': doctor_id,
		#															'duration': duration,
		#															'state': state,
		#															'x_create_procedure_automatic': x_create_procedure_automatic,
		#															'x_type': x_type,
																	#'x_chief_complaint': chief_complaint, 
																	#'x_target': 'doctor',

		#															'treatment': treatment_id, 
		#														})
		#print appointment
		#print self.appointment_ids




	@api.multi 
	def create_appointment(self, appointment_date, patient_id, doctor_id, duration, state, x_type, x_create_procedure_automatic, treatment_id):

		print 
		print 'Create Appointment'

		# Create
		#appointment = self.appointment_ids.create({
		appointment = self.env['oeh.medical.appointment'].create({
																	'appointment_date': appointment_date,

																	'patient': patient_id,	
																	'doctor': doctor_id,
																	'duration': duration,
																	'state': state,

																	'x_create_procedure_automatic': x_create_procedure_automatic,
																	'x_type': x_type,

																	#'x_chief_complaint': chief_complaint, 
																	#'x_target': 'doctor',

																	'treatment': treatment_id, 
																})
		#appointment_id = appointment.id

		return appointment 
	# create_appointment

