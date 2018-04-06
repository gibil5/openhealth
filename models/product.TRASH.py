

# 2 Feb 2018

	#'base': fields.selection(

	#	[('list_price', 'Public Price'), ('standard_price', 'Cost'), ('pricelist', 'Other Pricelist')], 

	#	string="Based on", 
	#	required=True,
	#	help='Base price for computation. \n Public Price: The base price will be the Sale/public Price. \n Cost Price : The base price will be the cost price. \n Other Pricelist : Computation of the base price based on another Pricelist.'
	#),






# 6 April 2018


	# Description - For Tickets 
	description = fields.Text(

			'Description',
		
			default="x", 

			#translate=True,
			#help="A precise description of the Product, used only for internal information purposes."

			#compute='_compute_description', 
		)



	#@api.multi
	#@api.depends('state')
	#def _compute_description(self):
	#	print 'jx'
	#	print 'compute description'
	#	for record in self:
	#		print 'jx'
	#		print record.description
	#		record.description = record.x_name_short
	#		print record.description








	
	# Dperecated !!!

	# Before 
	#x_date_updated = fields.Date(
	#		required=False, 
	#		)

	# Only Products 
	#x_brand = fields.Char(
	#		string="Marca", 
	#		required=False, 
	#	)

	#x_date_created = fields.Date(
	#		required=False, 
	#	)

