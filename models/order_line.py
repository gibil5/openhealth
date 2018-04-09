# -*- coding: utf-8 -*-
#
# 	Order Line
# 

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp



class sale_order_line(models.Model):
	_inherit='sale.order.line'

	#_name = 'openhealth.order_line'

	#_order = 'x_date_created asc'






# ----------------------------------------------------------- Sale Order Report ------------------------------------------------------

	order_report_id = fields.Many2one(

		'openhealth.order.report.nex', 
		
		string='Order Report Reference', 		
		required=False, 
	#	ondelete='cascade', index=True, copy=False
	)





# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	# Date Created 
	x_date_created = fields.Datetime(
			string='Fecha', 
		)






# ----------------------------------------------------------- Primitives ------------------------------------------------------


	x_qty = fields.Integer(

			compute='_compute_x_qty', 
		)


	@api.multi
	def _compute_x_qty(self):
		for record in self:

			record.x_qty = record.product_uom_qty







	# Quantity
	product_uom_qty = fields.Float(
		string='Quantity', 

		digits=(16, 0), 
		
		required=False,
		default=1.0
	)







	# Description  
	x_description = fields.Text(

			#string='Description', 
			string='Nombre compacto', 
		
			#required=True, 

			compute='_compute_x_description', 
		)


	@api.multi
	def _compute_x_description(self):
		for record in self:


			if record.product_id.x_name_short in ['generic_product','generic_service']: 

				#record.x_description = record.product_id.name
				record.x_description = record.name
			

			else: 
				#record.x_description = record.product_id.description
				#record.x_description = record.product_id.x_name_short
				record.x_description = record.product_id.x_name_ticket









	# Name 
	name = fields.Text(
			string='Description', 
			required=True, 
		)






	# Patient 
	patient_id = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente', 
		)











	order_id = fields.Many2one('sale.order', string='Order Reference', 		
		required=False, 
		ondelete='cascade', index=True, copy=False
	)







# ----------------------------------------------------------- On Changes ------------------------------------------------------

	# Product  
	#@api.onchange('product_id')
	#def _onchange_product_id(self):
	#	print 'jx'
	#	print 'Change Product'
		#if self.product_id.description != False: 
	#	self.name = self.product_id.description 






# ----------------------------------------------------------- Important ------------------------------------------------------


	# Vip in progress 
	x_vip_inprog = fields.Boolean(
			default=False, 
		
			compute='_compute_vip_inprog', 
		)

	@api.multi
	def _compute_vip_inprog(self):

		for record in self:

			for line in record.order_id.order_line:
				
				#if line.product_id.x_short_name == 'vip_card': 
				#if line.product_id.default_code == '57': 				
				if line.product_id.default_code == '495': 				
					record.x_vip_inprog = True








	# Price Unit
	price_unit = fields.Float(

		#'Unit Price', 
		'Precio', 
		
		required=True, 
		digits=dp.get_precision('Product Price'), 
		default=0.0, 
	
	
		#compute='_compute_price_unit', 
	)

	@api.multi
	def _compute_price_unit(self):

		for record in self:



			if record.x_price_manual != False: 						# Manual 				
				record.price_unit = record.x_price_manual



			else: 
				

				#if 	not record.order_id.x_partner_vip: 				
				if 		not record.order_id.x_partner_vip  		and  	not record.x_vip_inprog: 				# Not VIP
					record.price_unit = record.x_price_std



				else: 												# VIP
		
					if record.x_comeback    and  	record.x_price_vip_return != 0: 
						record.price_unit = record.product_id.x_price_vip_return

					else: 
						if record.x_price_vip != 0: 
							record.price_unit = record.x_price_vip
						else:
							record.price_unit = record.x_price_std









	# Comeback 
	x_comeback = fields.Boolean(
			string='Regreso', 		

			compute='_compute_comeback', 
		)


	@api.multi
	def _compute_comeback(self):

		for record in self:

			record.x_comeback = False

			for service in record.order_id.patient.x_service_quick_ids:
				if service.service.name == record.name  	and 	service.comeback: 
					record.x_comeback = True










	# Price manual
	x_price_manual = fields.Float(
			
			string="Precio manual",
			
			required=False, 

			#compute='_compute_price_manual', 
		)

	#@api.multi
	#def _compute_price_manual(self):
	#	for record in self:
	#		record.x_price_manual = record.product_id.list_price













	# Price std
	x_price_std = fields.Float(
			
			string="Precio Std",
			#string="Precio",
			
			required=False, 

			compute='_compute_price_std', 
		)

	@api.multi
	def _compute_price_std(self):
		for record in self:
			record.x_price_std = record.product_id.list_price





	# Price Vip
	x_price_vip = fields.Float(
			string="Precio Vip",
			required=False, 

			compute='_compute_price_vip', 
		)


	@api.multi
	def _compute_price_vip(self):
		for record in self:
			record.x_price_vip = record.product_id.x_price_vip






	# Price Vip Return
	x_price_vip_return = fields.Float(

			#string="Precio Vip Return",
			string="Precio Vip R",
		
			required=False, 

			compute='_compute_price_vip_return', 
		)

	@api.multi
	def _compute_price_vip_return(self):

		for record in self:
			record.x_price_vip_return = record.product_id.x_price_vip_return









# ----------------------------------------------------------- Actions ------------------------------------------------------

	@api.multi
	def create_myself(self):  

		print 
		print 'jx'
		print 'Create Myself'
		print 



# ----------------------------------------------------------- Standard ------------------------------------------------------



	product_uom = fields.Many2one(
		'product.uom', 
		string='Unit of Measure', 
		#required=True
		required = False,
	)


	customer_lead = fields.Float(
		'Delivery Lead Time', 
		#required=True, 
		required=False, 
		default=0.0,
		help="Number of days between the order confirmation and the shipping of the products to the customer", oldname="delay")


	order_id = fields.Many2one('sale.order', string='Order Reference', 		
		required=False, 
		ondelete='cascade', index=True, copy=False
	)

