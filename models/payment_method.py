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








	# Consistency 

	#subtotal = fields.Float(
	#		string = 'Sub-total', 
	#		required=True, 
	#	)

	#method = fields.Selection(
	#		string="Medio", 
	#		selection = ord_vars._payment_method_list, 			
	#		required=True, 
	#	)




















	# state 
	_state_list = [
					('draft', 'En curso'),
					('done', 'Completo'),
					#('cancel', 'Cancelled'),
				]


	state = fields.Selection(

			selection = _state_list, 	

			string='Estado',	

			#readonly=False,
			default='draft',

			compute="_compute_state",
			)


	@api.multi
	@api.depends('state')

	def _compute_state(self):
		for record in self:

			print 'Compute State'

			record.state = 'draft'


			#if	record.env['openhealth.sale_document'].search_count([('order','=', record.id),]):
			#	record.state = 'proof'

			if record.balance == 0.0:
				record.state = 'done'


		print record.state
		print 





	# Create Pm
	@api.multi 
	def create_pm_line(self):

		print 
		print 'Create Pm Line'



		#name = 'Pago #'
		nr_pm = self.env['openhealth.payment_method_line'].search_count([('payment_method','=', self.id),]) 
		name = 'Pago # ' + str(nr_pm + 1)



		method = 'cash'
		
		balance = self.balance

		payment_method_id = self.id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Line Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.payment_method_line',				
				#'res_id': payment_method_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {

							'default_payment_method': payment_method_id,					

							'default_name': name,
							'default_method': method,
							'default_subtotal': balance,


							#'default_payment_method_id', payment_method_id,


							#'default_order': self.id,
							
							#'default_total': self.x_amount_total,
							#'default_pm_total': self.pm_total,
						}
				}

		#ret = self.order.open_myself()
		#return ret 

	# open_order







	# Payment Method 
	pm_line_ids = fields.One2many(

			'openhealth.payment_method_line',

			'payment_method',		
			string="Pago #", 
		)







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
			string = 'Total a pagar', 
			required=True, 
		)



	pm_total = fields.Float(
			string = 'Total pagado', 
			required=True, 

			default=0, 
			compute="_compute_pm_total",
		)

	@api.multi
	#@api.depends('total', 'pm_total')
	def _compute_pm_total(self):
		for record in self:

			pm_total = 0

			for line in record.pm_line_ids:
				s = line.subtotal
				pm_total = pm_total + s

			record.pm_total = record.pm_total + pm_total








	balance = fields.Float(
			string = 'Saldo', 
			required=True, 
			readonly=True, 

			compute="_compute_balance",
		)

	@api.multi
	#@api.depends('total', 'pm_total')
	def _compute_balance(self):

		print 'Compute Balance'
		
		for record in self:
			record.balance = record.total - record.pm_total 

			#if record.balance == 0.0:
			#if record.total == record.pm_total:
			#	print 'Gotcha'
			#	record.state = 'done'
			#	print record.state  

		print 





	# On change - Balance
	#@api.onchange('balance')
	
	#def _onchange_balance(self):
		
	#	print 'Onchange Balance'

		#if self.balance == 0.0:
	#	if self.total == self.pm_total:
	#		print 'Gotcha'
	#		self.state = 'done'
	#		print self.state  





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

