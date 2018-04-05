


# 16 Dec 2017


	# Ooor - For consistency 
	#nr_treatments = fields.Integer(
	#		compute='_compute_nr_treatments',
	#		string = "Número de vacunas",
	#		default = 55, 
	#		)

	#@api.multi
	#def _compute_nr_treatements(self):
	#	for record in self:
	#		record.nr_treatments = 5  
	
			#record.x_nr_treatments = 5  
			#sub_total = 0 
			#for tr in record.treatment_ids:   
			#	sub_total = sub_total + 1  
			#record.x_nr_treatments= sub_total  



# 30 Dec 2017

	#_order = 'x_date_created desc'





	#@api.onchange('x_service_quick_ids')
	#def _onchange_x_service_quick_ids(self):
			

	#	print 'jx'
		#print 'On change service quick ids'


	#	for service in self.x_service_quick_ids:
	#		service.nr_hands_i = 3
	#		service.nr_body_local_i = 3
	#		service.nr_face_local_i = 3 

		#for service in self.x_service_quick_ids:

		#	zone = service.zone 
		#	print zone 

		#	if zone == 'hands': 
		#		print 'gotcha hands'
		#		service.nr_hands_i = service.nr_hands_i + 1

		#	elif zone == 'body_local':
		#		print 'gotcha bl'
		#		service.nr_body_local_i = service.nr_body_local_i + 1

		#	elif zone == 'face_local':
		#		print 'gotcha fl'
		#		service.nr_face_local_i = service.nr_face_local_i + 1






			# Counters 
			#print 'Counters'
			#for service in record.x_service_quick_ids:
			#	print service
			#	service.nr_hands_i = 6
			#	service.nr_body_local_i = 6
			#	service.nr_face_local_i = 6






# 28 Feb 2018

	# Estado de cuenta - Lines 
	#x_order_line_ids = fields.One2many(
	#		'sale.order.line',			 
	#		'patient_id', 
	#		string="Estado de cuenta",
	#	)


	#@api.multi
	#def _compute_x_order_line_ids(self):
	#	print 'jx'
	#	print 'Compute Order ids'
	#	for record in self:		
	#		record.x_order_line_ids.unlink()
	#		partner_id = record.partner_id.name
	#		orders = self.env['sale.order'].search([
	#														('partner_id', '=', partner_id),			
	#												],
	#												#order='start_date desc',
	#												#limit=1,
	#											)
	#		print orders
	#		for order in orders: 
	#			print 
	#			print order.name 
	#			for line in order.order_line: 
	#				print line.product_id
	#				print line.name
	#				print line.price_subtotal
	#				print line.create_date
					#ret = record.x_order_line_ids.create({
					#											'product_id': line.product_id.id,
					#											'name': line.name,
					#											'price_subtotal': line.price_subtotal,
					#									})










# 17 Mar 2017

		# My logic 
		# Create a Treatment - When Patient is created - DEPRECATED !
		#name = vals['name']
		#patient_id = self.env['oeh.medical.patient'].search([('name', '=', name),]).id 
		#treatment = self.env['openhealth.treatment'].create({'patient': patient_id,})


		# Update Partner 
		#print self.street  
		#if self.street != False:
		#if True:
		#	print 'Update Partner !'
		#	self.partner_id.street = self.street








# 5 April 2018

		# Lang 
		#self.lang = 'es_ES'


		# Validations
		#self.email = self.email.lower()
		#self.street = self.street.title()



		# Update Partner 
		#if self.street != False:

		#	print 'Update Partner !'

		#	self.partner_id.street = self.street

		#	self.partner_id.street2 = self.street2

		#	self.partner_id.street2_sel = self.street2_sel

		#	self.partner_id.zip = self.zip

		#	self.partner_id.city = self.city.title()

		#	self.partner_id.state_id = self.state_id

		#	self.partner_id.country_id = self.country_id

		#	self.partner_id.x_dni = self.x_dni

		#	self.partner_id.email = self.email

		#	self.partner_id.phone = self.phone

		#	self.partner_id.mobile = self.mobile

		#	self.partner_id.lang = 'es_ES'


		#if self.x_ruc != False:

		#	self.partner_id.x_ruc = self.x_ruc

		#	self.partner_id.x_firm = self.x_firm



