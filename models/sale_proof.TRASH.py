



	# Print
	@api.multi 
	def print_ticket(self):

		print 'jx'
		print 'Print Ticket'

		ret = 0 
		return ret 







# Other 



	cr = fields.Char(
			default='-------------------------------------------------------------------', 
		)


	warning = fields.Char(
			default='Por medio del presente, se informa que en caso de cancelación de tratamiento \
			o de la consulta por parte del paciente, ya sea de manera expresa o tácita, este autoriza \
			a la empresa la retención del 15% del costo del tratamiento o el 25% de la consulta, sea el caso, \
			por concepto de gastos administrativos y gastos operativos. \
			(Art. 67 Ley 29571, Art 40 Ley General de Salud)', 
		)



	serial_nr = fields.Char(
		)

	authorization = fields.Char(
		)





# My Company


	# Firm
	my_firm = fields.Char(
			"Razon social",

			#compute='_compute_my_firm', 
		)

	#@api.multi
	#@api.depends('')
	#def _compute_my_firm(self):
	#	for record in self:
	#		record.my_firm = record.order.x_my_company.x_firm




	# Ruc
	my_ruc = fields.Char(

			"Ruc",
			#compute='_compute_my_ruc', 
		)

	#@api.multi
	#@api.depends('')
	#def _compute_my_ruc(self):
	#	for record in self:
	#		record.my_ruc = record.order.x_my_company.x_ruc




	# Phone 
	my_phone = fields.Char(

			"Teléfono",
			#compute='_compute_my_phone', 
		)

	#@api.multi
	#@api.depends('')
	#def _compute_my_phone(self):
	#	for record in self:
	#		record.my_phone = record.order.x_my_company.phone





	# Address
	my_address = fields.Char(

			"Dirección",
			#compute='_compute_my_address', 
		)

	#@api.multi
	#@api.depends('')
	#def _compute_my_address(self):
	#	for record in self:
	#		com = record.order.x_my_company
	#		record.my_address = com.street + ' - ' + com.street2 + ' - ' + com.city





	# Website
	my_website = fields.Char(

			"Website",
			compute='_compute_my_website', 
		)

	@api.multi
	#@api.depends('')
	def _compute_my_website(self):
		for record in self:
			record.my_website = record.order.x_my_company.website




	# Email
	my_email = fields.Char(

			"Email",
			compute='_compute_my_email', 
		)

	@api.multi
	#@api.depends('')
	def _compute_my_email(self):
		for record in self:
			record.my_email = record.order.x_my_company.email










# Customer 



	# Name
	par_name = fields.Char(

			"Nombre",
			compute='_compute_par_name', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_name(self):
		for record in self:

			par = record.order.partner_id
			record.par_name = par.name
			






	# DNI
	par_dni = fields.Char(

			"DNI",
			compute='_compute_par_dni', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_dni(self):
		for record in self:

			#record.par_dni = record.order.partner_id.x_dni

			record.par_dni = record.partner.x_dni




	# Address
	par_address = fields.Char(

			"Dirección",
			compute='_compute_par_address', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_address(self):
		for record in self:

			#par = record.order.partner_id
			par = record.partner

			if par.street != False and par.street2 != False and par.city != False: 
				record.par_address = par.street + ' - ' + par.street2 + ' - ' + par.city





	# Ruc
	par_ruc = fields.Char(

			"Ruc",
			compute='_compute_par_ruc', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_ruc(self):
		for record in self:

			par = record.order.partner_id

			record.par_ruc = par.x_ruc





	# Firm
	par_firm = fields.Char(
			"Razon social",

			compute='_compute_par_firm', 
		)

	@api.multi
	#@api.depends('')
	def _compute_par_firm(self):
		for record in self:

			par = record.order.partner_id

			record.par_firm = par.x_firm




	# Counter
	#counter = fields.Char(
	#		string="Counter", 
	#		default="0", 
	#		required=True, 
	#	)

	# Code
	#code = fields.Char(
	#		string="Code", 
	#		default="x", 
	#		required=True, 
	#	)




	#sale_document = fields.Many2one('openhealth.sale_document',
	#		ondelete='cascade', 
	#		string="Sale document",
	#		)


	# Open Payment Method
	#@api.multi 
	#def open_pm(self):
		#print 
		#print 'Open Payment method'
	#	ret = self.payment_method.open_myself()
	#	return ret 
	# open_order












# Sale

	# Order lines 
	order_line = field_One2many=fields.One2many(

			'sale.order.line',
			'order_id',
			'Order line',

			compute='_compute_order_line', 			
	)

	@api.multi
	#@api.depends('')
	def _compute_order_line(self):
		for record in self:
			record.order_line = record.order.order_line





	# Order lines text 
	order_line_txt = field_One2many=fields.Text(

			'Order Lines Text',

			#default = '', 
			compute='_compute_order_line_txt', 			
	)

	@api.multi
	#@api.depends('')
	def _compute_order_line_txt(self):
		for record in self:

			print 'jx'
			print 'Compute order line txt'

			txt = 'Descripción\tCNT\tP. UNIT.\tSubtotal\n'

			for line in record.order_line: 
				print line
				print line.name 

				#txt = txt + line.name + '\t' + line.product_uom_qty + '\t' + line.price_unit + '\t' + line.price_subtotal + '\n'
				txt = txt + line.name + '\t' + str(line.product_uom_qty) + '\t' + str(line.price_unit) + '\t' + str(line.price_subtotal) + '\n'

				#txt = txt + line.name + '\n'
				#txt = txt + line.name 
				#txt = txt + line.name + '\n'


			record.order_line_txt = txt






	# Total in Words
	total_in_words = fields.Char(

			"",
			compute='_compute_total_in_words', 
		)

	@api.multi
	#@api.depends('')
	def _compute_total_in_words(self):
		for record in self:

			#words = record.total
			words = num2words(record.total, lang='es')

			record.total_in_words = words.title() + ' Soles'








	# Total Net
	total_net = fields.Float(

			"Neto",
			compute='_compute_total_net', 
		)

	@api.multi
	#@api.depends('')
	def _compute_total_net(self):
		for record in self:

			record.total_net = record.total * 0.82





	# Total Tax
	total_tax = fields.Float(

			"Neto",
			compute='_compute_total_tax', 
		)

	@api.multi
	#@api.depends('')
	def _compute_total_tax(self):
		for record in self:

			record.total_tax = record.total * 0.18


