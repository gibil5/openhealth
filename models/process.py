# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Process
# 
# Created: 				18 Feb 2017
# Last updated: 	 	Id.



from openerp import models, fields, api

import jxvars



class Process(models.Model):
	
	_name = 'openhealth.process'
	






	# ----------------------------------------------------------- Variables ------------------------------------------------------
	
	name = fields.Char(
			string="Proceso #", 
			#required=True, 
		)



	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Patient",
			index=True, 

			ondelete='cascade', 
			)

	physician = fields.Many2one(
			'oeh.medical.physician',
			string="Physician",
			index=True
			)
	
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 			
			#selection = tre_vars._chief_complaint_list, 
			selection = jxvars._chief_complaint_list, 
			)





	duration = fields.Integer(
			string="Días", 
			#compute='_compute_duration', 
			default = 0,
			)

	start_date = fields.Date(
			string="Fecha inicio", 
			#default = fields.Date.today
			)

	price_total = fields.Float(
			string='Total', 
			default = 0, 
			) 



# Process
