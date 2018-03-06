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

	max_count = fields.Integer(
		)




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
				('order', 						'order'),
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

	# Clear Mark 
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









	# Mark Name 
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








