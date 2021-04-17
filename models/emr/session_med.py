# -*- coding: utf-8 -*-
"""
	*** Session Med
	Created: 			24 Feb 2017
	Last up: 	 		29 mar 2021
"""
from openerp import models, fields, api
from datetime import datetime
from . import session_vars

#from openerp.addons.openhealth.models.commons.libs import commons_lib as lib
from .lib import user 

_fluency = "Fluencia (J/cm2)"
_frequency = "Frecuencia (Hz)"
_lesion_type = "Tipo de lesión"
_lesion_depth = "Profundidad de lesión"
_pulse_type = "Tipo de pulso"
_pulse_duration = "Duración de pulso"
_time_bet = "Tiempo entre pulsos"


class SessionMed(models.Model):	
	"""
	Class Session Med
	Defines the Data Model.
	Should not define the Business Rules. 
	"""	
	_name = 'openhealth.session.med'
	#_inherit = ['openhealth.session', 'base_multi_image.owner']
	_inherit = ['openhealth.session']


# ----------------------------------------------------------- Fields ------------------------------

#------------------------------------------------------ Quick ------------------
	quick_type=fields.Selection(
			selection = [
							('zoom','Zoom'),
							('resolve','Resolve'),
						],
			default="zoom", 
			string="Tipo",
			required=False, 
		)

	quick_manipule_zoom=fields.Selection(
			selection = [
							('532','532'),
							('785','785'),
							('1064','1064'),
						],
			string="Manipulo",
			required=False, 
		)

	quick_manipule_resolve=fields.Selection(
			selection = [
							('532','532'),
							#('785','785'),
							('1064','1064'),
						],
			string="Manipulo",
			required=False, 
		)

	quick_spot=fields.Char(
			string="Spot (mm)",
			required=False, 
		)

	quick_fluency = fields.Char(
			string=_fluency,	
			default='', 
		)

	quick_frequency=fields.Char(
			string=_frequency,
			default='', 
		)

	quick_observations=fields.Text(
			string="Observaciones",
			required=False, 
		)


#------------------------------------------------------ Quick - 2 --------------
	quick_type_2=fields.Selection(
			selection = [
							('zoom','Zoom'),
							('resolve','Resolve'),
						],
			default="zoom", 
			string="Tipo",
			required=False, 
		)

	quick_manipule_zoom_2=fields.Selection(
			selection = [
							('532','532'),
							('785','785'),
							('1064','1064'),
						],
			string="Manipulo",
			required=False, 
		)

	quick_manipule_resolve_2=fields.Selection(
			selection = [
							('532','532'),
							#('785','785'),
							('1064','1064'),
						],
			string="Manipulo",
			required=False, 
		)

	quick_spot_2=fields.Char(
			string="Spot (mm)",
			required=False, 
		)

	quick_fluency_2=fields.Char(
			string=_fluency,	
			default='', 
		)

	quick_frequency_2=fields.Char(
			string=_frequency,
			default='', 
		)

	quick_observations_2=fields.Text(
			string="Observaciones",
			required=False, 
		)


#------------------------------------------------------ Co2 --------------------
	co2_power=fields.Char(
			string="Potencia (W)",
			default='', 
		)
	
	co2_frequency=fields.Char(
			string=_frequency,
			default='', 
		)
	
	co2_energy=fields.Char(
			string="Energía de Pulso (mJ)",
			default='', 
		)

	co2_mode_emission=fields.Selection(
			string="Modo de EMISION",
			selection=session_vars._co2_mode_emission_list, 
		)

	co2_mode_exposure=fields.Selection(
			string="Modo de EXPOSICION",
			selection=session_vars._co2_mode_exposure_list, 
		)
	
	co2_fluency = fields.Char(
			string=_fluency,	
			default='', 
		)

	co2_density  = fields.Char(
			string="Densidad (%)",
			default='', 
		)

	co2_time  = fields.Char(
			string="Tiempo de permanencia (us)",
			default='', 	
		)

	co2_distance = fields.Char(
			string="Distancia (um)",
			default='', 
		)

	co2_observations=fields.Text(
			string="Observaciones",
		)


#------------------------------------------------------ Co2 2 ------------------
	co2_power_2=fields.Char(
			string="Potencia (W)",
			default='', 
		)
	
	co2_frequency_2=fields.Char(
			string=_frequency,
			default='', 
		)
	
	co2_energy_2=fields.Char(
			string="Energía de Pulso (mJ)",
			default='', 
		)

	co2_mode_emission_2=fields.Selection(
			string="Modo de EMISION",
			selection=session_vars._co2_mode_emission_list, 
		)
	
	co2_mode_exposure_2=fields.Selection(
			string="Modo de EXPOSICION",
			selection=session_vars._co2_mode_exposure_list, 
		)
	
	co2_fluency_2=fields.Char(
			string=_fluency,	
			default='', 
		)

	co2_density_2=fields.Char(
			string="Densidad (%)",
			default='', 
		)

	co2_time_2=fields.Char(
			string="Tiempo de permanencia (us)",
			default='', 	
		)

	co2_distance_2=fields.Char(
			string="Distancia (um)",
			default='', 
		)

	co2_observations_2=fields.Text(
			string="Observaciones",
			#default="x",
		)


