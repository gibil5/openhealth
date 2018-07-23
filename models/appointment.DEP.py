

	#'appointment_date': fields.datetime('Appointment Date',required=True, readonly=True,states={'Scheduled': [('readonly', False)]}),





	#def open_popup(self):
	#	return {
	#	        	'type': 'ir.actions.act_window',
	#	        	'name': 'Import Module',
	#	        	'view_type': 'form',
	#	        	'view_mode': 'form',
					#'target': 'new',
	#				'target': 'current',
	#	        	'res_model': 'oeh.medical.appointment',
		        	#'context': {
		        	#		#'default_partner_id':value, 			
		        	#		#'default_other_field':othervalues        			
		        	#		},
	#	    	}
	# open_popup






	# Search Treatment
	@api.multi
	def search_treatment(self):
		treatment = self.env['openhealth.treatment'].search([
																('patient', 'like', self.patient.name),
																('physician', 'like', self.doctor.name),
															],
															order='start_date desc',
															limit=1,
														)
		self.treatment = treatment.id



	# Create Treatment
	@api.multi
	def create_treatment(self):

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		start_date = self.appointment_date

		treatment = self.env['openhealth.treatment'].create({
																'patient': patient_id,	
																'physician': doctor_id,
																'start_date': start_date, 
															})
				
		self.treatment = treatment.id

		#print self.treatment  



# ----------------------------------------------------------- Treatment  ------------------------------------------------------


	# Button - Treatment 
	# -------------------
	@api.multi
	def open_treatment_current(self):  

		#print 
		#print 'Open Treatment'

		patient_id = self.patient.id 
		#print patient_id

		doctor_id = self.doctor.id
		#print doctor_id 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',

			# Window action 
			'res_model': 'openhealth.treatment',

			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',

			#'target': 'current',
			#'target': 'inline'.
			'target': 'new',

			'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
					},

			'context':   {
				'search_default_patient': patient_id,

				'default_patient': patient_id,

				'default_doctor': doctor_id,
			}
		}



# ----------------------------------------------------------- Cosmetology  ------------------------------------------------------
	procedure_cos = fields.Many2one('openhealth.procedure.cos',
			string="Proc. - Cos",
			#ondelete='cascade', 
		)







# ----------------------------------------------------------- Error Correction  ------------------------------------------------------

	# Number of clones  
	nr_clones = fields.Integer(
			string="nr_clones",

			compute="_compute_nr_clones",
	)

	@api.multi
	def _compute_nr_clones(self):
		for record in self:
			record.nr_clones =	self.env['oeh.medical.appointment'].search_count([
																						('appointment_date','=', record.appointment_date),
																						('doctor','=', record.doctor.name),
																					]) 
			if record.nr_clones > 1:
				#record.state = 'error'
				print 'Error'



	# Number of mac_clones  
	nr_mac_clones = fields.Integer(
			string="nr_mac_clones",
			
			compute="_compute_nr_mac_clones",
	)

	@api.multi
	def _compute_nr_mac_clones(self):
		for record in self:
			if record.x_machine != False: 
				record.nr_mac_clones =	self.env['oeh.medical.appointment'].search_count([
																							('appointment_date','=', record.appointment_date),
																							('x_machine','=', record.x_machine),
																					]) 
				if record.nr_mac_clones > 1:
					#record.state = 'error'
					print 'Error'
			else:
				record.nr_mac_clones = 1 





# ----------------------------------------------------------- Machine  ------------------------------------------------------

_hash_x_machine = {
							False:				'', 

							'laser_quick':		'Quick',					
							'criosurgery':		'Crio',
							'botulinum_toxin': 			'Botox', 
							'hyaluronic_acid': 			'Hial', 
							'hyaluronic_acid_repair': 	'Hial - R', 
							'intravenous_vitamin': 		'Vit Intra', 
							'lepismatic': 				'Lepi', 
							'mesotherapy_nctf': 		'Meso', 
							'plasma': 					'Plas', 
							'sclerotherapy': 			'Escle', 
							'chamber_reduction':	'Cam',
							'carboxy_diamond':		'CaDi',

							'laser_co2_1':		'C1',
							'laser_co2_2':		'C2',
							'laser_co2_3':		'C3',
							'laser_excilite':	'Exc',
							'laser_m22':		'M22',
							'laser_triactive':		'Tri',
}




	# Machine Short 
	x_machine_short = fields.Char(

			compute='_compute_x_machine_short',
		)

	#@api.multi
	@api.depends('x_machine')
	def _compute_x_machine_short(self):
		for record in self:
			if record.x_machine != False:
				#record.x_machine_short = self._hash_x_machine[record.x_machine]
				record.x_machine_short = app_vars._hash_x_machine[record.x_machine]




# ----------------------------------------------------------- Crud - Create  ------------------------------------------------------

		# Init - Deprecated 
		#appointment_date = vals['appointment_date']
		#x_type = vals['x_type']
		#if 'doctor' in vals:
		#	doctor = vals['doctor']		
		#if 'patient' in vals:
		#	patient = vals['patient']
		#x_create_procedure_automatic = vals['x_create_procedure_automatic']
		#if 'treatment' in vals:
		#	treatment = vals['treatment']
		#if 'cosmetology' in vals:					# Deprecated !
		#	cosmetology = vals['cosmetology']





	# On change 
	#@api.onchange('duration')
	#def _onchange_appointment_end(self):
	#	print
	#	print 'On change - App End'



# ----------------------------------------------------------- On change - Doctor  ------------------------------------------------------

	# Generates Error - Recursion !!!

	# On Change - Doctor
	@api.onchange('doctor', 'x_type')
	def _onchange_doctor(self):

		print 
		print 'On change Doctor'
		print 
		
		if self.doctor.name != False:
			self.x_error = 0

			# Check for collisions
			#ret = 0 
			ret = 1

			#appointment_date = self.appointment_date
			date_format = "%Y-%m-%d %H:%M:%S"
			delta = datetime.timedelta(hours=self.duration)


			# Auto behavior - Look for free slot 		
			while ret !=0:

				#print 'Gotcha !'
				#print self.appointment_date
				#print 

				ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor.name, self.duration, False, 'doctor', self.x_type)

				if ret != 0: 

					# New ad 
					sd = datetime.datetime.strptime(self.appointment_date, date_format)
					ad_dt = delta + sd
					ad = ad_dt.strftime("%Y-%m-%d %H:%M:%S")
					
					self.appointment_date = ad


			# Check - Deprecated 
			#if ret == 0:	# Success 
			#	tra = 1
			#else: 			#   Error
			#	self.x_error = 1
			#	self.doctor = False
			#	return {'warning': {'title': "Error: Colisión !",
			#						'message': 'Cita ya existente, con el ' + doctor_name + ": " + start + ' - ' + end + '.',
			#						}}

	# _onchange_doctor




# ----------------------------------------------------------- X Date  ------------------------------------------------------
	# Date 
	x_date = fields.Date(
			string="Fecha", 
		)

	@api.onchange('appointment_date')
	def _onchange_x_date(self):
		#print 
		#print 'On Change - App Date'

		if self.appointment_date != False: 
			#print 'Gotcha !'
			date_format = "%Y-%m-%d %H:%M:%S"
			#dt = datetime.datetime.strptime(self.appointment_date, date_format)
			dt = datetime.datetime.strptime(self.appointment_date, date_format) + datetime.timedelta(hours=-5,minutes=0)		# Correct for UTC Delta 
			self.x_date = dt.strftime("%Y-%m-%d")









