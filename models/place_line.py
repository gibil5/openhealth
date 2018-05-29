# -*- coding: utf-8 -*-
#
# 	Place
# 
# Created: 				18 May 2018
#

from openerp import models, fields, api


class PlaceLine(models.Model):
	
	#_inherit = 'openhealth.place.line'

	_name = 'openhealth.place.line'

	#_order = 'name asc'
	#_order = 'count desc'
	_order = 'x_count desc'



	# ----------------------------------------------------------- Relational ------------------------------------------------------
	marketing_id = fields.Many2one(
			'openhealth.marketing'
		)




	# ----------------------------------------------------------- Primitive ------------------------------------------------------
	name = fields.Char(
			'Nombre',
		)

	x_count = fields.Integer(
			'Nr',
		)





# ----------------------------------------------------------- Marketing ------------------------------------------------------

class CountryLine(models.Model):	

	_inherit = 'openhealth.place.line'
	
	_name = 'openhealth.country.line'
	
	#_order = 'idx asc'


class CityLine(models.Model):	
	
	_inherit = 'openhealth.place.line'
	
	_name = 'openhealth.city.line'
	
	#_order = 'idx asc'


class DistrictLine(models.Model):	
	
	_inherit = 'openhealth.place.line'
	
	_name = 'openhealth.district.line'
	
	#_order = 'idx asc'







