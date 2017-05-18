# -*- coding: utf-8 -*-
#
# 	payment_method_line
# 
#

from openerp import models, fields, api

import ord_vars


class payment_method_line(models.Model):
	
	_name = 'openhealth.payment_method_line'



	name = fields.Char(
			#string="Medio de Pago", 
			string="Pago", 
			required=True, 
			readonly=True, 
		)






	# Open Order
	@api.multi 
	def open_pm(self):

		print 
		print 'Open Pm'



		payment_method_id = self.payment_method.id  

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Order Current',


			# Window action 
			'res_model': 'openhealth.payment_method',
			'res_id': payment_method_id,


			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',


			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 

			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},			

			'context':   {

			}
		}


	# open_pm











	payment_method = fields.Many2one(

			'openhealth.payment_method',

			string="Módulo de Pago",

			ondelete='cascade', 
			required=True, 
			
			readonly=True, 
		)




	vspace = fields.Char(
			' ', 
			readonly=True
			)




	method = fields.Selection(
			string="Medio", 
			selection = ord_vars._payment_method_list, 			
			required=True, 
		)




	subtotal = fields.Float(
			string = 'Sub-total', 
			required=True, 
		)



	#@api.onchange('subtotal')
	#def _onchange_subtotal(self):
	#	self.balance = self.total - (self.pm_total + self.subtotal)



	code = fields.Char(
			string="Codigo", 
			#required=True, 
		)


