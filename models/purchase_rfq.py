# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase Rfq  
# 
# Created: 				30 Oct 2017
# Last updated: 	 	30 Oct 2017

from openerp import models, fields, api




class PurchaseOrderRfq(models.Model):
	
	_inherit = 'purchase.order'

	_name = 'purchase.order.rfq'

	_description = "Purchase Order Rfq"





	state = fields.Selection(
		[
			#('draft', 'Draft PO'),
			('draft', 'Borrador'),
			
			#('sent', 'RFQ Sent'),
			('sent', 'Enviado'),
			
			#('to approve', 'To Approve'),
			#('purchase', 'Purchase Order'),
			
			#('done', 'Done'),
			#('done', 'Completo'),
			('done', 'Cotizado'),


			('cancel', 'Cancelled')
		], 
		string='Status', 
		readonly=True, 
		index=True, 
		copy=False, 
		default='draft', 
		track_visibility='onchange'
	)




	READONLY_STATES = {
		'purchase': [('readonly', True)],
		'done': [('readonly', True)],
		'cancel': [('readonly', True)],
	}


	order_line = fields.One2many(


		#'purchase.order.line', 
		'purchase.order.line.rfq', 

		
		'order_id', 
		string='Order Lines', 
		states=READONLY_STATES, 
		copy=True
	)








	@api.multi
	def action_rfq_send(self):

		print 'jx'
		print 'Action Rfq Send'
		print 

		'''
		This function opens a window to compose an email, with the edi purchase template message loaded by default
		'''
		self.ensure_one()
		ir_model_data = self.env['ir.model.data']
		try:
			if self.env.context.get('send_rfq', False):
				template_id = ir_model_data.get_object_reference('purchase', 'email_template_edi_purchase')[1]
			else:
				template_id = ir_model_data.get_object_reference('purchase', 'email_template_edi_purchase_done')[1]
		except ValueError:
			template_id = False
		try:
			compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
		except ValueError:
			compose_form_id = False
		ctx = dict(self.env.context or {})



		# jx 
		#template_id = 22
		#template_id = 23
		template_id = self.env['mail.template'].search([('name', '=', 'RFQ - Send by Email - jx')]).id




		#'default_model': 'purchase.order',
		ctx.update({

			'default_model': 'purchase.order.rfq',
			
			'default_res_id': self.ids[0],
			'default_use_template': bool(template_id),
			'default_template_id': template_id,
			'default_composition_mode': 'comment',
		})
		return {

			#'name': _('Compose Email'),
		
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form_id, 'form')],
			'view_id': compose_form_id,
			'target': 'new',
			'context': ctx,
		}







