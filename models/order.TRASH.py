


# 16 Jun 2017


# ----------------------------------------------------------- Button - Reseve Machine  ------------------------------------------------------

	@api.multi 
	def reserve_machine_old(self):

		#print 'jx'
		#print 'Reserve Machine - Old'

		#self.x_machine = 'laser_co2_1'


		
		# Create Machine
		appointment_date = 	self.x_appointment_date
		doctor_name = 		self.x_doctor.name
		doctor_id = 		self.x_doctor.id
		patient_id = 		self.patient.id
		treatment_id = 		self.treatment.id
		duration = 			self.x_duration


		x_machine_old = 	self.x_machine




		#start_machine = 	self.x_machine
		start_machine = 	self.x_machine_req





		# New 
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration)
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		x_machine = mac_funcs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		

		


		self.x_machine = x_machine 
		self.x_appointment.x_machine = x_machine





		# If Sucess create Machine Appointment
		if x_machine != False:


			# Create Appointment - Machine 
			app = self.env['oeh.medical.appointment'].create(
															{
																'appointment_date': appointment_date,

																'patient': 		patient_id,																	

																'x_type': 		'procedure',

																'duration': 	duration,
																																
																'x_create_procedure_automatic': False, 

																'x_machine': 	x_machine,



							                    				#'x_target': 	'machine',
							                    				'x_target': 	self.x_target,


																'doctor': 		doctor_id,

																'treatment': 	treatment_id, 
															}
															)



			if app != False:

				# Unlink Old 
				rec_set = self.env['oeh.medical.appointment'].search([
																			('appointment_date', 'like', appointment_date), 
																			('doctor', '=', doctor_name), 
																			('x_machine', '=', x_machine_old),

																			('patient', '=', self.patient.name), 
																	])
				ret = rec_set.unlink()
				#print "ret: ", ret




		else:
			#print 'Error !'	
			#print 			


			return {	'warning': 	{'title': "Error: Colisión !",
						'message': 	'La sala ya está reservada.',   
			#' + start + ' - ' + end + '.',
						}}

	# reserve_machine




# 29 Aug 2017


	@api.multi 
	def action_confirm_deprecated(self):

		#print 
		#print 'jx'
		#print 'Action confirm - Over ridden'
		 
		#Write your logic here


		# Validate 
		#if self.x_machine != False:

		#print 'x_doctor.name: ', self.x_doctor.name
		#print 'x_machine', self.x_machine
		#print 'x_state', self.x_state



		#if self.x_doctor.name != False   and   self.x_machine == False:
		#if self.x_doctor.name != False   and   self.x_machine == False	 and 	self.x_machine_req != 'consultation':

		if self.x_treatment == 'laser_co2'   and   self.x_machine == False:
			#print 'Warning: Sala no Reservada !'
			tra = 1 
		else:
			#print 'Success !!!'

			#self.x_state = 'sale'
			#self.x_confirmed = True 


			#if self.x_family == 'consultation': 
			if self.x_family == 'consultation'	or 	self.x_family == 'procedure': 
				self.x_appointment.state = 'Scheduled'

				#self.state = 'confirmed'


			# State is changed here ! 
			res = super(sale_order, self).action_confirm()
			
			#self.state = 'confirmed'

		#else: 
			
		#res = super(sale_order, self).action_confirm()
		#Write your logic here
		
		#print
	# action_confirm
	






# Ooor

	#name = fields.Char(
	#		string="Presupuesto #"
	#	)

	# Test 
	#test = fields.Char(
	#	)

	# Type
	#x_type = fields.Selection(
	#		selection = ord_vars._owner_type_list, 
	#		string='Tipo', 
	#	)










