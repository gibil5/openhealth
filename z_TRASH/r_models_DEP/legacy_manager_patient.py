# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH -  Legacy Manager Patient
# 

# Created: 				6 Mar 2018
# Last updated: 	 	id


from openerp import models, fields, api
from . import leg_funcs
#import unidecode 
from . import leg_vars




class LegacyManagerPatient(models.Model):


	#_order = 'write_date desc'

	_description = 'Legacy Manager Patient'

	_inherit = 'openhealth.legacy.manager'

	_name = 'openhealth.legacy.manager.patient'










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
														#order='FechaCreacion desc',
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

	 				completeness = 0



		 			print patient




		 			ret = leg_funcs.create_patient(self, 	name, hc_code, doc_code, sex, 
		 													date_record, date_created, date_birth, 
		 													address, district, phone, mobile, email, 
		 													comment, 
		 													completeness		 													
		 											)

		 			print ret 


		 			count_create = count_create + 1
				print 


		
				print count
				count = count + 1 



		print count
		print count_create
		print 








	# Update Existing Patients 
	@api.multi 
	#def synchro_hc_code(self):
	def update_existing_patients(self):


		print 'jx'
		print 'Update Existing Patients'

	 	



		# Search criteria 

		#hc_code = '0010000005002'		# Dev 
		#hc_code = '0010000005000'		# Prod 

		hc_code = False
		x_dni = False
		dob = False
		sex = False
		x_date_created = False

		#name = 'ZAMBRANO OSPINAL AGAR LEONOR'
		#name = 'YLLACONZA SALCEDO ALICIA INES'




		# Max count 
 		max_count = self.max_count



 		# Select 
	 	patients_all = self.env['oeh.medical.patient'].search([
																('x_id_code', '=', 	hc_code), 
																('x_dni', '=', 		x_dni),
																('dob', '=', 		dob),
																('sex', '=', 		sex),
																('x_date_created', '=', x_date_created),


																#('name', '=', name), 
												],
															#order='write_date desc',
															#limit=1,
															limit=max_count,
												)

	 	print patients_all







	 	# Loop 
	 	for patient in patients_all:

	 		
	 		name = patient.name 

	 		print name 
	 		
	 		patient_legacy_exists = True



			nr = self.env['openhealth.legacy.patient'].search_count([																							
																			('NombreCompleto', '=', name),			

																		]) 
			

			# Test if exists in Legacy Patients 
			if nr == 0: 				
				name = name.title()
				print name 
				#print 'Titling'
				nr = self.env['openhealth.legacy.patient'].search_count([																							
																			('NombreCompleto', '=', name),
																		]) 
				if nr == 0: 
					#print 'This should not happen !!!'
					print 'Legacy Patient does not exist !!!'
					#print nr 
					patient_legacy_exists = False 






			# Legacy Patient 
	 		patient_leg = self.env['openhealth.legacy.patient'].search([
																			('NombreCompleto', '=', name), 
												],
															#order='write_date desc',
															limit=1,
												)

	 		
	 		


	 		# Update Patient 
	 		if patient_legacy_exists: 

	 			print 'gotcha !'
	 			print patient_leg.CODIGOhistoria
	 			print patient.x_id_code




 				# Init vars from Legacy 
				name = name

				# Personal 
				hc_code = patient_leg.CODIGOhistoria 
				doc_code = patient_leg.NumeroDocumento 				
				sex = patient_leg.Sexo 

				# Dates 
				date_record = patient_leg.FechaRegistro_d
				date_created = patient_leg.FechaCreacion_d
				date_birth = patient_leg.FechaNacimiento_d 

				# Contact
				address = patient_leg.Direccion 
				district = patient_leg.Distrito 
				phone = patient_leg.Telefono1 
				mobile = patient_leg.Telefono2 
				email = patient_leg.Correo 

				# Comment 
 				comment = 'legacy, corr all'
 				completeness = 1





 				# Update Patient 
				patient.name = name 

				patient.x_id_code = hc_code
				
				patient.x_dni = doc_code
				
				patient.sex = leg_vars._hac[sex]

				patient.x_date_record = date_record

				patient.x_date_created = date_created

				patient.x_datetime_created = date_created

				patient.dob = date_birth

				patient.street = address

				patient.x_district = district

				patient.phone = phone

				patient.mobile = mobile

				patient.email = email

				patient.comment = comment

				patient.completeness = completeness
	 		print 








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





