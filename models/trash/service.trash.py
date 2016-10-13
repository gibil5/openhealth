class ServiceBase(models.Model):
	#_name = 'openhealth.service'
	_inherit = 'product.template'


	def get_domain_servicebase(self,cr,uid,ids,context=None):

		context='laser_co2'
		print
		print context
		print 
		
		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																('x_treatment', '=', context)
																])
		return {'domain':{'service':[('id','in',lids)]}}








	co2_cheekbone = fields.Selection(
			selection = jxvars._co2_che_list, 
			string="Pómulos", 
			default='x',	
			)

	co2_hands = fields.Selection(
			selection = jxvars._co2_han_list, 
			string="Manos", 
			default='x',	
			)

	co2_neck = fields.Selection(
			selection = jxvars._co2_nec_list, 
			string="Cuello", 
			default='x',	
			)
	
	co2_vagina = fields.Selection(
			selection = jxvars._co2_vag_list, 
			string="Vagina", 
			default='x',	
			)
			
	co2_packages = fields.Selection(
			selection = jxvars._co2_pac_list, 
			string="Paquetes Rejuvenecimiento", 
			default='x',	
			)


	co2_allface_rejuvenation = fields.Selection(
			selection = jxvars._co2_rejuv_list, 
			string="Rejuvenecimiento facial", 
			default='x',	
			)

	co2_allface_acnesequels = fields.Selection(
			selection = jxvars._co2_acneseq_list, 
			string="Acné y secuelas", 
			default='x',	
			)




	co2_localface_stains = fields.Selection(
			selection = jxvars._co2_lfstains_list, 
			string="Manchas", 
			default='x',	
			)

	co2_localface_queratosis = fields.Selection(
			selection = jxvars._co2_lfqueratosis_list, 
			string="Queratosis", 
			default='x',	
			)

	co2_localface_mole = fields.Selection(
			selection = jxvars._co2_lfmole_list, 
			string="Lunar", 
			default='x',	
			)
			
	co2_localface_scar = fields.Selection(
			selection = jxvars._co2_lfscar_list, 
			string="Cicatriz", 
			default='x',	
			)

	co2_localface_cyst = fields.Selection(
			selection = jxvars._co2_lfcyst_list, 
			string="Quiste", 
			default='x',	
			)

	co2_localface_wart = fields.Selection(
			selection = jxvars._co2_lfwart_list, 
			string="Verruga", 
			default='x',	
			)








	time_2 = fields.Selection(
			selection = exc._time_list, 
			string="Tiempo", 
			default='none',	
			)

	time_3 = fields.Selection(
			selection = exc._time_list, 
			string="Tiempo", 
			default='none',	
			)
			
			
			
			
			
			
	@api.onchange('time_2')
	def _onchange_time_2(self):
	
		if self.time_2 != 'none':	
			
			self.time_2 = self.clear_all_times(self.time_2)

			self.time = self.time_2
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}
			
			
	@api.onchange('time_3')
	def _onchange_time_3(self):
	
		if self.time_3 != 'none':	
			
			self.time_3 = self.clear_all_times(self.time_3)

			self.time = self.time_3
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}
			
	
	
	# Client type 
	
	client_type = fields.Char(
			default='',	
	)
	
	
	client_type_1 = fields.Selection(
			selection = ipl._ctype_list, 
			string="Tipo de cliente", 
			default='none',	
			)


	@api.onchange('client_type_1')
	def _onchange_client_type_1(self):
	
		if self.client_type_1 != 'none':	
			#self.client_type_1 = self.clear_all(self.client_type_1)
			self.client_type = self.client_type_1
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_client_type', '=', self.client_type) ]},
			}
	