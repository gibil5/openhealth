



# 12 Apr 2018




	#@api.multi
	#def _compute_patient(self):
	#	for record in self:
	#		patient = self.env['oeh.medical.patient'].search([
	#															('name', '=', self.partner_id.name), 
	#													],
														#order='appointment_date desc',
	#													limit=1,
	#												)
	#		if patient.name != False:
	#			record.patient = patient










	#receipt = fields.Many2one(
	#	'openhealth.receipt',
	#	string='Boleta de venta',
	#)

	#x_invoice = fields.Many2one(
	#	'openhealth.invoice',
	#	string='Factura',
	#)

	#x_advertisement = fields.Many2one(
	#	'openhealth.advertisement',		
	#	string='Canje',
	#	)

	#x_sale_note = fields.Many2one(
	#	'openhealth.sale_note',		
	#	string='Nota de venta',
	#	)

	#x_ticket_receipt = fields.Many2one(
	#	'openhealth.ticket_receipt',		
	#	string='Ticket Boleta',
	#	)

	#x_ticket_invoice = fields.Many2one(
	#	'openhealth.ticket_invoice',		
	#	string='Ticket Factura',
	#	)







	# Legacy thing 

	# Type (product or service)
	#x_cancel_reason = fields.Char(
	#x_cancel_reason = fields.Selection(
	#		selection=ord_vars._owner_type_list, 
			#string='Motivo de anulación', 
	#		string='Tipo', 
	#	)

	# Product Odoo 
	#x_cancel_owner = fields.Char(
			#string='Quién anula', 
	#		string='Producto', 
	#	)




	# Categ
	#categ = fields.Char(
	#		'Categoria', 
	#		compute="_compute_categ",
	#	)

	#@api.multi
	#def _compute_categ(self):
	#	for record in self:
	#		for line in record.order_line:
	#			record.categ = line.product_id.categ_id.name




	# Deprecated !
	#margin = fields.Float(
	#		string="Margen"
	#	)





	# Comment 
	#comment = fields.Selection(
	#	[
	#	('product', 'Product'),
	#	('service', 'Service'),
	#	], 
	#	string='Comment', 
	#	default='product', 
	#	readonly=True
	#)
















	# Ooor - Highly Deprecated !!!
	#x_age = fields.Integer(string='Age', default=52, help='Age of student')

	#x_group = fields.Char(string='Group', compute='_compute_x_group', help='Group of student', store=True)

	#@api.depends('x_age')
	#def _compute_x_group(self):
	#	for record in self:
	#		record.x_group = 'NA'
	#		if record.x_age > 5 and record.x_age <= 10:
	#			record.x_group = 'A'
	#		elif record.x_age > 10 and record.x_age <= 12:
	#			record.x_group = 'B'
	#		elif record.x_age > 12:
	#			record.x_group = 'C'


	#x_year = fields.Char(
	#		compute="_compute_x_year",
	#		string='Year', 
	#		default=False, 
	#	)

	#@api.one
	#@api.depends('date_order')
	#def _compute_x_year(self):
	#	for record in self:
	#		date_format = "%Y-%m-%d %H:%M:%S"
	#		date = datetime.datetime.strptime(record.date_order, date_format)
	#		record.x_year = date.year


	#x_month = fields.Char(
	#		string='Month', 
	#		required=False, 
	#		compute="_compute_x_month",
	#	)

	#@api.depends('date_order')
	#def _compute_x_month(self):
	#	for record in self:
	#		date_format = "%Y-%m-%d %H:%M:%S"
	#		date = datetime.datetime.strptime(record.date_order, date_format)
	#		record.x_month = date.month






	#note = fields.Text(
	#		"Nota",					
	#	)



	# Doctor name  
	#x_doctor_name = fields.Char(
	#	)
	
	#doctor_name = fields.Char(
	#							default = 'generic doctor',
	#	)





	# Doctor name  
	#compute="_compute_x_doctor_name",
	#@api.multi
	#@api.depends('x_doctor')

	#def _compute_x_doctor_name(self):
	#	for record in self:
	#		record.x_doctor_name = record.x_doctor.name 





	# Partner name  
	#x_partner_name = fields.Char(
	#								default = 'generic partner',
									#compute="_compute_x_partner_name",
	#)
	
	#@api.multi
	#@api.depends('partner_id')

	#def _compute_x_partner_name(self):
	#	for record in self:
	#		record.x_partner_name = record.partner_id.name 






	# Number of paymethods  
	#pm_complete = fields.Boolean(
	#							default = False, 
	#							readonly=False,
								#string="Pm Complete",
								#compute="_compute_pm_complete",
	#)
	
	#@api.multi
	#@api.depends('pm_total')

	#def _compute_pm_complete(self):
	#	#print 'Compute Pm Complete'
	#	for record in self:
	#		if record.pm_total == record.x_amount_total: 
	#			#print 'Equal !'
	#			record.pm_complete = True
				#record.state = 'payment'
	#		else:
	#			#print 'Not Equal'
	#		#print record.pm_total
	#		#print record.x_amount_total
	#		#print record.pm_complete
	#		#print record.state





	# Payment Complete
	#x_payment_complete = fields.Boolean(
								#default = False, 
								#readonly=False,
								#string="Pm Complete",
	#)







	# Consultation - DEPRECATED !!!
	#consultation = fields.Many2one(
	#		'openhealth.consultation',
	#		string="Consulta",
	#		ondelete='cascade', 
	#	)




	#x_copy_created = fields.Boolean(
	#	default=False,
	#)





	#closing = fields.Many2one(
	#		'openhealth.closing',
	#		ondelete='cascade', 
	#		string="Cierre", 
	#	)






	# Target 
	#x_target = fields.Selection(
	#		string="Target", 
	#		selection = app_vars._target_list, 

	#		compute='_compute_x_target', 
	#	)


	#@api.multi
	#@api.depends('x_doctor')
	#def _compute_x_target(self):
	#	for record in self:
	#		if record.treatment.name != False: 
	#			record.x_target = 'doctor'
	#		if record.cosmetology.name != False: 
	#			record.x_target = 'therapist'








	# Total of Payments
	#pm_total = fields.Float(
								#string="Total",
								#compute="_compute_pm_total",
	#)
	
	#@api.multi

	#def _compute_pm_total(self):
	#	for record in self:
	#		total = 0.0
	#		for pm in record.x_payment_method:
	#			total = total + pm.subtotal
	#		record.pm_total = total
	#		record.x_payment_complete = True




	# Chief complaint 
	#x_chief_complaint = fields.Selection(
	#		string = 'Motivo de consulta', 
	#		selection = jxvars._chief_complaint_list, 
	#		)



