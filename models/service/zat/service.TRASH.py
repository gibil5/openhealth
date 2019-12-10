
# ----------------------------------------------------------- Nr ofs ------------------------------

	nr_hands_i = fields.Integer(
			'hands',
			#default=0,
			required=False,
		)

	nr_body_local_i = fields.Integer(
			'body local',
			required=False,
		)

	nr_face_local_i = fields.Integer(
			'face local',
			required=False,
		)

	nr_cheekbones = fields.Integer(
			'cheek',
			required=False,
		)

	nr_face_all = fields.Integer(
			'face all',
			required=False,
		)

	nr_face_all_hands = fields.Integer(
			'face all hands',
			required=False,
		)

	nr_face_all_neck = fields.Integer(
			'face all neck',
			required=False,
		)

	nr_neck = fields.Integer(
			'neck',
			required=False,
		)

	nr_neck_hands = fields.Integer(
			'neck hands',
			required=False,
		)



# ----------------------------------------------------------- Methods -----------------------------

	# Open Treatment
	@api.multi
	def open_treatment(self):
		"""
		high level support for doing this and that.
		"""
		ret = self.treatment.open_myself()
		return ret
	# open_treatment


	# Clear all
	def clear_all(self,token):
		"""
		high level support for doing this and that.
		"""
		self.clear_commons()
		self.clear_local()
		return token


	# Clear commons
	def clear_commons(self):
		"""
		high level support for doing this and that.
		"""
		#self.zone = 'none'
		self.pathology = 'none'


	# Clear times
	def clear_times(self,token):
		"""
		high level support for doing this and that.
		"""
		self.time = ''
		self.time_1 = 'none'
		return token


	# Clear Local
	def clear_local(self):
		"""
		high level support for doing this and that.
		"""
		pass


# ----------------------------------------------------------- Getters -----------------------------
	# Product
	def get_product(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Get Product'
		#print self.laser
		#print self.zone
		#print self.pathology
		#print self.time

		#if self.laser != False and self.zone != False and self.pathology != 'none':
		self.service = self.env['product.template'].search([
															('x_treatment', '=', 	self.laser),
															('x_zone', '=', 		self.zone),
															('x_pathology', '=', 	self.pathology),
															('x_time', '=', 		self.time),
													])
		#print self.service

	# Product M22
	def get_product_m22(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Get Product M22'
		self.service = self.env['product.template'].search([
															('x_treatment', '=', 	self.laser),
															('x_zone', '=', 		self.zone),
															('x_pathology', '=', 	self.pathology),
															('x_time', '=', 		self.time),
															('x_sessions', '=', 	self.nr_sessions)
													])

	# Medical
	def get_product_medical(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Get Product Medical'
		self.service = self.env['product.template'].search([
																('x_treatment', '=', 	self.x_treatment),
																('x_sessions', '=', 	self.sessions)
													])





# ----------------------------------------------------------- On changes --------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		if self.service != 'none':
			self.time_1 = self.service.x_time

	@api.onchange('nr_sessions_1')
	def _onchange_nr_sessions_1(self):
		if self.nr_sessions_1 != 'none':
			self.nr_sessions = self.nr_sessions_1
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_sessions', '=', self.nr_sessions) ]},
			}

	@api.onchange('time_1')
	def _onchange_time_1(self):
		if self.time_1 != 'none':
			self.time_1 = self.clear_times(self.time_1)
			self.time = self.time_1
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}




# ----------------------------------------------------------- Testers --------------------------------
	# Computes
	def test_computes(self):
		"""
		high level support for doing this and that.
		"""
		#print
		print('Service - Computes')
		print('name: ', self.name)
		print('name_short: ', self.name_short)
		print('code: ', self.code)
		print('price: ', self.price)
		print('price_vip: ', self.price_vip)


	# Actions
	def test_actions(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Service - Actions'
		self.open_line_current()
		self.open_treatment()
		self.clear_all('token')
		self.clear_times('token')
		self.clear_commons()

		#self.get_product()
		#self.get_product_m22()
		#self.get_product_medical()


	# Test
	def test(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Service - Test'

		# Computes
		self.test_computes()

		# Actions
		self.test_actions()

	# test
