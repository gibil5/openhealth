# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Patient Legacy Manager
# 

# Created: 				24 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api
import unidecode 
from . import leg_funcs




class LegacyManager(models.Model):


	#_order = 'write_date desc'

	_description = 'Legacy Manager'



	_inherit = 'openhealth.legacy'

	#_name = 'openhealth.patient.legacy'
	_name = 'openhealth.legacy.manager'







# ----------------------------------------------------------- Primitives ------------------------------------------------------


	ratio = fields.Float(
		)

	delta = fields.Integer(
		)




	source_count = fields.Integer(
		)

	target_count = fields.Integer(
		)






	name = fields.Char(
			#string='Nombre',
			required=True, 
		)


	x_type = fields.Selection(

			[	
				#('oeh.medical.patient', 		'oeh.medical.patient'),
				('patient', 					'patient'),
			], 

			string='Type',
			
			required=True, 
		)




	source = fields.Many2one(
			'openhealth.data.analyzer', 
		)

	target = fields.Many2one(
			'openhealth.data.analyzer', 
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------


	# Mark 
	@api.multi 
	def clear_mark_name(self):

		print 'jx'
		print 'Clear Mark Name'

		# Clear 
	 	patients_all = self.env['oeh.medical.patient'].search([
																	('x_mark', '=', 'name'), 
															],

															#order='write_date desc',
															#limit=1,
														)
	 	for patient in patients_all:
	 		patient.x_mark = False









	# Mark 
	@api.multi 
	def mark_name(self):

		print 'jx'
		print 'Mark Name'










 		#max_count = 10
 		#max_count = 100 
 		#max_count = 1000 
 		#max_count = 2000 
 		#max_count = 4000 
 		#max_count = 8000 
 		max_count = 20000 


	 	patients_all = self.env['oeh.medical.patient'].search([
																	#('name', '=', name), 
																	#('x_id_code', '=', hc_code), 
															],
															#order='write_date desc',

															#limit=1,
															limit=max_count,
														)




		patients = patients_all[:max_count]
	 	print patients



	 	for patient in patients:


	 		# Name 
	 		name = patient.name 

	 		#print name 
	 		
			nr = self.env['oeh.medical.patient'].search_count([
																										
																	('name', '=', name),			

															]) 
			
			#print nr 

			if nr > 1: 

				print 'gotcha !'
		 		print name 
				patient.x_mark = 'name'





			# Titleize 
	 		name = patient.name.title()

	 		#print name 
	 		
			nr = self.env['oeh.medical.patient'].search_count([
																										
																	('name', '=', name),			

															]) 
			
			#print nr 

			if nr > 0: 

				print 'gotcha !'
		 		print name 
				patient.x_mark = 'name'










	# Synchronize
	@api.multi 
	def synchro_hc_code(self):

		print 'jx'
		print 'Synchro HC code'

	 	

		#hc_code = '0010000005002'
		hc_code = '0010000005000'

 



	 	patients_all = self.env['oeh.medical.patient'].search([
																#('name', '=', name), 
																('x_id_code', '=', hc_code), 
												],
															#order='write_date desc',
															#limit=1,
												)

	 	#print patients_all



 		#max_count = 10
 		#max_count = 100
 		#max_count = 1000
 		max_count = 3000
 		#max_count = 20000



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








	# Synchronize
	@api.multi 
	def synchronize(self):

		print 'jx'
		print 'Synchronize'


 		#models = self.env[self.source.model].search([
 		models_all = self.env[self.source.model].search([
														
														#('name', '=', name), 
														('NombreCompleto', '!=', 'AAA'), 

												],

														#order='FechaRegistro desc',
														order='FechaCreacion desc',

														#limit=10,
														#limit=30,
														#limit=100,
											)

 		count = 0 
 		count_create = 0 
 		
 		#max_count = 10 
 		#max_count = 30 
 		#max_count = 50 
 		#max_count = 100
 		#max_count = 200
 		#max_count = 1000
 		#max_count = 2000
 		#max_count = 5000
 		max_count = 10000
 		#max_count = 20000


		models = models_all[:max_count]



		for model in models: 
			
			#while count < max_count:


				#print model 
				#print model.FechaRegistro 
				#print model.NombreCompleto 
				#print model.NumeroDocumento 
				#print model.FechaCreacion 



				#pre_name = model.NombreCompleto
				#name = " ".join(pre_name.split())


				foo = model.NombreCompleto			
				name = " ".join(foo.split())			# Strip white spaces, beginning, end and middle. 
				name = name.upper()						# To uppercase 
				#name = unidecode.unidecode(bar)		# Remove accents. Bad, removes also Ñ.



				print name 


	 			patient = self.env[self.target.model].search([
																('name', '=', name), 
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
					name = model.NombreCompleto 
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






	# Update 
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





	# Update 
	@api.multi 
	def update_data(self):

		print 'jx'
		print 'Update Data'


		self.source.update_data()
		self.source_count = self.source.count  

		self.target.update_data()
		self.target_count = self.target.count  


		# Parameters 
		self.ratio = (	float(self.target_count) / float(self.source_count)  ) * 100.
		self.delta = self.source_count - self.target_count
		
		print








