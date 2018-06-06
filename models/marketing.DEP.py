

# 6 Jun 2018 



# ----------------------------------------------------------- Sales ------------------------------------------------------
	
	# Sales
	@api.multi
	def patient_sales(self):  
		print 
		print 'Patient Sales'
		print 

		# Clean 
		self.patient_sale_count = 0 



		# Patient Lines 
		for pat_line in self.patient_line: 

			# Orders 
			orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)
			#print orders



			# Clean 
			pat_line.sale_line.unlink()

			# Orders
			for order in orders: 

				# Lines 
				for line in order.order_line: 
					
					# Create - Sales 
					sale_line = pat_line.sale_line.create({
														'name': line.name, 
														'product_id': line.product_id.id, 
														'x_date_created': order.date_order, 
														'product_uom_qty': line.product_uom_qty, 
														'price_unit': line.price_unit, 

														'patient_line_sale_id': pat_line.id, 
						})

			# Count
			self.patient_sale_count = self.patient_sale_count + len(pat_line.sale_line)


			# Update Patient Line 
			pat_line.update_nrs()

	# patient_sales





# ----------------------------------------------------------- Consultations ------------------------------------------------------
	
	# Consultations 
	@api.multi
	def patient_consu(self):  
		print 
		print 'Patient Consu'
		print 


		# Clean 
		self.patient_consu_count = 0 


		# Patient Lines 
		for pat_line in self.patient_line: 
			
			# Orders 
			orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)
			#print orders



			# Clean 
			pat_line.consu_line.unlink()

			# Orders
			for order in orders: 

				# Lines
				for line in order.order_line: 

					prod = line.product_id


					# Consu
					if prod.x_family in ['consultation']: 

						consu_line = pat_line.consu_line.create({
																	'name': line.name, 
																	'product_id': line.product_id.id, 
																	'x_date_created': order.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit, 

																	'patient_line_consu_id': pat_line.id, 
																})

			# Count
			self.patient_consu_count = self.patient_consu_count + len(pat_line.consu_line)

			# Update 
			pat_line.update_nrs()

	# patient_consus






# ----------------------------------------------------------- Procedures ------------------------------------------------------

	# Procedures
	@api.multi
	def patient_procedures(self):  
		
		print 
		print 'Patient Procedurs'


		# Clean 
		self.patient_proc_count = 0 


		# Patient Lines 
		for pat_line in self.patient_line: 

			# Orders 
			orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pat_line.patient.name),
													],
														#order='x_serial_nr asc',
														order='date_order asc',
														#limit=1,
												)
			#print orders



			# Clean 
			pat_line.procedure_line.unlink()

			# Orders
			for order in orders: 

				# Lines 
				for line in order.order_line: 

					# Vars 
					prod = line.product_id

					# Create 
					if 	prod.type not in ['product']	and		prod.x_family not in ['consultation']: 

						procedure_line = pat_line.procedure_line.create({
																			'name': line.name, 
																			'product_id': line.product_id.id, 
																			'x_date_created': order.date_order, 
																			'product_uom_qty': line.product_uom_qty, 
																			'price_unit': line.price_unit, 
																			'patient_line_proc_id': pat_line.id, 
																		})

			# Count
			self.patient_proc_count = self.patient_proc_count + len(pat_line.procedure_line)

			# Update 
			pat_line.update_nrs()

	# patient_procedures




