



# ----------------------------------------------------------- Prices - Vip ------------------------------
	# Price subtotal 
	price_subtotal = fields.Float(
			string="jx Sub-Total",

			compute="_compute_price_subtotal",
		)


	#@api.multi
	@api.depends('price_unit', 'x_price_vip')
	def _compute_price_subtotal(self):

		for record in self:
		
			if record.order_id.x_partner_vip and record.x_price_vip != 0.0:
					record.price_subtotal = record.x_price_vip * record.product_uom_qty

			else: 
				record.price_subtotal = record.price_unit * record.product_uom_qty



   # Price Unit
	price_unit = fields.Float(
		#'Unit Price', 
		'Precio', 
		required=True, 
		digits=dp.get_precision('Product Price'), 
		default=0.0, 
	
		compute='_compute_price_unit', 
	)

	@api.multi
	def _compute_price_unit(self):
		for record in self:

			# Manual
			if record.x_price_manual != False:                      									             
				record.price_unit = record.x_price_manual
			
			else:
				
				# Not VIP
				if      not record.order_id.x_partner_vip       and     not record.x_vip_inprog:       
					record.price_unit = record.x_price_std

				# VIP
				else:                                               									
					# Vip Return
					if record.x_comeback    and     record.x_price_vip_return != 0:
						record.price_unit = record.product_id.x_price_vip_return

					
					else: 
						# Just Vip	
						if record.x_price_vip != 0: 
							record.price_unit = record.x_price_vip
						
						# Standard
						else:
							record.price_unit = record.x_price_std



