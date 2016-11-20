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



	#products = fields.One2many(
	#products = fields.Many2one(
	#		'product.template',
	#		)
			
			
	#x_nex = fields.Char(
	#	default='nex',
	#)





	#state_changes = fields.Char(
	#		default='a',
	#		compute='_compute_state_changes', 
	#		)

	#@api.depends('state')	
	#def _compute_state_changes(self):
	#	print
	#	print 'jx'
	#	for record in self:
	#		record.state_changes = 'b'
	#		print record.state_changes










	#_state_list = [
    #     			('draft', 'Quotation'),
	#				('sent', 'Quotation Sent'),
	#				('sale', 'Sale Order'),
	#				('done', 'Done'),
	#				('cancel', 'Cancelled'),
    #     	   ]

	
	


	# State changes
	#@api.onchange('state')
	#def _onchange_state(self):
		
	#	print 
	#	print 'jx'
	#	print 'Order - State change'
	#	print self.state
		
		#self.x_state = 'b'
		
	#	name = 'name',

	#	patient = self.patient
		
	#	print patient
		
		#return {
		#	'warning': {
		#		'title': "Order - State",
		#		'message': self.state + ' ' + patient.name,
		#}}
		
		
		
	#	print self.consultation.treatment.procedure_ids
		
	#	self.consultation.treatment.procedure_ids.create({
			
	#										'name': 'name',
	#										'patient': patient.name,
											
											#'product_id': se.service.id,
											#'product_uom': se.service.uom_id.id,
											#'order_id': order_id,
											#'order_id': 33,
		#									'order_id': consultation_id,
	#									})

		
	#	print 
		

		
# 13 Nov 2016

			#print 'copy'
			#if not self.x_copy_created:			
			#if not self.x_copy_created  and  self.state == 'draft':			
				#ret = self.copy({
				#				#'state':'sale',
				#				'state':'sent',
				#			})	
				#self.x_copy_created = True
			#print ret 

	
	

# 19 Nov 2016

	# Price Subtotal 

	#x_price_subtotal_wigv = fields.Float(
	#		string="Subtotal",

	#		compute="_compute_x_price_subtotal_wigv",
	#	)

	#@api.multi
	#@api.depends('price_subtotal')
	
	#def _compute_x_price_subtotal_wigv(self):
	#	for record in self:
	#		record.x_price_subtotal_wigv = math.ceil(record.price_subtotal * 118.0)








	#x_mark = fields.Char(
	#	default='mark',
	#)

	#product_id = fields.Many2one(
	#	'product.product',
	#	'order_line',
	#	domain = [
	#				('type', '=', 'service'),
	#				('x_treatment', '=', 'laser_co2'),
	#			],

	#	)