# User by Doctor 
	# Doctor 
	#_dic_docuser = {
	#					'Dr. Medico': 		'Medico', 
	#					'Dr. Chavarri': 	'Fernando Chavarri', 
	#					'Dr. Canales': 		'Paul Canales', 
	#					'Dr. Escudero':		'Carlos Escudero', 
	#					'Dr. Gonzales':		'Leo Gonzales', 
	#					'Dr. Vasquez':		'Javier Vasquez', 
	#					'Dr. Alarcon': 		'Guillermo Alarcon', 
	#					'Dr. Monteverde':	'Piero Monteverde', 
	#					'Dr. Mendez':		'Carlos Mendez', 
	#					'Dra. Acosta':		' Desiree Acosta', 
	#					'Dra. Pedemonte':	'Maria Luisa Pedemonte', 
	#					'Eulalia':			'Eulalia Ruiz', 
	#				}
	
	#@api.onchange('x_doctor')	
	#def _onchange_x_doctor(self):
	#	user_name = self._dic_docuser[self.x_doctor.name]
	#	self.user_id = self.env['res.users'].search([('name', '=', user_name)]).id 


	#user_id = fields.Many2one('res.users', string='Salesperson', index=True, track_visibility='onchange', default=lambda self: self.env.user)

	#@api.multi
	#@api.depends('x_doctor')
	#def _compute_user_id(self):
	#	for record in self:
	#		if record.x_doctor.name != False:
	#			user_name = record._dic_docuser[record.x_doctor.name]
	#			record.user_id = record.env['res.users'].search([('name', '=', user_name)]).id 










# 6 Oct 2017


	#partner_invoice_id = fields.Many2one('res.partner', string='Invoice Address', readonly=True, 
	#	required=True, 
		#required=False, 
	#	states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Invoice address for current sales order.")

	#partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address', readonly=True, 
	#	required=True, 
		#required=False, 
	#	states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Delivery address for current sales order.")





	# Pricelist
	#@api.multi 
	#def _get_default_pl(self):
	#	pl = self.env['product.pricelist'].search([('name', '=', 'Public Pricelist')]).id 
	#	pl = 1 
	#	return pl

	#pricelist_id = fields.Many2one(
	#	'product.pricelist', 
	#	default=lambda self: self._get_default_pl(),
	#	string='Pricelist', required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Pricelist for current sales order.")


	#pricelist_id = fields.Many2one('product.pricelist', string='Pricelist', required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, help="Pricelist for current sales order.")




	# For Debugging purposes 
	@api.multi
	@api.onchange('partner_id')
	def onchange_partner_id(self):
		print 'jx'
		print 'onchange_partner_id'
		print self.partner_id
		print 

		"""
		Update the following fields when the partner is changed:
		- Pricelist
		- Payment term
		- Invoice address
		- Delivery address
		"""
		if not self.partner_id:

			print 'jx 2'

			self.update({
				'partner_invoice_id': False,
				'partner_shipping_id': False,
				'payment_term_id': False,
				'fiscal_position_id': False,
			})
			return



		addr = self.partner_id.address_get(['delivery', 'invoice'])


		print 'jx 3'
		print addr 
		print 'jx 4'
		print self.partner_id.property_payment_term_id
		print 'jx 5'
		print self.partner_id.property_product_pricelist.id
		print 'jx 6'
		print self.partner_id.property_product_pricelist
		print 'jx 7'


		values = {
			'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
			'payment_term_id': self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
			'partner_invoice_id': addr['invoice'],
			'partner_shipping_id': addr['delivery'],
		}

		print 'jx 10'

		if self.env.user.company_id.sale_note:
			values['note'] = self.with_context(lang=self.partner_id.lang).env.user.company_id.sale_note

		if self.partner_id.user_id:
			values['user_id'] = self.partner_id.user_id.id
		if self.partner_id.team_id:
			values['team_id'] = self.partner_id.team_id.id
		self.update(values)



# 20 Nov 2017

			#name = record.name
			#pre = name.split('-')[0]

			#if pre == 'BO' or  pre == 'BOL':
			#	record.x_type = 'receipt'

			#elif pre == 'FA':
			#	record.x_type = 'invoice'

			#elif pre == 'CP':
			#	record.x_type = 'advertisement'

			#elif pre == 'CN':
			#	record.x_type = 'sale_note'
			
			#elif pre == 'TKB':
			#	record.x_type = 'ticket_receipt'
			
			#elif pre == 'TKF':
			#	record.x_type = 'ticket_invoice'

			#else:
			#	print 'jx'
			#	print 'This should not happen'
			#	print pre 
			#	print 





	#order_day = fields.Char(	
	#		'Day', 
	#		default = lambda *a: str(date_order.strftime('%d')),
	#	)








