# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase   
# 
# Created: 				30 Oct 2017
# Last updated: 	 	14 Nov 2017

from openerp import models, fields, api




class PurchaseOrder(models.Model):
	
	_inherit = 'purchase.order'
	_description = "Purchase Order"




# New

	@api.multi
	def remove_myself(self):  

		self.state = 'cancel'
		self.unlink()



	state = fields.Selection([

		
		#('draft', 'Draft PO'),
		('draft', 'Draft'),
		


		('validated', 'Validado'),



		#('sent', 'RFQ Sent'),
		('sent', 'Enviado'),
		

		('to approve', 'To Approve'),
		

		#('purchase', 'Purchase Order'),
		('purchase', 'Orden de C/S'),
		

		#('done', 'Done'),
		('done', 'Completo'),
		

		#('cancel', 'Cancelled')
		('cancel', 'Cancelado')


		], string='Status', readonly=True, index=True, copy=False, default='draft', track_visibility='onchange')





	@api.multi
	def button_validate(self):

		self.write({'state': 'validated'})
		
		return {}



