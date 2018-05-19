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

	account_id = fields.Many2one(
			'openhealth.account.contasis'
		)





# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Bin 
	x_bin = fields.Char(
			'Bin', 
		)


	# Idx 
	idx = fields.Integer(
			'Idx', 
		)


	# Count 
	count = fields.Integer(
			'Nr', 
		)


	# Total 
	total = fields.Integer(
			'Total', 
		)


	# Percentage 
	percentage = fields.Float(
			'Porcentaje', 
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  

		#print
		#print 'Update Fields - Histo'

		if self.total != 0: 
			self.percentage = (  float(self.count) / float(self.total)  ) * 100