#------------------------------------------------------ Ipl --------------------
	ipl_fluency=fields.Float(
			string=_fluency,
			)
			
	ipl_phototype=fields.Char(
			string="Fototipo",
			required=False, 
			)
			
	ipl_lesion_type=fields.Char(
			string=_lesion_type,
			required=False, 
			)
	
	ipl_lesion_depth=fields.Char(
			string=_lesion_depth,
			required=False, 
			)
			
	ipl_pulse_type=fields.Selection(
			selection=session_vars._ipl_pulse_type,
			string=_pulse_type,
			required=False, 
			)
			
	ipl_pulse_duration=fields.Char(
			string=_pulse_duration,
			required=False, 
			)
			
	ipl_pulse_time_between=fields.Char(
			string=_time_bet,
			required=False, 
			)
			
	ipl_filter=fields.Char(
			string="Filtro",
			required=False, 
			)
			
	ipl_spot=fields.Char(
			string="Spot",
			required=False, 
			)
			
	ipl_observations=fields.Text(
			string="Observaciones",
			required=False, 
			)

#------------------------------------------------------ Ipl - 2 ----------------
	ipl_fluency_2=fields.Float(
			string=_fluency,
			)
			
	ipl_phototype_2=fields.Char(
			string="Fototipo",
			required=False, 
			)
			
	ipl_lesion_type_2=fields.Char(
			string=_lesion_type,
			required=False, 
			)
	
	ipl_lesion_depth_2=fields.Char(
			string=_lesion_depth,
			required=False, 
			)
			
	ipl_pulse_type_2=fields.Selection(
			selection=session_vars._ipl_pulse_type,
			string=_pulse_type,
			required=False, 
			)
			
	ipl_pulse_duration_2=fields.Char(
			string=_pulse_duration,
			required=False, 
			)
			
	ipl_pulse_time_between_2=fields.Char(
			string=_time_bet,
			required=False, 
			)
			
	ipl_filter_2=fields.Char(
			string="Filtro",
			required=False, 
			)
			
	ipl_spot_2=fields.Char(
			string="Spot",
			required=False, 
			)
			
	ipl_observations_2=fields.Text(
			string="Observaciones",
			required=False, 
			)

#------------------------------------------------------ Excilite ---------------
	exc_time=fields.Float(
			string="Tiempo de tratamiento",
			required=False, 
			)
			
	exc_dose=fields.Char(
			string="Dosis",
			required=False, 
			)
			
	exc_dose_selected=fields.Float(
			string="Seleccionado (J/cm2)",
			required=False, 
			)

	exc_dose_provided=fields.Float(
			string="Entregado (J/cm2)",
			required=False, 
			)

	exc_observations=fields.Text(
			string="Observaciones",
			required=False, 
			)

#------------------------------------------------------ Ndyag ------------------
	ndy_fluency=fields.Float(
			string=_fluency,
			)
			
	ndy_phototype=fields.Char(
			string="Fototipo",
			)
			
	ndy_lesion_type=fields.Char(
			string=_lesion_type,
			)
			
	ndy_lesion_depth=fields.Char(
			string=_lesion_depth,
			)
			
	ndy_pulse_type=fields.Selection(
			selection=session_vars._ndyag_pulse_type,
			string=_pulse_type,
			)
			
	ndy_pulse_duration=fields.Char(
			string=_pulse_duration,
			)

	ndy_pulse_time_between=fields.Char(
			string=_time_bet,
			)
			
	ndy_pulse_spot=fields.Selection(
			selection=session_vars._ndyag_pulse_spot,
			string="Spot",
			)
			
	ndy_observations=fields.Text(
			string="Observaciones",
			)


# ----------------------------------------------------------- Computes ---------
	# Nr Days after Session
	nr_days = fields.Integer(
			'Nr Dias', 

			compute='_compute_nr_days', 
		)
	@api.multi
	def _compute_nr_days(self):
		for record in self:
			#record.nr_days = lib.get_nr_days(self, record.procedure.session_date, record.evaluation_start_date)
			record.nr_days = user.get_nr_days(self, record.procedure.session_date, record.evaluation_start_date)



# ----------------------------------------------------------- Methods ------------------------------

# ----------------------------------------------------------- On changes -------
	# Autofill
	@api.onchange('x_autofill')	
	def _onchange_x_autofill(self):
		if self.x_autofill == True:
			self.co2_mode_emission = 'fractional'
			self.co2_mode_exposure = 'continuous'
			self.co2_observations = 'Cicatriz plana hiperpigmentada en pómulo derecho. Pápulas en pómulos.'
			self.co2_power = 1.5
			self.co2_energy = 150
			self.co2_frequency = 10
			self.co2_fluency = 20
			self.co2_density = 30
			self.co2_time = 40
			self.co2_distance = 50