#'task_date_from':fields.function(lambda *a,**k:{}, method=True, type='date',string="Task date from"),
#'task_date_to':fields.function(lambda *a,**k:{}, method=True, type='date',string="Task date to"),

	#task_date_from = fields.Date(
	#	default = lambda *a,#**k:{}, 
		#method=True, 
		#type='date', 
	#	string="Task date from", 
	#)

	#task_date_to = fields.Date(
	#	default=lambda *a,#**k:{}, 
		#method=True, 
	#	string="Task date to"
	#)





# 31 Dec 

	@api.depends('order_line.price_total')
	def _amount_all(self):
		"""
		Compute the total amounts of the SO.
		"""
		for order in self:
			amount_untaxed = amount_tax = 0.0
			for line in order.order_line:


				#amount_untaxed += line.price_subtotal
				amount_untaxed += 5
				#amount_untaxed += line.x_price_subtotal
				

				# FORWARDPORT UP TO 10.0
				if order.company_id.tax_calculation_rounding_method == 'round_globally':
					price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
					taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
					amount_tax += sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
				else:
					amount_tax += line.price_tax
			order.update({
				'amount_untaxed': order.pricelist_id.currency_id.round(amount_untaxed),
				'amount_tax': order.pricelist_id.currency_id.round(amount_tax),
				'amount_total': amount_untaxed + amount_tax,
			})







# 3 Jan 2018

	#@api.onchange('partner_id')
	#def _onchange_partner_id(self):

	#		if self.pricelist_id.name != False: 

	#			pl = self.env['product.pricelist'].search([
	#															('name', '=', 'VIP Return'), 
	#													],
														#order='appointment_date desc',
	#													limit=1,
	#												)
				#self.pricelist_id = pl
	#			self.pricelist_ret_id = pl



	# Pricelist 
	#pricelist_ret_id = fields.Many2one(
	#		'product.pricelist', 
	#		string='Pricelist Return', 
			#required=True, 
	#		readonly=True, 
			#states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
			#help="Pricelist for current sales order.", 
	#	)








	#order_line = field_One2many=fields.One2many(
	#	'sale.order.line',
	#	'order_id',
		#string='Order',
		#compute="_compute_order_line",
	#)

	#@api.multi
	#@api.depends('x_partner_vip')
	
	#def _compute_order_line(self):
	#	for record in self:
	#		#print 'compute_order_line'
	#		#print record.x_partner_vip 
	#		ret = record.update_order_lines()
	#		#print ret 









	#amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all', track_visibility='always')
	#amount_tax = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_amount_all', track_visibility='always')
	#amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all', track_visibility='always')






# 10 Jan 2018

				#serial_nr = ''

				#if record.x_type == 'ticket_invoice':
					#serial_nr = record.x_payment_method.ticket_invoice.counter.total 
					#serial_nr = record.x_payment_method.ticket_invoice.name 
				#	serial_nr = record.x_payment_method.saledoc_code 


				#elif record.x_type == 'ticket_receipt':
					#serial_nr = record.x_payment_method.ticket_receipt.counter.total 
					#serial_nr = record.x_payment_method.ticket_receipt.name 
				#	serial_nr = record.x_payment_method.saledoc_code 


				#elif record.x_type == 'receipt':
				#	serial_nr = record.x_payment_method.receipt.name 


				#elif record.x_type == 'invoice':
				#	serial_nr = record.x_payment_method.invoice.name 


				#elif record.x_type == 'advertisement':
				#	serial_nr = record.x_payment_method.advertisement.name 

				#elif record.x_type == 'sale_note':
				#	serial_nr = record.x_payment_method.sale_note.name 







# 11 Jan 2017

		#oid = self.id
		#order = self.env['sale.order'].search([ ('id', '=', oid), ], order='date_order desc', limit=1)
		#order_id = order.id
		#partner_id = order.partner_id
		#partner_id_id = order.partner_id.id
		#patient_name = partner_id.name 
		#print order 
		#print order_id
		#print partner_id_id



			#print line
			#print line.name 
			#print line.product_id.name


			#print 'jx'
			#print self.partner_id
			#print pl 
			#print self.partner_id.property_product_pricelist.name 





			#return {

				# Mandatory 
			#	'type': 'ir.actions.act_window',

			#	'name': 'Open Card',

				# Window action 
			#	'res_model': 'openhealth.card',

			#	'res_id': card_id,

				# Views 
			#	"views": [[False, "form"]],
				
			#	'view_mode': 'form',
				
			#	'target': 'current',

				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False, 

			#	'flags': {
			#			'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			#	},			

			#	'context':   {
			#		'default_name': name,
			#		'default_patient_name': patient_name,
			#	}
			#}







		#if payment_method_id == False:



		#print nr_pm
		#print name
		#print method
		#print 




