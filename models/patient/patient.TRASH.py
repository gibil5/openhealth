# 23 sep 2019
	@api.multi
	def test_treatment_ids(self):
		print()
		print('Default Treatment Ids')

		print(self.x_doctor)
		print(self.x_doctor.name)
		print(self.x_chief_complaint)

		# Doctors
		doctors = self.env['oeh.medical.physician'].search([
		#													('active', 'in', [True]),
															('name', 'in', [self.x_doctor.name]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		print(doctors)

		return [
					(0, 0, {
							'chief_complaint': self.x_chief_complaint,
							'physician': self.x_doctor.id,
				})
				for d in doctors
				#for s in slots
		]



	# Slots
	def _default_treatment_ids(self):
		print()
		print('Default Treatment Ids')

		print(self.x_doctor)
		print(self.x_doctor.name)
		print(self.x_doctor.id)
		print(self.x_chief_complaint)


		# Doctors
		doctors = self.env['oeh.medical.physician'].search([
		#													('active', 'in', [True]),
															('name', 'in', [self.x_doctor.name]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		print(doctors)

		return [
				(0, 0, {
							'chief_complaint': self.x_chief_complaint,
							'physician': self.x_doctor.id,
				})
				for d in doctors
				#for s in slots
		]

	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Doctor",
		)

	x_chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 						

			selection = eval_vars._chief_complaint_list,

			#required=False,
			#readonly=False, 
		)






# 30 Aug 2019


# ----------------------------------------------------------- HC Number ---------------------------
	# Default - HC Number
	@api.model
	def _get_default_id_code(self):
		print()
		print('Get Default Id Code')

		name_ctr = 'emr'

 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr),
														],
															#order='write_date desc',
															#limit=1,
														)

		# Manage Exception
		try:
			counter.ensure_one()

	 		# Init
	 		prefix = counter.prefix
	 		separator = counter.separator
	 		padding = counter.padding
	 		value = counter.value

			name = count_funcs.get_name(self, prefix, separator, padding, value)

			return name

		except:
			#print("An exception occurred")
			msg = "ERROR: Record Must be One."
			#class_name = type(counter).__name__
			#obj_name = counter.name
			#msg =  msg + '\n' + class_name + '\n' + obj_name
			msg =  msg 

			raise UserError(_(msg))

	# NC Number
	x_id_code = fields.Char(
			'Nr Historia Médica',

			default=_get_default_id_code,
		)


