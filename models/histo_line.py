# -*- coding: utf-8 -*-
#
# 	Histo Line
# 
# Created: 				16 May 2018
#

from openerp import models, fields, api

class HistoLine(models.Model):
	
	_name = 'openhealth.histo.line'

	_order = 'idx asc'




# ----------------------------------------------------------- Relational ------------------------------------------------------

	marketing_id = fields.Many2one(
			'openhealth.marketing'
		)





# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Bin 
	x_bin = fields.Char(
			'Bin', 
			#'Edades', 
		)


	# Bin name 
	x_bin_name = fields.Char(
			#'Bin', 
			'Edades', 
		)



	# Idx 
	idx = fields.Integer(
			'Idx', 
		)


	# Count 
	count = fields.Integer(
			#'Nr', 
			'Cantidad', 
		)


	# Total 
	total = fields.Integer(
			'Total', 
		)


	# Percentage 
	percentage = fields.Float(
			'Porcentaje', 
			digits=(16,1), 
		)





# ----------------------------------------------------------- Actions ------------------------------------------------------

	_h_bin_names = {
						False:		'0-4',
						'5':		'5-9',
						'10':		'10-14',
						'15':		'15-20',
						'20':		'20-24',
						'25':		'25-29',
						'30':		'30-34',
						'35':		'35-39',
						'40':		'40-44',
						'45':		'45-49',
						'50':		'50-54',
						'55':		'55-59',
						'60':		'60-64',
						'65':		'65 o más',
					}



	# Update Fields
	@api.multi
	def update_fields(self):  

		#print
		#print 'Update Fields - Histo'

		if self.total != 0: 
			self.percentage = (  float(self.count) / float(self.total)  ) * 100


		# Bin Name
		#print self.x_bin
		if self.x_bin in self._h_bin_names: 
			self.x_bin_name = self._h_bin_names[self.x_bin]




