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


