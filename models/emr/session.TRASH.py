# 27 Aug 2019
# Appointment is Highly Deprecated !
#




	#------------------------------------------------------ Create Appointment - Dep ----------------------------------------------------------
	@api.multi
	def open_appointment(self):  
		#print 
		#print 'open appointment'

		owner_id = self.id 
		owner_type = self.owner_type
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		treatment_id = self.procedure.treatment.id 
		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#appointment_date = '2016-12-23'

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
							'default_session': owner_id,	
							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							'default_x_type': owner_type,
							'default_appointment_date': appointment_date,
							}
				}
