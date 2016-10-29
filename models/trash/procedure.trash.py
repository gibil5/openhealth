

# 28 Oct 2016


	#vspace = fields.Char(
	#		' ', 
	#		readonly=True
	#		)

	#evaluation_start_date = fields.Date(
	#		string = "Fecha", 	
	#		default = fields.Date.today, 
	#		required=True, 
	#		)
	
	#chief_complaint = fields.Selection(
	#		string = 'Motivo de consulta', 
	#		selection = jxvars._pathology_list,  
	#		required=True, 
	#		)

	# Product
	#product = fields.Many2one(
	#		'product.template',
	#		string="Producto",
	#		required=True, 
	#		)
	
	#laser = fields.Selection(
	#		selection = jxvars._laser_type_list, 
	#		string="Láser", 			
	#		compute='_compute_laser', 			
	#		)
	
	#@api.depends('product')
	#def _compute_laser(self):
	#	for record in self:
	#		record.laser = record.product.x_treatment 


