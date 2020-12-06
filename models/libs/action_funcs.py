# -*- coding: utf-8 -*-
"""
	Action Funcs - Used by Treatment
	Created: 			02 Aug 2020
	Last up: 	 		 4 oct 2020
"""

_action_window = "ir.actions.act_window"

# ----------------------------------------------------------- Open myself ------
def open_myself(res_model, res_id):
	"""
	Used by Treatment - create_order_pro
	"""
	print()
	print('pl_creates - open_order')

	return {
		# Mandatory
		'type': _action_window,
		'name': 'Open Consultation Current',
		# Window action
		'res_model': res_model,
		'res_id': res_id,
		# Views
		"views": [[False, "form"]],
		'view_mode': 'form',
		'target': 'current',
		#'view_id': view_id,
		#"domain": [["patient", "=", self.patient.name]],
		#'auto_search': False,
		'flags': {
				'form': {'action_buttons': True, }
		},
		'context':   {}
	}

# ---------------------------------------------------- Open line current -------
def open_line_current(res_model, res_id):
	"""
	Used by Order
	"""
	print('open_line_current')
	return {
			'type': _action_window,
			'name': ' Edit Order Current',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': res_model,
			'res_id': res_id,
			'target': 'current',
			'flags': {
					'form': {'action_buttons': True, }
					},
			'context': {}
	}



# ----------------------------------------------------------- Create Shopping Cart -----------------
def open_order(order):
	"""
	Used by Treatment - create_order_pro
	"""
	print()
	print('pl_creates - open_order')

	return {
			# Created
			'res_id': order.id,
			# Mandatory
			'type': _action_window,
			'name': 'Open Order Current',
			# Window action
			'res_model': 'sale.order',
			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
					'form': {'action_buttons': True, }
					},
			'context': {}
		}
