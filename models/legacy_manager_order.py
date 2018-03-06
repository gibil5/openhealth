# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH -  Legacy Manager Order
# 

# Created: 				6 Mar 2018
# Last updated: 	 	id


from openerp import models, fields, api
#import unidecode 
#from . import leg_funcs




class LegacyManagerOrder(models.Model):


	#_order = 'write_date desc'

	_description = 'Legacy Manager Order'

	_inherit = 'openhealth.legacy.manager'

	_name = 'openhealth.legacy.manager.order'







# ----------------------------------------------------------- Primitives ------------------------------------------------------


	x_type = fields.Selection(

			[	
				('patient', 					'patient'),
				('order', 						'order'),
			], 

			string='Type',
			
			default='order', 

			required=True, 
		)



	#source = fields.Many2one(
	#		'openhealth.data.analyzer', 
			#'openhealth.legacy.patient'
			#'openhealth.legacy.order'
	#	)


	#target = fields.Many2one(
	#		'openhealth.data.analyzer', 
			#'oeh.medical.patient', 
			#'sale.order', 
	#	)





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi 
	def create_data(self):

		print 'jx'
		print 'Create Data'



		if self.source.name == False: 


			#name = 'patient legacy'
			#model = 'openhealth.legacy.patient'
			#obj = 'openhealth.data.analyzer'


			name = 'order legacy'
			model = 'openhealth.legacy.order'
			obj = 'openhealth.data.analyzer'



			#source = self.source.create({
			self.source = self.env[obj].create({
												'name': name,
												'model': model,
				})
			
			print self.source



		if self.target.name == False: 

			
			#name = 'patient'
			#model = 'oeh.medical.patient'
			#obj = 'openhealth.data.analyzer'

			name = 'order'
			model = 'sale.order'
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
		print 'Synchronize New Order'



 		#max_count = 10 
 		max_count = self.max_count



 		models_all = self.env[self.source.model].search([
														#('name', '=', name), 
														#('NombreCompleto', '!=', 'AAA'), 
												],

														#order='FechaRegistro desc',
														#order='FechaCreacion desc',

														#limit=10,
														#limit=30,
														#limit=100,
														limit=max_count,
											)
 		print models_all
 		print max_count



 		count = 0  		
 		count_create = 0 

		#models = models_all[:max_count]



		#for model in models: 
		for model in models_all: 


				foo = model.NombreCompleto			
				name_compact = " ".join(foo.split())			# Strip white spaces, beginning, end and middle. 
				name_compact_upper = name_compact.upper()		# To uppercase 
				#name = unidecode.unidecode(bar)				# Remove accents. Bad, removes also Ñ.


				print 
				print name_compact_upper 


	 			#patient = self.env[self.target.model].search([
	 			patient = self.env['oeh.medical.patient'].search([
																
																	#('name', '=', name), 
																	('name', '=', name_compact_upper), 
												
												],
			#												#order='write_date desc',
															limit=1,
												)
	 			#print patient

	 			#if patient == False: 
	 			if patient.name == False: 
	 				

	 				print 'This should not happen !'
	 			
	 			else: 


	 				serial_nr = model.serial_nr


		 			#order = self.env[self.target.model].search([
		 			order = self.env['sale.order'].search([

																	
																	#('name', '=', name), 
																	#('patient', '=', name_compact_upper), 
																	('x_serial_nr', '=', serial_nr), 
													
						
													],
				#												#order='write_date desc',
																limit=1,
													)

					

		 			if order.name == False: 

		 				print 
		 				print 'Create !'









