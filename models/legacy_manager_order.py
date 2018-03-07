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

	# Synchronize 
	@api.multi 
	def synchronize_new(self):

		print 'jx'
		print 'Synchronize Order'


 		max_count = self.max_count


 		models_all = self.env[self.source.model].search([
														#('name', '=', name), 
														#('NombreCompleto', '!=', 'AAA'), 
												],
														#order='FechaFactura_d desc',
														limit=max_count,
											)
 		print models_all
 		print max_count



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

	 			#if patient == False: 
	 			if patient.name == False: 
	 				
	 				print 'Patient does not exist.'
	 				print 'Will not be created.'
	 				#print 'This should not happen !'

	 			

	 			else: 	# Patient exists 

	 				print 'Search order'

	 				serial_nr = model.serial_nr

	 				print serial_nr

		 			order = self.env['sale.order'].search([
																	
																	#('name', '=', name), 
																	('x_serial_nr', '=', serial_nr), 
													
						
													],
																#order='write_date desc',
																limit=1,
													)

					print order 
					print order.name 


		 			if order.name == False: 

		 				print 
		 				print 'Create !'


		 				note = 'lm, created'


		 				name_pl = 'Public Pricelist'
		 				pricelist = self.env['product.pricelist'].search([
																			('name', '=', name_pl), 
																	],
																			#order='write_date desc',
																			limit=1,
																	)
		 				pricelist_id = pricelist.id




		 				name = model.NombreCompleto
		 				partner = self.env['res.partner'].search([
																			('name', '=', name), 
																	],
																			#order='write_date desc',
																			limit=1,
																	)
		 				partner_id = partner.id




		 				state = 'sale'



			 			order_nex = leg_funcs.create_order(self, 	serial_nr, pricelist_id, partner_id, state, 
			 												#name, hc_code, doc_code, sex, 
		 													#date_record, date_created, date_birth, 
		 													#address, district, phone, mobile, email, 
		 													note
		 											)
			 			print order_nex

			 			







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




