# -*- coding: utf-8 -*-
#
# 	Closing 
# 
# Created: 				18 Oct 2017
# Last updated: 	 	18 Oct 2017
#

from openerp import models, fields, api

import datetime

import clos_funcs



class Closing(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.closing'
	


# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_totals(self):  

		print 'jx'
		print 'Update totals'





		# Total 
		x_type = 'all'
		#orders = clos_funcs.get_orders(self, self.date)
		orders = clos_funcs.get_orders(self, self.date, x_type)
		print 'orders: ', orders
		print 

		amount_untaxed = 0 
		count = 0 
		for order in orders: 
	
			order.update_type()
	
			amount_untaxed = amount_untaxed + order.amount_untaxed 
			count = count + 1
		self.total = amount_untaxed




		#orders = self.env['sale.order'].search([
		#												('state', '=', 'sale'),	
		#												('date_order', 'like', date),
		#												('x_type', '=', 'receipt'),																												
		#										])

		

		# Receipts
		x_type = 'receipt'
		
		orders = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.rec_tot = total



		# Invoices
		x_type = 'invoice'
		
		orders = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.inv_tot = total



		# Ticket Invoices
		x_type = 'ticket_invoice'
		
		orders = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.tki_tot = total




		# Ticket Receipts
		x_type = 'ticket_receipt'
		
		orders = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.tkr_tot = total




		# Advertisement
		x_type = 'advertisement'
		
		orders = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.adv_tot = total




		# Sale notes 
		x_type = 'sale_note'
		
		orders = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.san_tot = total




		# Payment methods 
		x_type = 'all'
		orders = clos_funcs.get_orders(self, self.date, x_type)


		cash_tot = 0 
		ame_tot = 0 
		cuo_tot = 0 
		din_tot = 0 
		mac_tot = 0 
		mad_tot = 0 
		vic_tot = 0 
		vid_tot = 0 



		for order in orders: 

			for pm_line in order.x_payment_method.pm_line_ids: 
					

				if pm_line.method == 'cash':
					cash_tot = cash_tot + pm_line.subtotal  

				elif pm_line.method == 'american_express':
					ame_tot = ame_tot + pm_line.subtotal  

				elif pm_line.method == 'cuota_perfecta':
					cuo_tot = cuo_tot + pm_line.subtotal  



				elif pm_line.method == 'diners':
					din_tot = din_tot + pm_line.subtotal  

				elif pm_line.method == 'credit_master':
					mac_tot = mac_tot + pm_line.subtotal  

				elif pm_line.method == 'debit_master':
					mad_tot = mad_tot + pm_line.subtotal  



				elif pm_line.method == 'credit_visa':
					vic_tot = vic_tot + pm_line.subtotal  

				elif pm_line.method == 'debit_visa':
					vid_tot = vid_tot + pm_line.subtotal  





		self.cash_tot = cash_tot
		self.ame_tot = ame_tot
		self.cuo_tot = cuo_tot
		self.din_tot = din_tot
		self.mac_tot = mac_tot
		self.mad_tot = mad_tot
		self.vic_tot = vic_tot
		self.vid_tot = vid_tot




# ----------------------------------------------------------- Primitives ------------------------------------------------------
	# Other 
	vspace = fields.Char(
			' ', 
			readonly=True
		)


	# Name 
	name = fields.Char(
			string="Cierre de Caja #", 
			compute='_compute_name', 
		)
	@api.multi
	#@api.depends('x_appointment')
	def _compute_name(self):
		for record in self:
			record.name = record.date 




	# Dates
	date = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)

	date_time = fields.Datetime(
			string="Fecha y Hora", 
			#default = fields.Date.today, 
			default = datetime.datetime.now(),
			#readonly=True,
			#required=True, 
		)






# Total absolute
	total = fields.Float(
			'Total',
			default = 0, 

			#compute='_compute_total', 
		)




# Total partials - Form of payment 

	# Cash  
	cash_tot = fields.Float(
			'Efectivo',
			default = 0, 

			#compute='_compute_method_tot', 
		)

	# ame  
	ame_tot = fields.Float(
			'American Express',
			default = 0, 

			#compute='_compute_method_tot', 
		)

	# cuo  
	cuo_tot = fields.Float(
			'Cuota Perfecta',
			default = 0, 

			#compute='_compute_method_tot', 
		)




	# din  
	din_tot = fields.Float(
			'Diners',
			default = 0, 

			#compute='_compute_method_tot', 
		)

	# mac  
	mac_tot = fields.Float(
			'Mastercard - Crédito',
			default = 0, 

			#compute='_compute_method_tot', 
		)

	# mad  
	mad_tot = fields.Float(
			'Mastercard - Débito',
			default = 0, 

			#compute='_compute_method_tot', 
		)


	# vic  
	vic_tot = fields.Float(
			'Visa - Crédito',
			default = 0, 

			#compute='_compute_method_tot', 
		)


	# vid  
	vid_tot = fields.Float(
			'Visa - Débito',
			default = 0, 

			#compute='_compute_method_tot', 
		)






# Total partials - Proof of payment 
	
	# Receipts  
	rec_tot = fields.Float(
			'Boletas',
			default = 0, 

			#compute='_compute_rec_tot', 
		)

	# Invoices  
	inv_tot = fields.Float(
			'Facturas',
			default = 0, 

			#compute='_compute_inv_tot', 
		)


	# Ticket Invoices  
	tki_tot = fields.Float(
			'Tickets Factura',
			default = 0, 

			#compute='_compute_tki_tot', 
		)



	# Ticket Receipts 
	tkr_tot = fields.Float(
			'Tickets Boleta',
			default = 0, 

			#compute='_compute_tkr_tot', 
		)


	# Advetisements 
	adv_tot = fields.Float(
			'Canjes Publicidad',
			default = 0, 
			
			#compute='_compute_adv_tot', 
		)

	# Sale Notes 
	san_tot = fields.Float(
			'Canjes NV',
			default = 0, 
			
			#compute='_compute_san_tot', 
		)



