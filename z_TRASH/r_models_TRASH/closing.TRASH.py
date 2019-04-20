





	date_time = fields.Datetime(
			string="Fecha y Hora", 
			#default = fields.Date.today, 
			default = datetime.datetime.now(),
			#readonly=True,
			#required=True, 
		)








	# Method 
	method_tot = fields.Float(
			'Metodo',
			default = 0, 

			compute='_compute_method_tot', 
		)

	@api.multi
	#@api.depends('x_appointment')

	def _compute_method_tot(self):
		for record in self:

			#print 'jx'
			#print 'compute Method total'





			#date_begin, date_end = clos_funcs.get_dates(self, record.date)
			orders = clos_funcs.get_orders(self, record.date)




			#orders = record.env['sale.order'].search([
			#											('state', '=', 'sale'),														

			#											('date_order', '>=', date_begin),
			#											('date_order', '<', date_end),									
			#									])


			orders = clos_funcs.get_orders(self, record.date)


			cash_tot = 0 
			ame_tot = 0 
			cuo_tot = 0 

			din_tot = 0 
			mac_tot = 0 
			mad_tot = 0 

			vic_tot = 0 
			vid_tot = 0 


			for order in orders: 


				#print 'name: ', order.name
				#print 'date_order: ', order.date_order


				for pm_line in order.x_payment_method.pm_line_ids: 
					

					if pm_line.method == 'cash':
						cash_tot = cash_tot + pm_line.subtotal  

					elif pm_line.method == 'american_express':
						ame_tot = ame_tot + pm_line.subtotal  

					elif pm_line.method == 'cuota_perfecta':
						cuo_tot = cuo_tot + pm_line.subtotal  



					elif pm_line.method == 'diners':
						din_tot = din_tot + pm_line.subtotal  

					elif pm_line.method == 'credit_master':
						mac_tot = mac_tot + pm_line.subtotal  

					elif pm_line.method == 'debit_master':
						mad_tot = mad_tot + pm_line.subtotal  



					elif pm_line.method == 'credit_visa':
						vic_tot = vic_tot + pm_line.subtotal  

					elif pm_line.method == 'debit_visa':
						vid_tot = vid_tot + pm_line.subtotal  





			record.cash_tot = cash_tot
			record.ame_tot = ame_tot
			record.cuo_tot = cuo_tot

			record.din_tot = din_tot
			record.mac_tot = mac_tot
			record.mad_tot = mad_tot

			record.vic_tot = vic_tot
			record.vid_tot = vid_tot


			#print 'cash_tot: ', cash_tot, record.cash_tot
			#print 'ame_tot: ', ame_tot, record.ame_tot
			#print 'cuo_tot: ', cuo_tot, record.cuo_tot
			#print 'din_tot: ', record.din_tot
			#print 'mac_tot: ', record.mac_tot
			#print 'mad_tot: ', record.mad_tot
			#print 'vic_tot: ', record.vic_tot
			#print 'vid_tot: ', record.vid_tot
			#print 








	@api.multi
	#@api.depends('x_appointment')

	def _compute_rec_tot(self):


		for record in self:
			
			print 'jx'
			print 'compute Recibo total'




			clos_funcs.update_orders(self, record.date)



			date = record.date + ' '

			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														#('date_order', '=', date),
														('date_order', 'like', date),

														('x_type', '=', 'receipt'),														
														
														#('name', 'like', 'BO-'),														
												])

			total = 0 

			for order in orders: 
				total = total + order.amount_untaxed 

			record.rec_tot = total

			print 'orders: ', orders
			print 









	@api.multi
	#@api.depends('x_appointment')

	def _compute_inv_tot(self):
		for record in self:


			clos_funcs.update_orders(self, record.date)


			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),														
														
														('date_order', 'like', date),

														#('name', 'like', 'FA-'),														
														('x_type', '=', 'invoice'),

												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.inv_tot = total








	@api.multi
	#@api.depends('x_appointment')

	def _compute_tki_tot(self):
		for record in self:


			clos_funcs.update_orders(self, record.date)


			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'TKF-'),														
														('x_type', '=', 'ticket_invoice'),

												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.tki_tot = total









	@api.multi
	#@api.depends('x_appointment')

	def _compute_tkr_tot(self):
		for record in self:

			clos_funcs.update_orders(self, record.date)

			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'TKB-'),														
														('x_type', '=', 'ticket_receipt'),
												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.tkr_tot = total










	@api.multi
	#@api.depends('x_appointment')

	def _compute_adv_tot(self):
		for record in self:


			clos_funcs.update_orders(self, record.date)


			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'CP-'),														
														('x_type', '=', 'advertisement'),

												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.adv_tot = total







	@api.multi
	#@api.depends('x_appointment')

	def _compute_san_tot(self):
		for record in self:


			clos_funcs.update_orders(self, record.date)


			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'CN-'),														
														('x_type', '=', 'sale_note'),
												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.san_tot = total

















# Total Amount 

	@api.multi
	#@api.depends('x_appointment')

	def _compute_total(self):
		for record in self:

			print 'jx'
			print 'compute total'

			orders = clos_funcs.get_orders(self, record.date)

			print 'orders: ', orders
			print 


			amount_untaxed = 0 
			count = 0 

			for order in orders: 
				amount_untaxed = amount_untaxed + order.amount_untaxed 
				count = count + 1


			#print 'amount_untaxed: ', amount_untaxed
			#print 'count: ', count

			record.total = amount_untaxed
			
			print 'Out'
			print 








# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Create 
	@api.model
	def create(self,vals):

		print 
		print 'CRUD - Closing - Create'
		#print vals
		#print 


		# Put your logic here 
		res = super(Closing, self).create(vals)
		# Put your logic here 


		#date = vals['date']
		#clos_funcs.update_orders(self, date)


		return res

	# CRUD - Create 