# 5 April 2018

				# Card name 
				#counter = self.env['openhealth.counter'].search([('name', '=', 'vip')])
				#name = counter.total
				#counter.increase()











# 6 April 2018






# ----------------------------------------------------------- Reserve Machine ------------------------------------------------------

# The Machine Design Atrocity 


	# Reserve machine 
	@api.multi 
	def reserve_machine(self):

		print 'jx'
		print 'Reserve Machine'
		print 



		# There is an appointment 
		if self.x_appointment.name == False: 
			print 'There is no Appointment'


		else: 
			date_format = "%Y-%m-%d %H:%M:%S"
			duration = self.x_appointment.duration 
			delta = datetime.timedelta(hours=duration)


			# Easiest first 
			m_dic = {

						'consultation':			[], 

						'laser_quick': 			['laser_quick'], 
						'laser_co2_1': 			['laser_co2_1', 'laser_co2_2', 'laser_co2_3'], 
						'laser_excilite': 		['laser_excilite'], 
						'laser_m22': 			['laser_m22'], 


						'laser_triactive': 		['laser_triactive'], 
						'chamber_reduction': 	['chamber_reduction'], 
						'carboxy_diamond': 		['carboxy_diamond'], 


						'':						[], 
				}



			print 'x machine req'
			print self.x_machine_req


			m_list = m_dic[self.x_machine_req]

			ad_str = self.x_appointment.appointment_date

			k = 1.
			out = False 




			while not out		and  	  k < 6: 		

				for x_machine_req in m_list: 

					if not out: 				

						self.x_appointment.appointment_date = ad_str
						self.x_appointment.x_machine = x_machine_req
						nr_mc = self.get_nr_mc()

						if nr_mc == 1:		# Success - Get out 
							out = True 

				if not out: 	# Error - Change the date 
					ad = datetime.datetime.strptime(self.x_appointment.appointment_date, date_format) 
					ad_dt = delta + ad
					ad_str = ad_dt.strftime("%Y-%m-%d %H:%M:%S")

					k = k + 1.
		

	# reserve_machine


	# Machine Required  
	#x_machine_req = fields.Char(
	#		string='Sala req.',
	#		compute='_compute_x_machine_req', 
	#	)

	#@api.multi
	#@api.depends('x_product')
	#def _compute_x_machine_req(self):
	#	for record in self:
	#		tre = record.x_product.x_treatment
	#		mac = cosvars._hash_tre_mac[tre]
	#		record.x_machine_req = mac



	# Machine 
	#x_machine = fields.Selection(
	#		string="Sala", 
	#		selection = app_vars._machines_list, 
	#		required=False, 
			
	#		compute='_compute_x_machine', 		
	#	)

	#@api.multi
	#@api.depends('x_appointment')
	#def _compute_x_machine(self):
	#	for record in self:
	#		record.x_machine = record.x_appointment.x_machine










# ----------------------------------------------------------- Compute - Solving ------------------------------------------------------



	# Treatment
	#x_treatment = fields.Char(
	#		required=False, 			
	#		compute='_compute_x_treatment', 
	#		)

	#@api.multi
	#@api.depends('x_product')
	#def _compute_x_treatment(self):
	#	for record in self:
	#		record.x_treatment = record.x_product.x_treatment




	# Product
	#product = fields.Char(
	#		'Producto', 

	#		compute="_compute_product",
	#	)

	#@api.multi
	#@api.depends('partner_id')

	#def _compute_product(self):
	#	for record in self:
	#		for line in record.order_line:
	#			record.product = line.product_id.name




	# Product
	#x_product = fields.Many2one(
			#'product.template',			
	#		string="Producto",	
	#		required=False, 
			
			#domain = [			
			#			('x_origin', '=', False),						
			#		],

			#compute='_compute_x_product', 
	#	)



	#@api.multi
	#@api.depends('order_line')
	#def _compute_x_product(self):
	#	for record in self:
	#		flag = False
	#		for line in record.order_line:
	#			tre = line.product_id.x_treatment
	#			if  tre == 'laser_quick'  or 	tre == 'laser_co2' 	or 	tre == 'laser_excilite'	or 	tre == 'laser_ipl'	or tre == 'laser_ndyag'		or tre == 'consultation': 
	
	#				product = line.product_id.id
	
	#				flag = True 
	#		if flag: 
	#			record.x_product = product









