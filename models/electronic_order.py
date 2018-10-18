# -*- coding: utf-8 -*-
#
# 	Electronic Order 
# 
# 	Created: 			13 Sep 2018
# 	Last updated: 		13 Sep 2018
#
from openerp import models, fields, api
#import openerp.addons.decimal_precision as dp
import lib 

class electronic_order(models.Model):

	_name = 'openhealth.electronic.order'

	_inherit='openhealth.management.order.line'

	_description = "Openhealth Electronic Order"

	_order = 'serial_nr asc'




# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Lines 
	electronic_line_ids = fields.One2many(
			'openhealth.electronic.line', 
			'electronic_order_id',
		)



# ----------------------------------------------------------- Fields ------------------------------------------------------

	# Export Date 
	export_date = fields.Char(
			'Export Date',
			#default="2018_10_14", 

			compute='_compute_export_date', 
		)

	@api.multi
	#@api.depends('x_msg')
	def _compute_export_date(self):
		print 
		print 'Compute Export Date'

		for record in self:			

			#record.export_date = record.x_date_created 
			record.export_date = lib.correct_date(record.x_date_created).split()[0]





	# Id 
	id_serial_nr = fields.Char(
			'Id Serial Nr', 
		)



	# Counter Value 
	counter_value = fields.Integer(
			string="Contador", 
			#default=55, 
		)

	# Delta 
	delta = fields.Integer(
			'Delta',
		)




	# Amount total 
	amount_total = fields.Float(
			string = "Total",
			digits=(16,2), 
		)


	# Amount total - Net 
	amount_total_net = fields.Float(
			string = "Net",
			digits=(16,2), 
		)

	# Amount total - Tax 
	amount_total_tax = fields.Float(
			string = "Tax",
			digits=(16,2), 
		)



