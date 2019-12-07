# 7 Dec 2019



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

