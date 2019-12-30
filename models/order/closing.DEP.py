# 30 Dec 2019

# ----------------------------------------------------------- Update Totals -----------------------
	# Update Totals
	@api.multi
	def update_totals(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Totals')


		# Proof
		clos_funcs.set_proof_totals(self)

		# Form
		clos_funcs.set_form_totals(self)

		# All
		clos_funcs.set_totals(self)



		# Totals
		self.total_form = self.cash_tot + self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot
		self.total_form_wblack = self.total_proof_wblack
		self.cash_tot_wblack = self.cash_tot - (self.total_form - self.total_form_wblack)

		# Subtotals
		self.total_cards = self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot
		self.total_cash = self.cash_tot

	# update_totals








# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update(self):
		"""
		Build the Closing (Cierre de Caja). For a given day.
		"""
		print()
		print('Update')

		self.update_totals()

		#self.update_month()  	# Dep !











# ----------------------------------------------------------- Update All Months -------------------
	# Update Month
	@api.multi
	def update_month_all(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Month All')


		# Search
		configurator = self.env['openhealth.configurator'].search([
																	('name', 'in', ['closing']),
															],
																	order='date_begin,name asc',
																	limit=1,
														)
		print(configurator)
		print(configurator.name)

		date_begin = configurator.date_begin
		date_end = configurator.date_end

		# Search
		closings = self.env['openhealth.closing'].search([
																	('date', '>=', date_begin),
																	('date', '<', date_end),
																	#('owner', 'in', ['month']),
															],
																	order='date asc',
																	#limit=1000,
														)
		print(closings)

		for closing in closings:
			print(closing.name)
			closing.update_month()





# ----------------------------------------------------------- Update Month ------------------------
	# Update Month
	@api.multi
	def update_month(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update Month')

		month = self.date.split('-')[1]
		self.month = month

		year = self.date.split('-')[0]
		self.year = year






# ----------------------------------------------------------- Dep ---------------------------------
	#test_target = fields.Boolean(
	#		string="Test Target",
	#	)
