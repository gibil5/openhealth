# -*- coding: utf-8 -*-
#
# 	*** Session Med - Co2 - Deprecated
#

# Created: 				 22 Mar 2017
# Last updated: 	 	 22 Feb 2017 

from openerp import models, fields, api
from datetime import datetime



from . import session_vars



class SessionMedCo2(models.Model):
	
	_name = 'openhealth.session.med.co2'
	

	_inherit = 'openhealth.session.med'




	#------------------------------------------------------ Co2 ----------------------------------------------------------


	co2_power=fields.Float(
			string="Potencia (W)",
			)
	
	co2_frequency=fields.Float(
			string="Frecuencia (Hz)",
			)
	
	co2_energy=fields.Float(
			string="Energía de pulso (mJ)",
			)
	
	

	co2_mode_emission=fields.Selection(
			string="Modo de emisión",

			selection=session_vars._co2_mode_emission_list, 
			#default="x",
			)
	
	co2_mode_exposure=fields.Selection(
			string="Modo de exposición",

			selection=session_vars._co2_mode_exposure_list, 
			#default="x",
			)
	
	co2_observations=fields.Text(
			string="Observaciones",
			#default="x",
			)




