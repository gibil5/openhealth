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


			

	# ----------------------------------------------------------- Orders ------------------------------------------------------


	#order_line  = fields.One2many(
	#		'sale.order.line',
	#		'order_id',
	#)
			




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
	
	
	
	# ------------------------------------------------------------------------------------------------------------------------
	#  Order  
	# -----------
	
	
	
	# Products 
	#products = fields.One2many(
	#		'product.template',
	#		string="Product",
	#		default=[],
	#		compute='_compute_products', 
	#		)

	
	#@api.multi
	#@api.depends('service_co2_ids')
	
	#def _compute_products(self):
	#	for record in self:
			
	#		record.products = [3480, 3527, 3510]
			#record.products = []
			#for service in record.service_co2_ids:
			#	record.products.append(service)







	
	
	#@api.depends('service_co2_ids')
	#def _compute_order_line(self):	
	#def _compute_order(self):	
	#	print
	#	print 'mark'
		#order_id = self.order
		
	#	for record in self:
	#		for s in record.service_co2_ids:
	#			print 
	#			print s
	#			print s.service
	#			print 
	#			prod_id = s.service.id

	#			record.order.order_line.create({
	#										'product_id': prod_id,
	#										'product_uom' : s.service.uom_id.id,
											
											#'order_id': order_id,
											#'name': '',
	#										}) 
			
	#	print
		


	# Service 
	service_ids = fields.One2many(
			'openhealth.service', 
			'consultation', 
			string="Servicios",
			
			#compute='_compute_service_ids', 
	)
	
	#@api.multi
	#@api.depends('service_co2_ids')
	
	#def _compute_service_ids(self):
	#	print 
	#	for record in self:
	#		for s in record.service_co2_ids:
	#			print s
	#			print s.name
	#			print s.service.name
	#			print s.service.id
	#			print 
				#record.service_ids.create({
				#							'name':s.name,
				#							'service_id':s.service.id,
				#})
	#			values = {
	#						'name':s.name,
	#			}
				#record.service_ids.write(0, 0, values)
	#			record.service_ids.write(values)
		

	#@api.onchange('service_co2_ids')
	#def _onchange_service_co2_ids(self):	
	#	print
	#	print 'mark'
	#	print 
		
		#return {
		#	'warning': {
		#		'title': "service_co_ids",
		#		'message': '',
		#}}
		
	#	for s in self.service_co2_ids:
	#		print s
	#		print s.name
	#		print s.service.name
	#		print s.service.id
	#		print
	#		values = {
	#					'name':s.name,
	#				}
				#record.service_ids.write(0, 0, values)
	
	
	# Order
	order = fields.One2many(
			'sale.order',			 
			'consultation', 
			string="Order",
			)


	order_2 = fields.One2many(
			'sale.order',			 
			'consultation', 
			string="Order 2",
			)

				
	order_line = field_One2many=fields.One2many('sale.order.line',
		'consultation',
		#string='Order',
		
		#compute='_compute_order_line', 
		)
	
	#@api.multi
	@api.depends('order')
	
	def _compute_order_line(self):
		print "Compute order line"
		
		consultation_id = self.id
		order_id = self.order_2
		
		
		
		for record in self:	
			#record.order_line.id = record.order.order_line.id
			
			for se in record.service_co2_ids:
				print se.name 

				ol = record.order_line.create({
											'product_id': se.service.id,
											'name': se.name_short,
											'product_uom': se.service.uom_id.id,
											'order_id': order_id,
											#'order_id': 33,
		#									'order_id': consultation_id,
											
										})

		print 
	
	
		
	# Create Order - Button 
	@api.multi
	def create_order_current(self):  

		# Order 
		#print 
		#print 'jx'
		order_id = self.order.id
		
		#if self.order.nr_lines != 0:
			#print 'Unlink'
		#	u = self.order.remove_order_lines()
			#print u
		
		
		if self.order.nr_lines == 0:
			#print 'Create'
			nr_lines = self.order.x_create_order_lines()
			#print nr_lines
			#print 
		
		
		
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
			
			#'res_id': 23,
			'res_id': order_id,
			
			
			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			
			
			'target': 'current',

			'context':   {

				'default_consultation': consultation_id,

				'default_partner_id': partner_id,
				'default_patient': patient_id,				

				#'default_products': products_id,


				#'default_prod_array': prod_array,

				#'default_order_line': order_line_id,
			}
		}
							
				