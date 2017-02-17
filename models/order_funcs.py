# -*- coding: utf-8 -*-


from openerp import models, fields, api





# ---------------------------------------------- Event --------------------------------------------------------
@api.multi 
def create_event(self):

		print 
		print 'jx'
		print 'Create Event'
		print
		print

		nr_pm = self.env['openhealth.event'].search_count([('order','=', self.id),]) 

		name = 'Evento ' + str(nr_pm + 1)

		x_type = 'cancel'


		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.event',				
				#'res_id': receipt_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_order': self.id,

							'default_name': name,

							'default_x_type': x_type,
							}
				}

	# create_event





