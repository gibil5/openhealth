# -*- coding: utf-8 -*-
#
# 	*** Session Med
#
# Created: 			24 Feb 2017
# Last up: 	 		14 Aug 2018
#
from openerp import models, fields, api
from datetime import datetime
from . import session_vars
#from . import lib
from libs import lib

class SessionMed(models.Model):	
	_name = 'openhealth.session.med'
	#_inherit = 'openhealth.session'
	_inherit = ['openhealth.session', 'base_multi_image.owner']




# ----------------------------------------------------------- Nr Days ------------------------------------------------------

	# Nr Days after Session
	nr_days = fields.Integer(
			'Nr Dias', 

			compute='_compute_nr_days', 
		)

	@api.multi
	#@api.depends('state')
	def _compute_nr_days(self):
		for record in self:
			
			record.nr_days = lib.get_nr_days(self, record.procedure.session_date, record.evaluation_start_date)






#------------------------------------------------------ Quick ----------------------------------------------------------

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
			string="Fluencia (J/cm2)",	
			default='', 
		)

	quick_frequency=fields.Char(
			string="Frecuencia (Hz)",
			default='', 
		)

	quick_observations=fields.Text(
			string="Observaciones",
			required=False, 
		)




#------------------------------------------------------ Quick - 2 ----------------------------------------------------------

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
			string="Fluencia (J/cm2)",	
			default='', 
		)

	quick_frequency_2=fields.Char(
			string="Frecuencia (Hz)",
			default='', 
		)

	quick_observations_2=fields.Text(
			string="Observaciones",
			required=False, 
		)






#------------------------------------------------------ Co2 ----------------------------------------------------------

	co2_power=fields.Char(
			string="Potencia (W)",
			default='', 
		)
	
	co2_frequency=fields.Char(
			string="Frecuencia (Hz)",
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
			string="Fluencia (J/cm2)",	
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
			#default="x",
		)



#------------------------------------------------------ Co2 2 ----------------------------------------------------------

	co2_power_2=fields.Char(
			string="Potencia (W)",
			default='', 
		)
	
	co2_frequency_2=fields.Char(
			string="Frecuencia (Hz)",
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
			string="Fluencia (J/cm2)",	
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





#------------------------------------------------------ Ipl ----------------------------------------------------------

	ipl_fluency=fields.Float(
			string="Fluencia (J/cm2)",
			)
			
	ipl_phototype=fields.Char(
			string="Fototipo",
			required=False, 
			)
			
	ipl_lesion_type=fields.Char(
			string="Tipo de lesión",
			required=False, 
			)
	
	ipl_lesion_depth=fields.Char(
			string="Profundidad de lesión",
			required=False, 
			)
			
	ipl_pulse_type=fields.Selection(
			selection=session_vars._ipl_pulse_type,
			string="Tipo de pulso",
			required=False, 
			)
			
	ipl_pulse_duration=fields.Char(
			string="Duración de pulso",
			required=False, 
			)
			
	ipl_pulse_time_between=fields.Char(
			string="Tiempo entre pulsos",
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

	



#------------------------------------------------------ Ipl - 2 ----------------------------------------------------------

	ipl_fluency_2=fields.Float(
			string="Fluencia (J/cm2)",
			)
			
	ipl_phototype_2=fields.Char(
			string="Fototipo",
			required=False, 
			)
			
	ipl_lesion_type_2=fields.Char(
			string="Tipo de lesión",
			required=False, 
			)
	
	ipl_lesion_depth_2=fields.Char(
			string="Profundidad de lesión",
			required=False, 
			)
			
	ipl_pulse_type_2=fields.Selection(
			selection=session_vars._ipl_pulse_type,
			string="Tipo de pulso",
			required=False, 
			)
			
	ipl_pulse_duration_2=fields.Char(
			string="Duración de pulso",
			required=False, 
			)
			
	ipl_pulse_time_between_2=fields.Char(
			string="Tiempo entre pulsos",
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








#------------------------------------------------------ Excilite ----------------------------------------------------------

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




#------------------------------------------------------ Ndyag ----------------------------------------------------------

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
			selection=session_vars._ndyag_pulse_type,
			string="Tipo de pulso",
			)
			
	ndy_pulse_duration=fields.Char(
			string="Duración de pulso",
			)

	ndy_pulse_time_between=fields.Char(
			string="Tiempo entre pulsos",
			)
			
	ndy_pulse_spot=fields.Selection(
			selection=session_vars._ndyag_pulse_spot,
			string="Spot",
			)
			
	ndy_observations=fields.Text(
			string="Observaciones",
			)



