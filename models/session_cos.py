# -*- coding: utf-8 -*-
#
# 	*** Session Cos
#

# Created: 				 24 Feb 2017
# Last updated: 	 	 24 Feb 2017 



from openerp import models, fields, api
from datetime import datetime



from . import jxvars
from . import cosvars
from . import time_funcs
from . import jrfuncs




class SessionCos(models.Model):
	
	_name = 'openhealth.session.cos'
	
	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.session'




	treatment = fields.Many2one(
			'openhealth.treatment',
			#ondelete='cascade', 
			required=False, 
			)




	doctor = fields.Many2one(
			'oeh.medical.physician',

			string = "Cosmeatra", 	
			
			)





	#cosmetology = fields.Many2one('openhealth.cosmetology',
	#		ondelete='cascade', 
	#		string="Cosmetología",
			#required=True, 
	#		)



	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 

			selection = cosvars._chief_complaint_list, 

			#required=True, 
			required=False, 
			)





	procedure = fields.Many2one(

			'openhealth.procedure.cos',
			
			string="Procedimiento",
			
			readonly=True,
			
			ondelete='cascade', 


			#required=False, 
			#required=True, 
			)
			




	procedure_applied = fields.Selection(
			string = 'Procedimiento aplicado', 

			selection = cosvars._procedure_list, 

			#required=True, 
			#required=False, 
		)





	navel = fields.Float(
			string="Ombligo (cm)", 		
		)

	abdomen_low = fields.Float(
			string="Abdomen superior (cm)", 		
		)

	abdomen_high = fields.Float(
			string="Abdomen inferior (cm)", 		
		)





	config_volume = fields.Float(
			string="Dosificación (ml)", 		
		)

	config_time = fields.Float(
			string="Tiempo (min)", 		
		)



	comments = fields.Text(
			string="Comentarios", 
		)









	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

	@api.multi
	def open_line_current(self):  




		return {
				'type': 'ir.actions.act_window',

				'name': 'Edit Session Current', 
				
				'view_type': 'form',
				
				'view_mode': 'form',
				
				'res_model': self._name,
				
				'res_id': self.id,
				
				'target': 'current',

				'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
						},
				
				'context': {

							#'default_co2_power': co2_power,	
						}
		}


