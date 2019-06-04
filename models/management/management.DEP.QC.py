# 4 May 2019




# ----------------------------------------------------------- Update - QC -------------------------
	# Update QC
	@api.multi
	def update_qc(self, x_type):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Management - Update QC'

		# Init
		serial_nr_last = 0

		# Orders
		orders, count = mgt_funcs.get_orders_filter_type(self, self.date_begin, self.date_end, x_type)

		# Loop
		for order in orders:

			# Gap
			serial_nr = int(order.x_serial_nr.split('-')[1])
			if serial_nr_last != 0:
				delta = serial_nr - serial_nr_last
			else:									# First one
				delta = 1
			serial_nr_last = serial_nr
			# Update Delta
			order.x_delta = delta
			# Update Counter Value
			#order.x_counter_value = int(order.x_serial_nr.split('-')[1])


			# Checksum
			order.checksum()

	# update_qc



	# Update QC All - Used by the UI
	@api.multi
	def update_qc_all(self):
		"""
		high level support for doing this and that.
		"""
		# Gap and Checksum
		self.update_qc('ticket_receipt')
		self.update_qc('ticket_invoice')

