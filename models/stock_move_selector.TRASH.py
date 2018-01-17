

# 17 Jan 2018

		return {

			'type': 'ir.actions.act_window',
			'name': 'Open Stock Moves',
			'res_model': 'stock.move',
			#'res_id': treatment_id,


			# Views 

			#"views": [[False, "form"]],
			"views": [[False, "tree"]],

			#'view_mode': 'form',
			'view_mode': 'tree',

			'target': 'current',
			
			#'view_id': view_id,
			
			#'auto_search': False, 


			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},			


			"domain": 	[
							["product_id", "=", self.product_id.id], 
							#['state', '=', 'done'],
						],

			'context':   {}
		}