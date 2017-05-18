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
			string="Pagos", 
			
			#required=True, 
			#readonly=True, 

			compute='_compute_name', 
		)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'PA-' + str(record.id) 





	# Open Order
	@api.multi 
	def open_order(self):

		print 
		print 'Open order'


		ret = self.order.open_myself()

		return ret 
	# open_order






	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			required=True, 
			readonly=True, 
		)














	vspace = fields.Char(
			' ', 
			readonly=True
			)




	total = fields.Float(
			string = 'Total', 
			required=True, 
		)

	pm_total = fields.Float(
			string = 'Pm Total', 
			required=True, 
		)






	balance = fields.Float(
			string = 'Saldo', 
			required=True, 
			#compute="_compute_balance",
			readonly=True, 
		)

	#@api.multi
	#@api.depends('total', 'pm_total')
	#def _compute_balance(self):
	#	for record in self:
	#		record.balance = self.total - (self.pm_total + self.subtotal)










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

