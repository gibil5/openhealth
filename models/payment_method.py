# -*- coding: utf-8 -*-
#
# 	payment_method 
# 
#

from openerp import models, fields, api

import ord_vars


class payment_method(models.Model):
	
	_name = 'openhealth.payment_method'

	#_inherit='openhealth.sale_document'



	name = fields.Char(
			#string="Medio de Pago", 
			string="Nombre", 
			required=True, 
		)


	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			required=True, 
		)



	subtotal = fields.Float(
			string = 'Sub-total', 
			required=True, 
		)



	method = fields.Selection(
			string="Medio", 
			selection = ord_vars._payment_method_list, 			
			required=True, 
		)

	code = fields.Char(
			string="Codigo", 
			#required=True, 
		)




	# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Create 
	@api.model
	def create(self,vals):

		print 
		print 'jx'
		print 'Payment Method - Create Override'
		print 
		print vals
		print 
	


		#order = vals['order']
		#nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', order),]) 
		#name = 'MP-' + str(nr_pm + 1)
		#vals['name'] = name



		#Write your logic here
		res = super(payment_method, self).create(vals)
		#Write your logic here

		return res

