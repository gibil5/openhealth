





# ----------------------------------------------------------- Quick Laser - Relational ------------------------------------------------------

	# Quick Services 
	x_service_quick_ids = fields.One2many(
			'openhealth.service.quick', 
			'patient', 

			compute='_compute_service_quick_ids', 
		)

	@api.multi
	def _compute_service_quick_ids(self):		
		for record in self:		
			services = self.env['openhealth.service.quick'].search([
																		('patient', '=', record.name),			
																	],
																	order='create_date asc',
																	#limit=1,
																)
			record.x_service_quick_ids = services
	# _compute_service_quick_ids





# ----------------------------------------------------------- Quick Laser - Nr ofs ------------------------------------------------------

	# Hands 
	x_nr_quick_hands = fields.Integer(
			string='Manos', 
			default=0, 

			compute='_compute_nr_quick_hands', 
		)

	@api.multi
	def _compute_nr_quick_hands(self):
		zone = 'hands', 
		for record in self:		
			record.x_nr_quick_hands =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 
	# Body Local 
	x_nr_quick_body_local = fields.Integer(
			string='Localizado Cuerpo', 
			default=0, 

			compute='_compute_nr_quick_body_local', 
		)

	@api.multi
	def _compute_nr_quick_body_local(self):
		zone = 'body_local', 
		for record in self:		
			record.x_nr_quick_body_local =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 
	# Face Local 
	x_nr_quick_face_local = fields.Integer(
			string='Localizado Rostro', 
			default=0, 

			compute='_compute_nr_quick_face_local', 
		)

	@api.multi
	def _compute_nr_quick_face_local(self):
		zone = 'face_local', 
		for record in self:		
			record.x_nr_quick_face_local =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 

	# Cheekbones 
	x_nr_quick_cheekbones = fields.Integer(
			string='Pómulos', 
			default=0, 

			compute='_compute_nr_quick_cheekbones', 
		)

	@api.multi
	def _compute_nr_quick_cheekbones(self):
		zone = 'cheekbones', 
		for record in self:		
			record.x_nr_quick_cheekbones =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 

	# Face All 
	x_nr_quick_face_all = fields.Integer(
			string='Todo Rostro', 
			default=0, 

			compute='_compute_nr_quick_face_all', 
		)

	@api.multi
	def _compute_nr_quick_face_all(self):
		zone = 'face_all', 
		for record in self:		
			record.x_nr_quick_face_all =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 

	# Face All Hands
	x_nr_quick_face_all_hands = fields.Integer(
			string='Todo Rostro Manos', 
			default=0, 

			compute='_compute_nr_quick_face_all_hands', 
		)

	@api.multi
	def _compute_nr_quick_face_all_hands(self):
		zone = 'face_all_hands', 
		for record in self:		
			record.x_nr_quick_face_all_hands =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 

	# Face All Neck
	x_nr_quick_face_all_neck = fields.Integer(
			string='Todo Rostro Cuello', 
			default=0, 

			compute='_compute_nr_quick_face_all_neck', 
		)

	@api.multi
	def _compute_nr_quick_face_all_neck(self):
		zone = 'face_all_neck', 
		for record in self:		
			record.x_nr_quick_face_all_neck =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 

	# Neck
	x_nr_quick_neck = fields.Integer(
			string='Cuello', 
			default=0, 

			compute='_compute_nr_quick_neck', 
		)

	@api.multi
	def _compute_nr_quick_neck(self):
		zone = 'neck', 
		for record in self:		
			record.x_nr_quick_neck =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 

	# Neck Hands
	x_nr_quick_neck_hands = fields.Integer(
			string='Cuello y Manos', 
			default=0, 

			compute='_compute_nr_quick_neck_hands', 
		)

	@api.multi
	def _compute_nr_quick_neck_hands(self):
		zone = 'neck_hands', 
		for record in self:		
			record.x_nr_quick_neck_hands =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 














# ----------------------------------------------------------- Quality control ------------------------------------------------------

	# QC - Number of clones  
	x_nr_clones = fields.Integer(
			"QC - Nrc",

			#compute="_compute_x_nr_clones",
	)
	#@api.multi
	#def _compute_x_nr_clones(self):
	#	for record in self:
	#		record.x_nr_clones = self.env['oeh.medical.patient'].search_count([
	#																			('name','=', record.name),
	#																		])
	#		if record.x_nr_clones > 1:
	#			record.x_flag = 'error'
	#		else:
	#			record.x_flag = ''




	# QC - Lowcase
	x_lowcase = fields.Boolean(
			"QC - Low",

			#compute="_compute_x_lowcase",
	)
	#@api.multi
	#def _compute_x_lowcase(self):
	#	for record in self:
	#		if record.name != record.name.upper():
	#			record.x_lowcase = True
	#			record.x_flag = 'error'
	#		else:
	#			record.x_lowcase = False




	# Spaced 		- ?
	x_spaced = fields.Boolean(
		string="Spaced",
		default=False, 

		#compute='_compute_spaced', 
	)

	#@api.multi
	#@api.depends('name')
	#def _compute_spaced(self):
	#	for record in self:
	#		if record.name[0] == ' ':
	#			record.x_spaced = True








	# ----------------------------------------------------------- Buttons Update ------------------------------------------------------

	# Button - Update 
	@api.multi
	def x_update(self):  
		#print 
		#print 'Update'
		self.x_date_created = self.x_date_created






