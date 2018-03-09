# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - data_analyzer 
# 
# Created: 				24 Feb 2018
# Last updated: 	 	id
#
from openerp import models, fields, api

class DataAnalyzer(models.Model):

	_inherit = 'openhealth.data'

	#_order = 'write_date desc'

	_description = 'data_analyzer'

	_name = 'openhealth.data.analyzer'





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi 
	def update_data(self):

		print 'jx'
		print 'Update Data Analyzer'


 		#model = self.env[self.model].search([
		#												('name', '=', name), 
		#									],
		#												#order='write_date desc',
		#												limit=1,
		#									)




		if self.name == 'order': 				# Target Order 

			self.count = self.env[self.model].search_count([

																#('zone', '=', zone),			
																#('note', '!=', 'legacy'),			
																('note', 'not in', ['legacy','observed']),			
														
														]) 



		else: 									# Source Order Legacy 

			self.count = self.env[self.model].search_count([
				
														]) 





		#if self.model == 'openhealth.legacy.patient': 
		#	self.count = self.env[self.model].search_count([																							
																#('zone', '=', zone),			
		#												]) 
		#else: 
		#	self.count = self.env[self.model].search_count([																							
																#('zone', '=', zone),			
		#												]) 


		print





# ----------------------------------------------------------- Primitives ------------------------------------------------------

	count = fields.Integer(
		)


	name = fields.Char(
			required=True, 
		)

	model = fields.Selection(

			[	

				('openhealth.legacy.patient', 		'openhealth.legacy.patient'),
				('oeh.medical.patient', 			'oeh.medical.patient'),

				('openhealth.legacy.order', 		'openhealth.legacy.order'),
				('sale.order', 						'sale.order'),

			], 

			required=True, 
		)


