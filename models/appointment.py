# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
# Created: 				14 Nov 2016
# Last updated: 	 	Id. 

from openerp import models, fields, api
from datetime import datetime


class Appointment(models.Model):
	#_name = 'openhealth.appointment'

	_inherit = 'oeh.medical.appointment'



	name = fields.Char(
			#string="", 
			#default='',

			#compute='_compute_name', 
			required=True, 
			)





	vspace = fields.Char(
			' ', 
			readonly=True
			)




	# Duration


	_hash_duration = {
					'0.25' 	: 0.25, 
     				'0.5' 	: 0.5, 
     				'0.75' 	: 0.75, 
     				'1.0' 	: 1.0, 
				}




	_duration_list = [
        			('0.25', 	'15 min'),

        			('0.5', 	'30 min'),

        			('0.75', 	'45 min'),

        			('1.0', 	'60 min'),
        		]




	x_duration_min = fields.Selection(
			#'', 
			#readonly=True
			selection = _duration_list, 
		)

	@api.onchange('x_duration_min')

	def _onchange_x_duration_min(self):

		if self.x_duration_min != False:	
			self.duration = self._hash_duration[self.x_duration_min]




	duration = fields.Float(
	#duration = fields.Selection(
			#'', 
			#readonly=True
			#selection = _duration_list, 
		)










	


	# Type 
	_type_list = [
        			('consultation', 'Consulta'),

        			('procedure', 'Procedimiento'),

        			('session', 'Sesión'),

        			('control', 'Control'),

        		]

	x_type = fields.Selection(
				selection = _type_list, 
				
				string="Tipo",
				required=True, 
				)






	# ----------------------------------------------------------- Indexes ------------------------------------------------------

	treatment = fields.Many2one('openextension.treatment',
			string="Tratamiento",
			required=False, 
			ondelete='cascade', 
			)


	consultation = fields.Many2one('openhealth.consultation',
		string="Consulta",
		ondelete='cascade', 
	)


	procedure = fields.Many2one('openhealth.procedure',
		string="Procedimiento",
		ondelete='cascade', 
	)


	session = fields.Many2one('openhealth.session',
		string="Sesión",
		ondelete='cascade', 
	)

	control = fields.Many2one('openhealth.control',
		string="Control",
		ondelete='cascade', 
	)






	#@api.multi
	#@api.depends('start_date')

	#def _compute_name(self):
	#	print 'compute name'
	#	for record in self:
	#		idx = record.id
	#		if idx < 10:
	#			pre = 'AP000'
	#		elif idx < 100:
	#			pre = 'AP00'
	#		elif idx < 1000:
	#			pre = 'AP0'
	#		else:
	#			pre = 'AP'
	#		record.name =  pre + str(idx) 
	#	print self.name 
	#	print 




# ----------------------------------------------------------- Open ------------------------------------------------------

	@api.multi
	def open_popup(self):
	#def open_current(self):

		#the best thing you can calculate the default values 
		# however you like then pass them to the context

		print 
		print 'open popup'
		print 

		return {

        	'type': 'ir.actions.act_window',

        	'name': 'Import Module',

        	'view_type': 'form',

        	'view_mode': 'form',


			#'target': 'new',
			'target': 'current',


        	'res_model': 'oeh.medical.appointment',


        	'context': {

        			#'default_partner_id':value, 			
        			#'default_other_field':othervalues
        			
        			'default_patient':3025, 			
        			},

    		}








