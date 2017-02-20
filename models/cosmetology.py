# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Cosmetology
# 
# Created: 				18 Feb 2017
# Last updated: 	 	Id.



from openerp import models, fields, api

import jxvars



class Cosmetology(models.Model):
	
	_inherit = 'openhealth.process'	
	_name = 'openhealth.cosmetology'
	



	name = fields.Char(
			string="Cosmiatría #", 
			compute='_compute_name', 
		)




	therapist = fields.Many2one(
			'openhealth.therapist',
			required=True, 
			)



	patient = fields.Many2one(
			'oeh.medical.patient',
			required=True, 
			)



	chief_complaint = fields.Selection(
			selection = jxvars._chief_complaint_list, 
			required=True, 
			)




	# State 
	_state_list = [
        			#('empty', 			'Inicio'),

					#('consultation', 	'Consulta'),

        			('service', 		'Servicio'),
        			
        			('budget', 			'Presupuesto'),

        			('invoice', 		'Facturado'),
        			
        			('procedure', 		'Procedimiento'),

        			('sessions', 		'Sesiones'),

        			#('controls', 		'Controles'),

        			('done', 			'Completo'),
        		]


	state = fields.Selection(
			selection = _state_list, 
			string='State', 			
			default = False, 

			#compute="_compute_state",
		)



# ----------------------------------------------------------- Computes ------------------------------------------------------
	@api.multi
	#@api.depends('start_date')

	def _compute_name(self):
		for record in self:
			record.name = 'CO0000' + str(record.id) 







# ----------------------------------------------------------- Buttons ------------------------------------------------------
	@api.multi
	def open_line_current(self):  

		cosmetology_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Cosmetology Current', 
				'view_type': 'form',
				'view_mode': 'form',

				#'res_model': 'openhealth.cosmetology',
				'res_model': self._name,

				'res_id': cosmetology_id,

				#'target': 'inline'.
				'target': 'current',

				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								'form': {'action_buttons': True, }
							},

				'context': 	{
							}
		}





# ----------------------------------------------------------- Create Service ------------------------------------------------------
	@api.multi 
	def create_service(self):

		print 
		print 'jx'
		print 'Create Service'





# ----------------------------------------------------------- Create order ------------------------------------------------------
	@api.multi 
	def create_order(self):

		print 
		print 'jx'
		print 'Create order'





# ----------------------------------------------------------- Create invoice ------------------------------------------------------
	@api.multi 
	def create_invoice(self):

		print 
		print 'jx'
		print 'Create invoice'



# ----------------------------------------------------------- Create procedure ------------------------------------------------------
	@api.multi 
	def create_procedure(self):

		print 
		print 'jx'
		print 'Create procedure'




# ----------------------------------------------------------- Create session ------------------------------------------------------
	@api.multi 
	def create_sessions(self):

		print 
		print 'jx'
		print 'Create sessions'











