# 7 Dec 2019

# Updates



# ----------------------------------------------------------- Update Stats ------------------------
	def update_stats(self):
		"""
		Update Stats - Doctors, Families, Sub-families
		"""
		#print()
		#print('Update Stats')

		# Using collections - More Abstract !

		# Clean
		self.family_line.unlink()
		self.sub_family_line.unlink()

		# Init
		family_arr = []
		sub_family_arr = []
		_h_amount = {}
		_h_sub = {}

	# All
		# Loop - Doctors
		for doctor in self.doctor_line:

			# Loop - Order Lines
			for line in doctor.order_line:

				# Family
				family_arr.append(line.family)

				# Sub family
				sub_family_arr.append(line.sub_family)

				# Amount - Family
				if line.family in _h_amount:
					_h_amount[line.family] = _h_amount[line.family] + line.price_total

				else:
					_h_amount[line.family] = line.price_total

				# Amount - Sub Family
				if line.sub_family in _h_sub:
					_h_sub[line.sub_family] = _h_sub[line.sub_family] + line.price_total

				else:
					_h_sub[line.sub_family] = line.price_total

			# Doctor Stats
			doctor.stats()


	# By Family

		# Count
		counter_family = collections.Counter(family_arr)

		# Create
		for key in counter_family:
			count = counter_family[key]
			amount = _h_amount[key]
			family = self.family_line.create({
													'name': key,
													'x_count': count,
													'amount': amount,
													'management_id': self.id,
												})
			family.update()

			# Percentage
			if self.total_amount != 0:
				family.per_amo = family.amount / self.total_amount



	# Subfamily

		# Count
		counter_sub_family = collections.Counter(sub_family_arr)

		# Create
		for key in counter_sub_family:
			count = counter_sub_family[key]
			amount = _h_sub[key]
			sub_family = self.sub_family_line.create({
														'name': key,
														'x_count': count,
														'amount': amount,
														'management_id': self.id,
												})
			sub_family.update()

			# Percentage
			if self.total_amount != 0:
				sub_family.per_amo = sub_family.amount / self.total_amount

	# update_stats



