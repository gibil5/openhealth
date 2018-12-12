# -*- coding: utf-8 -*-
#
# 	Media Line
# 
# Created: 				6 June 2018
#

from openerp import models, fields, api

class MediaLine(models.Model):
	
	_name = 'openhealth.media.line'

	_order = 'idx asc'





# ----------------------------------------------------------- Relational ------------------------------------------------------

	marketing_id = fields.Many2one(
			'openhealth.marketing'
		)




# ----------------------------------------------------------- Primitive ------------------------------------------------------

	# Name 
	name = fields.Char( 
			'Media', 
		)


	# Name 
	name_sp = fields.Char( 
			'Medio', 
		)



	# Idx 
	idx = fields.Integer(
			'Idx', 
		)



	# Count
	count = fields.Integer(
			#'Cantidad', 
			'Pacientes', 
		)



	# Total
	total = fields.Integer(
			'Total Pacientes', 
		)


	# Percentage
	percentage = fields.Float(
			#'Porcentaje', 
			'Pacientes %', 
			digits=(16,1), 
		)





	_h_name = {
						#False:		'0-4',
					
						'none':			'Ninguno',
					
						'recommendation':		'Recomendación',

						'tv':			'Tv',

						'internet':		'Internet',

						'website':		'Sitio web',

						'mail':			'Mail',

						'undefined':	'Indefinido',
					}



# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  
		#print
		#print 'Update Fields - Histo'

		# Percentages
		if self.total != 0: 
			self.percentage = (  float(self.count) / float(self.total)  ) * 100


		# Name
		if self.name in self._h_name: 
			self.name_sp = self._h_name[self.name]





