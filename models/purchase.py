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

	_description = "Purchase Order"



	state = fields.Selection([
		('draft', 'Draft PO'),
		('sent', 'RFQ Sent'),
		('to approve', 'To Approve'),
		('purchase', 'Purchase Order'),
		('done', 'Done'),
		('cancel', 'Cancelled')
		], string='Status', readonly=True, index=True, copy=False, 

		#default='draft', 
		default='purchase', 

		track_visibility='onchange')



	READONLY_STATES = {
		#'purchase': [('readonly', True)],
		'purchase': [('readonly', False)],
		'done': [('readonly', True)],
		'cancel': [('readonly', True)],
	}

	partner_id = fields.Many2one('res.partner', string='Vendor', required=True, 
		
		states=READONLY_STATES, 

		change_default=True, track_visibility='always')


	order_line = fields.One2many('purchase.order.line', 'order_id', string='Order Lines', states=READONLY_STATES, copy=True)


	
