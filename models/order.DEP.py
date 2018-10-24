

# ----------------------------------------------------------- Action Confirm ------------------------------------------------------

	# Action confirm 
	@api.multi 
	def action_confirm_nex(self):
		print 
		print 'Action confirm - Nex'
		#print 
		



#Write your logic here - Begin

		# Generate Serial Number		
		#print 'Serial number and Type'
		#print self.x_serial_nr


		#if self.x_serial_nr != '': 
		if self.x_serial_nr != '' and self.x_admin_mode == False: 



			# Serial Number
		 	#counter = self.env['openhealth.counter'].search([
			#															('name', '=', self.x_type), 
			#														],
			#															#order='write_date desc',
			#															limit=1,
			#														)
		 	
		 	# Init 
			#separator = '-'
			#prefix = counter.prefix
			#padding = counter.padding

			# Value 
			#value = counter.value

			# Increase 
			#counter.increase()				# Here !!!

			# Calculate 
			#self.x_serial_nr = prefix + separator + str(value).zfill(padding)
			#self.x_counter_value = value





		 	# Init 
			#separator = self.x_separator
			#prefix = self.x_prefix 
			#padding = self.x_padding
			prefix = ord_vars._dic_prefix[self.x_type]


			# Value 
			self.x_counter_value = user.get_counter_value(self)
			

			print self.x_counter_value
			#print self.x_prefix
			print prefix
			print self.x_separator
			print self.x_padding



			#self.x_serial_nr = self.x_prefix + self.x_separator + str(self.x_counter_value).zfill(self.x_padding)
			self.x_serial_nr = prefix + self.x_separator + str(self.x_counter_value).zfill(self.x_padding)










		# Doctor User Name
		#if self.x_doctor.name != False: 
		#	uid = self.x_doctor.x_user_name.id
		#	self.x_doctor_uid = uid


#Write your logic here - End 

		# The actual procedure 
		res = super(sale_order, self).action_confirm()

#Write your logic here - Begin 
		

		# Date must be that of the Sale, not the budget. 
		#self.date_order = datetime.datetime.now()

		# Update Descriptors (family and product) 
		#self.update_descriptors()

		# Change Appointment State - To Invoiced 
		#self.update_appointment()

		# Vip Card - Detect and Create 
		#self.detect_create_card()

		# Create Procedure with Appointment 
		#if self.treatment.name != False: 
		#	print
		#	print 'Create Procedure'
		#	for line in self.order_line: 
		#		if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:
		#			self.create_procedure_wapp(line.product_id.x_treatment, line.product_id.id)
			# Update 
		#	self.x_procedure_created = True
		#	self.treatment.update_appointments()
		

	# action_confirm_nex






# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	# For Admin
	#@api.multi
	#def state_force(self):  
	#	if self.state in ['sale', 'cancel']: 
	#		self.state = 'editable'
	#	elif self.state == 'editable': 
	#		self.state = 'sale'




# ----------------------------------------------------------- Product Selector ------------------------------------------------------

		#x_type = context['x_type']




		#print 'Open Product Selector'
		#print context
		#print context['params']
		#print order_id
		#print res.id
		





		#if res.id != False: 			# Dep !
			
		#	res_id = res.id 

			# Reset 
		#	res.reset()

			# Initialize 
		#	res.order_id = order_id
		#	res.product_uom_qty = 1 
		#	res.x_type = x_type



# ----------------------------------------------------------- Events ------------------------------------------------------

	# Event 
	#event_ids = fields.One2many(
	#		'openhealth.event',
	#		'order',		
	#		string="Eventos", 
	#	)


	@api.multi 
	def cancel_order(self):
		self.x_cancel = True
		self.state = 'cancel'
		#ret = self.create_event()
		return(ret)


	@api.multi 
	def create_event(self):
		nr_pm = self.env['openhealth.event'].search_count([('order','=', self.id),]) 
		name = 'Evento ' + str(nr_pm + 1)
		x_type = 'cancel'

		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Current', 
				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',
				'res_model': 'openhealth.event',				
				#'res_id': receipt_id,
				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								'form': {'action_buttons': True, }
							},
				'context': {
								'default_order': self.id,
								'default_name': name,
								'default_x_type': x_type,
							}
				}







