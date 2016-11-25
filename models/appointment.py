# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
# Created: 				14 Nov 2016
# Last updated: 	 	Id. 

from openerp import models, fields, api

#from datetime import datetime
import datetime
import time_funcs


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





	# Date end 
	appointment_end = fields.Datetime(

			#compute="_compute_appointment_end",
			)








	# Colors 
	color_patient_id = fields.Integer(
			default=2,
		)

	_hash_colors_doctor = {

			'Dr. Acosta': 1,

			'Dr. Canales': 2,

			'Dr. Chavarri': 3,

			'Dr. Vasquez': 6,

			#'Dr. Acosta': 1,

		}


	color_doctor_id = fields.Integer(
			default=1,

			compute='_compute_color_doctor_id', 
		)


	#@api.multi
	@api.depends('doctor')
	def _compute_color_doctor_id(self):

		for record in self:	

			record.color_doctor_id = self._hash_colors_doctor[record.doctor.name]




	# Duration


	_hash_duration = {
					'0.25' 	: 0.25, 
     				'0.5' 	: 0.5, 
     				'0.75' 	: 0.75, 
     				'1.0' 	: 1.0, 
     				'2.0' 	: 2.0, 
				}




	_duration_list = [
        			('0.25', 	'15 min'),

        			('0.5', 	'30 min'),

        			('0.75', 	'45 min'),

        			('1.0', 	'60 min'),

        			('2.0', 	'120 min'),
        		]




	x_duration_min = fields.Selection(
			#'', 
			#readonly=True
			selection = _duration_list, 
		
			#default = '1.0',
			default = '0.5',
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
			default = 1.0,
		)










	


	# Type 
	_type_list = [
        			('consultation', 'Consulta'),
        			('procedure', 'Procedimiento'),
        			('session', 'Sesión'),
        			('control', 'Control'),

        			#('Consulta', 'Consulta'),
        			#('Procedimiento', 'Procedimiento'),
        			#('Sesion', 'Sesión'),
        			#('Control', 'Control'),
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



	# CRUD

	#@api.multi
	#def create(self):

	#@api.model
	#def create(self,vals):

	#	print 
	#	print 'jx Create - Override'
		
	#	print vals
	#	print vals['appointment_date']
	#	print vals['duration']
	#	print vals['appointment_end']
	#	print

	#	res = super(Appointment, self).create(vals)

	#	return res


	
	#@api.multi
	#@api.model
	#def write(self,vals):

		#print 
		#print 'jx Write - Override'
		#print
		
		#res = super(Appointment, self).write(vals)

		#return res




