# 10 Dec 2019


# ----------------------------------------------------------- Coder ? -------------------------
	# Coder
	x_coder = fields.Many2one(
			'openhealth.coder',
			'Coder',
		)


# ----------------------------------------------------------- Getters -------------------------

	# Get Treatment
	def get_treatment(self):
		"""
		Get Product Treatment
		Used by: Session, Control
		"""
		return self.x_treatment






# ----------------------------------------------------------- Codes -------------------------------
	# Code
	x_code_acc = fields.Char(
			'Code Acc',
		)

	# Get Code
	@api.multi
	def get_code(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Get Code'

		coder = self.env['openhealth.coder'].search([
															('type', 'in', ['product']),
															('sale_ok', 'in', [True]),
												],
													order='name asc',
													#limit=1,
												)


# ----------------------------------------------------------- Encode Error ------------------------

	@api.multi
	def encode_error(self):
		print()
		print('Encode Error')

		#name = "ECOGRAFIAS MUSCULOESQUELETICAS - Muñeca (Unilateral) - 1 sesion"

		print(self.name)


	@api.multi
	def fix_encode_error(self):
		"""
		Fix Encode Error
		"""
		print()
		print('Fix Encode Error')

		#self.name.replace("ñ", "nh")
		#self.name.replace(u"ñ", "nh")
		self.name = self.name.replace(u"ñ", "nh")

		print('Finished !')




# ----------------------------------------------------------- Fix ------------------------

	@api.multi
	def fix_procurements(self):
		"""
		Fix Procurements
		Set State to Cancel. For Manual Cancellation.
		"""
		print()
		print('Fix Procurements')


		procs = self.env['procurement.order'].search([
															#('type', 'in', ['product']),
															#('sale_ok', 'in', [True]),
												],
													#order='name asc',
													#limit=1,
												)

		for procurement in procs:
			#print()
			#print(procurement)
			#print(procurement.name)
			#print(procurement.state)
			#procurement.unlink()
			procurement.state = 'cancel'
		
		print('Finished !')

	# fix_procurements



	@api.multi
	def fix_stock(self):
		"""
		Cancels stock moves
		Remove manually
		"""
		print('Fix fstock')

		# Search
		moves = self.env['stock.move'].search([
													#('x_name_short', 'in', [name]),
												],
												#order='date_begin asc',
												#limit=10,
											)
		for stock_move in moves:
			#print()
			#print(stock_move)
			#print(stock_move.name)
			#print(stock_move.state)
			#stock_move.unlink()
			stock_move.state = 'cancel'

		print('Finished !')

	# fix_stock_moves


# ----------------------------------------------------------- Fix ------------------------

	@api.multi
	def fix_vic_error(self):
		"""
		Fix Vics
		For VICTAMINA bug
		"""
		print()
		print('Fix Vic Error')


		prods = self.env['product.template'].search([

															('name', 'like', 'VICTAMINA'),
												],
													#order='name asc',
													#limit=1,
												)

		for product in prods:
			print()
			#print(procurement)
			print(product.name)
			#print(procurement.state)
			#procurement.unlink()
			#procurement.state = 'cancel'

			product.name = product.name.replace("VICTAMINA", "VITAMINA")
		

		print('Finished !')

	# fix_vics







# ----------------------------------------------------------- Unfix  ------------------------------
	@api.multi
	def unfix_name(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Unfix Name'

		if self.x_name_unfixed not in [False, '']:
			self.name = self.x_name_unfixed

		if self.x_treatment in ['laser_quick']:
			if self.x_short_unfixed not in [False, '']:
				self.x_name_short = self.x_short_unfixed


# ----------------------------------------------------------- Fix  --------------------------------
	@api.multi
	def fix_name(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Fix Name'

		# Array Name
		name_arr = self.name.split('-')


		# Co2
		if self.x_treatment in ['laser_co2']:

			# To avoid repetition
			if len(name_arr) == 4:

				# Unfixed
				if self.x_name_unfixed in [False, '']:
					self.x_name_unfixed = self.name

				# Fix
				if self.x_go_flag:
					self.name = self.name.replace(" - 1", "")


		# Exc
		if self.x_treatment in ['laser_excilite', 'laser_ipl', 'laser_ndyag']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name

			# Fix
			if self.x_go_flag:
				self.name = self.x_generated



		# Cosmetolgy
		if self.x_family in ['cosmetology']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name

			# Fix
			if self.x_go_flag:
				self.name = self.x_generated




		# Quick
		if self.x_treatment in ['laser_quick']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name


			# Init
			short_arr = self.x_name_short.split('_')

			# Correct the Short Name
			if short_arr[0] in ['quick']:	# To avoid repetition

				# Unfixed
				if self.x_short_unfixed in [False, '']:
					self.x_short_unfixed = self.x_name_short

				short = self.x_name_short
				short_old = short

				for tup in [
								('quick', 'qui'),
								('face_all_hands', 'faa-han'), ('face_all_neck', 'faa-nec'), ('neck_hands', 'nec-han'),
								('body_local', 'bol'), ('face_local', 'fal'), ('face_all', 'faa'),
								('hands', 'han'), ('neck', 'nec'), ('cheekbones', 'che'),
								('rejuvenation', 'rej'), ('acne_sequels', 'acs'), ('scar', 'sca'),
								('mole', 'mol'), ('stains', 'sta'), ('keratosis', 'ker'), ('cyst', 'cys'),
								('tatoo', 'tat'), ('wart', 'war'),
								('1', '5m_one'),
								('2', '15m_one'),
								('3', '30m_one'),
								('4', '45m_one'),
							]:

					old = tup[0]
					new = tup[1]
					short = short.replace(old, new)

				# Fix Short
				if self.x_go_flag:
					self.x_name_short = short


			# Fix
			if self.x_go_flag:
				self.name = self.x_generated




# ----------------------------------------------------------- Test Computes --------------------------------
	# Test 
	@api.multi 
	def test_computes(self):
		#print()
		print('Product - Test Computes')
		print(self.x_name_ticket)
		print(self.x_generated)
		print(self.x_checksum_1)
		print(self.x_checksum_2)


# ----------------------------------------------------------- Test --------------------------------
	# Test 
	@api.multi 
	def test(self):
		#print()
		print('Product - Test')

		# Test Unit
		self.test_computes()
		#self.test_actions()
		#self.test_services()
	# test 


# ----------------------------------------------------------- Actions -----------------------------
	# Update
	@api.multi
	def update_level(self):
		"""
		high level support for doing this and that.
		"""
		#print 'jx'
		#print 'Update Product'
		self.x_level = self.x_pathology[-1]
		#print self.x_level
	# update_level










# 19 Sep 2019

#from . import gen  		# Dep 2019
#from . import gen_tic   	# Dep 2019





# ----------------------------------------------------------- Print Ticket -------------------------------
	#def get_name_ticket(self):
	#	"""
	#	Used by Print Ticket.
	#	"""
	#	return self.x_name_ticket


# ----------------------------------------------------------- Canonical -------------------------------
	#name = fields.Char(
	#	'Name', 
	#	required=True, 
	#	translate=True, 
	#	select=True
	#	)

	#type = fields.Selection(
	#		_get_product_template_type_wrapper, 
	#		'Product Type', 
	#		required=True,
	#       help="A consumable is a product for which you don't manage stock, a service is a non-material product provided by a company or an individual."
	#	)




# ----------------------------------------------------------- Checksum - Dep ----------------------------

	# Checksum 1 - Generated vs Name
	x_checksum_1 = fields.Char(
			'Checksum 1',

			compute='_compute_checksum_1',
		)
	@api.multi
	def _compute_checksum_1(self):
		for record in self:
			record.x_checksum_1 = lib.get_checksum_gen(record.x_generated, record.name)




	# Checksum 2 - Ticket Compact Name
	x_checksum_2 = fields.Char(
			'Checksum 2',

			compute='_compute_checksum_2',
		)
	@api.multi
	def _compute_checksum_2(self):
		for record in self:
			record.x_checksum_2 = lib.get_checksum_tic(record.x_name_ticket)




# ----------------------------------------------------------- Ticket - Dep -------------------------------
	# For Tickets
	x_name_ticket = fields.Char(
			default="x",

			compute='_compute_x_name_ticket',
		)

	@api.multi
	#@api.depends('state')
	def _compute_x_name_ticket(self):
		"""
		high level support for doing this and that.
		"""
		for record in self:
			record.x_name_ticket = gen_tic.gen_ticket_name(self, record.x_treatment, record.x_zone, record.x_pathology, record.x_family, record.type, record.x_name_short)



# ----------------------------------------------------------- Generated - Dep -------------------------------
	# Generated
	x_generated = fields.Char(
			'Generated',

			compute='_compute_generated',
		)
	@api.multi
	def _compute_generated(self):

		treatments = ['laser_excilite', 'laser_ipl', 'laser_ndyag']

		for record in self:

			if record.x_name_short not in [False, '']:

				# Co2
				if record.x_treatment in ['laser_co2']:
					record.x_generated = gen.get_generated_co2(record.x_name_short)

				# Exc, Ipl Ndyag
				elif record.x_treatment in treatments:
					record.x_generated = gen.get_generated_exc(record.x_name_short)

				# Consultation
				elif record.x_treatment in ['consultation']:
					record.x_generated = gen.get_generated_con(record.x_name_short)

				# Medical
				elif record.x_family in ['medical']:
					record.x_generated = gen.get_generated_med(record.x_name_short)

				# Cosmeto
				elif record.x_family in ['cosmetology']:
					record.x_generated = gen.get_generated_exc(record.x_name_short)


				# Products and Consu
				#elif record.type in ['product']:
				elif record.type in ['product', 'consu']:
					record.x_generated = gen.get_generated_prod(record.x_name_short)


				# Quick
				elif record.x_treatment in ['laser_quick']:
					record.x_generated = gen.get_generated_quick(record.x_name_short)


