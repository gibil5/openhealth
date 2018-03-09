# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH -  Legacy Manager Patient
# 

# Created: 				6 Mar 2018
# Last updated: 	 	id


from openerp import models, fields, api
#import unidecode 
#from . import leg_funcs




class LegacyManagerPatient(models.Model):


	#_order = 'write_date desc'

	_description = 'Legacy Manager Patient'

	_inherit = 'openhealth.legacy.manager'

	_name = 'openhealth.legacy.manager.patient'







# ----------------------------------------------------------- Primitives ------------------------------------------------------

	x_type = fields.Selection(

			[	
				('patient', 					'patient'),
				('order', 						'order'),
			], 

			string='Type',
			
			default='patient', 

			required=True, 
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Create Data  
	@api.multi 
	def create_data(self):

		print 'jx'
		print 'Create Data'



		if self.source.name == False: 

			name = 'patient legacy'
			model = 'openhealth.legacy.patient'
			obj = 'openhealth.data.analyzer'


			#source = self.source.create({
			self.source = self.env[obj].create({
												'name': name,
												'model': model,
				})
			
			print self.source



		if self.target.name == False: 
			
			name = 'patient'
			model = 'oeh.medical.patient'
			obj = 'openhealth.data.analyzer'
		

		#	target = self.target.create({
			self.target = self.env[obj].create({
												'name': name,
												'model': model,
				})
			print self.target

		print






	# Synchronize New 
	@api.multi 
	def synchronize_new(self):

		print 'jx'
		print 'Synchronize'


 		max_count = self.max_count


 		models_all = self.env[self.source.model].search([
														
															#('name', '=', name), 
															('NombreCompleto', '!=', 'AAA'), 

												],

														#order='FechaRegistro desc',
														order='FechaCreacion desc',

														limit=max_count,
											)

 		count = 0 
 		
 		count_create = 0 

		models = models_all[:max_count]



		for model in models: 
			
			#while count < max_count:


				#print model 
				#print model.FechaRegistro 
				#print model.NombreCompleto 
				#print model.NumeroDocumento 
				#print model.FechaCreacion 





				foo = model.NombreCompleto			
				name_compact = " ".join(foo.split())			# Strip white spaces, beginning, end and middle. 
				name_compact_upper = name_compact.upper()		# To uppercase 
				#name = unidecode.unidecode(bar)				# Remove accents. Bad, removes also Ñ.



				print name_compact_upper 


	 			patient = self.env[self.target.model].search([
																
																#('name', '=', name), 
																('name', '=', name_compact_upper), 
												
												],
			#												#order='write_date desc',
															limit=1,
												)
	 			#print patient

	 			#if patient == False: 
	 			if patient.name == False: 
	 				print 

	 				print 'Create !'

					print model 
					

					# Ids 
					#name = model.NombreCompleto 
					name = name_compact_upper 


					hc_code = model.CODIGOhistoria 
					doc_code = model.NumeroDocumento 
					sex = model.Sexo 


					# Dates 
					date_record = model.FechaRegistro_d
					date_created = model.FechaCreacion_d
					date_birth = model.FechaNacimiento_d 



					# Contact
					address = model.Direccion 
					district = model.Distrito 
					phone = model.Telefono1 
					mobile = model.Telefono2 
					email = model.Correo 


					# Comment 
					comment = 'legacy, lm, created'


		 			print patient




		 			ret = leg_funcs.create_patient(self, 	name, hc_code, doc_code, sex, 
		 													date_record, date_created, date_birth, 
		 													address, district, phone, mobile, email, 
		 													comment
		 											)

		 			print ret 


		 			count_create = count_create + 1
				print 


		
				print count
				count = count + 1 



		print count
		print count_create
		print 








	# Synchronize - HC Code 
	@api.multi 
	def synchro_hc_code(self):

		print 'jx'
		print 'Synchro HC code'

	 	

		#hc_code = '0010000005002'		# Dev 
		hc_code = '0010000005000'		# Prod 

 




		# Max 
 		#max_count = 10
 		#max_count = 100
 		#max_count = 1000
 		max_count = 3000
 		#max_count = 20000


	 	patients_all = self.env['oeh.medical.patient'].search([
																#('name', '=', name), 
																('x_id_code', '=', hc_code), 
												],
															#order='write_date desc',
															#limit=1,
															limit=max_count,
												)

	 	#print patients_all







		patients = patients_all[:max_count]

	 	print patients




	 	for patient in patients:


	 		name = patient.name 

	 		print name 
	 		

	 		abort = False


			nr = self.env['openhealth.legacy.patient'].search_count([																							
																			('NombreCompleto', '=', name),			

																		]) 
			

			if nr == 0: 
				name = name.title()
				print name 
				print 'Titling'


				nr = self.env['openhealth.legacy.patient'].search_count([																							
																			('NombreCompleto', '=', name),			

																		]) 

				if nr == 0: 
					print 'This should not happen !!!'
					print nr 
					abort = True 





	 		patient_leg = self.env['openhealth.legacy.patient'].search([
																			('NombreCompleto', '=', name), 
												],
															#order='write_date desc',
															limit=1,
												)

	 		


	 		if patient.x_id_code != patient_leg.CODIGOhistoria: 

	 			print 'gotcha !'

	 			print patient_leg.CODIGOhistoria
	 			print patient.x_id_code



	 			#if patient_leg.CODIGOhistoria != False: 
	 			if not abort: 

	 				comment = 'legacy, corr hd'
	 				
	 				patient.x_id_code = patient_leg.CODIGOhistoria
	 				patient.comment = comment
	 				patient.x_dni = patient_leg.NumeroDocumento






	 			print patient.x_id_code



	 		

	 		print 







