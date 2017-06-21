# -*- coding: utf-8 -*-
#
# 	*** Evaluation 
# 

# Created: 				19 Jun 2017
# Last updated: 	 	id. 



from openerp import models, fields, api
#from datetime import datetime

from . import eval_vars



#------------------------------------------------------------------------
class Image(models.Model):

	#_inherit = 'oeh.medical.evaluation'

	_name =	'openhealth.image'




	name = fields.Char(
			string = "Nombre", 	
			#required=True, 

			compute="_compute_name",
		)

	@api.multi
	
	def _compute_name(self):
		for record in self:

			record.name = 'name'

			#name = record.patient.name + '_' + record.date.split()[0]
			name = record.patient.name + '_' + record.date.split()[0] + '_' + record.description

			record.name = name




	image = fields.Binary(

			string="Visia", 

		)



	date = fields.Datetime(

			string = "Fecha y hora", 	
		
			default = fields.Date.today, 

			required=True, 
			)






	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
			
			required=True, 
			#required=False, 
		)


	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			#ondelete='cascade', 			

			required=True, 
		)




	control = fields.Many2one('openhealth.control',
			string="Control",		
			#ondelete='cascade', 
			required=True, 
	)


	evaluation_type = fields.Selection(
			selection = eval_vars.EVALUATION_TYPE, 
			string = 'Tipo',
			#default='', 
			
			required=True, 
			)




	IMAGE_DESCRIPTION = [
		
		('front', 'Frente'),

		('right', 'Derecha'),

		('left', 'Izquierda'),

	]


	description = fields.Selection(
			selection = IMAGE_DESCRIPTION, 
			string = 'Descripción',
			
			default='front', 
			
			required=True, 
			)





	@api.multi
	def open_line_current(self):  

		res_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Treatment Current', 
				'view_type': 'form',
				'view_mode': 'form',

				'res_model': self._name,
				#'res_model': 'openhealth.consultation',
				'res_id': res_id,


				'target': 'current',
				#'target': 'inline'.

				'flags': {
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': True, }
						},

				'context': {
						}
		}


