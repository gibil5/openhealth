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

		#('draft', 'Draft PO'),
		('draft', 'Borrador'),




		('validated', 'Validado'),		




		#('sent', 'RFQ Sent'),
		('sent', 'Enviado'),
		


		('to approve', 'To Approve'),		
		#('approved', 'Approved'),
		('approved', 'Aprobado'),




		#('purchase', 'Purchase Order'),
		#('purchase', 'Orden de C/S'),
		('purchase', 'Compra'),
		



		#('sent', 'Enviada'),
		

		#('done', 'Done'),
		('done', 'Completo'),
		

		
		('cancel', 'Cancelled')


		], string='Status', readonly=True, index=True, copy=False, 


		default='draft', 
		#default='purchase', 

		track_visibility='onchange')




	#@api.multi
	#def button_approve(self):

		#self.write({'state': 'purchase'})
	#	self.write({'state': 'approved'})
		
	#	self._create_picking()
	#	return {}



	# Send 
	@api.multi
	def action_validate(self):

		#jx
		self.state = 'validated'










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






	# Send 
	@api.multi
	def action_rfq_send(self):


		#jx
		#self.state = 'sent'
		self.state = 'purchase'



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
		ctx.update({
			'default_model': 'purchase.order',
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


