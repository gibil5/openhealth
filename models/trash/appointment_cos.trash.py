


# 3 March 2017




	#x_machine_cos = fields.Selection(
	#		string="Sala Cos", 
	#		selection = app_vars._machines_cos_list, 
			#required=True, 
	#	)


	#_hash_x_machine_cos = {
	#						False:				'', 

							#'laser_co2_1':		'C1',
							#'laser_co2_2':		'C2',
							#'laser_co2_3':		'C3',
							
	#						'laser_triactive':		'Tri',
	#						'chamber_reduction':	'Cam',
	#						'carboxy_diamond':		'CaDi',
	#					}



	#@api.multi
	#@api.depends('x_machine')
	#def _compute_x_machine_short(self):
	#	for record in self:
	#		if record.doctor.name != False:
	#			record.x_machine_short = self._hash_x_machine[record.x_machine]
	#		else:
	#			record.x_machine_short = self._hash_x_machine_cos[record.x_machine_cos]

	

	# ----------------------------------------------------------- On Change - Machine ------------------------------------------------------

	@api.onchange('x_machine_cos')

	def _onchange_x_machine_cos(self):

		print 
		print 'On change Machine - Cos'


		if self.x_machine_cos != False:	

			print self.x_machine_cos 

			print self.doctor.name
			print self.patient.name
			print self.appointment_date
			print self.x_date
			print self.duration
			print self.appointment_end

			print self.x_type  

			print 

			#self.x_error = 0



			# Check for collisions 

			#ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor.name, self.duration, self.x_machine_cos, 'machine')
			ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor.name, self.duration, self.x_machine_cos, 'therapist', self.x_type)



			if ret != 0:	# Error - Collision 


				#self.x_error = 1
				self.x_machine_cos = False

				return {
							'warning': {
									'title': "Error: Colisión !",
									'message': 'La sala ya está reservada: ' + start + ' - ' + end + '.',
						}}



			else: 			# Success 

				print 'Success !'
				print 
				



		print

	# _onchange_x_machine_cos














# 6 March 2017
	# ----------------------------------------------------------- On Change - Patient Therapist ------------------------------------------------------

	@api.onchange('patient','x_therapist')
	def _onchange_patient_therapist(self):

		print 
		print 'jx'
		print 'On Change PT'

		if self.patient != False and self.x_therapist != False:
				

			cosmetology = self.env['openhealth.cosmetology'].search([
																				('patient', 'like', self.patient.name),
																				('therapist', 'like', self.x_therapist.name),
																			],
																				order='start_date desc',
																				limit=1,
																			)
			self.cosmetology = cosmetology

			print 'jx'

		# _onchange_patient_therapist



	# ----------------------------------------------------------- On Change - Therapist ------------------------------------------------------


	@api.onchange('x_therapist')

	def _onchange_x_therapist(self):

		print 
		print 'jx'
		print 'On change - Therapist'

		print self.x_therapist.name



		if self.x_therapist.name != False:

			print self.x_therapist.name
			print self.patient.name
			print self.appointment_date
			print self.x_date
			print self.duration
			print self.appointment_end

			print self.x_type  
			print 

			#self.x_error = 0




			# Check for collisions
			ret = 0 

			#ret, x_therapist_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.x_therapist.name, self.duration, False, 'therapist')
			ret, x_therapist_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.x_therapist.name, self.duration, False, 'therapist', self.x_type)

			print ret 




			if ret != 0:	# Error 

				print 'Error: Collision !'
				print 


				#self.x_error = 1
				self.x_therapist = False

				return {
							'warning': {
									'title': "Error: Colisión !",
									'message': 'Cita ya existente, con la Cosmeatra ' + x_therapist_name + ": " + start + ' - ' + end + '.',
						}}


			else: 			# Success  

				print 'Success !'
				print 


		print 

	# _onchange_x_therapist







