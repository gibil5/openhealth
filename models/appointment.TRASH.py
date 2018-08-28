

# 1 Dec 2017


	#@api.multi
	#@api.depends('patient', 'doctor')
	#def _compute_treatment(self):
	#	for record in self:
	#		if record.patient != False and record.doctor != False:
				#treatment = self.env['openhealth.treatment'].search([
				#																('patient', 'like', self.patient.name),
				#																('doctor', 'like', self.doctor.name),
				#															],
				#																order='start_date desc',
				#																limit=1,
				#															)
				#record.treatment = treatment
				#record.treatment.id = 3
	#			#print 'jx'







	@api.onchange('patient','doctor')
	def _onchange_patient_doctor(self):

		if self.patient != False and self.doctor != False:
			

			if self.x_target == 'doctor': 	
				
				treatment = self.env['openhealth.treatment'].search([
																				('patient', 'like', self.patient.name),
																				
																				('physician', 'like', self.doctor.name),
																			
																			],
																				order='start_date desc',
																				limit=1,
																			)
				self.treatment = treatment



			else: 

				cosmetology = self.env['openhealth.cosmetology'].search([
																				('patient', 'like', self.patient.name),
																				
																				('physician', 'like', self.doctor.name),
																			
																			],
																				order='start_date desc',
																				limit=1,
																			)
				self.cosmetology = cosmetology
			


			#print 

	# _onchange_patient_doctor





	treatment = fields.Many2one(			
			'openhealth.treatment',
			string="Tratamiento",
			ondelete='cascade', 

			#required=False, 
			required=True, 

			#compute='_compute_treatment', 
		)


	@api.multi
	@api.depends('patient', 'doctor')
	def _compute_treatment(self):
		for record in self:
			if record.patient.name != False and record.doctor.name != False:	
				tre = self.env['openhealth.treatment'].search([
																	('patient', '=', record.patient.name),
																	('physician', '=', record.doctor.name),
															],
																order='start_date desc',
																limit=1,
																)
				#tre = False 
				record.treatment = tre






	#@api.multi 
	#def get_x_target(self):
	#	return self.x_target


	#x_target = 'therapist'

	#x_target = get_x_target
	#x_target = self.x_target




	#@api.multi
	#def _compute_x_type(self):
	#	for record in self:
	#		record.x_type = record.x_target




	#x_tree = fields.Boolean(
	#	)





	#@api.onchange('x_type')
	#def _onchange_x_type(self):
	#	if self.x_type != False:	
	#		if self.x_type == 'consultation'  or  self.x_type == 'procedure':
	#			self.x_duration_min = '0.5'
	#		elif self.x_type == 'control':
	#			self.x_duration_min = '0.25'







	#@api.onchange('x_duration_min')
	#def _onchange_x_duration_min(self):
	#	if self.x_duration_min != False:	
			#self.duration = self._hash_duration[self.x_duration_min]
	#		self.duration = self._hash_duration[self.x_duration_min]







	#@api.multi
	#@api.depends('start_date')

	#def _compute_name(self):
	#	#print 'compute name'
	#	for record in self:
	#		idx = record.id
	#		if idx < 10:
	#			pre = 'AP000'
	#		elif idx < 100:
	#			pre = 'AP00'
	#		elif idx < 1000:
	#			pre = 'AP0'
	#		else:
	#			pre = 'AP'
	#		record.name =  pre + str(idx) 
	#	#print self.name 
	#	#print 




	#default_doctor_id = fields.Integer(
	#		default=1, 
	#)



	# Chief complaint 		# DEPRECATED 
	x_chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 
			selection = eval_vars._chief_complaint_list, 
			)

	@api.onchange('x_chief_complaint')
	def _onchange_x_chief_complaint(self):
		if self.x_chief_complaint != False:	
			t = self.env['openhealth.treatment'].search([
																('chief_complaint', 'like', self.x_chief_complaint), 
																('patient', 'like', self.patient.name),
																('physician', 'like', self.doctor.name),
															],
															order='start_date desc',
															limit=1,
														)
			if len(t) == 1:
				self.treatment = t.id
			else:
				tra = 1 









	#@api.onchange('x_type')
	#def _onchange_x_type(self):
	#	self.x_type_cal = self._type_cal_dic[self.x_type]









	#APPOINTMENT_STATUS_PROXY = [
	#								('pre_scheduled', 	'No confirmado'),
	#								('Scheduled', 		'Confirmado'),
	#							]
	#x_state_proxy = fields.Selection(
	#		selection = APPOINTMENT_STATUS_PROXY, 
	#	)








	#x_error = fields.Integer(			
	#		default = 0, 
	#		required=True, 
	#	)




