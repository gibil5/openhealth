# -*- coding: utf-8 -*-
#
# 	Order Line
# 
#

from openerp import models, fields, api



class sale_order_line(models.Model):


	#_name = 'openhealth.order_line'

	_inherit='sale.order.line'



	x_price_vip = fields.Float(
			string="Precio Vip",
		)



