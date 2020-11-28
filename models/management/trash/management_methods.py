# 31 oct 2020 
		vector = [

			# Families
			self.amo_products,
			self.amo_consultations,
			self.amo_procedures,
			self.amo_credit_notes,
			self.amo_other,

			# Sub Families
			self.amo_co2,
			self.amo_exc,
			self.amo_ipl,
			self.amo_ndyag,
			self.amo_quick,

			self.amo_medical,
			self.amo_cosmetology,

			self.amo_sub_con_med,
			self.amo_sub_con_gyn,
			self.amo_sub_con_cha,

			self.amo_echo,
			self.amo_gyn,
			self.amo_prom,

			self.amo_topical,
			self.amo_card,
			self.amo_kit,

		]

		results = mgt_funcs.percentages_pure(vector, self.total_amount)






def create_doctor_data(self, doctor_name, orders):


	# For loop
	# Amount with State
	if order.state in ['credit_note']:
		amount = amount + order.x_amount_flow
	elif order.state in ['sale']:
		amount = amount + order.amount_total

	# Parse Data

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

	# Init

	# Price
	price_unit = line.price_unit						

	# Families
	family = line.product_id.get_family()
	sub_family = line.product_id.get_subsubfamily()



	# Deprecated - Update Families
	#if line.product_id.pl_price_list in ['2019']:
	#	order_line.pl_update_fields()



	if False:
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

											# Families
											'family': family, 
											'sub_family': sub_family, 
										})

	# State equal to Credit Note
	elif order.state in ['credit_note']:
		#print('CREDIT NOTE')

		# Order Lines
		for line in order.order_line:

			# Families
			family = line.product_id.get_family()
			sub_family = line.product_id.get_subsubfamily()

			# Price
			price_unit = order.x_amount_flow

			# Create
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
													'product_uom_qty': 		1,

													# Price
													'price_unit': 			price_unit,

													# Families
													'family': family, 
													'sub_family': sub_family, 
												})

			#print(line)
			#print(line.product_id)
			#print(line.product_id.name)

			# Deprecated !
			#if line.product_id.pl_price_list in ['2019']:
			#	order_line.pl_update_fields()

			#elif line.product_id.pl_price_list in ['2018']:
			#	order_line.update_fields()

		# Line Analysis Credit Note - End

