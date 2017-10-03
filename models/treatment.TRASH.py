

# 3 Oct 2017





# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):



		print 
		print 'CRUD - Treatment - Create'
		print 
		print vals



		print 'patient', self.patient.name
		print 'physicien', self.physician.name 


		app_c = self.env['oeh.medical.appointment'].search([
															('patient', '=', self.patient.name), 
															('x_type', '=', 'consultation'),
															('doctor', '=', self.physician.name), 
														],
														order='appointment_date desc',
														limit=1,
													)
		app_p = self.env['oeh.medical.appointment'].search([
															('patient', '=', self.patient.name), 
															('x_type', '=', 'procedure'),
															('doctor', '=', self.physician.name), 
														],
														order='appointment_date desc',
														limit=1,
													)

		print 'id', self.id

		print app_c 
		if app_c.id != False:
			app_c.treatment = self.id 
			print 'c id', app_c.id
			print 'treatment', app_c.treatment 


		print app_p 
		if app_p.id != False:
			app_p.treatment = self.id 
			print 'p id', app_p.id
			print 'treatment', app_p.treatment 






		# Put your logic here 
		res = super(Treatment, self).create(vals)
		# Put your logic here 

		return res

	# CRUD 
