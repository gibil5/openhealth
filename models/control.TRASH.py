

# 20 Dec 2017

	#@api.onchange('appointment')
	#def _onchange_appointment(self):
	#	self.evaluation_start_date = self.appointment.x_date


	#date_actual = fields.Date(
	#		string = "Fecha real", 	
			#required=True, 
	#	)

	#@api.onchange('evaluation_start_date')
	#def _onchange_evaluation_start_date(self):
	#	self.date_actual = self.evaluation_start_date




		#@api.multi
	#@api.depends('state')
	#def _compute_control_nr(self):
	#	for record in self:
	#		nr = 1
	#		record.control_nr = nr  





	#image_ids = fields.One2many(
	#		'openhealth.image', 
	#		'control', 
	#		string = "Fotos", 
	#	)









	
	#@api.multi
	#@api.depends('evaluation_start_date')
	#def _compute_evaluation_next_date(self):
	#	date_format = "%d days, 0:00:00"
	#	delta = datetime.timedelta(weeks=1)
	#	to = datetime.datetime.today()
	#	next_week = delta + to
	#	for record in self:
	#		record.evaluation_next_date = next_week



	#@api.onchange('evaluation_start_date')
	#def _onchange_evaluation_start_date(self):

	#	date_format = "%Y-%m-%d"
	#	delta = datetime.timedelta(weeks=1)
	#	sd = datetime.datetime.strptime(self.evaluation_start_date, date_format)
	#	next_week = delta + sd

	#	self.evaluation_next_date = next_week

		#print
		#print 'onchange'
		#print self.evaluation_start_date
		#print sd 
		#print next_week
		#print 






# 1 Feb 2018

	def _compute_state(self):
		for record in self:

			state = 'draft'


			#if record.nr_images > 0:
			#	state = 'inprogress'

			#if record.nr_images > 2:
			#	state = 'done'
			#	for image in record.image_ids:
			#		if image.name not in ['Frente', 'Derecha', 'Izquierda', 'frente', 'derecha', 'izquierda', 'FRENTE', 'DERECHA', 'IZQUIERDA', ]:
			#			state = 'inprogress'



			if record.x_done: 
				state = 'done'


			record.state = state



# 19 Jul 2018

	# Appointments 
	#appointment_ids = fields.One2many(
	#		'oeh.medical.appointment', 
	#		'control', 
	#		string = "Citas", 
	#	)





	# First Date 
	#@api.model
	#def _get_first_date(self):
		#first_date = self.control_date
	#	first_date = self.appointment.appointment_date	
	#	return first_date



	# Control date 
	#first_date = fields.Datetime(
	first_date = fields.Date(
			string = "Fecha Inicial", 	
			#default=_get_first_date, 
			#compute='_compute_first_date', 
		)

	#@api.multi
	#@api.depends('state')
	#def _compute_first_date(self):
	#	for record in self:
	#		if record.first_date == False: 		
	#			record.first_date = record.control_date




	# Control date 
	control_date = fields.Datetime(
			string = "Fecha Real", 	

			#required=True, 
		
			#compute='_compute_control_date', 
		)

	@api.multi
	#@api.depends('state')
	def _compute_control_date(self):
		for record in self:
			record.control_date = record.appointment.appointment_date



