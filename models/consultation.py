# -*- coding: utf-8 -*-
#
# 	Consultation 
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars



#------------------------------------------------------------------------
class Consultation(models.Model):
	_name = 'openhealth.consultation'
	_inherit = 'oeh.medical.evaluation'



	name = fields.Char(
			string = 'Consulta #',
			)


	#owner = fields.Char(
	#		string = 'Owner',
	#		)


	# ----------------------------- Services -----------------------------------

	# Service id 
	service_ids = fields.One2many(
	#service = fields.One2many(
			'openhealth.service', 
			#'treatment_id', 
			'consultation', 
			#string="Services"
			string="Servicios"
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




	# Service 
	service = fields.Many2one(
			'product.template',
			#domain = [
			#			('type', '=', 'service'),
			#			('x_treatment', '=', _jx_laser_type),
			#		],
			#string="Service", 
			string="Servicio", 
			)




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


	#x_observation = fields.Char(
	x_observation = fields.Text(
			string="Observación",
			#size=200,
			size=200,
			)

	x_next_evaluation_date = fields.Date(
			string = "Próxima cita", 	
			#default = fields.Date.today, 
			#required=True, 
			)

	

	# Intro

	x_reason_consultation = fields.Text(
			string = 'Motivo de consulta (detalle)', 
			)

	x_diagnosis = fields.Text(
			string = 'Diagnóstico', 
			)


	x_antecedents = fields.Text(
			string = 'Antecedentes médicos', 
			)


	x_allergies_medication = fields.Text(
			string = 'Alergias a medicamentos', 
			)



	# Evaluation 

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





	# Procedure 


	x_vspace = fields.Char(
			' ', 
			readonly=True
			)



	# Laser 
	x_laser_co2 = fields.Boolean(
			string = 'Láser Co2',
			)

	x_laser_excimer = fields.Boolean(
			string = 'Láser Exímero 308-nm',
			)

	x_laser_ndyag = fields.Boolean(
			string = 'Láser Ndyag',
			)

	x_laser_ipl = fields.Boolean(
			string = 'Láser IPL',
			)

	x_laser_rejuvenation_vaginal = fields.Boolean(
			string = 'Láser rejuvenecimiento vaginal',
			)



	# Other 
	x_criosurgery = fields.Boolean(
			string = 'Criocirugía',
			)

	x_acid_haluronic = fields.Boolean(
			string = 'Acido halurónico',
			)

	x_nutrition_deep = fields.Boolean(
			string = 'Nutrición profunda',
			)


	x_toxin_botulinum = fields.Boolean(
			string = 'Toxina Botulínica',
			)


	x_prp_rich = fields.Boolean(
			string = 'PRP rico en factores de crecimiento',
			)

	x_hydration_deep = fields.Boolean(
			string = 'Hidratación prof. Acido hialurónico',
			)


	x_corporal = fields.Boolean(
			string = 'Tratamiento corporal',
			)

	x_sclerotherapy = fields.Boolean(
			string = 'Escleroterapia',
			)

	x_vitamin_c = fields.Boolean(
			string = 'Vitamina C (EV)',
			)







	# Zone  

	x_areola = fields.Boolean(
			string = 'Areola',
			)

	x_armpits = fields.Boolean(
			string = 'Axilas',
			)

	x_beard = fields.Boolean(
			string = 'Barba',
			)

	x_belly = fields.Boolean(
			string = 'Barriga',
			)

	x_bikini = fields.Boolean(
			string = 'Bikini',
			)



	x_down_lip = fields.Boolean(
			string = 'Bozo/Bigote',
			)

	x_arm = fields.Boolean(
			string = 'Brazo',
			)

	x_head = fields.Boolean(
			string = 'Cabeza',
			)

	x_neck = fields.Boolean(
			string = 'Cuello',
			)

	x_back = fields.Boolean(
			string = 'Espalda',
			)






	x_front = fields.Boolean(
			string = 'Frente',
			)

	x_gluteus = fields.Boolean(
			string = 'Glúteo',
			)

	x_shoulders = fields.Boolean(
			string = 'Hombros',
			)

	x_linea_alba = fields.Boolean(
			string = 'Linea Alba',
			)

	x_body_localized = fields.Boolean(
			string = 'Localizado cuerpo',
			)




	x_face_localized = fields.Boolean(
			string = 'Localizado rostro',
			)

	x_hands = fields.Boolean(
			string = 'Manos',
			)

	x_chin = fields.Boolean(
			string = 'Mentón',
			)

	x_nape = fields.Boolean(
			string = 'Nuca',
			)

	x_sideburns = fields.Boolean(
			string = 'Patillas',
			)





	x_breast = fields.Boolean(
			string = 'Pecho',
			)

	x_leg = fields.Boolean(
			string = 'Pierna',
			)

	x_feet = fields.Boolean(
			string = 'Pies',
			)

	x_cheekbones = fields.Boolean(
			string = 'Pómulos',
			)

	x_face_all = fields.Boolean(
			string = 'Todo rostro',
			)




	x_nail = fields.Boolean(
			string = 'Uña',
			)

	x_vagina = fields.Boolean(
			string = 'Vagina',
			)







	

	# Smart - Pathology
	

			
	
	
	

			

	
	
	
	


			
			
	
	
	
	# Pathology

	acne_active = fields.Boolean(
			string = '',
			)
	
	acne_sequels = fields.Boolean(
			string = 'Acné y secuelas',
			)

	acne_sequels_1 = fields.Boolean(
			string = '1',
			)

	acne_sequels_2 = fields.Boolean(
			string = '2',
			)

	acne_sequels_3 = fields.Boolean(
			string = '3',
			)




	alopecia = fields.Boolean(
			string = '',
			)

	cyst = fields.Boolean(
			string = '',
			)

	depilation = fields.Boolean(
			string = '',
			)
 
	emangiomas = fields.Boolean(
			string = '',
			)
 
	keratosis = fields.Boolean(
			string = '',
			)
			

	
	
	
	keratosis_1 = fields.Boolean(
			string = '',
			)

	keratosis_2 = fields.Boolean(
			string = '',
			)

	keratosis_3 = fields.Boolean(
			string = '',
			)

	mole_1 = fields.Boolean(
			string = '',
			)

	mole_2 = fields.Boolean(
			string = '',
			)



	mole_3 = fields.Boolean(
			string = '',
			)

	monalisa_touch = fields.Boolean(
			string = '',
			)

	polyp = fields.Boolean(
			string = 'Polipo',
			)

	psoriasis = fields.Boolean(
			string = '',
			)

	rejuvenation_face_1 = fields.Boolean(
			string = '',
			)



	rejuvenation_face_2 = fields.Boolean(
			string = '',
			)

	rejuvenation_face_3 = fields.Boolean(
			string = '',
			)

	rejuvenation_face_hands = fields.Boolean(
			string = '',
			)

	rejuvenation_face_neck = fields.Boolean(
			string = '',
			)

	rejuvenation_face_neck_hands = fields.Boolean(
			string = '',
			)



	rejuvenation_facial = fields.Boolean(
			string = '',
			)

	rejuvenation_hands = fields.Boolean(
			string = '',
			)

	rejuvenation_neck = fields.Boolean(
			string = 'Rejuvenecimiento',
			)

	rosacea = fields.Boolean(
			string = '',
			)
 
	ruby_point = fields.Boolean(
			string = 'Punto Rubí',
			)



	ruby_points = fields.Boolean(
			string = '',
			)

	scar = fields.Boolean(
			string = 'Cicatriz',
			)

	scar_1 = fields.Boolean(
			string = '',
			)

	scar_2 = fields.Boolean(
			string = '',
			)

	scar_3 = fields.Boolean(
			string = '',
			)




	stain = fields.Boolean(
			string = 'Manchas',
			)


	stains_1 = fields.Boolean(
			string = '',
			)

	stains_2 = fields.Boolean(
			string = '',
			)

	stains_3 = fields.Boolean(
			string = '',
			)

	telangiectasia = fields.Boolean(
			string = '',
			)



	varices = fields.Boolean(
			string = '',
			)

	vitiligo = fields.Boolean(
			string = '',
			)

	wart = fields.Boolean(
			string = 'Verruga',
			)

	






	# Conclusion
	# ------------
	x_observations = fields.Text(
			string = 'Observaciones',
			)

	x_indications = fields.Text(
			string = 'Indicaciones',
			)






	# Laser Co2
	orientation = fields.Boolean(
			string = 'Orientation',
			)
	



	# Quotations
	# -----------------------------------------------------------------------------------------------------------------

	# Quotation 
	#quotation = fields.One2many(
	order = fields.One2many(
			#'openhealth.quotation', 
			#'openhealth.order',
			'sale.order',
			 
			#'treatment_id', 
			'consultation', 
			#string="Services"
			string="Presupuestos"
			)

	order_line  = fields.One2many(
			'sale.order.line',
			'order_id',
	)


	#------------------------------------ Buttons -----------------------------------------


	# Button - Treatment 
	# -------------------
	@api.multi
	def create_quotation_current(self):  

		patient_id = self.patient.id
		#doctor_id = self.doctor.id


		#partner_id = lambda self: self.env['res.partner'].search([('name','=','Javier Revilla')])
		#partner_id = lambda self: self.env['res.partner'].search([('name','=','Javier Revilla')])

		#partner_id = self.env['res.partner'].search([('name','=','Javier Revilla')]).id
		#partner_id = self.env['res.partner'].search([('name','=',self.patient.name)]).id
		partner_id = self.env['res.partner'].search([('name','=',self.patient.name)],limit=1).id
		
		
		print
		print partner_id
		#print partner_id.name
		print
		
		consultation_id = self.id 

		
		#order_line_id = self.env['sale.order.line'].new().id
		
		
		return {

			# Mandatory 
			#'type': 'ir.actions.act_window',
			#'name': 'Create Quotation Current',
			#'res_model': 'sale.order',
			#"views": [[False, "form"]],
			#'view_mode': 'form',
			#'target': 'current',
			
			
			'type': 'ir.actions.act_window',
			'name': ' Create Quotation Current', 
			'view_type': 'form',
			'view_mode': 'form',
			#'res_model': self._name,
			'res_model': 'sale.order',
			#'res_id': consultation_id,
			
			'flags': {
					'form': {'action_buttons': True, }
					},
			
			
			'target': 'current',
			#'target': 'new',
			

			'context':   {

				#'search_default_partner_id': patient_id,
				#'search_default_patient': patient_id,

				'default_partner_id': partner_id,
				#'default_patient': patient_id,
				
				'default_consultation': consultation_id,
				
				#'default_order_line': order_line_id,
				
			}
		}



	# Consultation - Quick Self Button  
	# ---------------------------------
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

				'context':   {
				}
		}




	# Clear Vars
	# ------------

	
	
	
	
	#@api.multi
	#def clear_vars_co2_allface(self):  
	#	self.co2_allface_rejuvenation = False
	#	self.co2_allface_acnesquels = False
	#	return {}


	#@api.multi
	#def clear_vars_co2_localface(self):  
	#	self.co2_cheekbone = False
	#	return {}
	
	
	#@api.multi
	#def clear_vars_co2_localbody(self):  
	#	self.co2_cheekbone = False
	#	return {}
	





	# Clear Procedures
	# ------------------
	
	@api.multi
	def clear_others(self,context=None):  
		
		print
		print 'jx: Mark'
		print
		
		self.co2_cheekbone = False
		#self.co2_hands = False
		self.co2_neck = False
		self.co2_vagina = False
		self.co2_packages = False

		return {}
	
	
	
	
	
	# Smart vars
	# ----------
	
	co2_cheekbone = fields.Selection(
			selection = jxvars._co2_che_list, 
			string="Pómulos", 
			#default='nil',	
			)
	
	co2_hands = fields.Selection(
			selection = jxvars._co2_han_list, 
			string="Manos", 
			#default='nil',	
			)

	co2_neck = fields.Selection(
			selection = jxvars._co2_nec_list, 
			string="Cuello", 
			#default='nil',	
			)
	
	co2_vagina = fields.Selection(
			selection = jxvars._co2_vag_list, 
			string="Vagina", 
			#default='nil',	
			)
			
	co2_packages = fields.Selection(
			selection = jxvars._co2_pac_list, 
			string="Paquetes Rejuvenecimiento", 
			#default='nil',	
			)

	co2_allface_rejuvenation = fields.Selection(
			selection = jxvars._co2_rejuv_list, 
			string="Rejuvenecimiento facial", 
			#default='nil',	
			)

	co2_allface_acnesequels = fields.Selection(
			selection = jxvars._co2_acneseq_list, 
			string="Acné y secuelas", 
			#default='nil',	
			)

	co2_localface_stains = fields.Selection(
			selection = jxvars._co2_lfstains_list, 
			string="Manchas", 
			#default='nil',	
			)
	
	
	
	# Clear All vars
	@api.multi
	def clear_vars_co2_focus(self):  

		self.co2_cheekbone = False
		self.co2_hands = False
		self.co2_neck = False
		self.co2_vagina = False
		self.co2_packages = False
		
		
		self.co2_allface_rejuvenation = False
		self.co2_allface_acnesequels = False
		
		self.co2_localface_stains = False

		return {}
	
	
	
	
	# smart Procedures
	# ------------------
	
	
	zone_glo = fields.Char(
		string='zone_glo',
		default='x',
		)
	
	
	@api.multi
	#def set_zone(self,cr,uid,ids,context=None):
	def set_zone(self,context=None):

		#print context
		print 'jx'
		print context

		print self.zone_glo
		zone_glo=context
		self.zone_glo=context
		print self.zone_glo
		print 'jx'
		
		return {self.zone_glo}

	
	
	
	
	# Open Services
	 
	#@api.multi
	#def open_service(self):  

	#	consultation_id = self.id 
				
	#	laser = 'laser_co2'
	#	zone = ''	
	#	pathology = ''

	#	return {
	#			'type': 'ir.actions.act_window',
	#			'name': ' New Service Current', 
	#			'view_type': 'form',
	#			'view_mode': 'form',				
	#			'res_model': 'openhealth.service',				
				#'res_id': consultation_id,
	#			'target': 'current',
	#			'flags': 	{
	#						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': True, }
	#						},

	#			'context': {
	#						'default_consultation': consultation_id,
												
	#						'default_laser': laser,
	#						'default_zone': zone,
	#						'default_pathology': pathology,
	#						}
	#			}
	
	
	

	# Procedure - Laser Co2 
	@api.multi
	def open_service_co2(self):  

		consultation_id = self.id 
		
		laser = 'laser_co2'
		#zone = 'cheekbones'	
		#pathology = 'stains'
		zone = ''	
		pathology = ''
		
		
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current - Laser Co2', 
				'view_type': 'form',
				'view_mode': 'form',				
				#'res_id': consultation_id,
				'target': 'current',
								
				#'res_model': 'openhealth.service',				
				#'res_model': 'openhealth.service_excilite',				
				#'res_model': 'openhealth.laserco2',				
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
				