# 27 June 2018 


	# Machine 
	#x_machine = fields.Selection(
	#		string="Sala", 
	#		selection = app_vars._machines_list, 
			#required=True, 
	#	)


	# On change - Machine
	#@api.onchange('x_machine')
	#def _onchange_x_machine(self):
	#	if self.x_machine != False:	
	#		self.x_error = 0

			# Check for collisions 
	#		ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor.name, self.duration, self.x_machine, 'machine', self.x_type)

	#		if ret != 0:	# Error 
	#			self.x_error = 1
	#			self.x_machine = False
	#			return {
	#						'warning': {	'title': "Error: Colisión !",
	#										'message': 'La sala ya está reservada: ' + start + ' - ' + end + '.',
	#					}}
	#		else: 			# Success 				
				# Treatment 
	#			self.treatment = self.env['openhealth.treatment'].search([
	#																		('patient', 'like', self.patient.name),
	#																		('physician', 'like', self.doctor.name),
	#																		],
	#																		order='start_date desc',
	#																		limit=1,
	#													)
				#print self.treatment 
		#print



	# X Time 
	#x_time = fields.Char(
	#		string="Hora", 

	#		compute="_compute_x_time",
	#	)

	#@api.multi
	#@api.depends('appointment_date')
	#def _compute_x_time(self):
	#	date_format = "%Y-%m-%d %H:%M:%S"
	#	for record in self:
	#		dt = datetime.datetime.strptime(record.appointment_date, date_format)
	#		delta = datetime.timedelta(hours=5)
	#		dt = dt - delta
	#		record.x_time = dt.strftime("%H:%M:%S")
	#		if record.state == 'pre_scheduled_control':
	#			record.x_time = ''


	# Duration
	#_hash_duration = {
	#				'0.25' 	: 0.25, 
    #				'0.5' 	: 0.5, 
     				#'0.75' 	: 0.75, 
     				#'1.0' 	: 1.0, 
     				#'2.0' 	: 2.0, 
	#			}


     # Duration min 
	#x_duration_min = fields.Selection(

	#		selection = app.vars._duration_list, 

	#		string="Duración (min)", 
		
			#default = '0.5',
			#default = '0.25',
			#readonly=True,
	#	)


	# Colors 
	#color_patient_id = fields.Integer(
	#		default=2,
	#	)


	# Color Doctor id 
	#_hash_colors_doctor = {
	#		'Dra. Acosta': 1,
	#		'Dr. Canales': 2,
	#		'Dr. Chavarri': 3,
	#		'Dr. Escudero': 4,
	#		'Dr. Gonzales': 5,
	#		'Dr. Vasquez': 6,
	#	}


	#color_doctor_id = fields.Integer(
	#		default=1,

	#		compute='_compute_color_doctor_id', 
	#	)

	#@api.multi
	#@api.depends('doctor')
	#def _compute_color_doctor_id(self):
	#	for record in self:	
	#		record.color_doctor_id = self._hash_colors_doctor[record.doctor.name]



	# Color x_type id 
	#color_x_type_id = fields.Integer(
	#		default=1,

	#		compute='_compute_color_x_type_id', 
	#	)

	#@api.multi
	#@api.depends('x_type')
	#def _compute_color_x_type_id(self):
	#	for record in self:	
	#		if record.x_type == 'procedure'   and   record.state == 'Pre-scheduled':
				#print 'Gotcha !!!'
	#			record.color_x_type_id = app_vars._hash_colors_x_type['procedure_pre_scheduled']
	#		else:
	#			record.color_x_type_id = app_vars._hash_colors_x_type[record.x_type]













	
	# Target 
	#x_target = fields.Selection(
	#		string="Target", 

			#selection = app_vars._target_list, 
			
	#		index=True,
	#		required=True, 
	#	)


	#@api.onchange('x_target')
	#def _onchange_x_target(self):
	#	if self.x_target == 'therapist':	
			#self.x_machine = [
			#					('laser_triactive','Triactivo'), 
			#					('chamber_reduction','Cámara de reducción'), 
			#					('carboxy_diamond','Carboxiterapia - Punta de Diamante'), 								
			#				]
			#return {
			#			'domain': 	{	'x_machine': [
			#											#('x_pathology', '=', self.pathology)
			#											('x_zone', '=', self.zone),
			#										]
			#						},
			#}





	# X Date 
	#x_date = fields.Date(
	#		string="Fecha", 

	#		compute="_compute_x_date",
	#	)

	#@api.multi
	#@api.depends('appointment_date')
	#def _compute_x_date(self):
	#	date_format = "%Y-%m-%d %H:%M:%S"
	#	for record in self:
	#		dt = datetime.datetime.strptime(record.appointment_date, date_format)
	#		record.x_date = dt.strftime("%Y-%m-%d")



	#_h_duration = {
	#				(0.25,0.25):	0.25,
	#				(0.5,0.5):		0.5,
	#				(0.45,0.45):	0.45,
	#				(1,1):			1,
	#			}	
	#duration_sel = fields.Selection(
	#		string="Duración (h)",	
	#		selection = [
	#						(0.25,0.25), 
	#						(0.5,0.5), 
	#						(0.45,0.45), 
	#						(1,1), 
	#					],
	#		default=0.5, 
	#	)

	#@api.onchange('duration_sel')
	#def _onchange_duration_sel(self):
	#	if self.duration_sel != False:	
			#self.duration = self._h_duration[self.duration_sel]
			#self.duration = self.duration_sel

	

		# State 
	#APPOINTMENT_STATUS = [			
	#		('pre_scheduled',	 		'No confirmado'),
	#		('Scheduled', 				'Confirmado'),
			#('pre_scheduled_control', 	'Pre-cita'),
	#		('pre_scheduled_control', 	'Sin Hora (Control)'),


			#('event', 					'Evento'),
			#('invoiced', 				'Facturado'),
			#('error', 					'Error'),
			#('completed', 				'Completo'),

			# Oe Health 
			#('Scheduled', 'Scheduled'),
			#('Completed', 'Completed'),
			#('Invoiced', 'Invoiced'),
	#	]



	#@api.onchange('x_type')
	#def _onchange_x_type(self):
	#	print
	#	print 'On change type'
	#	self.duration = 0.5
		#if self.x_type == 'event': 
		#	print 'Type equal event'
		#	self.state = 'event'





