# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH -  Legacy Manager Order
# 
# Created: 				6 Mar 2018
# Last updated: 	 	id
#

from openerp import models, fields, api
from . import leg_funcs

class LegacyManagerOrder(models.Model):

	#_order = 'write_date desc'

	_description = 'Legacy Manager Order'

	_inherit = 'openhealth.legacy.manager'

	_name = 'openhealth.legacy.manager.order'




# ----------------------------------------------------------- Actions ------------------------------------------------------


	# Update Serial Nr 
	@api.multi 
	def update_serial_nrs(self):

		print 'jx'
		print 'Update SNr'


		models = self.env['openhealth.legacy.order'].search([
																#('serial_nr', '=', serial_nr), 												
												],
																#order='FechaFactura_d desc',
																#limit=max_count,
											)

		for model in models: 
			model.serial_nr = model.NumeroSerie + '-' + model.NumeroFactura







	# Synchronize 
	@api.multi 
	def synchronize_new(self):

		print 
		print 'Synchronize Order'


 		max_count = self.max_count


 		models_all = self.env[self.source.model].search([
															#('name', '=', name), 
															#('NombreCompleto', '!=', 'AAA'), 
												],
															#order='FechaFactura_d desc',
															limit=max_count,
											)
 		#print models_all
 		#print max_count



 		count = 0  		
 		count_create = 0 




		for model in models_all: 

				foo = model.NombreCompleto			
				name_compact = " ".join(foo.split())			# Strip white spaces, beginning, end and middle. 
				name_compact_upper = name_compact.upper()		# To uppercase 


				print 
				print name_compact_upper 


	 			patient = self.env['oeh.medical.patient'].search([
																
																	('name', '=', name_compact_upper), 
												
												],
			#												#order='write_date desc',
															limit=1,
												)
	 			#print patient



	 			if patient.name == False: 						# Patien Does not exist. 
	 				

	 				print 'Patient does not exist.'
	 				print 'Create Patient !'

	 				#print 'Will not be created.'
	 				#print 
	 				#print 'This should not happen !'

	 			

	 				name = name_compact_upper
	 				comment = 'lm, created'
	 				completeness = 1

	 				hc_code = False
	 				doc_code = False
	 				sex = False
	 				date_record = False
	 				date_created = False
	 				date_birth = False
	 				address = False
	 				district = False
	 				phone = False
	 				mobile = False
	 				email = False


		 			ret = leg_funcs.create_patient(self, 	name, hc_code, doc_code, sex, 
		 													date_record, date_created, date_birth, 
		 													address, district, phone, mobile, email, 
		 													comment,
		 													completeness
		 											)

		 			print ret 





	 			else: 	# Patient exists 

	 				#print 'Search order'

	 				serial_nr = model.serial_nr

	 				#print serial_nr


	 				# Search Order 
		 			order = self.env['sale.order'].search([
																	
																	#('name', '=', name), 
																	('x_serial_nr', '=', serial_nr), 
													
						
													],
																#order='write_date desc',
																limit=1,
													)

					#print order 
					#print order.name 


		 			

		 			if order.name != False: 			# Order exists.

		 				print 'Order exists !'



		 			else: 								# Does not exist. Create ! 
		 			
		 				print 'Create Order !'


		 				note = 'lm, created'

		 				date = model.FechaFactura_d



		 				# Pricelist 
		 				name_pl = 'Public Pricelist'
		 				pricelist = self.env['product.pricelist'].search([
																			('name', '=', name_pl), 
																	],
																			#order='write_date desc',
																			limit=1,
																	)
		 				pricelist_id = pricelist.id





		 				#name = model.NombreCompleto
		 				name = name_compact_upper
		 				print name 



		 				# Partner 
		 				partner = self.env['res.partner'].search([
																			('name', '=', name), 
																	],
																			#order='write_date desc',
																			limit=1,
																	)
		 				partner_id = partner.id




		 				# Patient 
		 				patient = self.env['oeh.medical.patient'].search([
																			('name', '=', name), 
																	],
																			#order='write_date desc',
																			limit=1,
																	)
		 				patient_id = patient.id



		 				# State 
		 				state = 'sale'




		 				# Create Order 
			 			order_nex = leg_funcs.create_order(self, 	serial_nr, pricelist_id, partner_id, patient_id, state, 
			 												#max_count, 
			 												date, 
		 													note, 
		 											)
			 			#print order_nex

			 			







	# Create Data  
	@api.multi 
	def create_data(self):

		print 'jx'
		print 'Create Data'

		if self.source.name == False: 

			name = 'order legacy'
			model = 'openhealth.legacy.order'
			obj = 'openhealth.data.analyzer'

			self.source = self.env[obj].create({
												'name': name,
												'model': model,
				})
			
			print self.source

		if self.target.name == False: 

			name = 'order'
			model = 'sale.order'
			obj = 'openhealth.data.analyzer'

			self.target = self.env[obj].create({
												'name': name,
												'model': model,
				})
			print self.target

		print








	# Update Amount Total 
	@api.multi 
	def update_amount_total(self):

		print
		print 'Update Amount Total'


		#models = self.env['openhealth.legacy.order'].search([
		models = self.env['sale.order'].search([
																#('amount_total', '=', amount_total), 
																
																('note', '=', 'lm, created'), 

												],
																#order='FechaFactura_d desc',
																#limit=max_count,
											)

		amount_total = 0 


		for model in models: 

			amount_total = amount_total + model.amount_total



		self.amount_total = amount_total







	# Update Amount Total Legacy
	@api.multi 
	def update_amount_total_legacy(self):

		print
		print 'Update Amount Total Legacy'


		models = self.env['openhealth.legacy.order'].search([
																#('amount_total_legacy', '=', amount_total_legacy), 												
												],
																#order='FechaFactura_d desc',
																#limit=max_count,
											)

		amount_total_legacy = 0 

		for model in models: 
			amount_total_legacy = amount_total_legacy + float(model.totalitem) 

		self.amount_total_legacy = amount_total_legacy




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	amount_total = fields.Float(
			string="Amount Total", 
		)

	amount_total_legacy = fields.Float(
			string="Amount Total Legacy", 
		)








	x_type = fields.Selection(
			[	
				('patient', 					'patient'),
				('order', 						'order'),
			], 
			string='Type',
			default='order', 
			required=True, 
		)




