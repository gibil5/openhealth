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


