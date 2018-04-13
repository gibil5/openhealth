



# ----------------------------------------------------------- Test Bug ------------------------------------------------------
	# Test Bug 
	#@api.multi 
	#def test_bug(self):
	#	print 'jx'
	#	print 'Test and Hunt !'
	#	target_line = 'quick_body_local_cyst_2'
	#	print target_line
	#	ret = self.x_create_order_lines_target(target_line)
	#	print ret  



# ----------------------------------------------------------- Validate Stock Picking ------------------------------------------------------

	@api.multi 
	def do_transfer(self):
		print 'jx'
		print 'Do Transfer'
		print self.picking_ids
		for pick in self.picking_ids: 
			ret = pick.do_transfer()
			print ret


	# From Action confirm 
	@api.multi 
	def validate_stock_picking(self):
		print 'jx'
		print 'Validate Stock Picking'
		print self.picking_ids
		for pick in self.picking_ids: 
			print pick
			print pick.name 
			ret = pick.force_assign()
			print ret







# ----------------------------------------------------------- Buttons - Order  ------------------------------------------------------

	@api.multi
	def remove_myself(self):  
		self.x_reset()
		self.unlink()





# ----------------------------------------------------------- Nr Mac Clones  ------------------------------------------------------

	@api.multi 
	def get_nr_mc(self):
		nr_mac_clones =	self.env['oeh.medical.appointment'].search_count([
																			('appointment_date','=', self.x_appointment.appointment_date),													
																			('x_machine','=', self.x_appointment.x_machine),
																		]) 
		return nr_mac_clones







	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

	@api.multi
	def open_line_current(self):  

		consultation_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': consultation_id,
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}




