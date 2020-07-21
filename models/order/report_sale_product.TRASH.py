# 10 Dec

# ----------------------------------------------------------- Django ------------------------------------------------------
	# State
	state = fields.Selection(
			
			selection=[
							('stable', 'Estable'),
							('unstable', 'Inestable'),
			],

			string='Estado',
			default='unstable',
		)


	# Date Test
	date_test = fields.Datetime(
			string="Fecha Test", 
		)


	# Name 
	name = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)




	# Dates
	date_begin = fields.Date(
			string="Fecha Inicio", 
		)

	date_end = fields.Date(
			string="Fecha Final", 
		)










	# Management - For Testing - Dep ?
	management_id = fields.Many2one(
			'openhealth.management',
		)








# ----------------------------------------------------------- Update ------------------------------------------------------
	# Update 
	@api.multi
	def update(self):  
		"""
		Update RSP
		"""
		print()
		print('2018 - Report Sale Product - Update')

		# Clean 
		self.order_line_ids.unlink()
		self.item_counter_ids.unlink()


		# Init
		self.date_begin = self.name


		# Get Orders 
		#orders,count = mgt_funcs.get_orders_filter_fast(self, self.name, self.name)			# Only Sales

		if not self.several_dates:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_begin)

		else:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)

		print(orders)
		print(count)



		# Order lines
		self.create_lines(orders)




		# Item Counter 
		total_qty = 0
		total = 0 
		for order_line in self.order_line_ids: 

			# Init 
			name = order_line.product_id.name
			qty = order_line.product_uom_qty
			subtotal = order_line.price_total 
			total_qty = total_qty + qty
			total = total + subtotal

			#print(name)
			#print(qty)
			#print(subtotal)
			#print()


			# Search 
			prod_ctr = self.env['openhealth.item.counter'].search([
																		('name', '=', name),
																		('report_sale_product_id', '=', self.id),
																	],
																	#order='x_serial_nr asc',
																	limit=1,
																)
			#print prod_ctr


			# Create or update 
			if prod_ctr.name != False: 				
				prod_ctr.increase_qty(qty)
				prod_ctr.increase_total(subtotal)
			else:		# Create 
				ret = self.item_counter_ids.create({
															'name': name,
															'qty': qty, 
															'total': subtotal, 
															'report_sale_product_id': self.id,
													})
				#print ret 


		# Update Descriptors 
		self.total_qty = total_qty
		self.total = total
		#print 

	# update











# ----------------------------------------------------------- Dep - Test ------------------------------------------------------
	#test_target = fields.Boolean(
	#		string="Test Target", 
	#	)















# 16 Oct 2019
# Done by PL



# ----------------------------------------------------------- Create Lines - DEP ------------------------------------------------------

	# Create Lines 
	def create_lines(self, orders):  
		#print()
		#print('Create Lines')

		# Loop
		for order in orders: 

			for line in order.order_line: 

				if line.product_id.categ_id.name == 'Cremas':
					
					#print('Create !')

					# Create Order Line 
					ret = self.order_line_ids.create({
															'name': line.name,
															'product_id': line.product_id.id,
															'patient': order.patient.id,
															'price_unit': line.price_unit,
															'product_uom_qty': line.product_uom_qty, 
															'x_date_created': line.create_date,															

															'state': order.state,

															'report_sale_product_id': self.id,
													})

