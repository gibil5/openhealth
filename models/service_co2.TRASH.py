

# 20 Aug 2018 

	#co2_packages = fields.Selection(
	#		selection = service_co2_vars._co2_pac_list, 
	#		string="Paquetes Rejuvenecimiento", 
	#		default='none',	
	#		)


	#@api.onchange('co2_packages')
	#def _onchange_co2_packages(self):
	#	if self.co2_packages != 'none':	
	#		self.co2_packages = self.clear_all(self.co2_packages)
	#		self.zone = 'package'
	#		self.pathology = self.co2_packages
	#		return {
	#			'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
	#		}	



	# Clear 
		
	#def clear_all(self,token):
	#	self.clear_commons		
	#	self.clear_local  
	#	return token 






	@api.onchange('co2_lb_acneseq')
	def _onchange_co2_lb_acneseq(self):	
#jx			


			#self.service = self.env['product.template'].search([	
																	#('x_treatment', '=', 'laser_co2'),	
																	#('x_zone', '=', 'body_local'),	
																	#('x_pathology', '=', 'acne_sequels_1')

			#														('x_treatment', '=', self.laser),	
			#														('x_zone', '=', self.zone),	
			#														('x_pathology', '=', self.pathology)
			#													])



			#self.service = serv_funcs.product(self.laser, self.zone, self.pathology)




			#self.service = self.env['product.template'].search([	
			#														('x_treatment', '=', self.laser),	
			#														('x_zone', '=', self.zone),	
			#														('x_pathology', '=', self.pathology)
			#													])