# 12 Apr 2018


# Order line creation 
		#product_id = product.id
		#price_unit = product.list_price
		#x_price_vip = product.x_price_vip
		#product_uom = product.uom_id.id
		#print product
		#print product.id
		#print product.uom_id.id
		#print 


#jxx
		#ol = self.order_line.create({
		#								'product_id': product.id,
		#								'order_id': order_id,										

		#								'x_price_manual': price_manual, 


										#'name': target,
										#'name': product.name,
										#'state':'draft',
										#'price_unit': price_unit,
										#'x_price_vip': x_price_vip,
										#'product_uom': product_uom, 
		#							})







											#'name': target,
											#'name': product.name,
											#'state':'draft',
											#'x_price_vip': x_price_vip,
											#'product_uom': product_uom, 


											#'x_price_manual': price_manual, 
											#'name': target,
											#'name': product.name,
											#'state':'draft',
											#'x_price_vip': x_price_vip,
											#'product_uom': product_uom, 




										#'x_price_manual': price_manual, 
										#'name': target,
										#'name': product.name,
										#'state':'draft',
										#'price_unit': price_unit,
										#'x_price_vip': x_price_vip,
										#'product_uom': product_uom, 






	# Consistency 

	#subtotal = fields.Float(
	#		string = 'Sub-total', 
			#required=True, 
	#	)

	#method = fields.Selection(
	#		string="Medio", 
	#		selection = ord_vars._payment_method_list, 			
	#		required=True, 
	#	)

	# Number of paymethods  
	#pm_complete = fields.Boolean(
	#							default = False, 
	#							readonly=False,
								#string="Pm Complete",
								#compute="_compute_pm_complete",
	#)



	# Print Order
	#@api.multi 
	#def print_order(self):
		#print 
		#print 'Print Order'
		#ret = self.treatment.open_myself()
		#return ret 
	# open_treatment





		#nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', self.id),]) 
		#name = 'Pago ' + str(nr_pm + 1)
		#total = self.x_amount_total



	#@api.multi
	#@api.depends('x_appointment')
	#def _compute_x_doctor(self):
	#	for record in self:
	#		record.x_doctor = record.x_appointment.doctor












# 13 Apr 2018



# ----------------------------------------------------------- Button - Update Order ------------------------------------------------------

	@api.multi 
	def update_order(self):

		# Order 
		order_id = self.id

		# Appointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																	('patient', 'like', self.patient.name),	
																	('doctor', 'like', self.x_doctor.name), 	
																	('x_type', 'like', 'procedure'), 
																], 
																	order='appointment_date desc', limit=1)
		appointment_id = appointment.id
		self.x_appointment = appointment_id




		# Lines 
		ret = self.order_line.unlink()

		# Cosmetology 
		for service in self.cosmetology.service_ids:
			#print service

			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,
										service.service.x_price_vip
									)
			#print 



		# Doctor 
		#for service in self.consultation.service_co2_ids:
		for service in self.treatment.service_co2_ids:
			#print service

			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)
			#print 
		
		for service in self.consultation.service_excilite_ids:
			#print service
			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 										
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_ipl_ids:
			#print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_ndyag_ids:
			#print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_medical_ids:
			#print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		#print 

	# update_order 


	# Update Order lines app 
	@api.multi 
	def update_order_lines_app(self):

		#print 
		#print 'jx'
		#print 'Update Order Lines'


		for line in self.order_line:

			#print line


			product_id = line.product_id


			# If Service 
			if product_id.type == 'service':



				appointment = self.env['oeh.medical.appointment'].search([ 	
															('doctor', 'like', self.x_doctor.name), 	
															('patient', 'like', self.patient.name),		
															('x_type', 'like', 'procedure'), 
															('x_target', '=', 'doctor'), 
															#('state', 'like', 'pre_scheduled'), 
														], 
														order='appointment_date desc', limit=1)

				appointment_id = appointment.id

				


				# Line  
				line.x_appointment_date = appointment.appointment_date
				line.x_doctor_name = appointment.doctor.name
				line.x_duration = appointment.duration 
				

				#line.x_machine = False


				# Self 
				self.x_appointment = appointment

	# update_order_lines_app	







