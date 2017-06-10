# -*- coding: utf-8 -*-
#
# 	payment_method_line
# 
#

from openerp import models, fields, api

import ord_vars


class payment_method_line(models.Model):
	
	_name = 'openhealth.payment_method_line'




	# Test
	@api.multi 
	def x_test(self):
		print
		print 'X Test'

		print id

		#ctr = 5
		#self.name = 'Pago - ' + str(ctr)
		#self.name = 'Pago - '

		#for record in self:
		#	print record.name
		#	print record.payment_method
		
		print 





	# Name 
	name = fields.Char(
			#string="Medio de Pago", 
			string="Pago", 

			required=True, 
			#required=False, 
			
			#readonly=True, 
			#compute="_compute_name",
		)

	@api.multi
	#@api.depends('date_order')
	def _compute_name(self):
		print
		print 'PML - compute name'
		print 

		for record in self:

			ctr = 0

			#pm = record.env['openhealth.payment_method'].search([
			#															('id','=', record.payment_method)[0].id,
			#													],
																#order='appointment_date desc',
			#													limit=1,)
			#for line in pm.pm_line_ids:
			#	ctr = ctr+1

			#print ctr
			record.name = 'Pago - ' + str(ctr)

		print 




	# Open Order
	@api.multi 
	def open_pm(self):

		print 
		print 'Open Pm'



		payment_method_id = self.payment_method.id  

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Order Current',


			# Window action 
			'res_model': 'openhealth.payment_method',
			'res_id': payment_method_id,


			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',


			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 

			'flags': {
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},			

			'context':   {

			}
		}


	# open_pm











	payment_method = fields.Many2one(

			'openhealth.payment_method',

			string="Módulo de Pago",

			ondelete='cascade', 

			required=True, 
			#required=False, 
			
			#readonly=True, 
		)




	vspace = fields.Char(
			' ', 
			readonly=True
			)




	method = fields.Selection(
			string="Medio", 

			selection = ord_vars._payment_method_list, 			

			default="cash", 

			required=True, 
		)




	subtotal = fields.Float(
			string = 'Subtotal', 

			#default=self.balance, 

			required=True, 
		)



	#@api.onchange('subtotal')
	#def _onchange_subtotal(self):
	#	self.balance = self.total - (self.pm_total + self.subtotal)




	#code = fields.Char(
	#		string="Codigo", 
			#required=True, 
	#	)





# ----------------------------------------------------------- CRUD ------------------------------------------------------

# Create 
	@api.model
	def create(self,vals):
		print 
		print 'PML - Create - Override'
		print 
		print vals
		print 
	
	
		#Write your logic here
		res = super(payment_method_line, self).create(vals)
		#Write your logic here
		return res



# Write 
	@api.multi
	def write(self,vals):

		print 
		print 'PML - Write - Override'
		print 
		print vals

		res = super(payment_method_line, self).write(vals)
		#Write your logic here
		print 
		print 

		return res




