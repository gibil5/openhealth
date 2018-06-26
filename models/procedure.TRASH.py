


# 2 Feb 2018

	#nr_controls = fields.Integer(
	#		default=7, 
	#		compute="_compute_nr_controls",
	#	)
	#@api.multi
	#@api.depends('product')
	#def _compute_nr_controls(self):
	#	for record in self:





# 22 Jun 2018 

	#jx
	#@api.onchange('control_ids')
	#def _onchange_control_ids(self):
	#	print 
	#	print 'On change Control ids'
	#	rec = self.env['openhealth.control'].search([ 

	#													('procedure', '=', self.id),	
	#												], 
	#												order='evaluation_start_date', 
													#limit=1
	#												)
	#	print rec
	#	print 





	# Open Control 
	@api.multi
	def open_control(self):  

		# Data
		procedure_id = self.id 
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		evaluation_type = 'Periodic Control'
		product_id = self.product.id
		laser = self.laser
		
		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		return {
				# Mandatory 
				'type': 'ir.actions.act_window',
				'name': 'Open control Current',
				# Optional 
				'res_model': 'openhealth.control',
				'view_mode': 'form',
				"views": [[False, "form"]],
				'target': 'current',
				'context':   {
					'default_patient': patient_id,
					'default_doctor': doctor_id,
					'default_chief_complaint': chief_complaint,
					'default_evaluation_type':evaluation_type,				
					'default_product': product_id,
					'default_laser': laser,
					'default_evaluation_start_date': evaluation_start_date,
					'default_procedure': procedure_id,
			}
		}
	# open_control




# 25 Jun 2018

# ----------------------------------------------------------- Deprecated ? ------------------------------------------------------
	
	#key = fields.Char(
	#		string='key', 
	#		default='procedure', 
	#	)

	#model = fields.Char(
	#		string='model', 
	#		default='openhealth.session.med', 
	#	)

	#target = fields.Char(
	#		string='target', 
	#		default='doctor', 
	#	)





