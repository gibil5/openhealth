# -*- coding: utf-8 -*-
#
# 	*** Consultation 
# 

# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
#from datetime import datetime
from datetime import datetime,tzinfo,timedelta

import jxvars
import jrfuncs
import eval_vars
import time_funcs




class Consultation(models.Model):
	_name = 'openhealth.consultation'
	_inherit = 'oeh.medical.evaluation'



	# Name 
	name = fields.Char(
			string = 'Consulta #',
			)






	# Nr Services 
	nr_service = fields.Integer(
			default = 0, 
			compute="_compute_nr_service",
		)

	#@api.multi
	@api.depends('nr_service_co2', 'nr_service_excilite', 'nr_service_ipl', 'nr_service_ndyag')

	def _compute_nr_service(self):
		for record in self:

			record.nr_service = record.nr_service_co2 + record.nr_service_excilite + record.nr_service_ipl + record.nr_service_ndyag








	# Nr Services co2 
	nr_service_co2 = fields.Integer(
			default = 0, 
			compute="_compute_nr_service_co2",
		)

	#@api.multi
	@api.depends('service_co2_ids')

	def _compute_nr_service_co2(self):
		for record in self:
			record.nr_service_co2 = self.env['openhealth.service.co2'].search_count([('consultation','=', self.id)]) 





	# Nr Services Excilite 
	nr_service_excilite = fields.Integer(
			default = 0, 
			compute="_compute_nr_service_excilite",
		)

	#@api.multi
	@api.depends('service_excilite_ids')

	def _compute_nr_service_excilite(self):
		for record in self:
			record.nr_service_excilite = self.env['openhealth.service.excilite'].search_count([('consultation','=', self.id)]) 






	# Nr Services ipl 
	nr_service_ipl = fields.Integer(
			default = 0, 
			compute="_compute_nr_service_ipl",
		)

	#@api.multi
	@api.depends('service_ipl_ids')

	def _compute_nr_service_ipl(self):
		for record in self:
			record.nr_service_ipl = self.env['openhealth.service.ipl'].search_count([('consultation','=', self.id)]) 







	# Nr Services ndyag 
	nr_service_ndyag = fields.Integer(
			default = 0, 
			compute="_compute_nr_service_ndyag",
		)

	#@api.multi
	@api.depends('service_ndyag_ids')

	def _compute_nr_service_ndyag(self):
		for record in self:
			record.nr_service_ndyag = self.env['openhealth.service.ndyag'].search_count([('consultation','=', self.id)]) 

















	# Autofill

	x_autofill = fields.Boolean(
		string="Autofill",
		default=False, 
	)

	@api.onchange('x_autofill')
	
	def _onchange_x_autofill(self):

		if self.x_autofill == True:

			self.x_fitzpatrick = 'one'			
			self.x_photo_aging = 'one'

			self.x_diagnosis = 'a'

			self.x_antecedents = 'b'

			self.x_allergies_medication = 'c'

			self.x_observations = 'd'

			self.x_indications = 'e'



	# Owner 
	owner_type = fields.Char(
			default = 'consultation',
		)







	# Appointments 

	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'consultation', 
			string = "Citas", 
			)








	# Order line 

	pre_order = fields.One2many(		
			'sale.order',		
			'consultation', 
			string="Pre Order",
			
			domain = [
						('state', '=', 'draft'),

						('x_family', '=', 'private'),
					],
			)



	order_line = field_One2many=fields.One2many(
			'sale.order.line',
	
			'consultation',
	
			domain = [
						#('order_id', '=', pre_order),
						('state', '=', 'draft'),
					],

		#compute='_compute_order_line', 
	)



	#@api.multi
	#@api.depends('order')
	@api.depends('service_co2_ids')
	
	def _compute_order_line(self):

		print 
		print "Compute order line"
		
		consultation_id = self.id

		print self.pre_order
		print self.pre_order.id 

		order_id = self.pre_order.id
		#order_id = self.order.id
		
		
		for record in self:	
			#record.order_line.id = record.order.order_line.id
			
			for se in record.service_co2_ids:
				print se.name 

				ol = record.order_line.create({
											'product_id': se.service.id,
											'name': se.name_short,
											'product_uom': se.service.uom_id.id,


											'consultation': consultation_id,											
											'order_id': order_id,

											#'order_id': consultation_id,											
										})

		print 







	# Number of appointments
	
	nr_apps = fields.Integer(
				string="Citas",
				compute="_compute_nr_apps",
	)

	@api.multi
	
	def _compute_nr_apps(self):
		for record in self:

			ctr = 0 
			
			#for a in record.appointment:
			for a in record.appointment_ids:
				ctr = ctr + 1		

			record.nr_apps = ctr









	# Redefinition 


	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 

			#selection = jxvars._pathology_list, 
			selection = jxvars._chief_complaint_list, 

			#required=True, 
			)



	evaluation_type = fields.Selection(
			default = 'Pre-arraganged Appointment', 
			)





	# ----------------------------------------------------------- Treatment ------------------------------------------------------

	treatment = fields.Many2one('openextension.treatment',

			ondelete='cascade', 

			string="Tratamiento",
			required=True, 
			)







	# ----------------------------------------------------------- Orders ------------------------------------------------------

	order = fields.One2many(		
			'sale.order',		
			'consultation', 
			string="Order",
			domain = [

						('state', '=', 'draft'),
			
						('x_family', '=', 'private'),
					],
			)

		
	# Number 
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





	# ----------------------------------------------------------- Services --------------------------------------------------------


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
			string="Tratamiento Médico",
	)





	# Service 
	service_ids = fields.One2many(
			'openhealth.service', 
			'consultation', 
			string="Servicios",
			
			#compute='_compute_service_ids', 
	)




	# --------------------------------------------------------- Consultation ------------------------------------------------------
	
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
			)

	x_fitzpatrick = fields.Selection(
			selection = eval_vars.FITZ_TYPE, 
			string = 'Fitzpatrick',
			default = '', 
			)

	x_photo_aging = fields.Selection(
			selection = eval_vars.PHOTO_TYPE, 
			string = 'Foto-envejecimiento',
			default = '', 
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

	x_analysis_lab = fields.Boolean(
			string = 'Análisis de laboratorio', 
			)

	x_observations = fields.Text(
			string = 'Observaciones',
			)

	x_indications = fields.Text(
			string = 'Indicaciones',
			)








	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

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







	# ---------------------------------------------- Create Order --------------------------------------------------------

	
	@api.multi
	
	def create_order_current(self):  

		print 
		print 'jx'
		print 'create_order_current'



		# Treatment
		treatment_id = self.treatment.id 

		# Consultation
		consultation_id = self.id 


		# Patient
		patient_id = self.patient.id
		print 'patient_id: ', patient_id
		


		# Doctor
		doctor_id = self.doctor.id
		print 'doctor_id: ', doctor_id



		# Appointment Proc
		#appointment_proc = self.



		# Partner
		#partner_id = self.env['res.partner'].search([('name','=',self.patient.name)]).id
		#partner_id = self.env['res.partner'].search([('name','=',self.patient.name)],limit=1).id		
		#partner_id = self.env['oeh.medical.patient'].search([('name','like',self.patient.name)],limit=1).id
		
		partner_id = self.env['res.partner'].search([('name','like',self.patient.name)],limit=1).id



		print 'patient name: ', self.patient.name 

		print 'partner_id: ', partner_id




		# Chief complaint 
		chief_complaint = self.chief_complaint





		# Order 
		#order_id = self.order.id		
		consultation_id = self.id

		order_id = self.env['sale.order'].search([
													#('consultation','=',self.id),
													('consultation','=',consultation_id),
													
													('state','=','draft'),

													('x_family','=', 'private'),
												
												]).id

		print 'consultation_id: ', consultation_id
		print 'order_id: ', order_id



		# Create 
		if order_id == False:

			print 'create order'
			print 
			order = self.env['sale.order'].create(
													{
														'treatment': treatment_id,

														'partner_id': partner_id,
														'patient': patient_id,	
														'x_doctor': doctor_id,	

														'consultation':self.id,
														'state':'draft',
														'x_chief_complaint':chief_complaint,

														#'x_appointment': appointment_proc, 
													}
												)

			# Create order lines 
			ret = order.x_create_order_lines()
			print ret 



			# Copy 
			pre_order = order.copy({
								#'state':'sale',
								#'state':'sent',
								#'state':'pre-draft',

								'x_family':'private',
							})	


			order_id = order.id 
			print order
		

		print order_id
		print 

		


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': ' Create Quotation Current', 
			'view_type': 'form',
			'view_mode': 'form',
						

			'res_model': 'sale.order',
			
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


				'default_x_doctor': doctor_id,	


				'default_x_chief_complaint': chief_complaint,	
			}
		}


	# create_order_current












