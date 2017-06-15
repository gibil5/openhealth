# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Service Cosmetology
# 
# Created: 				18 Feb 2017
# Last updated: 	 	20 Feb 2017



from openerp import models, fields, api
from datetime import datetime



from . import prodvars
from . import cosvars



class ServiceCosmetology(models.Model):

	_name = 'openhealth.service.cosmetology'
	
	_inherit = 'openhealth.service'
	
	

# ----------------------------------------------------------- Canonicals ------------------------------------------------------

	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						#('type', '=', 'service'),
						#('x_treatment', '=', 'carboxytherapy'),
						('x_family', '=', 'cosmetology'),
					],
		)
	
	



	time_1 = fields.Selection(
			selection = prodvars._time_list, 
			string="Tiempo", 
			default='none',	
			)






	# Criosurgery
	cos_dia = fields.Selection(
			selection = cosvars._cos_dia_list, 
			default='none',

			string="Rostro (Limpieza facial profunda)",
			)





	# Carboxytherapy 

	cos_car_fac = fields.Selection(
			selection = cosvars._cos_car_list, 
			default='none',	
			string="Rostro",
			)


	cos_car_bod = fields.Selection(
			selection = cosvars._cos_car_list, 
			default='none',	
			string="Cuerpo",
			)





	# Laser Triactive
	cos_tri_fac = fields.Selection(
			selection = cosvars._cos_tri_list, 
			default='none',	
			string="Rostro, Papada y Cuello",
			)

	cos_tri_bod = fields.Selection(
			selection = cosvars._cos_tri_list, 
			default='none',	
			string="Todo Cuerpo",
			)





# ----------------------------------------------------------- On Changes ------------------------------------------------------


	# Diamond
	@api.onchange('cos_dia')
	def _onchange_cos_dia(self):
		
		if self.cos_dia != 'none':
			#print 
			#print 'cos_dia'
			#print 


			self.cos_dia = self.clear_all_med(self.cos_dia)
			#self.clear_local()



			self.x_treatment = 'diamond_tip'

			self.zone = 'face'

			self.pathology = 'deep_face_cleansing'
								
			self.time = '30 min'



			self.sessions = self.cos_dia

			return {
				'domain': {'service': [

										('x_treatment', '=', self.x_treatment),
				
										('x_sessions', '=', self.sessions),

										]},
			}







	# Carboxytherapy - Face

	@api.onchange('cos_car_fac')
	def _onchange_cos_car_fac(self):
		
		if self.cos_car_fac != 'none':
			#print 
			#print 'cos_car_fac'
			#print 

			self.cos_car_fac = self.clear_all_med(self.cos_car_fac)



			self.x_treatment = 'carboxytherapy'

			self.zone = 'face'

			self.pathology = 'rejuvenation_face'
								
			self.time = '30 min'


			self.sessions = self.cos_car_fac

			return {
				'domain': {'service': [

										('x_treatment', '=', self.x_treatment),
				
										('x_zone', '=', self.zone),

										('x_sessions', '=', self.sessions),

										]},
			}



	# Carboxytherapy - Body

	@api.onchange('cos_car_bod')
	def _onchange_cos_car_bod(self):
		
		if self.cos_car_bod != 'none':
			#print 
			#print 'cos_car_bod'
			#print 

			self.cos_car_bod = self.clear_all_med(self.cos_car_bod)



			self.x_treatment = 'carboxytherapy'

			self.zone = 'body'

			self.pathology = 'rejuvenation_face'
								
			self.time = '30 min'


			self.sessions = self.cos_car_bod


			return {
				'domain': {'service': [

										('x_treatment', '=', self.x_treatment),
				
										('x_zone', '=', self.zone),

										('x_sessions', '=', self.sessions),

										]},
			}




















	# Laser Triactive - Face
	@api.onchange('cos_tri_fac')
	def _onchange_cos_tri_fac(self):
		
		if self.cos_tri_fac != 'none':
			#print 
			#print 'cos_tri_fac'
			#print 

			self.cos_tri_fac = self.clear_all_med(self.cos_tri_fac)
			#self.clear_local()


			self.x_treatment = 'triactive_carboxytherapy'

			self.zone = 'face_doublechin_neck'

			self.pathology = 'reaffirmation'
								
			self.time = '30 min'



			self.sessions = self.cos_tri_fac


			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
				
										('x_zone', '=', self.zone),

										('x_sessions', '=', self.sessions),
										]},
			}






	# Laser Triactive - Body
	@api.onchange('cos_tri_bod')
	def _onchange_cos_tri_bod(self):
		
		if self.cos_tri_bod != 'none':
			#print 
			#print 'cos_tri_bod'
			#print 

			self.cos_tri_bod = self.clear_all_med(self.cos_tri_bod)
			#self.clear_local()


			self.x_treatment = 'triactive_carboxytherapy_reductionchamber'

			self.zone = 'body_all'

			self.pathology = 'reduction_weight_measures'
								
			self.time = '30 min'



			self.sessions = self.cos_tri_bod


			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
				
										('x_zone', '=', self.zone),

										('x_sessions', '=', self.sessions),
										]},
			}










# ----------------------------------------------------------- Functions ------------------------------------------------------

	def clear_all_med(self,token):		
		#self.clear_commons()
		self.clear_local_cos()
		return token


	@api.multi
	def clear_local_cos(self):

		#print 'clear_local_cos'
		
		self.cos_dia = 'none'
		self.cos_car = 'none'
		self.cos_tri = 'none'

		

