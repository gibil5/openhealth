

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




# 21 Jan 2018

	def do_new_transfer(self, cr, uid, ids, context=None):
		pack_op_obj = self.pool['stock.pack.operation']
		data_obj = self.pool['ir.model.data']
		for pick in self.browse(cr, uid, ids, context=context):
			to_delete = []
			if not pick.move_lines and not pick.pack_operation_ids:
				raise UserError(_('Please create some Initial Demand or Mark as Todo and create some Operations. '))
			# In draft or with no pack operations edited yet, ask if we can just do everything
			if pick.state == 'draft' or all([x.qty_done == 0.0 for x in pick.pack_operation_ids]):
				# If no lots when needed, raise error
				picking_type = pick.picking_type_id
				if (picking_type.use_create_lots or picking_type.use_existing_lots):
					for pack in pick.pack_operation_ids:
						if pack.product_id and pack.product_id.tracking != 'none':
							raise UserError(_('Some products require lots, so you need to specify those first!'))
				view = data_obj.xmlid_to_res_id(cr, uid, 'stock.view_immediate_transfer')
				wiz_id = self.pool['stock.immediate.transfer'].create(cr, uid, {'pick_id': pick.id}, context=context)
				return {
					 'name': _('Immediate Transfer?'),
					 'type': 'ir.actions.act_window',
					 'view_type': 'form',
					 'view_mode': 'form',
					 'res_model': 'stock.immediate.transfer',
					 'views': [(view, 'form')],
					 'view_id': view,
					 'target': 'new',
					 'res_id': wiz_id,
					 'context': context,
				 }

			# Check backorder should check for other barcodes
			if self.check_backorder(cr, uid, pick, context=context):
				view = data_obj.xmlid_to_res_id(cr, uid, 'stock.view_backorder_confirmation')
				wiz_id = self.pool['stock.backorder.confirmation'].create(cr, uid, {'pick_id': pick.id}, context=context)
				return {
						 'name': _('Create Backorder?'),
						 'type': 'ir.actions.act_window',
						 'view_type': 'form',
						 'view_mode': 'form',
						 'res_model': 'stock.backorder.confirmation',
						 'views': [(view, 'form')],
						 'view_id': view,
						 'target': 'new',
						 'res_id': wiz_id,
						 'context': context,
					 }
			for operation in pick.pack_operation_ids:
				if operation.qty_done < 0:
					raise UserError(_('No negative quantities allowed'))
				if operation.qty_done > 0:
					pack_op_obj.write(cr, uid, operation.id, {'product_qty': operation.qty_done}, context=context)
				else:
					to_delete.append(operation.id)
			if to_delete:
				pack_op_obj.unlink(cr, uid, to_delete, context=context)
		self.do_transfer(cr, uid, ids, context=context)
		return







# 9 Feb 2018

	#location_dest_id = fields.Many2one(
	#		'stock.location', 
	#		required=True,
	#		string="Destination Location Zone",
	#		default=_default_location_destination, 
	#		readonly=True, 
	#		states={'draft': [('readonly', False)]}
	#	)

	#min_date = fields.function(
	#		get_min_max_date, 
	#		multi="min_max_date", 
	#		fnct_inv=_set_min_date,
	#		store={'stock.move': (_get_pickings_dates_priority, ['date_expected', 'picking_id'], 20)}, type='datetime', states={'done': [('readonly', True)], 'cancel': [('readonly', True)]}, string='Scheduled Date', select=1, help="Scheduled time for the first part of the shipment to be processed. Setting manually a value here would set it as expected date for all the stock moves.", 
	#		track_visibility='onchange'
	#	)






	@api.multi
	def remove_myself(self):  

		print 'jx'
		print 'Remove myself'


		#self.pack_operation_exist = False
		#self.picking_type_id = False
		#self.state = 'draft'

		#for po in self.pack_operation_pack_ids:
		#	po.state = 'draft'
		
		#for po in self.pack_operation_product_ids:
		#	po.state = 'draft'
		
		#for po in self.pack_operation_ids:
		#	po.state = 'draft'

		#self.pack_operation_pack_ids.unlink()
		#self.pack_operation_product_ids.unlink()
		#self.pack_operation_ids.unlink()



		self.unlink()



