







	# Account Lines 
	#account_line = fields.One2many(
	#		'openhealth.account.line', 
	#		'marketing_id', 
	#	)

	# Payment Lines 
	#payment_line = fields.One2many(
	#		'openhealth.payment_method_line',
	#		'marketing_id', 			
	#	)




	# Update Orders
	@api.multi
	def update_orders(self):  

		print
		print 'Update Orders'



		# Clear 
		self.account_line.unlink()
		self.payment_line.unlink()



		# Orders 
		orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)

		amount_sum = 0 
		count = 0 



		# Loop 
		for order in orders: 
			
			# Stats 
			amount_sum = amount_sum + order.amount_untaxed 
			count = count + 1
		
		
			# Vars Order 
			serial_nr = order.x_serial_nr


			date = order.date_order
			#print date 


			patient = order.patient.id 
			x_type = order.x_type


			state = order.state



			# Document and Document type 
			if x_type in ['invoice', 'ticket_invoice']: 	# Ruc 
				document = order.patient.x_ruc
				document_type = '6'
			else: 
				if order.patient.x_dni != False: 			# Dni
					document = order.patient.x_dni
					document_type = '1'
				else: 
					document = order.patient.x_id_doc
					document_type = acc_funcs._doc_type[order.patient.x_id_doc_type]




			# Account Lines 
			for line in order.order_line:

				amount = line.price_subtotal
				amount_net, amount_tax = acc_funcs.get_net_tax(self, amount)
				
				
				product = line.product_id.id
				qty = line.product_uom_qty


				acc_line = self.account_line.create({
														'name': order.name, 
														'patient': patient, 

														
														'product': product, 
														'qty': qty, 


														'state': state, 


														'serial_nr': serial_nr, 
														'x_type': x_type, 
														'document': document, 					# Id Doc
														'document_type': document_type, 		# Id Doc Type 
														


														#jx
														'date': date,
														'date_time': date,

														#'date_char': date.split()[0],
														#'time_char': date.split()[1],
														


														'amount': amount,
														'amount_net': amount_net,
														'amount_tax': amount_tax,

														'marketing_id': self.id, 
					})

				acc_line.update_fields()





			# Payment Lines 
			for line in order.x_payment_method.pm_line_ids:

				#amount = line.price_subtotal
				#amount_net, amount_tax = acc_funcs.get_net_tax(self, amount)


				pay_line = self.payment_line.create({
														#'patient': patient, 
														#'serial_nr': serial_nr, 
														#'x_type': x_type, 
														#'document': document, 					# Id Doc
														#'document_type': document_type, 		# Id Doc Type 
														#'date': date,
														#'date_time': date,
														#'amount': amount,
														#'amount_net': amount_net,
														#'amount_tax': amount_tax,

														'patient': patient, 
														'serial_nr': serial_nr, 
														'x_type': x_type, 
														'date_time': date,

														'name': line.name, 
														'subtotal': line.subtotal, 
														'method': line.method, 
																												
														'marketing_id': self.id, 
					})









		# Stats 
		self.total_amount = amount_sum
		self.total_count = count

	# update_orders





# 28 May 2018

	# Type 
	#x_type = fields.Selection(
	#		selection=[	
	#					('order', 		'Ventas'),
	#					('patient', 	'Pacientes Nuevos'),
	#		], 
	#		string="Tipo",
	#		required=True, 
	#	)


	# Dates
	#date = fields.Date(
	#		string="Fecha", 
	#		default = fields.Date.today, 
			#readonly=True,
	#		required=True, 
	#	)


	# Totals
	#total_amount = fields.Float(
			#'Total Monto',
	#		'Total',
	#		readonly=True, 
	#	)





# ----------------------------------------------------------- Update Legacy ------------------------------------------------------

	# Update Patients Legacy
	@api.multi
	def update_patients_legacy(self):  

		print
		print 'Update Patients Legacy'

		# Clear 
		self.patient_line.unlink()



		# Orders 
		mode = 'legacy'
		patients,count = resap_funcs.get_patients_filter(self, self.date_begin, self.date_end, mode)



		self.total_count = count

		# Loop 
		for patient in patients: 

			pat_line = self.patient_line.create({
														'date_create': patient.create_date,

														'date_record': patient.x_date_record,

														
														'patient': patient.id, 
														'sex': patient.sex, 
														'dob': patient.dob, 
														'age': patient.age, 
														'first_contact': patient.x_first_contact, 
														'education': patient.x_education_level, 
														'vip': patient.x_vip, 
														'country': patient.country_id.name, 
														'city': patient.city, 
														'district': patient.street2, 

														'marketing_id': self.id, 
					})


			ret = pat_line.update_fields()


			#if ret == -1:
			#	print 'Age undefined !'



		# Set Stats 
		#self.set_stats()

	# update_patients_legacy





		# Counter({u'Peru': 92, u'United States': 1})





# 5 Jun 2018

						#print prod.name
						#print prod.type
						#print prod.categ_id.name 
						#print prod.x_family
						#print prod.x_treatment						
						#print 



