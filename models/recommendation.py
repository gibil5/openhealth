# -*- coding: utf-8 -*-
#
# 	Recommendation 
# 
#

from openerp import models, fields, api



class recommendation(models.Model):
	
	_name = 'openhealth.recommendation'
	#_inherit='sale.order'
	




	name = fields.Char(
			string="Recomendacion #"
		)



	treatment = fields.Many2one(
			'openhealth.treatment',		
			readonly=True, 				
			ondelete='cascade', 
			)



	#consultation = fields.Many2many(
	#		'openhealth.consultation',			
			#ondelete='cascade', 
	#		)









# ---------------------------------------------- Create Service - Co2 --------------------------------------------------------

	@api.multi
	def create_service_co2(self):  

		#consultation_id = self.consultation
		#consultation = self.env['openhealth.consultation'].search([('treatment','=', self.treatment.id)]) 
		#consultation_id = consultation.id



		treatment_id = self.treatment.id 


		x_treatment = False

		laser = 'laser_co2'

		zone = False			
		#zone = ''	
		
		pathology = ''
		
		
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Co2', 

				'res_model': 'openhealth.service.co2',				
				#'res_id': consultation_id,


				"views": [[False, "form"]],
				#'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': True, }
							'form': {'action_buttons': False, }
							},


				'context': {							
							'default_treatment': treatment_id,

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							'default_x_treatment': x_treatment,
							}
				}

	# create_service_co2





# ---------------------------------------------- Create Service - Excilite --------------------------------------------------------
	 
	@api.multi
	def create_service_excilite(self):  

		print 
		print 'jx'
		print 'Create Service Excilite'
		print 

		consultation_id = self.id 
		treatment_id = self.treatment.id 
		
		print consultation_id
		print treatment_id
		print 


		laser = 'laser_excilite'
		zone = ''	
		pathology = ''
				

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Excilite', 

				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',				
								

				'res_model': 'openhealth.service.excilite',				
				#'res_id': 23,
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {

							#'default_consultation': consultation_id,	
							'default_treatment': treatment_id,


							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							#'default_x_treatment': x_treatment,
							}
				}
				
	# create_service_excilite
		
				


				
# ---------------------------------------------- Create Service - IPL --------------------------------------------------------
		
	@api.multi
	def create_service_ipl(self):  

		consultation_id = self.id 
		treatment_id = self.treatment.id 

		
		laser = 'laser_ipl'
		zone = ''	
		pathology = ''
			

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Excilite', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',				
				
				#'res_id': 23,
				
				'res_model': 'openhealth.service.ipl',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							#'default_consultation': consultation_id,					
							'default_treatment': treatment_id,

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							#'default_x_treatment': x_treatment,
							}
				}

	# create_service_ipl




# ---------------------------------------------- Create Service - NDYAG --------------------------------------------------------
	
	@api.multi
	def create_service_ndyag(self):  

		consultation_id = self.id 
		treatment_id = self.treatment.id 

		
		laser = 'laser_ndyag'
		zone = ''	
		pathology = ''
				

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Ndyag', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',				
				
				#'res_id': 23,
				
				'res_model': 'openhealth.service.ndyag',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							#'default_consultation': consultation_id,					
							'default_treatment': treatment_id,

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							#'default_x_treatment': x_treatment,
							}
				}
	
	# create_service_ndyag



	
# ---------------------------------------------- Create Service - MEDICAL --------------------------------------------------------

	@api.multi
	def create_service_medical(self):  

		consultation_id = self.id 
		treatment_id = self.treatment.id 

		
		family = 'medical'

		laser = 'medical'
		zone = ''	
		pathology = ''

		

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Medical', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',
				
				'res_model': 'openhealth.service.medical',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							#'default_consultation': consultation_id,					
							'default_treatment': treatment_id,

							'default_family': family,
							'default_laser': laser,
							#'default_zone': zone,
							#'default_pathology': pathology,

							#'default_x_treatment': x_treatment,
							}
				}
					
	# create_service_medical


