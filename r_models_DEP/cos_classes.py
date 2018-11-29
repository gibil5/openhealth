# -*- coding: utf-8 -*-
#
# 	***  Cos Classes - Deprecated
# 
# Created: 				 1 Nov 2016
# 

from openerp import models, fields, api
from datetime import datetime,tzinfo,timedelta

from . import cosvars
from . import eval_vars
from . import time_funcs
from . import app_vars

from . import prodvars

from . import jrfuncs


# ----------------------------------------------------------- ConsultationCos ------------------------------------------------------

class ConsultationCos(models.Model):
	_inherit = 'openhealth.consultation'
	_name = 'openhealth.consultation.cos'
	


	treatment = fields.Many2one('openhealth.treatment',
			ondelete='cascade', 
			string="Tratamiento",
			required=False, 
		)


	# Open cosmetology
	@api.multi 
	def open_cosmetology(self):
		ret = self.cosmetology.open_myself()
		return ret 



	#x_target = fields.Selection(
	#		string="Target", 
	#		selection = app_vars._target_list, 
	#		default="therapist", 
	#	)


	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Cosmeatra", 	
			)


	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 
			selection = cosvars._chief_complaint_list, 
			required=False, 
			)


	x_antecedents_chirurgical = fields.Text(
			string = '', 
			)


	x_treatments_former = fields.Text(
			string = '', 
			)


	# Number of sessions 
	nr_sessions = fields.Integer(
			string="Número de Sesiones",
	)





# ----------------------------------------------------------- ProcedureCos ------------------------------------------------------

class ProcedureCos(models.Model):	
	_name = 'openhealth.procedure.cos'
	_inherit = 'openhealth.procedure'



	# Relational

	session_ids = fields.One2many(
			'openhealth.session.cos', 			
			'procedure', 
			string = "sessiones", 
		)


	treatment = fields.Many2one(
			'openhealth.treatment',
			required=False, 
		)

	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Cosmeatra", 	
		)


	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 
			selection = cosvars._chief_complaint_list, 
			required=False, 
		)


	# Keys

	key = fields.Char(
			string='key', 			
			default='procedure_cos', 
		)

	model = fields.Char(
			string='model', 
			default='openhealth.session.cos', 
		)

	target = fields.Char(
			string='target', 
			default='therapist', 
		)



	@api.multi
	def create_sessions(self): 
		model = 'openhealth.session.cos'
		ret = procedure_funcs.create_sessions_go(self, model)



	@api.multi
	def create_session_one(self): 

		# Init
		procedure_id = self.id 
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		evaluation_type = 'Session'
		product_id = self.product.id
		treatment_id = False
		cosmetology_id = self.cosmetology.id
		laser = self.laser
		
		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		# Apointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																	('patient', 'like', self.patient.name),		
																	('doctor', 'like', self.doctor.name), 	
																	('x_type', 'like', 'procedure'), 
																], 
																order='appointment_date desc', limit=1)

		appointment_id = appointment.id

		# Create 
		session = self.env['openhealth.session.cos'].create({
																'patient': patient_id,
																'doctor': doctor_id,													
																'chief_complaint': chief_complaint,
																'evaluation_start_date': evaluation_start_date,
																'evaluation_type':evaluation_type,
																'product': product_id,
																'laser': laser,
																'procedure': procedure_id,				
																'appointment': appointment_id,
																'treatment': treatment_id,				
																'cosmetology': cosmetology_id,				
															})
		session_id = session.id 

		# Update
		ret = jrfuncs.update_appointment_go(self, appointment_id, session_id, 'session')


		return {

				# Mandatory 
				'type': 'ir.actions.act_window',
				'name': 'Open session Current',
				# Optional 
				#'res_model': 'openhealth.session',
				'res_model': 'openhealth.session.cos',
				'res_id': session_id,
				'view_mode': 'form',
				"views": [[False, "form"]],
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, }
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						},			
				'context':   {
								'default_patient': patient_id,
								'default_doctor': doctor_id,
								'default_chief_complaint': chief_complaint,
								'default_evaluation_start_date': evaluation_start_date,
								'default_evaluation_type':evaluation_type,
								'default_product': product_id,
								'default_laser': laser,
								'default_procedure': procedure_id,
								'default_appointment': appointment_id,
								'default_treatment': treatment_id,
								'default_cosmetology': cosmetology_id,
							}
				}
	# create_session_one








# ----------------------------------------------------------- SessionCos ------------------------------------------------------

class SessionCos(models.Model):	
	_name = 'openhealth.session.cos'
	_inherit = 'openhealth.session'

	treatment = fields.Many2one(
			'openhealth.treatment',
			required=False, 
		)

	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Cosmeatra", 	
		)

	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 
			selection = cosvars._chief_complaint_list, 
			required=False, 
		)

	procedure = fields.Many2one(
			'openhealth.procedure.cos',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
		)
			
	procedure_applied = fields.Selection(
			string = 'Procedimiento aplicado', 
			selection = cosvars._procedure_list, 
		)

	navel = fields.Float(
			string="Ombligo (cm)", 		
		)

	abdomen_low = fields.Float(
			string="Abdomen superior (cm)", 		
		)

	abdomen_high = fields.Float(
			string="Abdomen inferior (cm)", 		
		)

	config_volume = fields.Float(
			string="Dosificación (ml)", 		
		)

	config_time = fields.Float(
			string="Tiempo (min)", 		
		)

	comments = fields.Text(
			string="Comentarios", 
		)


	@api.multi
	def open_line_current(self):  
		return {
				'type': 'ir.actions.act_window',
				'name': 'Edit Session Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': self.id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
						},
				'context': {
							#'default_co2_power': co2_power,	
						}
			}







