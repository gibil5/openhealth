# ----------------------------------------------------------- Dep -----------------------------	
	# Note
	#x_note = fields.Text(
	#		'Nota', 
	#	)
	#x_firm_address = fields.Char(
	#		"Dirección (Razón social)",
	#	)




	# Dni - Test - For Digits and Length - Deprecated !
	#@api.onchange('x_dni')
	#def _onchange_x_dni(self):

	#	ret = lib.test_for_digits(self, self.x_dni)		
	#	return ret if ret != 0 else 'don'

	#	ret = lib.test_for_length(self, self.x_dni, 8)
	#	return ret if ret != 0 else 'don'


	# Ruc - Test - For Digits - Deprecated
	#@api.onchange('x_ruc')
	#def _onchange_x_ruc(self):
		
	#	ret = lib.test_for_digits(self, self.x_ruc)		
	#	return ret if ret != 0 else 'don'

	#	ret = lib.test_for_length(self, self.x_ruc, 11)		
	#	return ret if ret != 0 else 'don'




	def create(self,vals):
		# Search 
 		#patient = self.env['oeh.medical.patient'].search([
		#														('name', '=', res.name), 
		#												],
		#													#order='write_date desc',
		#													limit=1,
		#												)
 		#if patient.x_test != False: 
		#	res.x_test = patient.x_test



