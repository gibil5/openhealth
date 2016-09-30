



	@api.multi
	def open_oeh_new(self):  
		patient_id = self.patient.id
		doctor_id = self.physician.id

		treatment_id = self.id 
		#view_id = self.id 

		return {
			'name': 'Import Module',
			'view_type': 'form',
			'view_mode': 'form',

			#'view_id': False,
			#'view_id': view_id,

			'domain': '[]',
			'flags': {'form': {'action_buttons': True}}, 

			'target': 'new',
			#'target': 'current',

			#'res_model': 'openhealth.evaluation3',
			'res_model': 'oeh.medical.evaluation',

			'type': 'ir.actions.act_window',

			'context':   {
				#'default_partner_id':value,
				#'default_other_field':othervalues,
				'search_default_treatment': treatment_id,
				'default_patient': patient_id,
				'default_doctor': doctor_id,
			}
		}




	# Eval 3 
	@api.multi
	def open_eval3_new(self):  
		patient_id = self.patient.id
		doctor_id = self.physician.id

		return {
			'name': 'Import Module',
			'view_type': 'form',
			'view_mode': 'form',

			'target': 'new',
			#'target': 'current',

			'res_model': 'openhealth.evaluation3',
			#'res_model': 'oeh.medical.evaluation',

			'type': 'ir.actions.act_window',
			'context':   {
				#'default_partner_id':value,
				#'default_other_field':othervalues,
				'default_patient': patient_id,
				'default_doctor': doctor_id,
			}
		}
