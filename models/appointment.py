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
			required=True, 
			ondelete='cascade', 
			)


	consultation = fields.Many2one('openhealth.consultation',
		string="Consulta",
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



