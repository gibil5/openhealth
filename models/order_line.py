# -*- coding: utf-8 -*-
#
# 	Order Line
# 

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

import lib
import user

class sale_order_line(models.Model):

	_inherit='sale.order.line'
	#_name = 'openhealth.order_line'
	#_order = 'x_date_created asc'




# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update Recommendations 
	@api.multi
	def update_recos(self):  

		#print 
		#print 'Update - Recommendations'


		# Init 
		family = self.product_id.x_family
		treatment = self.product_id.x_treatment
		if family in ['laser', 'consultation', 'consultation_gyn']: 
			categ = treatment
		else: 
			categ = family


		# Print 
		#print family
		#print treatment
		#print categ
		#print self.service_co2_id 
		#print self.service_co2_id.state 
		#print hasattr(self.service_co2_id, 'state')
		#print self.service_co2_id is None



		#if categ == 'laser_co2'		and 	self.service_co2_id.state != False: 								
		#if categ == 'laser_co2'		and 	self.service_co2_id != False: 								
			#self.service_co2_id.state = 'sale'
		#elif categ == 'laser_excilite'		and 	self.service_excilite_id.state != False: 
			#self.service_excilite_id.state = 'sale'
		#elif categ == 'laser_ipl'		and 	self.service_ipl_id.state != False: 
			#self.service_ipl_id.state = 'sale'
		#elif categ == 'laser_ndyag'		and 	self.service_ndyag_id.state != False: 
			#self.service_ndyag_id.state = 'sale'
		#elif categ == 'laser_quick'		and 	self.service_quick_id.state != False: 
			#self.service_quick_id.state = 'sale'
		#elif categ == 'medical'			and 	self.service_medical_id.state != False: 
			#self.service_medical_id.state = 'sale'
		#elif categ == 'cosmetology'		and 	self.service_cosmetology_id.state != False: 
			#self.service_cosmetology_id.state = 'sale'
			#if self.service_product_id.state != False: 
			#	self.service_product_id.state = 'sale'



		# Co2
		if categ == 'laser_co2': 									
			lib.change_state(self.service_co2_id, 'sale')


		# Exc
		elif categ == 'laser_excilite': 
			lib.change_state(self.service_excilite_id, 'sale')


		# Ipl
		elif categ == 'laser_ipl': 
			lib.change_state(self.service_ipl_id, 'sale')


		# Ndyag
		elif categ == 'laser_ndyag': 
			lib.change_state(self.service_ndyag_id, 'sale')


		# Quick
		elif categ == 'laser_quick': 
			lib.change_state(self.service_quick_id, 'sale')


		# Medical
		elif categ == 'medical': 
			lib.change_state(self.service_medical_id, 'sale')


		# Cosmetology
		elif categ == 'cosmetology': 
			lib.change_state(self.service_cosmetology_id, 'sale')



		# Consultation
		elif categ == 'consultation': 
			#self.service_consultation_id.state = 'sale'
			print 


		# Products 
		else:
			lib.change_state(self.service_product_id, 'sale')




# ---------------------------------------------- Open Line Current --------------------------------------------------------

	# Open Line 
	@api.multi
	def open_line_current(self): 

		res_id = self.id 
		
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Service Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,

				'res_id': res_id,
				
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},

				'context': {
				}
		}
	# open_line_current 




# ----------------------------------------------------------- Recommendations ------------------------------------------------------

	# Recommendation 

	# Product 
	service_product_id = fields.Many2one(
			'openhealth.service.product', 
			string='Product', 
		)


	# Consultation
	service_consultation_id = fields.Many2one(
			'openhealth.service.consultation', 
			string='Consultation', 
		)


	# Laser 
	service_co2_id = fields.Many2one(
			'openhealth.service.co2', 
			string='Co2', 
		)

	service_quick_id = fields.Many2one(
			'openhealth.service.quick', 
			string='Quick', 
		)

	service_vip_id = fields.Many2one(
			'openhealth.service.vip', 
			string='Vip', 
		)

	service_excilite_id = fields.Many2one(
			'openhealth.service.excilite', 
			string='Excilite', 
		)

	service_ipl_id = fields.Many2one(
			'openhealth.service.ipl', 
			string='Ipl', 
		)

	service_ndyag_id = fields.Many2one(
			'openhealth.service.ndyag', 
			string='Ndyag', 
		)


	# Medical 
	service_medical_id = fields.Many2one(
			'openhealth.service.medical', 
			string='Medical', 
		)


	# Cosmetology 
	service_cosmetology_id = fields.Many2one(
			'openhealth.service.cosmetology', 
			string='Cosmetology', 
		)




# ----------------------------------------------------------- Blocked ------------------------------------------------------

	# Product 
	product_id = fields.Many2one(
			'product.product', 
			string='Product', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			
			#default=lambda self: user._get_default_id(self, 'product'),

			ondelete='restrict', 
			required=True
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

			default=-1, 

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

