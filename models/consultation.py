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



	treatment = fields.Many2one('openextension.treatment',
			string="Tratamiento",
			ondelete='cascade', 
			)
			
			

	name = fields.Char(
			string = 'Consulta #',
			)


	x_vspace = fields.Char(
			' ', 
			readonly=True
			)




	# Number of Orders 
	nr_orders = fields.Integer(
			string="Presupuestos",
			compute="_compute_nr_orders",
	)
	
	#@api.multi
	@api.depends('order')
	
	def _compute_nr_orders(self):
		for record in self:
			ctr = 0 
			for c in record.order:
				ctr = ctr + 1
			record.nr_orders = ctr




	# ----------------------------------------------------------- Orders ------------------------------------------------------



			




	# ----------------------------------------------------------- Services --------------------------------------------------------

	# Services
	











	# --------------------------------------------------------- Consultation ------------------------------------------------------





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
			required=True, 
			)

	x_antecedents = fields.Text(
			string = 'Antecedentes médicos', 
			required=True, 
			)

	x_allergies_medication = fields.Text(
			string = 'Alergias a medicamentos', 
			required=True, 
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
			required=True, 
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
			required=True, 
			)




	x_analysis_lab = fields.Boolean(
			string = 'Análisis de laboratorio', 
			required=False, 
			)

	x_observations = fields.Text(
			string = 'Observaciones',
			required=True, 
			)

	x_indications = fields.Text(
			string = 'Indicaciones',
			required=True, 
			)







	








	#----------------------------------------------------------- Buttons ------------------------------------------------------------







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
	
	
	
	



	
	service_co2_ids = fields.One2many(
			'openhealth.service.co2', 
			'consultation', 
			string="Servicios Co2",
	)
	
	service_excilite_ids = fields.One2many(
			'openhealth.service.excilite', 
			'consultation', 
			string="Servicios Excilite",
	)

	service_ipl_ids = fields.One2many(
			'openhealth.service.ipl', 
			'consultation', 
			string="Servicios Ipl",
	)

	service_ndyag_ids = fields.One2many(
			'openhealth.service.ndyag', 
			'consultation', 
			string="Servicios Ndyag",
	)




	service_medical_ids = fields.One2many(

			'openhealth.service.medical', 
		
			'consultation', 
			string="Tratamiento médico",
	)





	# Service - Laser Co2 
	# ---------------------
	@api.multi
	def open_service_co2(self):  

		consultation_id = self.id 
		
		laser = 'laser_co2'
		zone = ''	
		pathology = ''
				
		#self.service_ids = [39]
		
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Co2', 
				'view_type': 'form',
				'view_mode': 'form',			
					
				#'res_id': 23,
				#'res_id': 39,
				
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
	
	


	# Service 
	service_ids = fields.One2many(
			'openhealth.service', 
			'consultation', 
			string="Servicios",
			
			#compute='_compute_service_ids', 
	)





	# ------------------------------------------------------ Order ------------------------------------------------------------------
	#	
	#

	
	# Order
	order = fields.One2many(		
			'sale.order',		

			'consultation', 
			string="Order",

			domain = [
						('state', '=', 'draft'),
					],
			)




	order_2 = fields.One2many(
		
			'sale.order',		
			#'openhealth.order',	

			'consultation', 
			string="Order 2",
			)
		


		
	# Create Order - Button 
	
	@api.multi
	
	def create_order_current(self):  

		print 
		print 'jx'
		print 'create_order_current'




		# Order 2
		#self.order_2 = self.order.copy()




		# Order 
		#order_id = self.order.id		
		order_id = self.env['sale.order'].search([
													('consultation','=',self.id),
													('state','=','draft'),
												]).id

		# Treatment
		treatment_id = self.treatment.id 


		# Consultation
		consultation_id = self.id 

		# Patient
		patient_id = self.patient.id
		
		# Partner
		#partner_id = self.env['res.partner'].search([('name','=',self.patient.name)]).id
		partner_id = self.env['res.partner'].search([('name','=',self.patient.name)],limit=1).id
		

		

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': ' Create Quotation Current', 
			'view_type': 'form',
			'view_mode': 'form',
			

			
			'res_model': 'sale.order',
			#'res_model': 'openhealth.order',


			
			#'res_id': 23,
			'res_id': order_id,
			
			
			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			
			
			'target': 'current',

			'context':   {

				'default_consultation': consultation_id,

				'default_treatment': treatment_id,


				'default_partner_id': partner_id,
				'default_patient': patient_id,				

			}
		}
							
				