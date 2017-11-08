# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase   
# 
# Created: 				30 Oct 2017
# Last updated: 	 	 8 Nov 2017

from openerp import models, fields, api




class PurchaseOrder(models.Model):
	
	_inherit = 'purchase.order'
	_description = "Purchase Order"




# New


	# Cancel Reason 
	x_cancel_reason = fields.Text(

		'Motivo de rechazo', 
	)







# Primitives 

	# State 
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
		

		#('done', 'Done'),
		#('done', 'Completo'),
		('done', 'Entregado'),
		


		#('cancel', 'Cancelled')
		('cancel', 'Rechazado')


		], string='Status', readonly=True, index=True, copy=False, 


		default='draft', 
		#default='purchase', 

		track_visibility='onchange', 
	)







	# Validate Button  
	@api.multi
	def action_validate(self):
		#jx
		self.state = 'validated'




	# Send Action 
	@api.multi
	def action_rfq_send(self):

		#jx Code
		#self.state = 'sent'
		self.state = 'purchase'



		# Original 
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


