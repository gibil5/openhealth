# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Patient Legacy 
# 

# Created: 				23 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api
from datetime import datetime



class PatientLegacy(models.Model):


	#_order = 'write_date desc'

	_description = 'Patient Legacy'



	_inherit = 'openhealth.legacy'

	#_name = 'openhealth.patient.legacy'
	_name = 'openhealth.legacy.patient'







# ----------------------------------------------------------- Primitives ------------------------------------------------------


	CODIGOhistoria = fields.Char()

	NombreCompleto = fields.Char()

	NumeroDocumento = fields.Char()

	FechaRegistro = fields.Char()


