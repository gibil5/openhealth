# -*- coding: utf-8 -*-
#
# 	Management Line 
# 
# Created: 				18 May 2018
#

from openerp import models, fields, api


class ManagementLine(models.Model):
	
	#_inherit = 'openhealth.mgt.line'

	_name = 'openhealth.mgt.line'

	_order = 'x_count desc'



	# ----------------------------------------------------------- Relational ------------------------------------------------------

	management_id = fields.Many2one(
			'openhealth.management'
		)




	# ----------------------------------------------------------- Primitive ------------------------------------------------------
	name = fields.Char(
			'Nombre',
		)


	x_count = fields.Integer(
			'Nr',
		)


	amount = fields.Float(
			'Monto',
			digits=(16,1), 
		)




# ----------------------------------------------------------- Management ------------------------------------------------------

class DoctorLine(models.Model):	

	_inherit = 'openhealth.mgt.line'
	
	_name = 'openhealth.mgt.doctor.line'
	
	#_order = 'idx asc'



class FamilyLine(models.Model):	

	_inherit = 'openhealth.mgt.line'
	
	_name = 'openhealth.mgt.family.line'
	
	#_order = 'idx asc'



class SubFamilyLine(models.Model):	

	_inherit = 'openhealth.mgt.line'
	
	_name = 'openhealth.mgt.sub_family.line'
	
	#_order = 'idx asc'