# 28 Aug 

# ----------------------------------------------------------- Deprecated ------------------------------------------------------

	#x_target = fields.Char()

	#x_machine = fields.Char()

	# Create procedure Flag 
	#x_create_procedure_automatic = fields.Boolean(
	#		string="¿ Cita para Procedimiento ?",
	#		default=False, 
	#	)


# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Write 
	#@api.model
	#def write(self,vals):

	#	print 
	#	print 'Appointment - Write'


		#Write your logic here
	#	res = super(Appointment, self).write(vals)
		#Write your logic here

		#print res.control
		#print res.appointment_date
		#res.control.update_dates(res.appointment_date)

	#	return res
	# CRUD - Write 



# ----------------------------------------------------------- CRUD ------------------------------------------------------
	# Create 
	@api.model
	def create(self,vals):

		#print
		#print 'Appointment - Create'

		# Super 
		#print 'mark'
		res = super(Appointment, self).create(vals)
		#print 'mark'

		# Init 
		appointment_date = res.appointment_date
		x_type = res.x_type
		doctor_id = res.doctor.id
		patient_id = res.patient.id
		treatment_id = res.treatment.id
		
		#x_create_procedure_automatic = res.x_create_procedure_automatic


		# Create Procedure Flag - Deprecated
		#if x_type == 'consultation'  and  x_create_procedure_automatic:
		#	date_format = "%Y-%m-%d %H:%M:%S"
		#	adate_con = datetime.datetime.strptime(appointment_date, date_format)
		#	delta_fix = datetime.timedelta(hours=1.5)
		#	adate_base = adate_con + delta_fix
		#	app = appfuncs.create_appointment_procedure(self, adate_base, doctor_id, patient_id, treatment_id, x_create_procedure_automatic)

		return res
	# create
# CRUD


