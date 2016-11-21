# -*- coding: utf-8 -*-
#
# 	Control 	
# 

from openerp import models, fields, api

#from datetime import datetime
import datetime


import jxvars




class Control(models.Model):
	_name = 'openhealth.control'
	_inherit = 'oeh.medical.evaluation'




	# Appointments 

	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'control', 

			string = "Citas", 
			)





	name = fields.Char(
			string = 'Control #',
			)


	observation = fields.Text(
			string="Observación",
			size=200,
			required=True,
			)


	evaluation_next_date = fields.Date(
			string = "Fecha próximo control", 	
			#compute='_compute_evaluation_next_date', 
			required=True, 
			#default = fields.Date.today, 
			)

	
	#@api.multi
	#@api.depends('evaluation_start_date')
	#def _compute_evaluation_next_date(self):
	#	date_format = "%d days, 0:00:00"
	#	delta = datetime.timedelta(weeks=1)
	#	to = datetime.datetime.today()
	#	next_week = delta + to
	#	for record in self:
	#		record.evaluation_next_date = next_week



	@api.onchange('evaluation_start_date')
	def _onchange_evaluation_start_date(self):

		date_format = "%Y-%m-%d"

		delta = datetime.timedelta(weeks=1)
		#to = datetime.datetime.today()
		sd = datetime.datetime.strptime(self.evaluation_start_date, date_format)
		next_week = delta + sd

		self.evaluation_next_date = next_week

		#print
		#print 'onchange'
		#print self.evaluation_start_date
		#print sd 
		#print next_week
		#print 





	# Relational 

	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
			)
			
			
	
			


