# -*- coding: utf-8 -*-
#
# 	Event 
# 
#

from openerp import models, fields, api

import event_vars



class Event(models.Model):
	
	_name = 'openhealth.event'

	#_inherit='openhealth.sale_document'



	name = fields.Char(
			string="Evento #", 
			required=True, 
			compute='_compute_name', 
			)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'EV-' + str(record.id) 




	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			required=True, 
		)




  	message = fields.Char(
			string="Mensaje", 
			required=True, 
			)

  	owner = fields.Char(
			string="Quién ?", 
			required=True, 
			)




	x_type = fields.Selection(

			string="Tipo", 

			selection = event_vars._events_list, 
						
			required=True, 
		)


