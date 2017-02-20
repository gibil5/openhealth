
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






# 19 Feb 2017

	#patient = fields.Many2one(
	#		'oeh.medical.patient',
	#		string="Paciente", 
			#index=True
	#		ondelete='cascade', 
	#		)

	#physician = fields.Many2one(
	#		'oeh.medical.physician',
	#		string="Médico", 
	#		index=True
	#		)

	#chief_complaint = fields.Selection(
	#		string = 'Motivo de consulta', 			
	#		selection = jxvars._chief_complaint_list, 
	#		)


	#start_date = fields.Date(
	#		string="Fecha inicio", 
	#		default = fields.Date.today
	#		)	

	#price_total = fields.Float(
	#		string='Total', 
	#		default = 0, 
			#compute='_compute_price_total', 
	#		) 

