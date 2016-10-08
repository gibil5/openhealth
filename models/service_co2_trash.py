	@api.onchange('co2_hands_stains')
	def _onchange_co2_hands_stains(self):
		if self.co2_hands_stains == True:		
			#self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

	@api.onchange('co2_hands_scar')
	def _onchange_co2_hands_scar(self):
		if self.co2_hands_scar == True:	
			self.co2_hands_stains = False
			#self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

	@api.onchange('co2_hands_wart')
	def _onchange_co2_hands_wart(self):
		if self.co2_hands_wart == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			#self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

	@api.onchange('co2_hands_rejuvenation')
	def _onchange_co2_hands_rejuvenation(self):
		if self.co2_hands_rejuvenation == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			#self.co2_hands_rejuvenation = False







	# Booleans
	
	co2_hands_stains = fields.Boolean(
			string="Manchas", 
			default=False,	
			#compute='_compute_co2_hands_stains', 
			)
	#@api.depends('co2_hands_scar')
	#def _compute_co2_hands_stains(self):
	#	for record in self:
	#		record.hands_stains=True
	
	
	
			
	co2_hands_scar = fields.Boolean(
			string="Cicatriz", 
			default=False,	
			)
	co2_hands_wart = fields.Boolean(
			string="Verruga", 
			default=False,	
			)
	co2_hands_rejuvenation = fields.Boolean(
			string="Rejuvenecimiento", 
			default=False,	
			)





	# On change 

	# Smart 

	#@api.onchange('co2_hands_stains', 'co2_hands_scar', 'co2_hands_wart', 'co2_hands_rejuvenation')
	#@api.onchange('field1', 'field2')
	
	@api.onchange('co2_hands_stains', 'co2_hands_scar')
	def _onchange_co2_hands(self):
		
		print
		print 'jx'
		print
		
		if self.co2_hands_stains == True:		
			#self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_scar == True:	
			self.co2_hands_stains = False
			#self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_wart == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			#self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_rejuvenation == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			#self.co2_hands_rejuvenation = False

			



	co2_neck_scar = fields.Boolean(
			string="Cuello Cicatriz", 
			default=False,	
			#compute='_compute_co2_neck', 
			)





			
	@api.depends('co2_hands')
	def _compute_co2_neck(self):
		for record in self:
			record.co2_neck=False
			
			
			
			
			
			
			
	
	@api.multi
	def clear_all(self):
	#def clear_all(self,cr,uid,ids,context=None):
		
		
		self.co2_hands = False
		self.co2_cheekbone = False
		self.co2_neck = False
		self.co2_vagina = False
		self.co2_packages = False

		self.co2_neck_scar = False
		
		print
		print self.co2_hands
		print
		
		#print 'jx: Mark'
		#print context 

		return {}
		
		
	
	
	
	def clear_others(self,me):
		arr = [ 
				self.co2_allface_rejuvenation, 
				self.co2_allface_acnesequels, 
			]
		for vax in arr:
			if me != vax: 
				print vax
				vax = 'none'
				print vax 
		print
		
		
		
		
	#@api.onchange('co2_allface_rejuvenation', 'co2_allface_acnesequels')
	
	#def _onchange_co2_allface(self):
	#	print 
	#	print 'jx'

	#	if self.co2_allface_rejuvenation != 'none':
	#		self.co2_allface_acnesequels = 'none'
	#		print 'rejuv'

	#	if self.co2_allface_acnesequels != 'none':
	#		self.co2_allface_rejuvenation = 'none'
	#		print 'acneseq'
		
	#	print
		
		


	@api.onchange('co2_allface_rejuvenation')
	def _onchange_co2_afr(self):

		if self.co2_allface_rejuvenation != 'none':				
			self.co2_allface_acnesequels = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'face_all'),('x_pathology', '=', self.co2_allface_rejuvenation)]},
		}
		
		
	@api.onchange('co2_allface_acnesequels')
	def _onchange_co2_afa(self):

		if self.co2_allface_acnesequels != 'none':	
			self.co2_allface_rejuvenation = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'face_all'),('x_pathology', '=', self.co2_allface_acnesequels)]},
		}
		
		
		
		
		
	_lb_vars = [ 
		#self.co2_lb_acneseq,
		#self.co2_lb_stains,
		#self.co2_lb_queratosis,
		#self.co2_lb_mole,		
		#self.co2_lb_scar,
		#self.co2_lb_cyst,
		#self.co2_lb_wart,

		#co2_lb_acneseq,
		co2_lb_stains,
		co2_lb_queratosis,
		co2_lb_mole,		
		co2_lb_scar,
		co2_lb_cyst,
		co2_lb_wart,

		]
		
		
		
	#def clear_all(self,idx):
		
		#if idx != 0:
		#	self.co2_lb_acneseq = 'none'

		#if idx != 1:
		#	self.co2_lb_scar = 'none'

		#if idx != 2:
		#	self.co2_lb_mole = 'none'

		#if idx != 3:
		#	self.co2_lb_stains = 'none'

		#if idx != 4:
		#	self.co2_lb_queratosis = 'none'

		#if idx != 5:
		#	self.co2_lb_cyst = 'none'
		
		#if idx != 6:
		#	self.co2_lb_wart = 'none'
	
	
	@api.onchange('co2_lf_stains')
	def _onchange_co2_lf_stains(self):

		if self.co2_lf_stains != 'none':	
			
			#self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}


	@api.onchange('co2_lf_queratosis')
	def _onchange_co2_lf_queratosis(self):

		if self.co2_lf_queratosis != 'none':	
			
			self.co2_lf_stains = 'none'
			#self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}
		
		
	@api.onchange('co2_lf_mole')
	def _onchange_co2_lf_mole(self):

		if self.co2_lf_mole != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			#self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}







	@api.onchange('co2_lf_scar')
	def _onchange_co2_lf_scar(self):

		if self.co2_lf_scar != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			#self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}
		
		
	@api.onchange('co2_lf_cyst')
	def _onchange_co2_lf_cyst(self):

		if self.co2_lf_cyst != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			#self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}		


	@api.onchange('co2_lf_wart')
	def _onchange_co2_lf_wart(self):

		if self.co2_lf_wart != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			#self.co2_lf_wart = 'none'
				
		return {}



	@api.onchange('co2_allface_rejuvenation')
	def _onchange_co2_afr(self):
		print 
		print 'a'
		
		if self.co2_allface_rejuvenation != 'none':				
			self.co2_allface_acnesequels = 'none'
			#self.co2_allface_rejuvenation = 'none'

		print 
		return {}


	@api.onchange('co2_allface_acnesequels')
	def _onchange_co2_afa(self):
		print 
		print 'b'

		if self.co2_allface_acnesequels != 'none':	
			self.co2_allface_rejuvenation = 'none'
			
		print 
		return {}

	
	
	
	
	
	
	@api.onchange('co2_hands')
	def _onchange_co2_hands(self):
		
		if self.co2_hands != 'none':	
			
			#self.co2_hands = 'none'
			self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'hands'),('x_pathology', '=', self.co2_hands)]},
		}


		
	@api.onchange('co2_neck')
	def _onchange_co2_neck(self):

		if self.co2_neck != 'none':	
			
			self.co2_hands = 'none'
			#self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'neck'),('x_pathology', '=', self.co2_neck)]},
		}



	@api.onchange('co2_cheekbone')
	def _onchange_co2_cheekbone(self):

		if self.co2_cheekbone != 'none':	
			self.co2_hands = 'none'
			self.co2_neck = 'none'
			#self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'cheekbone'),('x_pathology', '=', self.co2_cheekbone)]},
		}



	@api.onchange('co2_vagina')
	def _onchange_co2_vagina(self):

		if self.co2_vagina != 'none':	
			
			self.co2_hands = 'none'
			self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			#self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'vagina'),('x_pathology', '=', self.co2_vagina)]},
		}
		
		
		
	@api.onchange('co2_packages')
	def _onchange_co2_packages(self):

		if self.co2_packages != 'none':	
			
			self.co2_hands = 'none'
			self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			#self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'packages'),('x_pathology', '=', self.co2_packages)]},
		}	





	
	
		
		