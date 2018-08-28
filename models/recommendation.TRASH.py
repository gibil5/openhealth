

# 27 Aug 2018 
	@api.multi
	def create_service_quick(self):  

		patient_id = self.treatment.patient.id
		physician_id = self.treatment.physician.id


		# Quick 
		#nr_hands = self.treatment.nr_quick_hands
		#nr_body_local = self.treatment.nr_quick_body_local
		#nr_face_local = self.treatment.nr_quick_face_local

		#nr_cheekbones = self.treatment.nr_quick_cheekbones
		#nr_face_all = self.treatment.nr_quick_face_all
		#nr_face_all_hands = self.treatment.nr_quick_face_all_hands

		#nr_face_all_neck = self.treatment.nr_quick_face_all_neck
		#nr_neck = self.treatment.nr_quick_neck
		#nr_neck_hands = self.treatment.nr_quick_neck_hands



		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser quick', 
				'res_model': 'openhealth.service.quick',				
				#'res_id': consultation_id,
				"views": [[False, "form"]],
				#'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',
				'flags': 	{
								'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
							},
				'context': {
								# Quick 
								#'default_nr_hands_i': nr_hands, 
								#'default_nr_body_local_i': nr_body_local, 
								#'default_nr_face_local_i': nr_face_local, 
								#'default_nr_cheekbones': nr_cheekbones, 
								#'default_nr_face_all': nr_face_all, 
								#'default_nr_face_all_hands': nr_face_all_hands, 
								#'default_nr_face_all_neck': nr_face_all_neck, 
								#'default_nr_neck': nr_neck, 
								#'default_nr_neck_hands': nr_neck_hands, 


								'default_patient': patient_id,
								'default_physician': physician_id,
								'default_laser': laser,							
								'default_zone': zone,
								'default_pathology': pathology,
								'default_x_treatment': x_treatment,
								'default_treatment': treatment_id,
							}
				}
	# create_service_quick

