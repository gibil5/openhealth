# -*- coding: utf-8 -*-
#
#
# 	Closing 
# 
# Created: 				18 Oct 2017
# Last updated: 	 	18 Oct 2017
#



from openerp import models, fields, api
#import datetime
from datetime import datetime


class Closing(models.Model):
	
	#_inherit='sale.closing'
	_name = 'openhealth.closing'
	


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





	vspace = fields.Char(
			' ', 
			readonly=True
		)




	# Date 
	date = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)


	date_time = fields.Datetime(
			string="Fecha y Hora", 

			#default = fields.Date.today, 
			default = datetime.now(),

			#readonly=True,
			#required=True, 
		)






	# Cash  
	cash_tot = fields.Float(
			'Efectivo',
			default = 0, 

			compute='_compute_method_tot', 
		)

	# ame  
	ame_tot = fields.Float(
			'American Express',
			default = 0, 

			compute='_compute_method_tot', 
		)

	# cuo  
	cuo_tot = fields.Float(
			'Cuota Perfecta',
			default = 0, 

			compute='_compute_method_tot', 
		)




	# din  
	din_tot = fields.Float(
			'Diners',
			default = 0, 

			compute='_compute_method_tot', 
		)

	# mac  
	mac_tot = fields.Float(
			'Mastercard - Crédito',
			default = 0, 

			compute='_compute_method_tot', 
		)

	# mad  
	mad_tot = fields.Float(
			'Mastercard - Débito',
			default = 0, 

			compute='_compute_method_tot', 
		)






	# vic  
	vic_tot = fields.Float(
			'Visa - Crédito',
			default = 0, 

			compute='_compute_method_tot', 
		)


	# vid  
	vid_tot = fields.Float(
			'Visa - Débito',
			default = 0, 

			compute='_compute_method_tot', 
		)









	# Method 
	method_tot = fields.Float(
			'Metodo',
			default = 0, 

			compute='_compute_method_tot', 
		)

	@api.multi
	#@api.depends('x_appointment')

	def _compute_method_tot(self):
		for record in self:

			#print 'jx'
			#print 'compute Method total'

			date = record.date + ' '

			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),														
														('date_order', 'like', date),
												])

			cash_tot = 0 
			ame_tot = 0 
			cuo_tot = 0 

			din_tot = 0 
			mac_tot = 0 
			mad_tot = 0 

			vic_tot = 0 
			vid_tot = 0 


			for order in orders: 


				#print 'name: ', order.name
				#print 'date_order: ', order.date_order


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





			record.cash_tot = cash_tot
			record.ame_tot = ame_tot
			record.cuo_tot = cuo_tot

			record.din_tot = din_tot
			record.mac_tot = mac_tot
			record.mad_tot = mad_tot

			record.vic_tot = vic_tot
			record.vid_tot = vid_tot


			#print 'cash_tot: ', cash_tot, record.cash_tot
			#print 'ame_tot: ', ame_tot, record.ame_tot
			#print 'cuo_tot: ', cuo_tot, record.cuo_tot
			#print 'din_tot: ', record.din_tot
			#print 'mac_tot: ', record.mac_tot
			#print 'mad_tot: ', record.mad_tot
			#print 'vic_tot: ', record.vic_tot
			#print 'vid_tot: ', record.vid_tot
			#print 





	# Receipts - Total 
	rec_tot = fields.Float(
			'Boletas',
			default = 0, 
			compute='_compute_rec_tot', 
		)

	@api.multi
	#@api.depends('x_appointment')

	def _compute_rec_tot(self):


		for record in self:
			#print 'jx'
			#print 'compute REC total'

			date = record.date + ' '

			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														#('date_order', '=', date),
														('date_order', 'like', date),

														('x_type', '=', 'receipt'),														
														
														#('name', 'like', 'BO-'),														
												])

			total = 0 

			for order in orders: 
				total = total + order.amount_untaxed 

			record.rec_tot = total

			#print 'orders: ', orders
			#print 







	# Invoices - Total 
	inv_tot = fields.Float(
			'Facturas',
			default = 0, 
			compute='_compute_inv_tot', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_inv_tot(self):
		for record in self:
			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),														
														
														('date_order', 'like', date),

														#('name', 'like', 'FA-'),														
														('x_type', '=', 'invoice'),

												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.inv_tot = total






	# Ticket Invoices - Total 
	tki_tot = fields.Float(
			'Tickets Factura',
			default = 0, 
			compute='_compute_tki_tot', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_tki_tot(self):
		for record in self:
			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'TKF-'),														
														('x_type', '=', 'ticket_invoice'),

												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.tki_tot = total







	# Ticket Receipt - Total 
	tkr_tot = fields.Float(
			'Tickets Boleta',
			default = 0, 
			compute='_compute_tkr_tot', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_tkr_tot(self):
		for record in self:
			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'TKB-'),														
														('x_type', '=', 'ticket_receipt'),
												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.tkr_tot = total









	# Advetisement - Total 
	adv_tot = fields.Float(
			'Canjes Publicidad',
			default = 0, 
			compute='_compute_adv_tot', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_adv_tot(self):
		for record in self:
			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'CP-'),														
														('x_type', '=', 'advertisement'),

												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.adv_tot = total





	# Sale Note - Total 
	san_tot = fields.Float(
			'Canjes NV',
			default = 0, 
			compute='_compute_san_tot', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_san_tot(self):
		for record in self:
			date = record.date + ' '
			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),	

														('date_order', 'like', date),
														
														#('name', 'like', 'CN-'),														
														('x_type', '=', 'sale_note'),
												])
			total = 0 
			for order in orders: 
				total = total + order.amount_untaxed 
			record.san_tot = total
















	# Total 
	total = fields.Float(
			'Total',
			default = 0, 
			compute='_compute_total', 
		)



	@api.multi
	#@api.depends('x_appointment')

	def _compute_total(self):
		for record in self:

			#print 'jx'
			#print 'compute total'

			date = record.date + ' '
			#print 'date: ', date 


			orders = record.env['sale.order'].search([
														('state', '=', 'sale'),														
														#('date_order', 'like', '2017-10-18 '),
														('date_order', 'like', date),
												])

			#print 'orders: ', orders


			amount_untaxed = 0 
			count = 0 

			for order in orders: 
				amount_untaxed = amount_untaxed + order.amount_untaxed 
				count = count + 1


			#print 'amount_untaxed: ', amount_untaxed
			#print 'count: ', count

			#record.total = 5.5 
			record.total = amount_untaxed
			#print 




	# orders 
	#order_ids = fields.One2many(
	#		'sale.order',			 
	#		'closing', 
	#		string="Ventas",
	#		domain = [
	#					('state', '=', 'sale'),
	#					('date_order', '=', '2017-10-18'),
	#				],
	#	)





