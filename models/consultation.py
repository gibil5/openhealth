# -*- coding: utf-8 -*-
#
# 	Consultation 
# 

from openerp import models, fields, api
from datetime import datetime





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


	chief_complaint = fields.Char(
			string = 'Motivo de consulta', 
			default = '', 
			required=True, 
			)





	#-----------------------------------------------------------------------------
	# Aggregated 



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





	# Pathology







	# Conclusion
	# ------------
	x_observations = fields.Text(
			string = 'Observaciones',
			)

	x_indications = fields.Text(
			string = 'Indicaciones',
			)








	# Quotations
	# -----------------------------------------------------------------------------------------------------------------

	# Quotation 
	quotation = fields.One2many(
			'openhealth.quotation', 
			#'treatment_id', 
			'consultation', 
			#string="Services"
			string="Presupuestos"
			)




	# Buttons
	# -----------------------------------------------------------------------------------------------------------------

	# Button - Treatment 
	# -------------------
	@api.multi
	def create_quotation_current(self):  

		patient_id = self.patient.id
		doctor_id = self.doctor.id

		consultation_id = self.id 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Create Quotation Current',

			# Window action 
			'res_model': 'openhealth.quotation',

			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			'target': 'current',

			'context':   {
				'search_default_patient': patient_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,

				'default_consultation': consultation_id,
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
						'form': {'action_buttons': True, }
						},

				'context':   {
				}
		}

