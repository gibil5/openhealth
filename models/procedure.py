# -*- coding: utf-8 -*-
#
# 	Procedure 	
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars




class Procedure(models.Model):
	_name = 'openhealth.procedure'
	_inherit = 'oeh.medical.evaluation'


	name = fields.Char(
			string = 'Procedimiento #',
			)

	vspace = fields.Char(
			' ', 
			readonly=True
			)


	control_ids = fields.One2many(
			'openhealth.control', 
			'procedure', 
			string = "Controles", 
			)
			
			



	# Produc 
	product = fields.Many2one(
			'product.template',

			#domain = [
			#			('type', '=', 'service'),
			#			('x_treatment', '=', _jx_laser_type),
			#		],

			string="Producto",
			required=True, 
			)
	
	laser = fields.Selection(
			selection = jxvars._laser_type_list, 
			string="Láser", 			
			compute='_compute_laser', 
			
			#default='none',
			#required=True, 
			#index=True
			)
	
	#@api.multi
	@api.depends('product')
	def _compute_laser(self):
		for record in self:
			record.laser = record.product.x_treatment 
	


	# Calibration - Co2

	co2_power=fields.Float(
			string="Potencia (W)",
			)
	
	co2_frequency=fields.Float(
			string="Frecuencia (Hz)",
			)
	
	co2_energy=fields.Float(
			string="Energía de pulso (mJ)",
			)
	
	co2_mode_emission=fields.Char(
			string="Modo de emisión",
			)
	
	co2_mode_exposure=fields.Char(
			string="Modo de exposición",
			)
	
	co2_observations=fields.Text(
			string="Observaciones",
			)



	# Calibration - Excilite
	exc_time=fields.Float(
			string="Tiempo de tratamiento",
			)
			
	exc_dose=fields.Char(
			string="Dosis",
			)
			
	exc_dose_selected=fields.Float(
			string="Seleccionado (J/cm2)",
			)

	exc_dose_provided=fields.Float(
			string="Entregado (J/cm2)",
			)

	exc_observations=fields.Text(
			string="Observaciones",
			)



	# Calibration - Ipl
	ipl_fluency=fields.Float(
			string="Fluencia (J/cm2)",
			)
			
	ipl_phototype=fields.Char(
			string="Fototipo",
			)
			
	ipl_lesion_type=fields.Char(
			string="Tipo de lesión",
			)
	
	ipl_lesion_depth=fields.Char(
			string="Profundidad de lesión",
			)
			
	ipl_pulse_type=fields.Selection(
			selection=jxvars._ipl_pulse_type,
			string="Tipo de pulso",
			)
			
	ipl_pulse_duration=fields.Char(
			string="Duración de pulso",
			)
			
	ipl_pulse_time_between=fields.Char(
			string="Tiempo entre pulsos",
			)
			
	ipl_filter=fields.Char(
			string="Filtro",
			)
			
	ipl_spot=fields.Char(
			string="Spot",
			)
			
	ipl_observations=fields.Text(
			string="Observaciones",
			)

	
	
	# Calibration - Ndyag
	ndy_fluency=fields.Float(
			string="Fluencia (J/cm2)",
			)
			
	ndy_phototype=fields.Char(
			string="Fototipo",
			)
			
	ndy_lesion_type=fields.Char(
			string="Tipo de lesión",
			)
			
			
	
	ndy_lesion_depth=fields.Char(
			string="Profundidad de lesión",
			)
			
	ndy_pulse_type=fields.Selection(
			selection=jxvars._ndyag_pulse_type,
			string="Tipo de pulso",
			)
			
	ndy_pulse_duration=fields.Char(
			string="Duración de pulso",
			)
			
			
			
	ndy_pulse_time_between=fields.Char(
			string="Tiempo entre pulsos",
			)
			
	ndy_pulse_spot=fields.Selection(
			selection=jxvars._ndyag_pulse_spot,
			string="Spot",
			)
			
	ndy_observations=fields.Text(
			string="Observaciones",
			)
	
	
	
	
	
	
	
	
	


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
			string = 'Tipo de evaluación',

			#default = 'Pre-arraganged Appointment', 
			default = 'Ambulatory', 
			#default = 'Periodic Control', 

			required=True, 
			)


	evaluation_start_date = fields.Date(
			string = "Fecha", 	
			default = fields.Date.today, 
			required=True, 
			)



	# Motivo de consulta
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 
			selection = jxvars._pathology_list, 
			#default = '', 
			required=True, 
			)





	#------------------------------------- Aggregated ----------------------------------------


	#------------------------------------ Buttons -----------------------------------------

	# Consultation - Quick Self Button  
	# ---------------------------------

	@api.multi
	def open_line_current(self):  

		procedure_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Consultation Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': procedure_id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},

				'context':   {
				}
		}




	# Control 
	# ---------
	@api.multi
	def open_control(self):  

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		
		procedure_id = self.id 


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open control Current',

			'res_model': 'openhealth.control',

			'view_mode': 'form',
			"views": [[False, "form"]],

			'target': 'current',

			'context':   {
				#'search_default_treatment': treatment_id,
				#'default_treatment': treatment_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_chief_complaint': chief_complaint,
				'default_procedure': procedure_id,
				
				
			}
		}

