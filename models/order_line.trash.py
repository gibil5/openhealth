
# ------------------------------------------------------------------------------------------------------------------------------#
#  																															  	#
# ----------------------------------------------------------- Order line -------------------------------------------------------#
#																																#
# ------------------------------------------------------------------------------------------------------------------------------#





# 19 Jan 2016



	# Procedure
	#x_appointment_date = fields.Datetime(
	#		string="Fecha", 
			#readonly=True,
			#readonly=False,
			#states={'Scheduled': [('readonly', False)]})
	#		)

	#x_doctor_name = fields.Char(
	#		string="Médico", 
	#	)

	#x_machine = fields.Selection(
	#		string="Sala", 
	#		selection = jxvars._machines_list, 
			#required=True, 
	#	)

	#x_duration = fields.Float(
	#		string="Duración", 
	#	)








# 17 Jan 2017



	#@api.multi
	#@api.depends('x_price')	
	#def _compute_price_total(self):
	#	for record in self:
	#		record.x_price_wigv = math.ceil(record.x_price * 1.18)


	#@api.onchange('price_total')
	
	#def _onchange_price_total(self):
	#	print 
	#	print 'on change price total'
	#	print self.price_total

	#	self.price_total = math.ceil(self.price_total)

	#	print self.price_total
	#	print 



	x_price_vip_wigv = fields.Float(
			string="Precio Vip",

			compute="_compute_x_price_vip_wigv",
		)

	#@api.multi
	@api.depends('x_price_vip')
	
	def _compute_x_price_vip_wigv(self):
		for record in self:

			if record.x_price_vip == 0.0:
				#record.x_price_vip = record.x_price
				price_vip = record.x_price
			else:
				price_vip = record.x_price_vip


			#record.x_price_vip_wigv = math.ceil(record.x_price_vip * 1.18)
			record.x_price_vip_wigv = math.ceil(price_vip * 1.18)





	x_price_wigv = fields.Float(
			string="Precio",

			compute="_compute_x_price_wigv",
		)


	#@api.multi
	@api.depends('x_price')
	
	def _compute_x_price_wigv(self):
		for record in self:
			record.x_price_wigv = math.ceil(record.x_price * 1.18)




	x_price = fields.Float(
			string="Price Std",
		)






