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

		self.target.update_data()

		print





