# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase   
# 
# Created: 				30 Oct 2017
# Last updated: 	 	30 Oct 2017

from openerp import models, fields, api




class PurchaseOrder(models.Model):
	
	_inherit = 'purchase.order'

	#_name = 'purchase.order.rfq'




	state = fields.Selection(
		[
			#('draft', 'Draft PO'),
			('draft', 'Borrador'),
			
			#('sent', 'RFQ Sent'),
			('sent', 'Enviado'),


			#('to approve', 'To Approve'),
			('to approve', 'Validar'),


			#('purchase', 'Purchase Order'),
			('purchase', 'Orden de C/S'),

			






			('bill_ready', 'Factura lista'),

			('bill_paid', 'Factura pagada'),

			('product_received', 'Producto recibido'),




			#('cancel', 'Cancelled')
			('cancel', 'Cancelado'), 

			#('done', 'Done'),
			('done', 'Completo'),
			#('done', 'Cotizado'),
		], 
		string='Status', 
		readonly=True, 
		index=True, 
		copy=False, 
		default='draft', 
		track_visibility='onchange'
	)








	x_type = fields.Selection(

		[	
			#('rfq', 	'Request for quotation'),
			#('po', 		'Purchase order'),
			('rfq', 	'Demanda de Cotización'),
			('po', 		'Orden de C/S'),
		], 
			
		string='Tipo', 

		required=True, 
		#required=False, 

	)

