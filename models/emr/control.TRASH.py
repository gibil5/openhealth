# 19 Sep 2019
# Clean up

#----------------------------------------------------------- Deprecated ------------------------------------------------------------

	# Appointment 
	#appointment = fields.Many2one(
	#		'oeh.medical.appointment',
	#		'Cita', 
	#		required=False, 
	#	)


	# State Appointment 
	#state_app = fields.Selection(
	#		selection = app_vars._state_list, 
	#		string = 'Estado Cita', 

	#		compute='_compute_state_app', 
	#	)
	
	#@api.multi
	#@api.depends('state')
	#def _compute_state_app(self):
	#	for record in self:		
	#		record.state_app = record.appointment.state





# 27 Aug 2019
# Appointment is Highly Deprecated !
#



# ----------------------------------------------------------- Open App ------------------------------------------------------

	# Open Appointment 
	@api.multi
	def open_appointment(self):  

		owner_id = self.id 
		owner_type = self.owner_type
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		treatment_id = self.procedure.treatment.id 

		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Appointment', 
				'view_type': 'form',	
				'view_mode': 'calendar',			
				'target': 'current',
				'res_model': 'oeh.medical.appointment',				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},
				'context': {
							'default_control': owner_id,
							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							'default_x_type': owner_type,
							'default_appointment_date': appointment_date,
							}
				}

















# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	#@api.onchange('appointment')
	#def _onchange_appointment(self):
	#	print 
	#	print 'On Change - Appointment'
		#self.control_date = self.appointment.appointment_date



# ----------------------------------------------------------- CRUD ------------------------------------------------------

	#@api.multi
	#def unlink(self):
		#print 
		#print 'Unlink - Override'
		#print self.appointment
		#self.appointment.unlink() 
		#print 
	#	return models.Model.unlink(self)
