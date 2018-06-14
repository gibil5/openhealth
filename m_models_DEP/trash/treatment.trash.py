
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








# 19 May 2017

			#consultation = self.env['openhealth.consultation'].search([
			#																('treatment','=', self.id),
			#																#('name','like', record.patient.name),
			#															],
																		#order='appointment_date desc',
			#															limit=1,)

			#con = self.consultation_ids[0]
			#print con




			#if self.service_excilite_ids.name != False:
			#	service = self.service_excilite_ids[0].service

			#if self.service_ipl_ids.name != False:
			#	service = self.service_ipl_ids[0].service

			#if self.service_ndyag_ids.name != False:
			#	service = self.service_ndyag_ids[0].service

			#if self.service_medical_ids.name != False:
			#	service = self.service_medical_ids[0].service




			#if self.service_co2_ids.name != False:
			#	service = self.service_co2_ids[0].service

			
			services_co2 = self.env['openhealth.service.co2'].search([(
																		'treatment','=', self.id),
																	],
																		#order='appointment_date desc',
																		#limit=1,						
																	)			

			services_excilite = self.env['openhealth.service.excilite'].search([(
																		'treatment','=', self.id),
																	],
																		#order='appointment_date desc',
																		#limit=1,						
																	)

			services_ipl = self.env['openhealth.service.ipl'].search([(
																		'treatment','=', self.id),
																	],
																		#order='appointment_date desc',
																		#limit=1,						
																	)

			services_ndyag = self.env['openhealth.service.ndyag'].search([(
																		'treatment','=', self.id),
																	],
																		#order='appointment_date desc',
																		#limit=1,						
																	)	

			services_medical = self.env['openhealth.service.medical'].search([(
																		'treatment','=', self.id),
																	],
																		#order='appointment_date desc',
																		#limit=1,						
																	)	


			services = services_co2 + services_excilite + services_ipl + services_ndyag + services_medical

			if services != False: 

				for service in services: 

					target_line = service.service.x_name_short
					
					ret = order.x_create_order_lines_target(target_line)
					
					print ret 