# ----------------------------------------------------------- Testing Units ------------------------------------------------------

	# Unit Testing 
	@api.multi
	def test_units(self):  

		print 
		print 'Unit Testing Begin'

		self.treatment.create_order('consultation')

		self.test_clean_services()
		self.treatment.create_order('procedure')

		self.update_descriptors_all()

		self.update_type()

		self.state_change()
		self.state_change()

		self.x_type = 'ticket_receipt'
		self.print_ticket()
		self.x_type = 'ticket_invoice'
		self.print_ticket()


		self.cancel_order()
		self.activate_order()
		self.state = 'sale'

		print 
		print 'Unit Testing End'
		print 



	# Clean Services 
	@api.multi
	def test_clean_services(self):  
		for service in self.treatment.service_vip_ids:
			service.state = 'draft'
		for service in self.treatment.service_co2_ids:
			service.state = 'draft'
		for service in self.treatment.service_quick_ids:
			service.state = 'draft'
		for service in self.treatment.service_excilite_ids:
			service.state = 'draft'
		for service in self.treatment.service_ipl_ids:
			service.state = 'draft'
		for service in self.treatment.service_ndyag_ids:
			service.state = 'draft'
		for service in self.treatment.service_medical_ids:
			service.state = 'draft'





# ----------------------------------------------------------- Batch - Update Type ------------------------------------------------------

	# Used by Closing
	# Update type from batch 
	@api.multi
	def update_type(self):
		#print 
		#print 'update type'
		if self.x_payment_method != False: 
			#print 'Gotcha'
			self.x_type = self.x_payment_method.saledoc
			#print self.x_type






# ----------------------------------------------------------- Counters ------------------------------------------------------

	def _get_default_counter(self, x_type):
		#print 
		#print 'Get Default Counter'
		#print x_type
		
		_h_name = {
					'tkr' : 	'ticket_receipt', 
					'tki' : 	'ticket_invoice', 
					'rec' : 	'receipt', 
					'inv' : 	'invoice', 
					'san' : 	'sale_note', 
					'adv' : 	'advertisement', 
		}
		name = _h_name[x_type]
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name), 
														],
															#order='write_date desc',
															limit=1,
														)
		
		#print counter
		#print 
		return counter
	# _get_default_counter



	# Ticket Receipt 
	counter_tkr = fields.Many2one(
			'openhealth.counter', 
			default=lambda self: self._get_default_counter('tkr'),
		)

	# Ticket Invoice 
	counter_tki = fields.Many2one(
			'openhealth.counter', 
			default=lambda self: self._get_default_counter('tki'),
		)

	# Receipt 
	counter_rec = fields.Many2one(
			'openhealth.counter', 
			default=lambda self: self._get_default_counter('rec'),
		)

	# Invoice 
	counter_inv = fields.Many2one(
			'openhealth.counter', 
			default=lambda self: self._get_default_counter('inv'),
		)

	# Sale Note 
	counter_san = fields.Many2one(
			'openhealth.counter', 
			default=lambda self: self._get_default_counter('san'),
		)

	# Advertisement  
	counter_adv = fields.Many2one(
			'openhealth.counter', 
			default=lambda self: self._get_default_counter('adv'),
		)









# ----------------------------------------------------------- Create order lines - Deprecated ------------------------------------------------------
	
	# From Treatment 
	#@api.multi 	
	#def x_create_order_lines_target(self, name_short, price_manual, price_applied, reco_id):		

	#	print 
	#	print 'Order - Create Order Lines'

		#ret = ord_funcs.create_order_lines(self, name_short, price_manual, price_applied, reco_id)
	#	ret = ord_funcs.create_order_lines_reco(self, name_short, price_manual, price_applied, reco_id)




# ----------------------------------------------------------- Clean ------------------------------------------------------
	# Clean  
	@api.multi 
	def clean(self):
		print 
		print 'Clean'
		self.state == 'draft'





# ----------------------------------------------------------- action confirm ------------------------------------------------------

		#_h_counter = {
		#				'ticket_receipt':  self.counter_tkr, 
		#				'ticket_invoice':  self.counter_tki, 
		#				'receipt':  self.counter_rec, 
		#				'invoice':  self.counter_inv, 
		#				'sale_note':  self.counter_san, 
		#				'advertisement':  self.counter_adv, 
		#}

			#counter = _h_counter[self.x_type]





		#for proc in self.treatment.procedure_ids: 
		#	proc.create_controls()
		#	proc.create_sessions()


		# Deprecated !

		# Reserve Machine 			
		#if self.x_family == 'procedure': 
		#	self.reserve_machine()

		# Stock Picking - Validate 		
		#print 'Picking'
		#self.validate_stock_picking()
		#self.do_transfer()
		

	# action_confirm_nex







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




# ----------------------------------------------------------- User ------------------------------------------------------
	#user_id = fields.Many2one(
	#		'res.users', 
	#		string='Salesperson', 
	#		index=True, 
	#		track_visibility='onchange', 
	#		default=lambda self: self.env.user
	#	)




