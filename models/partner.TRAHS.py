

# 6 Oct 2017




# Extremely Dangerous !!!
# Do not do this. 


	#property_product_pricelist = fields.Many2one(
	#	relation='product.pricelist', 
	#	string="Sale Pricelist", 
	#	help="This pricelist will be used, instead of the default one, for sales to the current partner", 
		#compute='_compute_property_product_pricelist', 
	#)


#	@api.multi
	#@api.depends('x_card')

#	def _compute_property_product_pricelist(self):
#		for record in self:
			#x_card = record.env['openhealth.card'].search([
			#												('patient_name','=', record.name),
			#											],
														#order='appointment_date desc',
			#											limit=1,)

			#if x_card.name != False:
			#	record.property_product_pricelist = True 
			#record.property_product_pricelist = 'VIP'
			#record.property_product_pricelist = 'VIP' 
#			record.property_product_pricelist = False 
# 



