


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









# 5 April 2018



# ----------------------------------------------------------- Hard wired ------------------------------------------------------


	# READY 

	# Email 
	#email = fields.Char(
	#		string = 'Email',  
	#		placeholder = '',
	#		required=True, 
			#required=False, 
	#	)


	#x_dni = fields.Char(
	#		string = "DNI", 	
			#required=True, 
			#required=False, 
	#	)



	# IN PROG 

	#country_id = fields.Many2one(
	#		'res.country', 
	#		string = 'País', 

	#		default = 175,	# Peru

			#required=False, 
	#		required=True, 
	#	)



	#city = fields.Selection(
	#		selection = pat_vars._city_list, 
	#		string = 'Departamento',  
	#		default = 'lima', 

	#		required=True, 
			#required=False, 
	#	)



	#street2 = fields.Char(
	#		string = "Distrito", 	
			
			#required=True, 
	#		required=False, 
	#	)



	#street2_sel = fields.Selection(
	#		selection = pat_vars._street2_list, 
	#		string = "Distrito", 	
			
			#required=True, 
	#		required=False, 
	#	)




	#street = fields.Char(
	#		string = "Dirección", 	

	#		required=False, 
	#	)




	#zip = fields.Integer(
	#		string = 'Código',  
			#compute='_compute_zip', 

			#required=True, 			
	#		required=False, 			
	#	)


	# Deprecated 
	#@api.multi
	#def _compute_zip(self):
	#	for record in self:
	#		if (record.street2 in pat_vars.zip_dic) and (record.city == 'lima')  :
	#			record.zip=pat_vars.zip_dic[record.street2]
	#		else:
	#			record.zip=0











# 7 April 2018

	#x_sex_name = fields.Char(
	#		'Sexo', 
	#		required=True, 
	#		compute='_compute_x_sex_name', 
	#	)
	#@api.multi
	#def _compute_x_sex_name(self):
	#	for record in self:
	#		record.x_sex_name = record._dic[record.sex] 




	# Phone 1
	#@api.onchange('phone_1')
	#def _onchange_phone_1(self):
	#	ret = pat_funcs.test_for_digits(self, self.phone_1)
	#	if ret != 0: 
	#		return ret



	# Phone 2
	#@api.onchange('phone_2')
	#def _onchange_phone_2(self):
	#	ret = pat_funcs.test_for_digits(self, self.phone_2)
	#	if ret != 0: 
	#		return ret


	# Deprecated ? 
	#phone_1 = fields.Char(
	#	string="Teléfono 1",
		
		#required=True, 
	#	required=False, 
	#	)

	#phone_2 = fields.Char(
	#	string="Teléfono 2",

	#	required=False, 
	#	)








# 8 April 2018

# Deprecated

	#@api.multi
	#@api.depends('x_date_created')

	#def _compute_x_month_created(self):
	#	for record in self:
	#		#print 
	#		#print 'Compute x_month_created'
	#		record.x_month_created = record.x_date_created.split('-')[1]




	#@api.onchange('x_date_created')
	#def _onchange_x_date_created(self):
		#self.x_datetime_created = self.x_date_created  
		#self.x_datetime_created = '10/03/2017 20:00:00'
	#	self.x_datetime_created = '2017-10-03 20:00:00'
	#'%Y-%m-%d %H:%M:%S'




	#@api.multi
	#@api.depends('state')
	#def _compute_x_datetime_created(self):
	#	for record in self:
	#		if record.comment == 'legacy':
				#record.x_datetime_created = record.x_date_created
	#			record.x_datetime_created = ''




	#@api.multi
	#@api.depends('x_date_created')

	#def _compute_x_year_created(self):
	#	for record in self:
	#		#print 
	#		#print 'Compute x_year_created'
	#		record.x_year_created = record.x_date_created.split('-')[0]





# 16 Apr 2018



	# Date time created 
	#x_datetime_created = fields.Datetime(
	#		string = "Fecha de Creación",
	#		required=False, 

			#default = fields.Datetime.now, 
			#readonly = True, 
			#store=True, 
			#compute='_compute_x_datetime_created', 
	#	)


	#@api.onchange('x_date_created')
	#def _onchange_x_date_created(self):
	#	self.x_year_created = self.x_date_created.split('-')[0]
	#	self.x_month_created = self.x_date_created.split('-')[1]



	#x_year = fields.Char(
	#		string='Year', 
	#		required=False, 
	#	)

	#x_month = fields.Char(
	#		string='Month',
			#required=True, 
	#		required=False, 
	#	)

	#x_year_created = fields.Char(
	#		string='Year created', 
			#default = '', 
			#required=False, 
	#		index=True, 
			#compute='_compute_x_year_created', 
	#	)

	#x_month_created = fields.Char(
	#		string='Month created', 
			#default = '', 
			#required=True, 
			#compute='_compute_x_month_created', 
	#	)




	#x_status = fields.Char(
	#		string='Status', 
	#		default = '00', 
			#required=False, 
	#		required=True, 
	#	)




	# Mark  
	#x_mark = fields.Char(
	#		string='Mark', 
	#	)


	#@api.onchange('x_allergies')
	#def _onchange_x_allergies(self):
	#	if self.x_allergies != False: 
	#		self.x_allergies = self.x_allergies.strip().title()



	#identification_code=fields.Char(
	#		'Patient ID',
	#		size=256, 
	#		help='Patient Identifier provided by the Health Center',
	#		readonly=True
	#	)




	#x_nothing = fields.Char(
	#	'Nothing', 
	#)


	# QC - Flag  
	#x_flag = fields.Char(
	#	"Flag",
	#	default = '', 
	#	store=True, 
	#)




	# Commons 
	#vspace = fields.Char(
	#		' ', 
	#		readonly=True
	#		)





	#x_state = fields.Selection(
	#		selection = pat_vars._state_list, 
	#		string='Estado', 			
	#		default = 'active', 

	#		compute='_compute_x_state', 
	#	)


	#@api.multi
	#@api.depends('state')
	#def _compute_x_state(self):
	#	for record in self:
	#		flag = False
	#		for treatment in record.treatment_ids:
	#			if treatment.progress == False: 
	#				flag = True
	#		if flag:
	#			record.x_state = 'incomplete'
	#		else:
	#			record.x_state = 'active'







# 28 May 2018

# ----------------------------------------------------------- Deprecated ? ------------------------------------------------------

	#x_state = fields.Selection(		
	#	pat_vars._state_list, 
	#	string="Estado", 
		#default='draft', 
		#default='done', 
	#	default='active', 
	#)



