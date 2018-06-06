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

	#_order = 'x_count desc'
	#_order = 'count desc'
	_order = 'name asc'



	# ----------------------------------------------------------- Relational ------------------------------------------------------
	marketing_id = fields.Many2one(
			'openhealth.marketing'
		)




	# ----------------------------------------------------------- Primitive ------------------------------------------------------
	name = fields.Char(
			'Nombre',
		)



	sector = fields.Char(
			'Sector',
		)




	#x_count = fields.Integer(
	count = fields.Integer(
			'Nr',
		)


	count_c = fields.Char(
			'Nr c',
		)



	code = fields.Integer(
			'Código',
		)




	# ----------------------------------------------------------- Actions ------------------------------------------------------

	@api.multi
	def update_fields(self):  

		#print
		#print 'Update Fields - Place'

		if self.count != 0:
			self.count_c = str(self.count)



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







