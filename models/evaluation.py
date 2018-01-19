# -*- coding: utf-8 -*-
#
# 	*** Evaluation 
# 

# Created: 				26 Aug 2016
# Last updated: 	 	28 Oct 2016



from openerp import models, fields, api

from datetime import datetime
from . import eval_vars
from . import prodvars



#------------------------------------------------------------------------
class Evaluation(models.Model):

	_inherit = 'oeh.medical.evaluation'

	#_name =	'openhealth.evaluation5'




	# Zone 
	zone = fields.Selection(
			selection = prodvars._zone_list, 
			string="Zona",

			compute='_compute_zone', 			
			)
	
	#@api.multi
	@api.depends('product')
	def _compute_zone(self):
		for record in self:
			record.zone = record.product.x_zone




	# Pathology 
	pathology = fields.Selection(
			selection = prodvars._pathology_list, 
			string="Patología", 			

			compute='_compute_pathology', 			
			)
	
	#@api.multi
	@api.depends('product')
	def _compute_pathology(self):
		for record in self:
			record.pathology = record.product.x_pathology







	# level 
	level = fields.Selection(

			selection = prodvars._level_list, 
		
			string="Nivel",

			compute='_compute_level', 			
			)
	
	#@api.multi
	@api.depends('product')
	def _compute_level(self):
		for record in self:
			record.level = record.product.x_level















	# Vertical space 
	vspace = fields.Char(
			' ', 
			readonly=True
			)




	# Autofill
	x_autofill = fields.Boolean(
		string="Autofill",
		default=False, 
	)
	



	# Nr images 
	nr_images = fields.Integer(
			string = "Nr Visia", 	
			#required=True, 

			compute="_compute_nr_images",
		)

	@api.multi
	def _compute_nr_images(self):
		for record in self:
			ctr = 0
			for image in record.image_ids:
				ctr = ctr + 1
			record.nr_images = ctr





	# Evaluation Nr
	evaluation_nr = fields.Integer(
			string="Evaluation #", 
			default=1, 

			required=True, 
			#compute='_compute_evaluation_nr', 
			)
	#@api.multi
	#@api.depends('state')
	#def _compute_evaluation_nr(self):
	#	for record in self:
	#		nr = 1
	#		record.evaluation_nr = nr  





	# Done
	x_done = fields.Boolean(
			default=False,
			string="Realizado", 			
		)




	# State 
	state = fields.Selection(
			selection = eval_vars._state_list, 
			string='Estado',	
			default='draft',

			#compute='_compute_state', 
			)






	# Open Treatment
	@api.multi 
	def open_treatment(self):

		#print 
		#print 'Open Treatment'

		treatment = self.env['openhealth.treatment'].search([('id','=', self.treatment.id)]) 
		treatment_id = treatment.id  


		ret = treatment.open_myself()

		return ret 
	# open_treatment








	appointment = fields.Many2one(

			'oeh.medical.appointment',			

			string='Cita #', 

			required=False, 

			#ondelete='cascade', 
		)









# ----------------------------------------------------------- Relationals ------------------------------------------------------

	treatment = fields.Many2one(
			'openhealth.treatment',			
			ondelete='cascade', 

			required=True, 

			readonly=True, 
			)


	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
			)

















	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			ondelete='cascade', 			

			required=True, 

			readonly=True, 
	)



	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
			
			required=True, 
			#required=False, 

			readonly=True, 
		)






	#evaluation_start_date = fields.Date(
	evaluation_start_date = fields.Datetime(

			string = "Fecha y hora", 	
		
			#default = fields.Date.today, 
			required=True, 

			readonly=True, 
		)




	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 

			#selection = jxvars._pathology_list, 
			#selection = jxvars._chief_complaint_list, 
			selection = eval_vars._chief_complaint_list, 

			required=True, 
			)




	evaluation_type = fields.Selection(
			selection = eval_vars.EVALUATION_TYPE, 
			string = 'Tipo',
			#default='', 
			
			required=True, 
			)



	


	# Product
	product = fields.Many2one(
		
			'product.template',
		
			string="Producto",
		
			#required=True, 

			domain = [
						('x_origin', '=', False),
					],
		)
	





	laser = fields.Selection(

			#selection = jxvars._laser_type_list, 	
			#selection = service_vars._laser_type_list, 
			selection = prodvars._laser_type_list, 
			
			string="Láser", 			
			compute='_compute_laser', 			
			)
	

	
	#@api.multi
	@api.depends('product')
	def _compute_laser(self):
		for record in self:
			record.laser = record.product.x_treatment 














