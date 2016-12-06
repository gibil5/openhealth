
# 6 December 2016

		#evaluation_start_date = datetime.today()
		#evaluation_start_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
		#evaluation_start_date = datetime.today().strftime("%Y-%m-%d")
		#evaluation_start_date = datetime.now().strftime("%Y-%m-%d")
		#evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d")
		#date_format = "%m-%d-%Y"
		#evaluation_start_date = datetime.strptime(evaluation_start_date, date_format)
		#print evaluation_start_date 






# Button - Procedure 

#@api.multi
#def open_procedure_current(self):  

#	patient_id = self.patient.id
#	doctor_id = self.physician.id
#	treatment_id = self.id 

#	return {
			# Mandatory 
#			'type': 'ir.actions.act_window',
#			'name': 'Open Procedure Current',

			# Window action 
#			'res_model': 'openhealth.procedure',

			# Views 
#			"views": [[False, "form"]],

#			'view_mode': 'form',

#			'target': 'current',

#			'context':   {
#				'search_default_treatment': treatment_id,
#				'default_patient': patient_id,
#				'default_doctor': doctor_id,
#				'default_treatment': treatment_id,								
#			}
#	}


