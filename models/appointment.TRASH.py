

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