# ----------------------------------------------------------- Button - Update Lines ------------------------------------------------------
	@api.multi 
	def update_line(self, order_id, product_id, name, list_price, uom_id, x_price_vip):
		order = self.env['sale.order'].search([
															('id', '=', order_id),
															#('name', 'like', name),
													])
		line = order.order_line.create({
											'order_id': order.id,
											'product_id': product_id,
											'name': name,
											'product_uom': uom_id, 
											'x_price_vip': x_price_vip, 
											'x_partner_vip': self.x_partner_vip
										})
		return line
	# update_line





	# Order lines 
	@api.multi 
	def clean_order_lines(self):
		if self.state == 'draft':
			ret = self.remove_order_lines()









			#res.default_code = ''
			#res.product_id = False
			#res.x_type = x_type
			#res.price_manual_flag = False
			#res.price_manual = 0
			#res.family = False
			#res.treatment = False
			#res.zone = False
			#res.family = False

			#if x_type == 'product': 
			#	res.treatment = False
			#	res.zone = False
			#	res.family = False






			#record.x_date_order_corr = record.date_order
			#date_field1 = datetime.strptime(date_field1, DATETIME_FORMAT)
			#date_field2 = datetime.strptime(date_field2, DATETIME_FORMAT)
			#date_field2 = date_field1 + timedelta(hours=5,minutes=30)

			#date_field2 = datetime.strptime(date_field2, DATETIME_FORMAT)
			#date_field2 = date_field1 + datetime.timedelta(hours=5,minutes=0)

			#date_field2 = datetime.datetime.strptime(date_field2, DATETIME_FORMAT_2)






			#compute="_compute_x_serial_nr",

	#@api.multi
	#@api.depends('partner_id')
	#def _compute_x_serial_nr(self):
	#	for record in self:
	#		if record.x_payment_method != False: 
	#			serial_nr = record.x_payment_method.saledoc_code 
	#			record.x_serial_nr = serial_nr









			#if record.x_target == 'doctor': 
			#	app = self.env['oeh.medical.appointment'].search([
			#														('patient', '=', record.patient.name), 
			#														('x_type', '=', 'procedure'),
			#														('x_target', '=', record.x_target),
			#														('doctor', '=', record.x_doctor.name), 
			#												],
			#												order='appointment_date desc',
			#												limit=1,)


			#else:		# therapist 
			#	app = self.env['oeh.medical.appointment'].search([
			#														('patient', '=', record.patient.name), 
			#														('x_type', '=', 'procedure'),
			#														('x_target', '=', record.x_target),

			#														('x_therapist', '=', record.x_therapist.name), 
			#												],
			#												order='appointment_date desc',
			#												limit=1,)

			






			#print 
			#print 'jx'
			#print 'Compute Partner Vip'


			#rec_set = self.env['sale.order'].search([
			#												('partner_id','=', record.partner_id.id),
			#												('state','=', 'sale'),
			#											]) 			
			#for rec in rec_set:
			#	for line in rec.order_line:
			#		if line.name == 'Tarjeta VIP':
			#			record.x_partner_vip = True 









