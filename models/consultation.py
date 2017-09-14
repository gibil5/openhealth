# -*- coding: utf-8 -*-
#
# 	*** Consultation 
# 

# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
#from datetime import datetime
from datetime import datetime,tzinfo,timedelta


#from . import jxvars
from . import cosvars
from . import jrfuncs
from . import eval_vars
from . import time_funcs
from . import app_vars



class Consultation(models.Model):

	_name = 'openhealth.consultation'

	#_inherit = 'oeh.medical.evaluation'
	_inherit = ['openhealth.base', 'oeh.medical.evaluation']
	


	# Name 
	name = fields.Char(
			string = 'Consulta #',
			)













	# state 
	state = fields.Selection(

			selection = eval_vars._state_list, 
		
			#string='Estado',	
			#default='draft',

			compute='_compute_state', 
			)

	@api.multi
	#@api.depends('state')

	def _compute_state(self):
		for record in self:


			pro = 0

			if record.x_fitzpatrick != False:
				pro = pro + 1

			if record.x_photo_aging != False:
				pro = pro + 1
			
			if record.x_diagnosis != False:
				pro = pro + 1
			
			if record.x_antecedents != False:
				pro = pro + 1


			if record.x_allergies_medication != False:
				pro = pro + 1

			if record.x_observations != False:
				pro = pro + 1

			if record.x_indications != False:
				pro = pro + 1


			if pro == 0:
				record.state = 'draft'
			elif pro == 7:
				record.state = 'done'
			elif 0 < pro < 7: 
				record.state = 'inprogress'





	progress = fields.Float(
			string='Progreso', 			
			default = 0., 

			compute='_compute_progress', 
		)


	@api.multi
	#@api.depends('state')

	def _compute_progress(self):
		for record in self:
			#print 
			#print 'jx'
			#print 'Compute progress'
			record.progress = eval_vars._hash_progress[record.state]
			#print 









	x_profile = fields.Selection(
			string="Perfil psicológico", 
			selection=app_vars._profile_list, 
		)





	x_target = fields.Selection(
			string="Target", 
			selection = app_vars._target_list, 
			default="doctor", 

			#required=True, 
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





	# Nr Services medical 
	nr_service_medical = fields.Integer(
			default = 0, 
			compute="_compute_nr_service_medical",
		)

	#@api.multi
	@api.depends('service_medical_ids')

	def _compute_nr_service_medical(self):
		for record in self:
			record.nr_service_medical = self.env['openhealth.service.medical'].search_count([('consultation','=', self.id)]) 


















	@api.onchange('x_autofill')
	
	def _onchange_x_autofill(self):

		if self.x_autofill == True:

			self.x_fitzpatrick = 'two'	

			self.x_photo_aging = 'three'

			self.x_diagnosis = '1. Acné activo. 2. Secuelas de acné.'

			self.x_antecedents = 'Demostración con Punta de Diamante. Niega enfermedades y cirugías.'

			self.x_allergies_medication = 'Niega AMs.'

			self.x_observations = 'Cicatriz plana hiperpigmentada en pómulo derecho. Pápulas en pómulos.'

			self.x_indications = 'Láser Co2 Fraccional.'




	# Owner 
	owner_type = fields.Char(
			default = 'consultation',
		)







	# Appointments 
	appointment_ids = fields.One2many(


			'oeh.medical.appointment', 
			#'openhealth.appointment', 


			'consultation', 
			string = "Citas", 
			required=True, 
		)








	# Order line 

	pre_order = fields.One2many(		
			'sale.order',		
			'consultation', 
			string="Pre Order",
			
			domain = [
						('state', '=', 'draft'),

						#('x_family', '=', 'private'),
					],
			)












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

			#selection = jxvars._chief_complaint_list, 
			selection = eval_vars._chief_complaint_list, 

			#required=True, 
			required=False, 
			)










	evaluation_type = fields.Selection(
			default = 'Pre-arraganged Appointment', 
			)






	# ----------------------------------------------------------- Treatment ------------------------------------------------------

	treatment = fields.Many2one('openhealth.treatment',

			ondelete='cascade', 

			string="Tratamiento",
			#required=True, 
			)











	# ----------------------------------------------------------- Orders ------------------------------------------------------

	#order = fields.One2many(		
	#		'sale.order',		
	#		'consultation', 
	#		string="Order",
	#		domain = [
	#					('state', '=', 'draft'),
	#				],
	#		)

	# Number 
	#nr_orders = fields.Integer(
	#		string="Presupuestos",
	#		compute="_compute_nr_orders",
	#)
	
	#@api.multi
	#@api.depends('order')
	
	#def _compute_nr_orders(self):
	#	for record in self:
	#		ctr = 0 
	#		for c in record.order:
	#			ctr = ctr + 1
	#		record.nr_orders = ctr





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

	x_analysis_lab = fields.Boolean(
			string = 'Análisis de laboratorio', 
			default=False, 
			)

	x_observations = fields.Text(
			string = 'Observaciones',

			#required=True, 
			required=False, 
			)

	x_indications = fields.Text(
			string = 'Indicaciones',
			required=True, 
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

		#print 
		#print 'jx'
		#print 'create_order_current'



		treatment_id = self.treatment.id 
		consultation_id = self.id 
		patient_id = self.patient.id
		doctor_id = self.doctor.id

		#chief_complaint = self.chief_complaint


		partner_id = self.env['res.partner'].search([('name','like',self.patient.name)],limit=1).id


		#print 'patient_id: ', patient_id
		#print 'doctor_id: ', doctor_id
		#print 'patient name: ', self.patient.name 
		#print 'partner_id: ', partner_id


		consultation_id = self.id



		# Order - Search
		order_id = self.env['sale.order'].search([
													('consultation','=',consultation_id),													
													('state','=','draft'),

													#('x_family','=', 'private'),
												]).id

		#print 'consultation_id: ', consultation_id
		#print 'order_id: ', order_id



		# Order - Create 
		if order_id == False:

			order = self.env['sale.order'].create(
													{
														'treatment': treatment_id,
														'partner_id': partner_id,
														'patient': patient_id,	
														'x_doctor': doctor_id,	
														'consultation':self.id,
														'state':'draft',

														#'x_chief_complaint':chief_complaint,
													}
												)

			# Create order lines 
			ret = order.x_create_order_lines()
			#print ret 




			# Copy 
			#pre_order = order.copy({
										#'x_family':'private',
			#				})	




			order_id = order.id 
			#print order
		

		#print order_id
		#print 

		


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
							
							#'default_x_chief_complaint': chief_complaint,	
						}
			}


	# create_order_current












# ---------------------------------------------- Open Appointment --------------------------------------------------------


	@api.multi
	def open_appointment(self):  

		#print 
		#print 'open appointment'

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

		#print 
		#print 'jx'
		#print 'Create Consultation - Override - CRUD'
		#print 
		#print vals
		#print 
	
		
		consultation_id = self.id
		#print 'consultation_id: ', consultation_id


		appointment_id = vals['appointment']
		#print 'appointment_id: ', appointment_id
		#print 



		# Return 
		res = super(Consultation, self).create(vals)

		return res


	# create - CRUD 




# ---------------------------------------------- Create Service --------------------------------------------------------

	# Create Service
	 
	@api.multi
	def create_service(self):  
		consultation_id = self.id 				
		treatment_id = self.treatment.id 

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
							'default_treatment': treatment_id,


							'default_laser': laser,
							'default_zone': zone,
							'default_pathology': pathology,
							}
				}

	# create_service