# ----------------------------------------------------------- Cosmetology ------------------------------------------------------


	cosmetology_ids = fields.One2many(
			'openhealth.cosmetology', 		
			'patient', 
			string="Cosmiatrías"
			)



	# Nr Cosmetologies 
	x_nr_cosmetologies = fields.Integer(
			'Nr Cosmiatrías', 
			default=0, 

			compute='_compute_x_nr_cosmetologies',
		)

	@api.multi
	#@api.depends('x_allergies')
	def _compute_x_nr_cosmetologies(self):
		for record in self:
			count = 0 
			for tr in record.cosmetology_ids:   
				count = count + 1  
			record.x_nr_cosmetologies = count  




# ----------------------------------------------------------- Buttons Cosmetology ------------------------------------------------------

	# Button - Cosmetology 
	# -------------------
	@api.multi
	def open_cosmetology_current(self):  

		cosmetology_id = self.env['openhealth.cosmetology'].search([
																		('patient','=', self.id),
																],
																order='start_date desc',
																limit=1,).id
		#print 
		#print 'Open Cosmetology'
		patient_id = self.id 
		#print patient_id
		return {
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open cosmetology Current',
			# Window action 
			'res_model': 'openhealth.cosmetology',
			'res_id': cosmetology_id,
			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},	
			'context':   {
				'search_default_patient': patient_id,
				'default_patient': patient_id,
			}
		}
	# open_cosmetology_current 





# ----------------------------------------------------------- Remove Myself ------------------------------------------------------

	# Removem
	#@api.multi
	#def remove_myself(self):  	
	#	self.unlink()



# ----------------------------------------------------------- CRUD ------------------------------------------------------

# Create 
	@api.model
	def create(self,vals):

		print 
		print 'CRUD - Patient - Create'
		print 
		#print vals
	




		# Assign and Increase Counter 
		#if 'x_id_code' in vals: 

		#	name_ctr = 'emr'

	 	#	counter = self.env['openhealth.counter'].search([
		#															('name', '=', name_ctr), 
		#													],
																#order='write_date desc',
		#														limit=1,
		#													)


		#	name = count_funcs.get_name(self, counter.prefix, counter.separator, counter.padding, counter.value)

		#	vals['x_id_code'] = name 

		#	counter.increase()		# Here !!!


		#	print 'Gotcha !'
		#	print counter
		#	print name 
		#	print 'Increased'

		#else:
		#	print 'NOT Assigned nor Increased !'









		# Put your logic here 
		res = super(Patient, self).create(vals)
		# Put your logic here 





		# Increase - Must be after creation 
		name_ctr = 'emr'
	 	counter = self.env['openhealth.counter'].search([
																	('name', '=', name_ctr), 
															],
																#order='write_date desc',
																limit=1,
															)
		counter.increase()		# Here !!!
		print 'Increased'
		print 
		
		#print self.x_id_code



		# Date record 
		print res.create_date
		print res.write_date 
		print res.x_date_record 

		if res.x_date_record == False: 
			res.x_date_record = res.create_date

		print res.create_date
		print res.write_date 
		print res.x_date_record 
		print 


		return res
	# CRUD - Create 






# Write - Deprecated ? 
	@api.multi
	def write(self,vals):

		#print 
		#print 'jx'
		#print 'CRUD - Patient - Write'
		#print 
		#print vals
		#print 
		#print 

		#if vals['x_doctor'] != False: 
		#	print vals['x_doctor']
		#if vals['user_id'] != False: 
		#	print vals['user_id']


		# Assign and Increase Counter 
		#if 'x_id_code' in vals: 
		#	print 'Assigned and Increased'
		#	print vals['x_id_code']
		#else:
		#	print 'NOT Assigned nor Increased !'



		#Write your logic here
		res = super(Patient, self).write(vals)
		#Write your logic here


		# Update Date Record 
		#if self.x_date_record == False: 
		#	self.x_date_record = self.write_date
		#print self.write_date
		#print self.create_date
		#print self.x_date_record 
		#print 

		return res

	# CRUD - Write 


