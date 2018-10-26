# -*- coding: utf-8 -*-
#
# 		*** RES Company 
# 
# 		Created: 			25 Oct 2016
# 		Last updated: 	 	25 Oct 2018 
#
#from openerp.osv import fields, osv
from openerp import models, fields, api


#class res_company(osv.osv):
class res_company(models.Model):
	_inherit = 'res.company'
	#_name = "res.company"
	#_description = 'Companies'
	#_order = 'name'



# ----------------------------------------------------------- Address -----------------------------	
	# Address
	x_address = fields.Char(
			"Dirección",

			compute='_compute_x_address', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_address(self):
		for record in self:
			if record.street != False and record.street2 != False and record.city != False:
				record.x_address = record.street.title() + ' ' + record.street2.title() + ' - ' + record.city.title()




	# Warning
	x_warning = fields.Text(
			'Condiciones de Venta', 
		)



