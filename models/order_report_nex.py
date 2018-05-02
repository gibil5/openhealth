# -*- coding: utf-8 -*-
#
# 	Order Report Nex
# 
#
from openerp import models, fields, api

import ord_vars


class order_report_nex(models.Model):

	_name = 'openhealth.order.report.nex'

	_description = "Openhealth Order Report Nex"








# ----------------------------------------------------------- Critical ------------------------------------------------------
	# Lines
	order_line_ids = fields.One2many(
		
			#'openhealth.order.report.nex.line', 
			'openhealth.report.order_line', 

			'order_report_nex_id', 
			string="Estado de cuenta",
		)







# ----------------------------------------------------------- Nex ------------------------------------------------------


	name = fields.Char()


	# Partner 
	partner_id = fields.Many2one(
			'res.partner',
			string = "Cliente", 	
			ondelete='cascade', 			
			required=False, 
		)













	# Total 
	amount_total_report = fields.Float(
			'Total S/.', 
			default='0', 

			compute='_compute_amount_total_report', 
		)

	@api.multi
	def _compute_amount_total_report(self):
		for record in self:		
			total = 0 

			for line in record.order_line_ids: 
				total = total + line.price_subtotal 
			
			record.amount_total_report = total






# ----------------------------------------------------------- Actions ------------------------------------------------------


	# Update 
	@api.multi 
	def update_order_report(self):

		print
		print 'Update'



		# Clean 
		self.order_line_ids.unlink()



		# Init 
		partner_id = self.partner_id.name

		orders = self.env['sale.order'].search([
															('partner_id', '=', partner_id),			
															('state', '=', 'sale'),			
													],
													#order='start_date desc',
													#limit=1,
												)
		print orders
		print 


		# Loop Create
		for order in orders: 
			#print 
			#print order.name 


			for line in order.order_line: 
				
				#print line.product_id
				#print line.name
				#print line.price_subtotal
				#print line.price_total
				#print line.price_unit				
				#print line.product_uom_qty
				#print line.create_date
				#print 


				ret = self.order_line_ids.create({
															'name': line.name,

															'product_id': line.product_id.id,

															'price_unit': line.price_unit,
															
															'product_uom_qty': line.product_uom_qty, 

															'order_report_nex_id': self.id,


															'x_date_created': line.create_date,															
													})

				#print ret 
				#print ret.price_subtotal
				#print ret.price_total
				#print ret.price_unit				
				#print ret.product_uom_qty
				#print 


