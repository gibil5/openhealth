# -*- coding: utf-8 -*-
#
# 	Electronic Order 
# 
# 	Created: 			13 Sep 2018
# 	Last updated: 		13 Sep 2018
#
from openerp import models, fields, api

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
		)


	# Amount total - Net 
	amount_total_net = fields.Float(
			string = "Net",
		)

	# Amount total - Tax 
	amount_total_tax = fields.Float(
			string = "Tax",
		)

