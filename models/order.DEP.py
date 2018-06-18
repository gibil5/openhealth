



# ----------------------------------------------------------- Test and Hunt ------------------------------------------------------
	# Test Bug 
	#@api.multi 
	#def test_bug(self):
	#	print 'jx'
	#	print 'Test and Hunt !'
	#	target_line = 'quick_body_local_cyst_2'
	#	print target_line
	#	ret = self.x_create_order_lines_target(target_line)
	#	print ret  



# ----------------------------------------------------------- Validate Stock Picking ------------------------------------------------------

	@api.multi 
	def do_transfer(self):
		print 'jx'
		print 'Do Transfer'
		print self.picking_ids
		for pick in self.picking_ids: 
			ret = pick.do_transfer()
			print ret


	# From Action confirm 
	@api.multi 
	def validate_stock_picking(self):
		print 'jx'
		print 'Validate Stock Picking'
		print self.picking_ids
		for pick in self.picking_ids: 
			print pick
			print pick.name 
			ret = pick.force_assign()
			print ret











# ----------------------------------------------------------- Nr Mac Clones  ------------------------------------------------------

	@api.multi 
	def get_nr_mc(self):
		nr_mac_clones =	self.env['oeh.medical.appointment'].search_count([
																			('appointment_date','=', self.x_appointment.appointment_date),													
																			('x_machine','=', self.x_appointment.x_machine),
																		]) 
		return nr_mac_clones










	# Open Cosmetology
	#@api.multi 
	#def open_cosmetology(self):
		#print 
		#print 'Open cosmetology'
	#	ret = self.cosmetology.open_myself()
	#	return ret 
	# open_cosmetology






	# Open Treatment
	@api.multi 
	def open_treatment(self):

		if self.treatment.name != False:
			ret = self.treatment.open_myself()
		elif self.cosmetology.name != False:
			ret = self.cosmetology.open_myself()
		else:
			#print 'This should not happen !'
			ret = 0 

		return ret 







	# Default Doctor
	@api.multi
	def _get_default_doctor(self): 
		name = 'Clinica Chavarri'
		doctor = self.env['oeh.medical.physician'].search([
																		('name', '=', name),			
																	],
																	#order='start_date desc',
																	limit=1,
																)
		return doctor.id 








# ----------------------------------------------------------- Appointment ------------------------------------------------------

# In Action Confirm

		#if self.x_family == 'consultation'	or 	self.x_family == 'procedure': 
		#	if self.x_appointment.name != False: 
		#		self.x_appointment.state = 'invoiced'



	# Appointment 
	x_appointment = fields.Many2one(
			'oeh.medical.appointment',
			string='Cita', 
			required=False, 

			compute='_compute_x_appointment', 
		)



	@api.multi
	#@api.depends('x_appointment')

	def _compute_x_appointment(self):
		for record in self:

			# Procedure 
			if record.x_family == 'procedure':				
				app = self.env['oeh.medical.appointment'].search([
																	('patient', '=', record.patient.name), 
																	('x_type', '=', 'procedure'),
																	('doctor', '=', record.x_doctor.name), 
																	#('x_target', '=', record.x_target),	
																],
																	order='appointment_date desc',
																	limit=1,
																)
			# Consultation or Product 
			elif record.x_family == 'consultation'	or  record.x_family == 'product':			

				app = self.env['oeh.medical.appointment'].search([
																	('patient', '=', record.patient.name), 
																	('x_type', '=', 'consultation'),
																	('doctor', '=', record.x_doctor.name), 
																	#('x_target', '=', record.x_target),	
																],
																	order='appointment_date desc',
																	limit=1,
																)
			
			else:
				app = False

			record.x_appointment = app

		# compute_x_appointment






# 17 Jun 2018 



# ----------------------------------------------------------- Update Legacy - Type ------------------------------------------------------

	# Update Jan 
	@api.multi
	def update_type_legacy_jan(self):
		print 
		print 'Update Type Legacy Jan'

		# Legacy
 		models = self.env['sale.order'].search([
																('date_order', '>=', '2018-01-01'), 
																('date_order', '<', '2018-02-01'), 
													],
																order='date_order asc',
																#limit=1000,
												)
 		print models
 		for model in models: 
 			if model.x_type == False: 
 				model.update_type_legacy()

 	# update_type_legacy_jan



	# Update Feb
	@api.multi
	def update_type_legacy_feb(self):
		print 
		print 'Update Type Legacy Feb'
		# Legacy
 		models = self.env['sale.order'].search([
																('date_order', '>=', '2018-02-01'), 
																('date_order', '<', '2018-03-01'), 

													],
																order='date_order asc',
																#limit=1000,
												)
 		print models
 		for model in models: 
 			if model.x_type == False: 
 				model.update_type_legacy()
 
 	# update_type_legacy_feb






	# Update Mar
	@api.multi
	def update_type_legacy_mar(self):
		print 
		print 'Update Type Legacy Mar'
		# Legacy
 		models = self.env['sale.order'].search([
																('date_order', '>=', '2018-03-01'), 
																('date_order', '<', '2018-04-01'), 

													],
																order='date_order asc',
																#limit=1000,
												)
 		print models
 		for model in models: 
 			if model.x_type == False: 
 				model.update_type_legacy()

 	# update_type_legacy_mar








 	# Update Type Legacy 
	@api.multi
	def update_type_legacy(self):
		print 
		print 'Update Type Legacy'
		# Legacy
 		model = self.env['openhealth.legacy.order'].search([
																('serial_nr', '=', self.x_serial_nr), 
																										],
																#order='FechaFactura_d desc',
																limit=1,
												)
 		print model.serial_nr
 		print model.tipodocumento
 		print 
 		if self.x_type == False: 
 			self.x_type = ord_vars._dic_type_leg[model.tipodocumento]

 	# update_type_legacy






