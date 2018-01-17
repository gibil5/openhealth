

# 17 Jan 2018


	def _default_location_destination(self):
		# retrieve picking type from context; if none this returns an empty recordset

		#picking_type_id = self._context.get('default_picking_type_id')


		name = 'Cremas Despacho'

		pt = self.env['stock.picking.type'].search([
															('name', '=', name),			
				
													],
													#order='start_date desc',
													limit=1,
													)

		picking_type_id	= pt.id 



		picking_type = self.env['stock.picking.type'].browse(picking_type_id)
		
		return picking_type.default_location_dest_id



	location_dest_id = fields.Many2one(
			'stock.location', 
			required=True,
			
			#string="Destination Location Zone",
			string="Destino",

			default=_default_location_destination, 
			
			readonly=True, 
			states={'draft': [('readonly', False)]}, 
		)

