# -*- coding: utf-8 -*-
#
# 	*** Consultation Cos
# 

# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
from datetime import datetime,tzinfo,timedelta


from . import jxvars
from . import cosvars
from . import jrfuncs
from . import eval_vars
from . import time_funcs
from . import app_vars



class ConsultationCos(models.Model):

	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.consultation'

	_name = 'openhealth.consultation.cos'
	




	x_target = fields.Selection(
			string="Target", 
			selection = app_vars._target_list, 
			default="therapist", 

			#required=True, 
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



	x_antecedents_chirurgical = fields.Text(
			string = '', 
			)


	x_treatments_former = fields.Text(
			string = '', 
			)



	# Number of sessions 
	nr_sessions = fields.Integer(
			string="Número de Sesiones",
			#compute="_compute_nr_sessions",
	)
	#@api.multi
	#def _compute_nr_sessions(self):
	#	for record in self:
	#		record.nr_sessions=self.env['openhealth.session'].search_count([
	#																('treatment','=', record.id),
	#																]) 
	#		record.nr_sessions=0