# ---------------------------------------------- Open Appointment --------------------------------------------------------


	@api.multi
	def open_appointment(self):  

		print 
		print 'open appointment'

		owner_id = self.id 
		owner_type = self.owner_type

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		treatment_id = self.treatment.id 



		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#appointment_date = '2016-12-23'


		return {
				'type': 'ir.actions.act_window',

				'name': ' New Appointment', 
				
				'view_type': 'form',
				
				#'view_mode': 'form',			
				'view_mode': 'calendar',			
				
				'target': 'current',
				

				'res_model': 'oeh.medical.appointment',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_consultation': owner_id,					
							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,

							'default_x_type': owner_type,


							'default_appointment_date': appointment_date,
							}
				}

	# open_appointment




# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):

		print 
		print 'jx'
		print 'Create Consultation - Override - CRUD'
		print 
		print vals
		print 
	
		
		consultation_id = self.id
		print 'consultation_id: ', consultation_id


		appointment_id = vals['appointment']
		print 'appointment_id: ', appointment_id
		print 



		# Return 
		res = super(Consultation, self).create(vals)

		return res


	# create - CRUD 




# ---------------------------------------------- Create Service --------------------------------------------------------

	# Create Service
	 
	@api.multi
	def create_service(self):  
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

	# create_service





# ---------------------------------------------- Create Service - Co2 --------------------------------------------------------

	@api.multi
	def create_service_co2(self):  

		consultation_id = self.id 
		treatment_id = self.treatment.id 

		laser = 'laser_co2'
		zone = ''	
		pathology = ''
		
		
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Co2', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.service.co2',				
				#'res_id': consultation_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {

							'default_consultation': consultation_id,
							'default_treatment': treatment_id,


							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,

							}
				}

	# create_service_co2





