

# 18 nov 2017


			return {
					'type': 'ir.actions.act_window',
					'name': ' New Proof Current', 

					'view_type': 'form',
					'view_mode': 'form',	
					'target': 'current',

					'res_model': model,
					'res_id': proof_id,

					'flags': 	{
									#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
									'form': {'action_buttons': True, }
								},

					'context': {
								'default_payment_method': self.id,
								'default_total': self.total,							
								'default_date_created': self.date_created,
								'default_order': self.order.id,
								'default_name': self.saledoc_code,
								'default_partner': self.partner.id,
								'default_my_firm': self.order.x_my_company.x_firm, 
								'default_my_address': self.order.x_my_company.x_address, 
								'default_my_ruc': self.order.x_my_company.x_ruc, 
								'default_my_phone': self.order.x_my_company.phone, 
							}
					}

