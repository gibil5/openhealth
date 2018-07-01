# -*- coding: utf-8 -*-
#
# 		*** Treatment
# 
# Created: 			26 Aug 2016
# Last up: 	 		28 Jun 2018
#

from openerp import models, fields, api

from datetime import datetime
from . import treatment_funcs
from . import time_funcs
from . import treatment_vars

class Treatment(models.Model):

	_inherit = 'openhealth.process'	

	_name = 'openhealth.treatment'
	
	_order = 'write_date desc'




# ----------------------------------------------------------- Testing ------------------------------------------------------

	# Clear  
	@api.multi 
	def clear(self):

		print 
		print 'Clear'

		# Clean
		#for app in self.appointment_ids: 
		#	app.remove_myself()
		self.appointment_ids.unlink()





	# Test  
	@api.multi 
	def test(self):

		print 
		print 'Testing'

		# Date 
		GMT = time_funcs.Zone(0,False,'GMT')
		#self.start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		self.start_date = datetime.now(GMT).strftime("%Y-%m-%d")

		
		# Init 
		patient_id = self.patient.id
		doctor_id = self.physician.id
		duration = 0.5
		state = 'pre_scheduled'
		x_type = 'consultation'

		#x_create_procedure_automatic = True
		x_create_procedure_automatic = False
		
		treatment_id = self.id 

		#appointment_date = self.start_date
		appointment_date = self.start_date + ' 14:00:00'			# 09:00:00


		# Appointment 
		#appointment = self.create_appointment(appointment_date, patient_id, doctor_id, duration, state, x_type, x_create_procedure_automatic, treatment_id)


		# Create
		#appointment = self.env['oeh.medical.appointment'].create({
		#appointment = self.appointment_ids.create({
		#															'appointment_date': appointment_date,
		#															'patient': patient_id,	
		#															'doctor': doctor_id,
		#															'duration': duration,
		#															'state': state,
		#															'x_create_procedure_automatic': x_create_procedure_automatic,
		#															'x_type': x_type,
																	#'x_chief_complaint': chief_complaint, 
																	#'x_target': 'doctor',

		#															'treatment': treatment_id, 
		#														})
		#print appointment
		#print self.appointment_ids






		self.create_order_con()




		print 
	# testing




	@api.multi 
	def create_appointment(self, appointment_date, patient_id, doctor_id, duration, state, x_type, x_create_procedure_automatic, treatment_id):

		print 
		print 'Create Appointment'

		# Create
		#appointment = self.appointment_ids.create({
		appointment = self.env['oeh.medical.appointment'].create({
																	'appointment_date': appointment_date,

																	'patient': patient_id,	
																	'doctor': doctor_id,
																	'duration': duration,
																	'state': state,

																	'x_create_procedure_automatic': x_create_procedure_automatic,
																	'x_type': x_type,

																	#'x_chief_complaint': chief_complaint, 
																	#'x_target': 'doctor',

																	'treatment': treatment_id, 
																})
		#appointment_id = appointment.id

		return appointment 
	# create_appointment




# ----------------------------------------------------------- Manual ------------------------------------------------------

	# Manual
	add_procedures = fields.Boolean(
			string="Control Manual", 
			default=False, 
		)	

	# Reset  
	@api.multi 
	def reset_procs(self):
		self.add_procedures = False 

	# Toggle  
	@api.multi 
	def toggle_add_procedures(self):
		self.add_procedures = not self.add_procedures 



# ----------------------------------------------------------- Alta ------------------------------------------------------

	# Closed 
	treatment_closed = fields.Boolean(
			string="De Alta",
			default=False,
		)


