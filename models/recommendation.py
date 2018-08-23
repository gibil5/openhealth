# -*- coding: utf-8 -*-
#
# 	Recommendation 
# 
#
from openerp import models, fields, api

class recommendation(models.Model):
	
	_name = 'openhealth.recommendation'
	

	name = fields.Char(
			string="Recomendacion #"
		)

	treatment = fields.Many2one(
			'openhealth.treatment',		
			readonly=True, 				
			ondelete='cascade', 
			)




# ---------------------------------------------- Create Service - product --------------------------------------------------------

	@api.multi
	def create_service_product(self):  

		patient_id = self.treatment.patient.id
		physician_id = self.treatment.physician.id
		treatment_id = self.treatment.id 
		
		
		laser = 'laser_vip'
		x_treatment = False		
		zone = False			
		pathology = ''
		

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - product', 

				'res_model': 'openhealth.service.product',		

				#'res_id': consultation_id,
				"views": [[False, "form"]],
				#'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',

				'flags': 	{
								'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
							},

				'context': {							

								'default_patient': patient_id,
								'default_physician': physician_id,
								'default_treatment': treatment_id,
								
								'default_zone': zone,
								'default_pathology': pathology,
								'default_x_treatment': x_treatment,

								#'default_laser': laser,							
							}
				}
	# create_service_product









# ---------------------------------------------- Create Service - vip --------------------------------------------------------

	@api.multi
	def create_service_vip(self):  


		patient_id = self.treatment.patient.id
		physician_id = self.treatment.physician.id
		treatment_id = self.treatment.id 
		
		
		#laser = 'laser_vip'
		x_treatment = False		
		zone = False			
		pathology = ''
		

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Vip', 

				'res_model': 'openhealth.service.vip',		

				#'res_id': consultation_id,
				"views": [[False, "form"]],
				#'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',

				'flags': 	{
								'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
							},

				'context': {							

								'default_patient': patient_id,
								'default_physician': physician_id,
								'default_treatment': treatment_id,
								
								'default_zone': zone,
								'default_pathology': pathology,
								'default_x_treatment': x_treatment,

								#'default_laser': laser,							
							}
				}
	# create_service_vip






# ---------------------------------------------- Create Service - quick --------------------------------------------------------

	@api.multi
	def create_service_quick(self):  


		patient_id = self.treatment.patient.id
		physician_id = self.treatment.physician.id


		# Quick 
		#nr_hands = self.treatment.nr_quick_hands
		#nr_body_local = self.treatment.nr_quick_body_local
		#nr_face_local = self.treatment.nr_quick_face_local

		#nr_cheekbones = self.treatment.nr_quick_cheekbones
		#nr_face_all = self.treatment.nr_quick_face_all
		#nr_face_all_hands = self.treatment.nr_quick_face_all_hands

		#nr_face_all_neck = self.treatment.nr_quick_face_all_neck
		#nr_neck = self.treatment.nr_quick_neck
		#nr_neck_hands = self.treatment.nr_quick_neck_hands




		treatment_id = self.treatment.id 

		laser = 'laser_quick'

		#x_treatment = False	
		x_treatment = 'laser_quick'	

		zone = False	
				
		pathology = ''
		
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser quick', 

				'res_model': 'openhealth.service.quick',				
				#'res_id': consultation_id,

				"views": [[False, "form"]],

				#'view_type': 'form',
				
				'view_mode': 'form',	
				
				'target': 'current',


				'flags': 	{
								'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
							},


				'context': {
								# Quick 
								#'default_nr_hands_i': nr_hands, 
								#'default_nr_body_local_i': nr_body_local, 
								#'default_nr_face_local_i': nr_face_local, 

								#'default_nr_cheekbones': nr_cheekbones, 
								#'default_nr_face_all': nr_face_all, 
								#'default_nr_face_all_hands': nr_face_all_hands, 

								#'default_nr_face_all_neck': nr_face_all_neck, 
								#'default_nr_neck': nr_neck, 
								#'default_nr_neck_hands': nr_neck_hands, 


								'default_patient': patient_id,
								'default_physician': physician_id,
								'default_laser': laser,							
								'default_zone': zone,
								'default_pathology': pathology,

								'default_x_treatment': x_treatment,

								'default_treatment': treatment_id,
							}
				}
	# create_service_quick

















# ---------------------------------------------- Create Service - Co2 --------------------------------------------------------

	@api.multi
	def create_service_co2(self):  
		treatment_id = self.treatment.id 
		x_treatment = False
		laser = 'laser_co2'
		zone = False			
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
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': False, }
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

		consultation_id = self.id 
		treatment_id = self.treatment.id 
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
							'default_treatment': treatment_id,
							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,
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
								
				'res_model': 'openhealth.service.ipl',				
				#'res_id': 23,
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_treatment': treatment_id,
							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,
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
								
				'res_model': 'openhealth.service.ndyag',				
				#'res_id': 23,
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_treatment': treatment_id,
							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,
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
							'default_treatment': treatment_id,
							'default_family': family,
							'default_laser': laser,
							}
				}
					
	# create_service_medical








# ---------------------------------------------- Create Service - Cosmetology --------------------------------------------------------

	@api.multi
	def create_service_cosmetology(self):  

		consultation_id = self.id 

		treatment_id = self.treatment.id 		
		
		family = 'cosmetology'
		
		laser = 'cosmetology'
		
		zone = ''	
		
		pathology = ''

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Cosmetology', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',
				
				'res_model': 'openhealth.service.cosmetology',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_treatment': treatment_id,
							'default_family': family,
							'default_laser': laser,
							}
				}
					
	# create_service_medical
