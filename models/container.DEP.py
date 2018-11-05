

# ----------------------------------------------------------- Import ---------------------------------
#import importx

	# Import Txt
	@api.multi
	def import_txt(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Import TXT'

		# Clean
		self.txt_ref_ids.unlink()

		# Import
		importx.import_txt(self)




# ----------------------------------------------------------- CN -----------------------
	#cn_invoice_create = fields.Boolean(
	#		'Credit Note Invoice',
	#	)

	#cn_receipt_create = fields.Boolean(
	#		'Credit Note Receipt',
	#	)


# ----------------------------------------------------------- My Init -----------------------
	def my_init(self, patient, partner, doctor, treatment):
		"""
		high level support for doing this and that.
		"""
		print
		print 'My Init'

		self.patient = patient
		self.partner = partner
		self.doctor = doctor
		self.treatment = treatment


# ----------------------------------------------------------- Sync -----------------------
#import rsync
	# Sync Txt
	#@api.multi
	#def sync_txt(self):
	#	"""
	#	high level support for doing this and that.
	#	"""
	#	print
	#	print 'Sync - Txt'
	#	# Sync
	#	rsync.synchronize()


# ----------------------------------------------------------- Correct -----------------------
	# Correct
	@api.multi
	def test_correct(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Correct'

		# Loop
		for electronic in self.electronic_order_ids:

			# Correct DNI
			#if order.id_doc in [False]:
			#	if order.id_doc_type in ['dni']:
			#		order.patient.x_id_doc = order.patient.x_dni

			# Correct Counter
			#order.counter_value = int(order.serial_nr.split('-')[1])


			# Correct Gap
			if electronic.delta != 1:

				#print 'Patch the Gap !'
				#print electronic.receptor
				#print electronic.serial_nr
				#print electronic.counter_value


				# Init
				patient_id = self.patient.id
				doctor_id = self.doctor.id
				short_name = 'product_1'
				qty = 1
				treatment_id = False
				x_type = 'receipt'

				pricelist_id = self.patient.property_product_pricelist.id


				# Create
				order = creates.create_order_fast(self, patient_id, doctor_id, treatment_id, short_name, qty, x_type, pricelist_id)


				# Pay
				test_case = 'dni,receipt,product_1,1'
				order.test(test_case)

				# Update
				counter = electronic.counter_value - 1
				order.write({
							'x_counter_value': counter,
						})
				#print ret

				# Generate
				order.generate_serial_nr()
				delta_hou = 0
				delta_min = 0
				delta_sec = -30
				order.generate_date_order(electronic.x_date_created, delta_hou, delta_min, delta_sec)

				# Update
				state = 'cancel'
				order.write({
							'state': state,
						})

