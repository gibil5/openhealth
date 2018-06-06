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





	# Counts
	count = fields.Integer(
			#'Cantidad', 
			'Total', 
		)

	count_m = fields.Integer(
			'Hombres', 
		)

	count_f = fields.Integer(
			'Mujeres', 
		)




	# Percentages
	percentage = fields.Float(
			#'Porcentaje', 
			'Pacientes %', 
			digits=(16,1), 
		)

	percentage_m = fields.Float(
			'Hombres %', 
			digits=(16,1), 
		)

	percentage_f = fields.Float(
			'Mujeres %', 
			digits=(16,1), 
		)








	# Totals
	total = fields.Integer(
			'Total Pacientes', 
		)

	total_m = fields.Integer(
			'Total Hombres', 
		)

	total_f = fields.Integer(
			'Total Mujeres', 
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


		# Percentages
		if self.total != 0: 
			self.percentage = (  float(self.count) / float(self.total)  ) * 100

		if self.total_m != 0: 
			self.percentage_m = (  float(self.count_m) / float(self.total_m)  ) * 100

		if self.total_f != 0: 
			self.percentage_f = (  float(self.count_f) / float(self.total_f)  ) * 100



		# Bin Name
		#print self.x_bin
		if self.x_bin in self._h_bin_names: 
			self.x_bin_name = self._h_bin_names[self.x_bin]