# ----------------------------------------------------------- Update - Fast -----------------------
	# Update
	@api.multi
	def update_fast(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Update Fast')
		t0 = timer()
		self.update_sales_fast()
		t1 = timer()
		self.delta_fast = t1 - t0
		#print self.delta_fast
		#print
	# update


# ----------------------------------------------------------- Update Prod -------------------------
	# Update Days
	@api.multi
	def update_productivity(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Productivity')
		
		self.create_days()
		#print(self.day_line)

		self.update_day_cumulative()
		
		self.update_day_avg()


# ----------------------------------------------------------- Update Daily -------------------------
	# Update Daily
	@api.multi
	def update_daily(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update daily')
		for doctor in self.doctor_line:
			doctor.update_daily()


# ----------------------------------------------------------- Update Doctors ----------------------
	# Update
	@api.multi
	def update_doctors(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Doctors')
		t0 = timer()

		self.update_sales_by_doctor()

		self.update_stats()

		#self.update_counters()
		#self.update_qc()
		t1 = timer()
		self.delta_doctor = t1 - t0
		#print self.delta_doctor
		#print
	# update_doctors



# ----------------------------------------------------------- Update Sales - By Doctor ------------

	# Update Sales
	def update_sales_by_doctor(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update Sales - By Doctor')

		# Clean
		self.doctor_line.unlink()

		# Init vars
		total_amount = 0
		total_count = 0
		total_tickets = 0

		# Create Doctors
		doctors = [
					'Dr. Chavarri',
					'Dr. Canales',
					'Dr. Gonzales',
					'Dr. Monteverde',
					'Eulalia',
					'Dr. Abriojo',
					'Dr. Castillo',
					'Dr. Loaiza',
					'Dr. Escudero',
					'Clinica Chavarri',
				]


		# Loop
		for doctor in doctors:
			doctor = self.doctor_line.create({
												'name': doctor,

												'management_id': self.id,
										})



		# Create Sales - By Doctor
		for doctor in self.doctor_line:

			#print(doctor.name)

			# Clear
			doctor.order_line.unlink()


#jx
			# Orders
			# Must include Credit Notes
			orders, count = mgt_funcs.get_orders_filter_by_doctor\
															(self, self.date_begin, self.date_end, doctor.name)

			#print(orders)
			#print(count)



			# Init Loop
			amount = 0
			count = 0
			tickets = 0


			# Loop
			for order in orders:

				# Tickets
				tickets = tickets + 1

				# Filter Block
				if not order.x_block_flow:


					# Parse Data

					# Amount
					#amount = amount + order.amount_total

					# Amount with State
					if order.state in ['credit_note']:
						#amount = amount - order.amount_total
						#amount = amount - order.amount_total
						#amount = amount - order.x_credit_note_amount
						
						amount = amount + order.x_amount_flow
						
						print('Gotcha !')
						print(amount)

					elif order.state in ['sale']:
						amount = amount + order.amount_total




					# Id Doc
					if order.x_type in ['ticket_invoice', 'invoice']:
						receptor = order.patient.x_firm.upper()
						id_doc = order.patient.x_ruc
						id_doc_type = 'ruc'
						id_doc_type_code = '6'
					else:
						receptor = order.patient.name
						id_doc = order.patient.x_id_doc
						id_doc_type = order.patient.x_id_doc_type
						id_doc_type_code = order.patient.x_id_doc_type_code
						# Pre-Electronic
						if id_doc_type is False or id_doc is False:
							id_doc = order.patient.x_dni
							id_doc_type = 'dni'
							id_doc_type_code = '1'




					# Sale
					if order.state in ['sale']:  	# Sale - Do Line Analysis

						# Order Lines
						for line in order.order_line:

							count = count + 1

							
							# State
							#if order.state in ['credit_note']:
							#	price_unit = -line.price_unit
							#elif order.state in ['sale']:
							#	price_unit = line.price_unit

							
							# Price
							price_unit = line.price_unit
							

							# Here !!!
							#jx
							order_line = doctor.order_line.create({
																	'date_order_date': order.date_order,
																	'x_date_created': order.date_order,

																	'name': order.name,
																	'receptor': 	receptor,
																	'patient': 		order.patient.id,
																	'doctor': order.x_doctor.id,
																	'serial_nr': order.x_serial_nr,

																	# Type of Sale
																	'type_code': 	order.x_type_code,
																	'x_type': 		order.x_type,

																	# Id Doc
																	'id_doc': 				id_doc,
																	'id_doc_type': 			id_doc_type,
																	'id_doc_type_code': 	id_doc_type_code,

																	# State
																	'state': order.state,

																	# Handles
																	'doctor_id': doctor.id,
																	'management_id': self.id,



																	# Line
																	'product_id': 			line.product_id.id,
																	'product_uom_qty': 		line.product_uom_qty,

																	# Price
																	'price_unit': 			price_unit,
																})
							order_line.update_fields()
						# Line Analysis - End
					# Conditional State Sale - End



					# Credit Note
					elif order.state in ['credit_note']:

						# Price
						price_unit = order.x_amount_flow

						# Here !!!
						#jx
						order_line = doctor.order_line.create({
																'date_order_date': order.date_order,
																'x_date_created': order.date_order,

																'name': order.name,
																'receptor': 	receptor,
																'patient': 		order.patient.id,
																'doctor': order.x_doctor.id,
																'serial_nr': order.x_serial_nr,

																# Type of Sale
																'type_code': 	order.x_type_code,
																'x_type': 		order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# State
																'state': order.state,

																# Handles
																'doctor_id': doctor.id,
																'management_id': self.id,



																# Line
																#'product_id': 			product_id.id,
																'product_uom_qty': 		1,

																# Price
																'price_unit': 			price_unit,
															})

						order_line.update_fields()
					# Conditional State CN - End

				# Filter Block - End

			# Loop - End



			# Stats
			doctor.amount = amount
			doctor.x_count = count
			# Percentage
			if self.total_amount != 0: 
				doctor.per_amo = (doctor.amount / self.total_amount)


			# Totals - Dep !
			#total_amount = total_amount + amount
			#total_count = total_count + count
			#total_tickets = total_tickets + tickets

	# update_sales_by_doctor












	# Doctor
	#doctor_line = fields.One2many(
	#		'openhealth.management.doctor.line',
	#		'management_id',
	#	)


# ----------------------------------------------------------- DEP ----------------------

	# State Array - Dep !
	#state_arr = fields.Char()

	#state_arr = fields.Selection(
	#		selection=mgt_vars._state_arr_list,
	#		string='State Array',
	#		default='sale',
	#		required=True,
	#	)

	# Time Line
	#base_dir = fields.Char()









# 4 May 2019


	# Container
	container = fields.Many2one(
			'openhealth.container',
		)


# ----------------------------------------------------------- Dep ----------------------------------
	# Electronic
	electronic_order = fields.One2many(
			'openhealth.electronic.order',
			'management_id',
		)


# ----------------------------------------------------------- Electronic - Clear ------------------
	# Clear
	@api.multi
	def clear_electronic(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Electronic - Clear'
		# Clean
		self.electronic_order.unlink()


# ----------------------------------------------------------- Update Sales - Electronic -----------

	# Update Electronic
	@api.multi
	def update_electronic(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update - Electronic')

		# Clean
		self.electronic_order.unlink()


		# Orders
		orders, count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, \
																						self.state_arr, self.type_arr)
		print(orders)
		print(count)

		# Init
		amount_total = 0
		receipt_count = 0
		invoice_count = 0

		# Loop
		for order in orders:
			#print order
			#print order.x_type

			# Generate Id Doc
			if order.x_type in ['ticket_invoice', 'invoice']:
				receptor = order.patient.x_firm.upper()
				id_doc = order.patient.x_ruc
				id_doc_type = 'ruc'
				id_doc_type_code = '6'
			else:
				receptor = order.patient.name
				id_doc = order.patient.x_id_doc
				id_doc_type = order.patient.x_id_doc_type
				id_doc_type_code = order.patient.x_id_doc_type_code

			# Patch
			#if order.patient.x_id_doc == False and order.patient.x_id_doc_type == False:
			if not order.patient.x_id_doc and not order.patient.x_id_doc_type:
				if order.patient.x_dni != False:
					id_doc = order.patient.x_dni
					id_doc_type = 'dni'
					id_doc_type_code = 1


			#print(receptor)
			#print(id_doc)
			#print(id_doc_type)
			#print(id_doc_type_code)


			# Create Electronic Order
			electronic_order = self.electronic_order.create({
																#'amount_total': 		order.amount_total,
																'amount_total_net': 	order.x_total_net,
																'amount_total_tax': 	order.x_total_tax,

																'amount_total': 		order.x_amount_flow,



																'receptor': 		receptor,
																'patient': 			order.patient.id,
																'name': 			order.name,
																'x_date_created': 	order.date_order,
																'doctor': 			order.x_doctor.id,
																'state': 			order.state,
																'serial_nr': 		order.x_serial_nr,
																'type_code': 		order.x_type_code,
																'x_type': 			order.x_type,
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																
																'counter_value': 		order.x_counter_value,
																'delta': 				order.x_delta,

																'management_id': self.id,
																'container_id': self.container.id,

																# Credit Note
																'credit_note_owner': 	order.x_credit_note_owner.id,
																'credit_note_type': 	order.x_credit_note_type,
			})


			# Create Lines
			for line in order.order_line:
				#print line
				#print line.product_id.name
				#print line.product_uom_qty
				#print line.price_unit
				#print electronic_order
				#print

				electronic_order.electronic_line_ids.create({
																					# Line
																					'product_id': 			line.product_id.id,
																					'product_uom_qty': 		line.product_uom_qty,
																					'price_unit': 			line.price_unit,

																					# Rel
																					'electronic_order_id': electronic_order.id,
					})



			# Update Amount Total
			#if order.state in ['sale', 'cancel']:
			if order.state in ['sale', 'cancel', 'credit_note']:


				# Total
				#amount_total = amount_total + order.amount_total
				amount_total = amount_total + order.x_amount_flow


				# Count
				if order.x_type in ['ticket_receipt']:
					receipt_count = receipt_count + 1
				elif order.x_type in ['ticket_invoice']:
					invoice_count = invoice_count + 1



		return amount_total, receipt_count, invoice_count

	# update_electronic





# April 2019

	# Day Doctor
	#day_doctor_line = fields.One2many(
	#		'openhealth.management.day.doctor.line',
	#		'management_id',
	#	)






# ----------------------------------------------------------- Update All Years -------------------
	# Update All Years
	@api.multi
	def update_all_years(self):
		"""
		Update All Years
		"""
		print()
		print('Update All Years')

		# Search
		managements = self.env['openhealth.management'].search([
																	('owner', 'in', ['year']),
															],
																	order='date_begin asc',
																	#limit=1000,
														)
		# Loop
		for mgt in managements:
			print(mgt.name)
			mgt.update_fast()

	# update_all_years


# ----------------------------------------------------------- Update All Months -------------------
	# Update All Months
	@api.multi
	def update_all_months(self):
		"""
		Update All Months
		"""
		print()
		print('Update All Months')

		# Search
		managements = self.env['openhealth.management'].search([
																	('owner', 'not in', ['account', 'year']),
															],
																	order='date_begin asc',
																	#limit=1000,
														)
		# Loop
		for mgt in managements:
			print(mgt.name)
			mgt.update_fast()

	# update_all_months

