# -*- coding: utf-8 -*-
#
# 	*** Session Med
#
# Created: 				 24 Feb 2017
#

from openerp import models, fields, api
from datetime import datetime
from . import time_funcs
from . import jrfuncs
from . import session_vars
from . import jxvars


class SessionMed(models.Model):
	
	_name = 'openhealth.session.med'
	
	#_inherit = 'openhealth.session'
	_inherit = ['openhealth.session', 'base_multi_image.owner']






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
			selection=jxvars._ipl_pulse_type,
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




