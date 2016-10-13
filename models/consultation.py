# -*- coding: utf-8 -*-
#
# 	Consultation 
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars




class Consultation(models.Model):
	_name = 'openhealth.consultation'
	_inherit = 'oeh.medical.evaluation'


	name = fields.Char(
			string = 'Consulta #',
			)


	x_vspace = fields.Char(
			' ', 
			readonly=True
			)
			
			
	# Quotations
	# -----------------------------------------------------------------------------------------------------------------

	order = fields.One2many(
			#'openhealth.quotation', 
			#'openhealth.order',
			'sale.order',
			 
			#'treatment_id', 
			'consultation', 
			string="Presupuestos"
			)

	order_line  = fields.One2many(
			'sale.order.line',
			'order_id',
	)
			

	# ----------------------------- Services -----------------------------------

	# Service id 
	#service_ids = fields.One2many(
	#		'openhealth.service', 
			#'treatment_id', 
	#		'consultation', 
			#string="Services"
	#		string="Servicios"
	#)


	# Service 
	service = fields.Many2one(
	#service = fields.One2many(	
			'product.template',

			#'consultation',
			
			string="Servicio", 
	)



	# Laser 
	_laser_type_list = [
			('laser_co2','Laser Co2'), 
			('laser_excilite','Laser Excilite'), 
			('laser_ipl','Laser Ipl'), 
			('laser_ndyag','Laser Ndyag'), 
			]

	laser = fields.Selection(
			selection = _laser_type_list, 
			string="Laser",  
			default='laser_co2',
			required=True, 
			index=True
			)



	# Name short 
	code = fields.Char(
			compute='_compute_code', 
			#string='Short name'
			string='Código'
			)

	@api.depends('service')

	def _compute_code(self):
		for record in self:
			record.code = record.service.x_name_short 









	#Price 
	price = fields.Float(
			compute='_compute_price', 
			#string='Price'
			string='Precio'
			) 

	#@api.multi
	@api.depends('service')

	def _compute_price(self):
		for record in self:
			record.price= (record.service.list_price)



	def get_domain_service(self,cr,uid,ids,context=None):

		#print context

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[('x_treatment', '=', context)])
		return {'domain':{'service':[('id','in',lids)]}}













	# ----------------------------- Consultation -----------------------------------
	# Go 

	#treatment_id = fields.Many2one('openextension.treatment',
	treatment = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			)



	EVALUATION_TYPE = [
			#('Pre-arraganged Appointment', 'Primera consulta'),
			('Pre-arraganged Appointment', 'Consulta'),
			('Ambulatory', 'Procedimiento'),
			('Periodic Control', 'Control'),
			]

	evaluation_type = fields.Selection(
			selection = EVALUATION_TYPE, 
			string = 'Tipo',

			default = 'Pre-arraganged Appointment', 
			#default = 'Ambulatory', 
			#default = 'Periodic Control', 

			required=True, 
			)



	evaluation_start_date = fields.Date(
			string = "Fecha", 	
			default = fields.Date.today, 
			required=True, 
			)



	_chief_complaint_list = [
			#('Pre-arraganged Appointment', 'Primera consulta'),
			('one', '1'),
			('two', '2'),
			('three', '3'),
			
			
			]
			
	#chief_complaint = fields.Char(
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 
			#default = '', 
			
			#selection = _chief_complaint_list, 
			selection = jxvars._pathology_list, 

			required=True, 
			)






	#-----------------------------------------------------------------------------
	# Aggregated 


	
	x_reason_consultation = fields.Text(
			string = 'Motivo de consulta (detalle)', 
			)
	
	x_observation = fields.Text(
			string="Observación",
			size=200,
			)


	x_next_evaluation_date = fields.Date(
			string = "Próxima cita", 	
			#default = fields.Date.today, 
			#required=True, 
			)

	
	

	# First consultation

	x_diagnosis = fields.Text(
			string = 'Diagnóstico', 
			)

	x_antecedents = fields.Text(
			string = 'Antecedentes médicos', 
			)

	x_allergies_medication = fields.Text(
			string = 'Alergias a medicamentos', 
			)

	FITZ_TYPE = [
			('one','I'),
			('two','II'),
			('three','III'),
			('four','IV'),
			('five','V'),
			('six','VI')
			]

	x_fitzpatrick = fields.Selection(
			selection = FITZ_TYPE, 
			string = 'Fitzpatrick',
			default = '', 
			)

	PHOTO_TYPE = [
			('one','I (1,2,3)'),
			('two','II (4,5,6)'),
			('three','III (7,8,9)')
			]

	x_photo_aging = fields.Selection(
			selection = PHOTO_TYPE, 
			string = 'Foto-envejecimiento',
			default = '', 
			)


	x_analysis_lab = fields.Boolean(
			string = 'Análisis de laboratorio', 
			)

	x_observations = fields.Text(
			string = 'Observaciones',
			)

	x_indications = fields.Text(
			string = 'Indicaciones',
			)







	








	#----------------------------------------------------------- Buttons ------------------------------------------------------------


	#  Quotation  
	# -----------
	@api.multi
	def create_quotation_current(self):  

		patient_id = self.patient.id

		#partner_id = self.env['res.partner'].search([('name','=','Javier Revilla')]).id
		#partner_id = self.env['res.partner'].search([('name','=',self.patient.name)]).id
		partner_id = self.env['res.partner'].search([('name','=',self.patient.name)],limit=1).id
				
		consultation_id = self.id 
		
		#order_line_id = self.env['sale.order.line'].new().id
		
		
		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': ' Create Quotation Current', 
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'sale.order',
			
			'flags': {
					'form': {'action_buttons': True, }
					},			
			
			'target': 'current',

			'context':   {

				'default_partner_id': partner_id,
				#'default_patient': patient_id,				
				'default_consultation': consultation_id,
				#'default_order_line': order_line_id,
			}
		}





	# Quick Self Button  
	# ------------------
	@api.multi
	def open_line_current(self):  

		consultation_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Consultation Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': consultation_id,
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}





	# Service
	# --------
	 
	@api.multi
	def open_service(self):  
		consultation_id = self.id 				
		laser = ''
		zone = ''	
		pathology = ''

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current', 
				'view_type': 'form',
				'view_mode': 'form',				
				'res_model': 'openhealth.service',				
				#'res_id': consultation_id,
				'target': 'current',
				'flags': 	{
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': True, }
							},
				'context': {
							'default_consultation': consultation_id,					
							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,
							}
				}
	
	
	
	

	# Service - Laser Co2 
	# ---------------------
	
	@api.multi
	def open_service_co2(self):  

		consultation_id = self.id 
		
		laser = 'laser_co2'
		zone = ''	
		pathology = ''
				
		
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Co2', 
				'view_type': 'form',
				'view_mode': 'form',			
					
				#'res_id': 23,
				
				'target': 'current',
								
				'res_model': 'openhealth.service.co2',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_consultation': consultation_id,					

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							}
				}
				



	# Service - Laser Excilite
	# -------------------------
	 
	@api.multi
	def open_service_excilite(self):  

		consultation_id = self.id 
		
		laser = 'laser_excilite'
		zone = ''	
		pathology = ''
				
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Excilite', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',				
				
				#'res_id': 23,
				
				'res_model': 'openhealth.service.excilite',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_consultation': consultation_id,					

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							}
				}
				
				
				
				
	# Service - Laser Ipl 
	# ----------------------
		
	@api.multi
	def open_service_ipl(self):  

		consultation_id = self.id 
		
		laser = 'laser_ipl'
		zone = ''	
		pathology = ''
				
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Excilite', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',				
				
				#'res_id': 23,
				
				'res_model': 'openhealth.service.ipl',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_consultation': consultation_id,					

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							}
				}




	# Service - Laser Ndyag 
	# ----------------------
	
	@api.multi
	def open_service_ndyag(self):  

		consultation_id = self.id 
		
		laser = 'laser_ndyag'
		zone = ''	
		pathology = ''
				
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Ndyag', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',				
				
				#'res_id': 23,
				
				'res_model': 'openhealth.service.ndyag',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_consultation': consultation_id,					

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							}
				}
							
				