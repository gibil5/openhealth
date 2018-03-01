# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Patient Legacy Manager
# 

# Created: 				24 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api




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
			#required=True, 
		)




	source = fields.Many2one(
			'openhealth.data.analyzer', 
		)

	target = fields.Many2one(
			'openhealth.data.analyzer', 
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------


	# Synchronize
	@api.multi 
	def synchronize(self):

		print 'jx'
		print 'Synchronize'


 		models = self.env[self.source.model].search([
														
														#('name', '=', name), 
														('NombreCompleto', '!=', 'AAA'), 

												],

														order='FechaRegistro desc',

														#limit=10,
														#limit=100,
											)

 		count = 0 

		for model in models: 
			

			#print model 
			#print model.NombreCompleto 
			#print model.FechaRegistro 


			name = model.NombreCompleto


 			patient = self.env[self.target.model].search([
															('name', '=', name), 
											],
		#												#order='write_date desc',
														limit=1,
											)
 			#print patient

 			#if patient == False: 
 			if patient.name == False: 
 				print 'Create !'
				print model 
				print model.NombreCompleto 
				print model.FechaRegistro 
	 			print patient

	 			count = count + 1

			print 


		print count
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