# ----------------------------------------------------------- Deprecated ------------------------------------------------------

	#currency_id = fields.Many2one(
	#		"res.currency", 
	#		related='pricelist_id.currency_id', 
	#		string="Currency", 
	#		readonly=True, 
	#		required=False, 
	#	)


	# Patient - For Reporting 
	#patient_id = fields.Many2one(
	#		'oeh.medical.patient',
	#		string='Paciente', 
	#	)


	#cr = fields.Char(
	#		#default='-------------------------------------------------------------------', 
	#		default='--------------------------------------------------------------', 
	#	)


	# Number of saledocs  
	#nr_saledocs = fields.Integer(
	#		string="Documentos de venta",
	#		compute="_compute_nr_saledocs",
	#)
	#@api.multi
	#def _compute_nr_saledocs(self):
	#	for record in self:
	#		receipt =			self.env['openhealth.receipt'].search_count([('order','=', record.id),]) 
	#		invoice =			self.env['openhealth.invoice'].search_count([('order','=', record.id),]) 
	#		advertisement =		self.env['openhealth.advertisement'].search_count([('order','=', record.id),]) 
	#		sale_note =			self.env['openhealth.sale_note'].search_count([('order','=', record.id),]) 
	#		ticket_receipt =	self.env['openhealth.ticket_receipt'].search_count([('order','=', record.id),]) 
	#		ticket_invoice =	self.env['openhealth.ticket_invoice'].search_count([('order','=', record.id),]) 
	#		record.nr_saledocs= receipt + invoice + advertisement + sale_note + ticket_receipt + ticket_receipt



	# Number of paymethods  
	#nr_pay_methods = fields.Integer(
	#		string="Documentos de venta",

	#		compute="_compute_nr_pay_methods",
	#)
	#@api.multi
	#def _compute_nr_pay_methods(self):
	#	for record in self:
	#		pm = self.env['openhealth.payment_method'].search_count([('order','=', record.id),]) 
	#		record.nr_pay_methods = pm



	#@api.multi 
	#def create_sale_document(self):
		# Search 
	#	sale_document_id = self.env['openhealth.sale_document'].search([('order','=',self.id),]).id
		# Create 
	#	if sale_document_id == False:
	#		sale_document = self.env['openhealth.sale_document'].create({
	#																		'order': self.id,
	#																		'total': self.x_amount_total, 
	#																		'partner': self.partner_id.id,				
	#																	})
	#		sale_document_id = sale_document.id 
	#	self.sale_document = sale_document_id

		# State
	#	self.state = 'proof'

	#	return {
	#			'type': 'ir.actions.act_window',
	#			'name': ' New sale_document Current', 
	#			'view_type': 'form',
	#			'view_mode': 'form',	
	#			'target': 'current',
	#			'res_model': 'openhealth.sale_document',				
	#			'res_id': sale_document_id,
	#			'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
	#						'form': {'action_buttons': True, }
	#						},
	#			'context': {
	#						'default_order': self.id,
	#						'default_total': self.x_amount_total,
	#						'default_partner': self.partner_id.id,
	#						}
	#			}
	# create_sale_document




	#x_payment_method_code = fields.Char(
	#		string="Código", 						
	#		required=False, 
	#	)


	#x_appointment_date = fields.Datetime(
	#		string="Fecha", 
	#		required=False, 

	#		compute='_compute_x_appointment_date', 			
	#		)


	#x_duration = fields.Float(
	#		string="Duración (h)", 
	#		required=False, 

	#		compute='_compute_x_duration', 			
	#		)



	#@api.depends('x_appointment')
	#def _compute_x_appointment_date(self):
	#	for record in self:
	#		record.x_appointment_date = record.x_appointment.appointment_date



	#@api.depends('x_appointment')
	#def _compute_x_duration(self):
	#	for record in self:
	#		record.x_duration = record.x_appointment.duration


	#validity_date = fields.Char(
	#		string="Fecha de expiración"
	#	)


	#x_confirmed = fields.Boolean(
	#		default=False, 
	#	)



	# Nr treatments 
	#nr_treatments = fields.Integer(
	#		default=0,
	#		compute='_compute_nr_treatments', 
	#	)
	#@api.multi
	#def _compute_nr_treatments(self):
	#	for record in self:
	#		nr = record.env['openhealth.treatment'].search_count([
	#																	('physician', '=', record.x_doctor.name ), 
	#																])
	#		record.nr_treatments = nr


	# Nr cosmetologies 
	#nr_cosmetologies = fields.Integer(
	#		default=0,
	#		compute='_compute_nr_cosmetologies', 
	#	)
	#@api.multi
	#def _compute_nr_cosmetologies(self):
	#	for record in self:
	#		nr = record.env['openhealth.cosmetology'].search_count([
	#																	('physician', '=', record.x_doctor.name ), 
	#																])
	#		record.nr_cosmetologies = nr








				#print 'jx'
				#print 'Create VIP Card'
				#print card
				#print card.name
				#print self.partner_id.name				
				#print



