


# Old
	# Names 
	#name = fields.Char(
		#required=True, 
		#readonly=True, 
		#string = "Nombre completo", 	

		#default='x',

		#compute='_compute_name',
	#)


	#'name': fields.char('Name', select=True),
	#name = fields.Char(
	#	string='Name', 
	#	select=True,

		#default='x',
		#readonly=True, 
		#compute='_compute_name',
	#	)





# 26 Oct 2016

	def test_dni(self,cr,uid,ids,context=None):
		print context

		if context and (not context.isdigit()):
			return {
					'warning': {
						'title': "Error: DNI no es número",
						'message': context,
					}}

		if context and (len(str(context))!= 8):
			return {
					'warning': {
						'title': "Error: DNI no tiene 8 cifras",
						'message': context,
					}}
					
		return {}


# 4 dec 2016
	# Patient Autofill 
	# -------------------
	@api.multi
	def autofill_patient(self):  

		#self.dob = 

		self.a_dni = '09817194'
		self.a_allergies = 'Ninguna'


						<!-- Autofill --> 
						<!--
						<button 
							type="object" 
							class="oe_highlight oe_right"
							string="Autofill" 

							name="autofill_patient" 
						/>
						-->