# ----------------------------------------------------------- AppointmentCos ------------------------------------------------------

class AppointmentCos(models.Model):
	_inherit = 'oeh.medical.appointment'

	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			string="Cosmiatría",
			ondelete='cascade', 
			required=False, 	
		)

	@api.depends('doctor')
	def _compute_x_doctor_code(self):
		for record in self:
			record.x_doctor_code = app_vars._hash_doctor_code[record.doctor.name]









# ----------------------------------------------------------- ServiceCosmetology ------------------------------------------------------

class ServiceCosmetology(models.Model):
	_name = 'openhealth.service.cosmetology'
	_inherit = 'openhealth.service'
	

	@api.multi 
	def open_cosmetology(self):
		ret = self.cosmetology.open_myself()
		return ret 




	# ----------------------------------------------------------- Canonicals ------------------------------------------------------

	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('x_family', '=', 'cosmetology'),
					],
		)
	
	
	time_1 = fields.Selection(
			selection = prodvars._time_list, 
			string="Tiempo", 
			default='none',	
		)


	# Criosurgery
	cos_dia = fields.Selection(
			selection = cosvars._cos_dia_list, 
			default='none',
			string="Rostro (Limpieza facial profunda)",
		)


	# Carboxytherapy 
	cos_car_fac = fields.Selection(
			selection = cosvars._cos_car_list, 
			default='none',	
			string="Rostro",
			)

	cos_car_bod = fields.Selection(
			selection = cosvars._cos_car_list, 
			default='none',	
			string="Cuerpo",
			)

	# Laser Triactive
	cos_tri_fac = fields.Selection(
			selection = cosvars._cos_tri_list, 
			default='none',	
			string="Rostro, Papada y Cuello",
			)

	cos_tri_bod = fields.Selection(
			selection = cosvars._cos_tri_list, 
			default='none',	
			string="Todo Cuerpo",
			)


	# ----------------------------------------------------------- On Changes ------------------------------------------------------

	# Diamond
	@api.onchange('cos_dia')
	def _onchange_cos_dia(self):
		
		if self.cos_dia != 'none':
			self.cos_dia = self.clear_all_med(self.cos_dia)
			self.x_treatment = 'diamond_tip'
			self.zone = 'face'
			self.pathology = 'deep_face_cleansing'	
			self.time = '30 min'
			self.sessions = self.cos_dia

			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_sessions', '=', self.sessions),
										]},
			}


	# Carboxytherapy - Face
	@api.onchange('cos_car_fac')
	def _onchange_cos_car_fac(self):
		
		if self.cos_car_fac != 'none':
			self.cos_car_fac = self.clear_all_med(self.cos_car_fac)
			self.x_treatment = 'carboxytherapy'
			self.zone = 'face'
			self.pathology = 'rejuvenation_face'	
			self.time = '30 min'
			self.sessions = self.cos_car_fac

			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_zone', '=', self.zone),
										('x_sessions', '=', self.sessions),
										]},
			}



	# Carboxytherapy - Body
	@api.onchange('cos_car_bod')
	def _onchange_cos_car_bod(self):
		
		if self.cos_car_bod != 'none':
			self.cos_car_bod = self.clear_all_med(self.cos_car_bod)
			self.x_treatment = 'carboxytherapy'
			self.zone = 'body'
			self.pathology = 'rejuvenation_face'	
			self.time = '30 min'
			self.sessions = self.cos_car_bod


			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_zone', '=', self.zone),
										('x_sessions', '=', self.sessions),

										]},
			}




	# Laser Triactive - Face
	@api.onchange('cos_tri_fac')
	def _onchange_cos_tri_fac(self):
		
		if self.cos_tri_fac != 'none':
			#print 
			#print 'cos_tri_fac'
			#print 

			self.cos_tri_fac = self.clear_all_med(self.cos_tri_fac)
			#self.clear_local()


			self.x_treatment = 'triactive_carboxytherapy'

			self.zone = 'face_doublechin_neck'

			self.pathology = 'reaffirmation'
								
			self.time = '30 min'



			self.sessions = self.cos_tri_fac


			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
				
										('x_zone', '=', self.zone),

										('x_sessions', '=', self.sessions),
										]},
			}






	# Laser Triactive - Body
	@api.onchange('cos_tri_bod')
	def _onchange_cos_tri_bod(self):
		
		if self.cos_tri_bod != 'none':
			self.cos_tri_bod = self.clear_all_med(self.cos_tri_bod)
			self.x_treatment = 'triactive_carboxytherapy_reductionchamber'
			self.zone = 'body_all'
			self.pathology = 'reduction_weight_measures'
			self.time = '30 min'
			self.sessions = self.cos_tri_bod

			return {
						'domain': {'service': [
												('x_treatment', '=', self.x_treatment),				
												('x_zone', '=', self.zone),
												('x_sessions', '=', self.sessions),
										]},
			}




	# ----------------------------------------------------------- Functions ------------------------------------------------------

	def clear_all_med(self,token):		
		#self.clear_commons()
		self.clear_local_cos()
		return token

	@api.multi
	def clear_local_cos(self):		
		self.cos_dia = 'none'
		self.cos_car = 'none'
		self.cos_tri = 'none'

		
