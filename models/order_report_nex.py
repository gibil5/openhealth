# -*- coding: utf-8 -*-
#
# 	Order Report Nex
# 
# Created: 				14 Nov 2017
# Last updated: 	 	22 Jun 2018
#

from openerp import models, fields, api
import ord_vars

class order_report_nex(models.Model):

	_name = 'openhealth.order.report.nex'

	_description = "Openhealth Order Report Nex"




# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Lines
	order_line_ids = fields.One2many(		
			'openhealth.report.order_line', 
			'order_report_nex_id', 
			string="Estado de cuenta",
		)



# ----------------------------------------------------------- Canonical ------------------------------------------------------

	# Name 
	name = fields.Char()


	# Partner 
	partner_id = fields.Many2one(
			'res.partner',
			string = "Cliente", 	
			ondelete='cascade', 			
			required=False, 
		)


	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			#ondelete='cascade', 			
			required=False, 
		)


	# Total Sale
	amount_total_sale = fields.Float(
			'Total Ventas S/.', 
			default='0', 
		)


	# Total Budget 
	amount_total_budget = fields.Float(
			#'Total Presupuestos S/.', 
			'Presupuestos S/.', 
			default='0', 
		)


	# Total 
	amount_total_report = fields.Float(
			'Total S/.', 
			default='0', 
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Totals
	@api.multi 
	def update_totals(self):

		# Init 
		total = 0 
		total_sale = 0 
		total_budget = 0 

		for line in self.order_line_ids: 			
			total = total + line.price_subtotal 
			if line.state == 'sale': 
				total_sale = total_sale + line.price_subtotal 
			elif line.state == 'draft': 
				total_budget = total_budget + line.price_subtotal 

		self.amount_total_report = total
		self.amount_total_sale = total_sale
		self.amount_total_budget = total_budget





# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update 
	@api.multi 
	def update_order_report(self):

		# Clean 
		self.order_line_ids.unlink()

		# Init 
		partner_id = self.partner_id.name
		patient_name = self.patient.name
		orders = self.env['sale.order'].search([
															#('state', '=', 'sale'),			
															#('partner_id', '=', partner_id),
															('patient', '=', patient_name),
													],
													#order='start_date desc',
													#limit=1,
												)
		# Loop - Create Lines 
		for order in orders: 

			for line in order.order_line: 
				
				ret = self.order_line_ids.create({
															'name': line.name,
															'product_id': line.product_id.id,
															'price_unit': line.price_unit,
															'product_uom_qty': line.product_uom_qty, 
															'x_date_created': line.create_date,															
															'state': order.state,

															'order_report_nex_id': self.id,
													})

				#print ret 

		# Update 
		self.update_totals()

	# update_order_report