# ----------------------------------------------------------- Canonical ------------------------------------------------------

	# Name 
	name = fields.Char(
			string="Tratamiento #", 

			compute='_compute_name', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_name(self):
		for record in self:
			record.name = 'TR0000' + str(record.id) 


	# Space 
	vspace = fields.Char(
			' ', 
			readonly=True
		)


	# Active 
	active = fields.Boolean(
			default=True, 
		)


	# Sex
	patient_sex = fields.Char(
			string="Sexo", 

			compute='_compute_patient_sex', 
		)

	@api.multi
	def _compute_patient_sex(self):
		for record in self:		
			if record.patient.sex != False: 
				record.patient_sex = record.patient.sex[0]


	# Age
	patient_age = fields.Char(
			string="Edad", 

			compute='_compute_patient_age', 
		)

	@api.multi
	def _compute_patient_age(self):
		for record in self:		
			if record.patient.age != False: 
				record.patient_age = record.patient.age.split()[0]


	# City 
	patient_city = fields.Char(
			string="Lugar de procedencia", 
			
			compute='_compute_patient_city', 
		)

	@api.multi
	def _compute_patient_city(self):
		for record in self:		
			if record.patient.city_char != False: 
				city = record.patient.city_char
				record.patient_city = city.title()





# ----------------------------------------------------------- Vip in prog ------------------------------------------------------

	# Vip in progress 
	x_vip_inprog = fields.Boolean(
			string="Vip en progreso", 
			default=False, 
		
			compute='_compute_vip_inprog', 
		)

	@api.multi
	def _compute_vip_inprog(self):
		for record in self:
			nr_vip = self.env['openhealth.service.vip'].search_count([		
																		('treatment','=', record.id),
																		#('state','=', 'draft'),
				]) 
			if nr_vip > 0: 
				record.x_vip_inprog = True 





# ----------------------------------------------------------- Quick Nr Ofs ------------------------------------------------------

	# Quick Hands
	nr_quick_hands = fields.Integer(
			string='Manos', 
			default=11, 

			compute='_compute_nr_quick_hands', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_hands(self):
		for record in self:
			record.nr_quick_hands = record.patient.x_nr_quick_hands



	# Quick Body Local
	nr_quick_body_local = fields.Integer(
			string='Localizado Cuerpo', 
			default=11, 

			compute='_compute_nr_quick_body_local', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_body_local(self):
		for record in self:
			record.nr_quick_body_local = record.patient.x_nr_quick_body_local


	# Quick Face Local
	nr_quick_face_local = fields.Integer(
			string='Localizado Rostro', 
			default=11, 

			compute='_compute_nr_quick_face_local', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_face_local(self):
		for record in self:
			record.nr_quick_face_local = record.patient.x_nr_quick_face_local



	# Quick cheekbones
	nr_quick_cheekbones = fields.Integer(
			string='Pómulos', 
			default=11, 

			compute='_compute_nr_quick_cheekbones', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_cheekbones(self):
		for record in self:
			record.nr_quick_cheekbones = record.patient.x_nr_quick_cheekbones


	# Quick face_all
	nr_quick_face_all = fields.Integer(
			string='Todo Rostro', 
			default=11, 

			compute='_compute_nr_quick_face_all', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_face_all(self):
		for record in self:
			record.nr_quick_face_all = record.patient.x_nr_quick_face_all



	# Quick face_all_hands
	nr_quick_face_all_hands = fields.Integer(
			string='Todo Rostro Manos', 
			default=11, 

			compute='_compute_nr_quick_face_all_hands', 
		)

	@api.multi
	#@api.depends('start_date')
	def _compute_nr_quick_face_all_hands(self):
		for record in self:
			record.nr_quick_face_all_hands = record.patient.x_nr_quick_face_all_hands



	# Quick face_all_neck
	nr_quick_face_all_neck = fields.Integer(
			string='Todo Rostro Cuello', 
			default=11, 

			compute='_compute_nr_quick_face_all_neck', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_nr_quick_face_all_neck(self):
		for record in self:
			record.nr_quick_face_all_neck = record.patient.x_nr_quick_face_all_neck



	# Quick neck
	nr_quick_neck = fields.Integer(
			string='Cuello', 
			default=11, 

			compute='_compute_nr_quick_neck', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_nr_quick_neck(self):
		for record in self:
			record.nr_quick_neck = record.patient.x_nr_quick_neck



	# Quick neck_hands
	nr_quick_neck_hands = fields.Integer(
			string='Cuello Manos', 
			default=11, 

			compute='_compute_nr_quick_neck_hands', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_nr_quick_neck_hands(self):
		for record in self:
			record.nr_quick_neck_hands = record.patient.x_nr_quick_neck_hands





	

# ----------------------------------------------------------- Relational ------------------------------------------------------

	consultation_ids = fields.One2many(
			'openhealth.consultation', 
			'treatment', 
			string = "Consultas", 
		)

	recommendation_ids = fields.One2many(
			'openhealth.recommendation', 
			'treatment', 
			string = "Recomendaciones", 
		)

	procedure_ids = fields.One2many(
			'openhealth.procedure', 
			'treatment', 
			string = "Procedimientos", 
		)

	session_ids = fields.One2many(
			'openhealth.session.med', 
			'treatment', 
			string = "Sesiones", 
		)

	control_ids = fields.One2many(
			'openhealth.control', 
			'treatment', 
			string = "Controles", 
		)

	# Service 
	service_ids = fields.One2many(
			'openhealth.service', 	
			'treatment', 
			string="Servicios"
		)

	# Co2
	service_co2_ids = fields.One2many(
			'openhealth.service.co2', 
			'treatment', 
			string="Servicios Co2"
			)

	# Excilite
	service_excilite_ids = fields.One2many(
			'openhealth.service.excilite', 
			'treatment', 
			string="Servicios Excilite"
			)

	# Ipl
	service_ipl_ids = fields.One2many(
			'openhealth.service.ipl', 
			'treatment', 
			string="Servicios ipl"
			)


	# Ndyag
	service_ndyag_ids = fields.One2many(
			'openhealth.service.ndyag', 
			'treatment', 
			string="Servicios ndyag"
			)

	# Medical
	service_medical_ids = fields.One2many(
			'openhealth.service.medical', 
			'treatment', 
			string="Servicios medical"
			)

	# Reservations 
	reservation_ids = fields.One2many(
			'oeh.medical.appointment', 
			'treatment', 
			string = "Reserva de sala", 
			domain = [
						('x_machine', '!=', 'false'),	
					],
			)

	# Appointments 
	appointment_ids = fields.One2many(
			'oeh.medical.appointment',  
			'treatment', 
			string = "Citas", 
			domain = [
						('x_target', '=', 'doctor'),
					],
			)

	# Orders 
	order_ids = fields.One2many(
			'sale.order',			 
			'treatment', 
			string="Presupuestos",
		)

	# Orders Procedures
	order_pro_ids = fields.One2many(
			'sale.order',			 
			'treatment', 
			string="Presupuestos",
			domain = [
						('x_family', '=', 'procedure'),
					],
		)

	# Vip
	service_vip_ids = fields.One2many(
			'openhealth.service.vip', 
			'treatment', 
			string="Servicios vip"
			)

	# Quick
	service_quick_ids = fields.One2many(
			'openhealth.service.quick', 
			'treatment', 
			string="Servicios quick"
			)




# ----------------------------------------------------------- Consultation Progress ------------------------------------------------------
	
	# Consultation progress
	consultation_progress = fields.Float(
			default = 0, 

			compute="_compute_progress",
		)

	@api.multi
	#@api.depends('consultation_ids')
	def _compute_progress(self):
		for record in self:
			for con in record.consultation_ids:
				record.consultation_progress = con.progress



# ----------------------------------------------------------- State ------------------------------------------------------
	
	# State 
	state = fields.Selection(
			selection = treatment_vars._state_list, 
			string='Estado', 
			default = 'empty', 

			compute="_compute_state",
		)



	@api.multi
	#@api.depends('consultation_ids')
	def _compute_state(self):
		for record in self:

			#state = False
			state = 'empty'

			if record.nr_appointments > 0:
				state = 'appointment'

			if record.nr_budgets_cons > 0:
				state = 'budget_consultation'

			if record.nr_invoices_cons > 0:
				state = 'invoice_consultation'

			if record.consultation_progress == 100:
				state = 'consultation'

			if record.nr_services > 0:
				state = 'service'

			if record.nr_budgets_pro > 0:
				state = 'budget_procedure'

			if record.nr_invoices_pro > 0:
				state = 'invoice_procedure'

			if record.nr_procedures > 0:
				state = 'procedure'

			if record.nr_sessions > 0:
				state = 'sessions'

			if record.nr_controls > 0:
				state = 'controls'

			if record.treatment_closed:
				state = 'done'

			record.state = state
	# _compute_state





# ----------------------------------------------------------- Number ofs ------------------------------------------------------

	# Appointments 
	nr_appointments = fields.Integer(
			string="Citas",

			compute="_compute_nr_appointments",
	)
	@api.multi
	def _compute_nr_appointments(self):
		for record in self:
			record.nr_appointments=self.env['oeh.medical.appointment'].search_count([
																						('treatment','=', record.id),
																						#('x_target','=', 'doctor'),
																	]) 


	# Budgets - Consultations 			# DEP ? 
	nr_budgets_cons = fields.Integer(
			string="Presupuestos Consultas",
			
			compute="_compute_nr_budgets_cons",
	)
	@api.multi
	def _compute_nr_budgets_cons(self):
		for record in self:
			record.nr_budgets_cons=self.env['sale.order'].search_count([
																	('treatment','=', record.id),
																	('x_family','=', 'consultation'),
																	('state','=', 'draft'),
																	]) 

	# Invoices - Consultations
	nr_invoices_cons = fields.Integer(
			string="Facturas Consultas",
			
			compute="_compute_nr_invoices_cons",
	)
	@api.multi
	def _compute_nr_invoices_cons(self):
		for record in self:
			record.nr_invoices_cons=self.env['sale.order'].search_count([
																			('treatment','=', record.id),
																			('x_family','=', 'consultation'),
																			('state','=', 'sale'),
																	]) 

	# Consultations 
	nr_consultations = fields.Integer(
			string="Nr Consultas",

			compute="_compute_nr_consultations",
	)
	#@api.multi
	@api.depends('consultation_ids')
	def _compute_nr_consultations(self):
		for record in self:
			ctr = 0 
			for c in record.consultation_ids:
				ctr = ctr + 1
			record.nr_consultations = ctr







	# Budgets - Proc   					# DEP ?  
	nr_budgets_pro = fields.Integer(
			string="Presupuestos - Pro",
			
			compute="_compute_nr_budgets_pro",
	)
	@api.multi
	def _compute_nr_budgets_pro(self):
		for record in self:
			record.nr_budgets_pro=self.env['sale.order'].search_count([
																		('treatment','=', record.id),
																		('x_family','=', 'procedure'),
																		('state','=', 'draft'),
																	]) 

	# Invoices - Proc
	nr_invoices_pro = fields.Integer(
			string="Facturas",
			
			compute="_compute_nr_invoices_pro",
	)
	@api.multi
	def _compute_nr_invoices_pro(self):
		for record in self:
			record.nr_invoices_pro=self.env['sale.order'].search_count([
																			('treatment','=', record.id),	
																			('x_family','=', 'procedure'),
																			('state','=', 'sale'),
																	]) 

	# Procedures 
	nr_procedures = fields.Integer(
			string="Procedimientos",

			compute="_compute_nr_procedures",
	)
	@api.multi
	def _compute_nr_procedures(self):
		for record in self:
			record.nr_procedures=self.env['openhealth.procedure'].search_count([
																					('treatment','=', record.id),
																	]) 


	# Sessions 
	nr_sessions = fields.Integer(
			string="Sesiones",
			
			compute="_compute_nr_sessions",
	)
	@api.multi
	def _compute_nr_sessions(self):
		for record in self:
			record.nr_sessions=self.env['openhealth.session.med'].search_count([
																					('treatment','=', record.id),
																				]) 

	# Controls 
	nr_controls = fields.Integer(
			string="Controles",

			compute="_compute_nr_controls",
	)
	@api.multi
	def _compute_nr_controls(self):
		for record in self:
			record.nr_controls=0
			record.nr_controls=self.env['openhealth.control'].search_count([
																	('treatment','=', record.id),	
																	])																	
																	#order='appointment_date desc', limit=1)



	# Orders 
	nr_orders = fields.Integer(
			string="Presupuestos",

			compute="_compute_nr_orders",
	)
	@api.multi
	def _compute_nr_orders(self):
		for record in self:
			ctr = 0 			
			for c in record.consultation_ids:
				for o in c.order:
					ctr = ctr + 1
			record.nr_orders = ctr








# ----------------------------------------------------------- Number ofs - Services ------------------------------------------------------
	# Number of Services  
	nr_services = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services",
	)
	@api.multi
	def _compute_nr_services(self):
		for record in self:

			quick =		self.env['openhealth.service.quick'].search_count([('treatment','=', record.id),]) 
			vip =		self.env['openhealth.service.vip'].search_count([('treatment','=', record.id),]) 
			co2 =		self.env['openhealth.service.co2'].search_count([('treatment','=', record.id),]) 
			exc = 		self.env['openhealth.service.excilite'].search_count([('treatment','=', record.id),]) 
			ipl = 		self.env['openhealth.service.ipl'].search_count([('treatment','=', record.id),]) 
			ndyag = 	self.env['openhealth.service.ndyag'].search_count([('treatment','=', record.id),]) 
			medical =	self.env['openhealth.service.medical'].search_count([('treatment','=', record.id),]) 

			record.nr_services = vip + quick + co2 + exc + ipl + ndyag + medical



	# vip
	nr_services_vip = fields.Integer(
			string="Servicios vip",

			compute="_compute_nr_services_vip",
	)
	@api.multi
	def _compute_nr_services_vip(self):
		for record in self:
			services =		self.env['openhealth.service.vip'].search_count([('treatment','=', record.id),]) 
			record.nr_services_vip = services 



	# Quick
	nr_services_quick = fields.Integer(
			string="Servicios Quick",
			
			compute="_compute_nr_services_quick",
	)
	@api.multi
	def _compute_nr_services_quick(self):
		for record in self:
			services =		self.env['openhealth.service.quick'].search_count([('treatment','=', record.id),]) 
			record.nr_services_quick = services 



	# Co2
	nr_services_co2 = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_co2",
	)
	@api.multi
	def _compute_nr_services_co2(self):
		for record in self:
			services =		self.env['openhealth.service.co2'].search_count([('treatment','=', record.id),]) 
			record.nr_services_co2 = services 



	# excilite
	nr_services_excilite = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_excilite",
	)
	@api.multi
	def _compute_nr_services_excilite(self):
		for record in self:
			services = 		self.env['openhealth.service.excilite'].search_count([('treatment','=', record.id),]) 
			record.nr_services_excilite = services 


	# ipl
	nr_services_ipl = fields.Integer(
			string="Servicios",
			
			compute="_compute_nr_services_ipl",
	)
	@api.multi
	def _compute_nr_services_ipl(self):
		for record in self:
			services = 		self.env['openhealth.service.ipl'].search_count([('treatment','=', record.id),]) 
			record.nr_services_ipl = services 



	# ndyag
	nr_services_ndyag = fields.Integer(
			string="Servicios",
			
			compute="_compute_nr_services_ndyag",
	)
	@api.multi
	def _compute_nr_services_ndyag(self):
		for record in self:
			services = 		self.env['openhealth.service.ndyag'].search_count([('treatment','=', record.id),]) 
			record.nr_services_ndyag = services 


	# medical
	nr_services_medical = fields.Integer(
			string="Servicios",
			
			compute="_compute_nr_services_medical",
	)
	@api.multi
	def _compute_nr_services_medical(self):
		for record in self:
			services = 		self.env['openhealth.service.medical'].search_count([('treatment','=', record.id),]) 
			record.nr_services_medical = services 







# ----------------------------------------------------------- Open Myself ------------------------------------------------------
	# Open Myself
	@api.multi 
	def open_myself(self):

		treatment_id = self.id  

		return {
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action 
			'res_model': 'openhealth.treatment',
			'res_id': treatment_id,
			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 
			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},			
			'context':   {}
		}
	# open_myself




# ----------------------------------------------------------- Creates - Manual, Process and Testing ------------------------------------------------------



# ----------------------------------------------------------- Create Order  ------------------------------------------------------

	# Partner 
	partner_id = fields.Many2one(
			'res.partner',
			string = "Cliente", 	

			compute='_compute_partner_id', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_partner_id(self):
		for record in self:
			partner = record.env['res.partner'].search([
															('name','like', record.patient.name),
				
														],
														#order='appointment_date desc',
														limit=1,)

			record.partner_id = partner 
	# _compute_partner_id



	# Create Order - By Doctor 
	@api.multi 
	def create_order(self, target):

		#print
		#print 'Create Order'
		#print target


		# Init
		#note = self.partner_id.comment

		# Doctor 
		doctor_id = treatment_funcs.get_actual_doctor(self)
		if doctor_id == False: 
			doctor_id = self.physician.id 

		# Pricelist 
		if self.x_vip_inprog: 
	 		pl = self.env['product.pricelist'].search([
																('name', 'like', 'VIP'), 
														],
															#order='write_date desc',
															limit=1,
														)
		 	pl_id = pl.id 
	 	else: 
	 		pl = self.env['product.pricelist'].search([
																('name', 'like', 'Public Pricelist'), 
																#('name', '=', 'Public Pricelist'), 
														],
															#order='write_date desc',
															limit=1,
														)
	 		# jx - Hack !
		 	#pl_id = pl.id 
		 	pl_id = 1

	 	#print self.x_vip_inprog
	 	#print pl
	 	#print pl.name
	 	#print pl.id
	 	#pl_id = pl.id 


		# Create Order 
		order = self.env['sale.order'].create({
														'x_doctor': doctor_id,	
														'partner_id': self.partner_id.id,
														'patient': self.patient.id,	
														'state':'draft',
														'pricelist_id': pl_id, 
														'x_family': target, 

														'treatment': self.id,
													}
												)


		# Create order lines 
		if target == 'consultation':
			if self.chief_complaint in ['monalisa_touch']:
				target_line = 'con_gyn'
			else:
				target_line = 'con_med'

			price_manual = 0
			price_applied = 0
			ret = order.x_create_order_lines_target(target_line, price_manual, price_applied)
			

		else:  		# Procedures 
			order_id = order.id
			ret = treatment_funcs.create_order_lines(self, 'vip', order_id)
			ret = treatment_funcs.create_order_lines(self, 'quick', order_id)
			ret = treatment_funcs.create_order_lines(self, 'co2', order_id)
			ret = treatment_funcs.create_order_lines(self, 'excilite', order_id)
			ret = treatment_funcs.create_order_lines(self, 'ipl', order_id)
			ret = treatment_funcs.create_order_lines(self, 'ndyag', order_id)
			ret = treatment_funcs.create_order_lines(self, 'medical', order_id)

		return order
	# create_order




# ----------------------------------------------------------- Create Order Consultation  ------------------------------------------------------
	@api.multi 
	def create_order_con(self):

		# Init 
		target = 'consultation'
		order = self.create_order(target)		
		return {
				# Created 
				'res_id': order.id,
				# Mandatory 
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action 
				'res_model': 'sale.order',
				# Views 
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',

				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False, 
				
				'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						},			
				'context': {}
		}

	# create_order_con



# ----------------------------------------------------------- Create Procedures  ------------------------------------------------------
	@api.multi
	def create_procedure(self):
		if self.nr_invoices_pro > 0:
			ret = treatment_funcs.create_procedure_go(self)
	# create_procedure 








# ----------------------------------------------------- Create Consultation ------------------------------------------------------------

	# Create Consultation 
	@api.multi
	def create_consultation(self):  

		# Init vars 
		patient_id = self.patient.id
		treatment_id = self.id 
		chief_complaint = self.chief_complaint

		# Doctor 
		doctor_id = treatment_funcs.get_actual_doctor(self)
		if doctor_id == False: 
			doctor_id = self.physician.id

		# Date 
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		# Apointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																	('patient', '=', self.patient.name),		
																	('doctor', '=', self.physician.name),
																	('x_type', '=', 'consultation'),
															], 
															order='appointment_date desc', limit=1)
		appointment_id = appointment.id

		# Search  
		consultation = self.env['openhealth.consultation'].search([
																		('treatment','=', self.id),
																],
																#order='appointment_date desc',
																limit=1,)
		# Create if it does not exist 
		if consultation.name == False:
			# Change App state 
			if appointment.name != False: 
				appointment.state = 'Scheduled'

			# Consultation 
			consultation = self.env['openhealth.consultation'].create({
																		'patient': patient_id,													
																		'treatment': treatment_id,	
																		'evaluation_start_date': evaluation_start_date,
																		'chief_complaint': chief_complaint,
																		'appointment': appointment_id,
																		'doctor': doctor_id,
													})
			consultation_id = consultation.id 

			# Update
			rec_set = self.env['oeh.medical.appointment'].browse([
																	appointment_id																
																])
			ret = rec_set.write({
									'consultation': consultation_id,
								})

		consultation_id = consultation.id 

		# Update Patient 
		#consultation.update_patient()		

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action 
			'res_model': 'openhealth.consultation',
			'res_id': consultation_id,
			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#'view_id': 'oeh_medical_evaluation_view',
			#'view_id': 'oehealth.oeh_medical_evaluation_view',
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 
			'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
					},			
			'context':   {
							'search_default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							'default_treatment': treatment_id,		
							'default_evaluation_start_date': evaluation_start_date,
							'default_chief_complaint': chief_complaint,
							'default_appointment': appointment_id,
			}
		}


	# create_consultation_man







# -----------------------------------------------------------  Create Order Pro  ------------------------------------------------------
	@api.multi 
	def create_order_pro(self):

		target = 'procedure'
		order = self.create_order(target)		

		return {
				# Created 
				'res_id': order.id,
				# Mandatory 
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action 
				'res_model': 'sale.order',
				# Views 
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',
				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False, 
				'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						},			
				'context': {}
		}
	# create_order_pro



# ----------------------------------------------------------- Create Recommendation  ------------------------------------------------------

	@api.multi
	def create_service(self):

		treatment_id = self.id

		return {
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action 
			#'res_model': 'openhealth.consultation',
			#'res_id': consultation_id,
			#'res_model': 'openhealth.service',
			'res_model': 'openhealth.recommendation',
			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 
			'flags': {
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': False, }
					},			
			'context':   {
							#'default_consultation': consultation_id,
							'default_treatment': treatment_id,					
					}
		}
	# create_service
