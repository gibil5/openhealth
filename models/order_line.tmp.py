






	x_price_subtotal = fields.Monetary(
			string='Subtotal - jx', 
			readonly=True, 
			#store=True, 

			compute='_compute_x_price_subtotal', 
		)

	@api.multi
	def _compute_x_price_subtotal(self):
		for record in self:
			if record.x_comeback: 
				record.x_price_subtotal = record.product_id.x_price_vip_return
			else:		
				record.x_price_subtotal = 55















#product_uom_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'), required=True, default=1.0)
#product_uom = fields.Many2one('product.uom', string='Unit of Measure', required=True)











	x_test = fields.Char(
			compute='_compute_test', 
		)


	@api.multi

	def _compute_test(self):

		for record in self:

			record.x_test = 'x'

			for service in record.order_id.patient.x_service_quick_ids:

				if service.service.name == record.name  	and 	service.comeback: 
				
					record.x_test = 'GOTCHA !'










	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
		for line in self:

			price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
			
			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
			
			line.update({
				'price_tax': taxes['total_included'] - taxes['total_excluded'],
				
				'price_total': taxes['total_included'],

				'price_subtotal': taxes['total_excluded'],
			})



	# Price Subtotal 
	#price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal - jx', readonly=True, store=True)


	#price_subtotal = fields.Float(
	#		string="Precio Vip",
	#		required=False, 

	#		compute='_compute_price_subtotal', 
	#	)




