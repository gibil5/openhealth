
# ----------------------------------------------------------- Product ----------	
	#product_id = fields.Many2one(
	#	'product.product',
	#	string='Product', 
	#	domain=[('sale_ok', '=', True)], 
	#	change_default=True, 
	#	ondelete='restrict', 
	#	required=True
	#	)




# ----------------------------------------------------------- New ----------
	# Price manual
	x_price_manual = fields.Float(
		string="Precio manual",
		required=False,
		default=-1,
	)

	# Price std
	x_price_std = fields.Float(
		string="Precio Std",
		required=False,

		compute='_compute_price_std',
	)

	@api.multi
	def _compute_price_std(self):
		for record in self:
			record.x_price_std = record.product_id.list_price

	# Price Vip
	x_price_vip = fields.Float(
		string="Precio Vip",
		required=False,

		compute='_compute_price_vip',
	)

	@api.multi
	def _compute_price_vip(self):
		for record in self:
			record.x_price_vip = record.product_id.x_price_vip


	# Price Vip Return
	x_price_vip_return = fields.Float(
		string="Precio Vip R",
		required=False,

		compute='_compute_price_vip_return',
	)

	@api.multi
	def _compute_price_vip_return(self):
		for record in self:
			record.x_price_vip_return = record.product_id.x_price_vip_return





	#x_qty_int = fields.Integer(
	x_qty = fields.Integer(
			compute='_compute_x_qty',
		)

	@api.multi
	def _compute_x_qty(self):
		for record in self:
			record.x_qty = record.product_uom_qty




# ----------------------------------------------------------- Vip ---------------------------------

	# Vip in progress
	x_vip_inprog = fields.Boolean(
			default=False,
			compute='_compute_vip_inprog',
		)

	@api.multi
	def _compute_vip_inprog(self):
		for record in self:
			for line in record.order_id.order_line:
				if line.product_id.default_code == '495':
					record.x_vip_inprog = True





# ----------------------------------------------------------- Compact -----------------------------
	# Description
	x_description = fields.Text(
		string='Nombre compacto',

		compute='_compute_x_description',
	)

	@api.multi
	def _compute_x_description(self):
		for record in self:
			if record.product_id.x_name_short in ['generic_product', 'generic_service']:
				record.x_description = record.name
			else:
				record.x_description = record.product_id.x_name_ticket






















