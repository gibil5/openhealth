# -*- coding: utf-8 -*-
#
# 	Quotation 
# 

from openerp import models, fields, api
from datetime import datetime





#------------------------------------------------------------------------
class Order(models.Model):
	
	#_name = 'openhealth.order'
	_inherit = 'sale.order'

		
	order_line  = fields.One2many(
			'sale.order.line',
			'order_id',
			domain = [
						('id', '=', '3201'),
			#			('doctor', '=', PHYSICIAN),
			],
	)
	
	
	def get_domain_order_line(self,cr,uid,ids,context=None):

		context = 'laser_co2'
		print 
		print context
		print 

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[('x_treatment', '=', context)])
		return {'domain':{'service':[('id','in',lids)]}}
		
		
	


	name = fields.Char(
			string = 'Order #',
			#string = 'Procedimiento #',
	)
			
	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
	)
			

	patient = fields.Many2one(
			'oeh.medical.patient',
			#string="Patient", 
			string="Paciente", 
			#required=True, 

	        #default='This is the actual model',

			index=True
	)
			
			
			
	#partner_invoice_id = fields.Many2one(
	#		'res.partner',
	#		required=False, 
	#)
	
	#partner_shipping_id = fields.Many2one(
	#		'res.partner',
	#		required=False, 			
	#)
	
	pricelist_id = fields.Many2one(
			'product.pricelist',
			required=False, 					
	)


	currency_id = fields.Many2one(
			'res.currency',
			required=False, 					
	)




	
	