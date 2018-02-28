# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - data_analyzer 
# 

# Created: 				24 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api



class DataAnalyzer(models.Model):

	_inherit = 'openhealth.data'

	#_order = 'write_date desc'

	_description = 'data_analyzer'



	_name = 'openhealth.data.analyzer'







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
			], 

			required=True, 
		)




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


		self.count = self.env[self.model].search_count([																							
														#('zone', '=', zone),			
												]) 

		print