# ---------------------------------------------- Create Service - Excilite --------------------------------------------------------
	 
	@api.multi
	def create_service_excilite(self):  

		print 
		print 'jx'
		print 'Create Service Excilite'
		print 

		consultation_id = self.id 
		treatment_id = self.treatment.id 
		
		print consultation_id
		print treatment_id
		print 


		laser = 'laser_excilite'
		zone = ''	
		pathology = ''
				

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Excilite', 

				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',				
								

				'res_model': 'openhealth.service.excilite',				
				#'res_id': 23,
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {

							'default_consultation': consultation_id,	
							'default_treatment': treatment_id,

							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,
							}
				}
				
	# create_service_excilite
		
				


				
# ---------------------------------------------- Create Service - IPL --------------------------------------------------------
		
	@api.multi
	def create_service_ipl(self):  

		consultation_id = self.id 
		treatment_id = self.treatment.id 

		
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

							'default_treatment': treatment_id,


							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,
							}
				}

	# create_service_ipl




# ---------------------------------------------- Create Service - NDYAG --------------------------------------------------------
	
	@api.multi
	def create_service_ndyag(self):  

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
	
	# create_service_ndyag



	
# ---------------------------------------------- Create Service - MEDICAL --------------------------------------------------------

	@api.multi
	def create_service_medical(self):  

		consultation_id = self.id 
		
		family = 'medical'

		laser = 'medical'
		zone = ''	
		pathology = ''

		

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Medical', 
				'view_type': 'form',
				'view_mode': 'form',			
				'target': 'current',
				
				'res_model': 'openhealth.service.medical',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_consultation': consultation_id,					

							'default_family': family,

							'default_laser': laser,

							#'default_zone': zone,
							#'default_pathology': pathology,

							}
				}
					
	# create_service_medical


