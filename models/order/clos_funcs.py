# -*- coding: utf-8 -*-
"""
 		clos_funcs.py
 
 		Created: 			       2016
		Last up: 	 		 4 Sep 2018
"""
from openerp import models, fields, api
import datetime



# ----------------------------------------------------------- Set Totals ---------------------------

def set_totals(self):
	print()
	print('Set All')

	
	# Get Orders
	x_type = 'all'
	orders, count = get_orders(self, self.date, x_type)

	# Init
	amount_untaxed = 0
	count = 0

	# Loop
	for order in orders:
		amount_untaxed = amount_untaxed + order.amount_untaxed
		count = count + 1

	# Total
	self.total = amount_untaxed

# set_totals



# ----------------------------------------------------------- Set Proof ---------------------------

def set_proof_totals(self):
	print()
	print('Set By Proof')




	# Receipt

	# Get Orders
	x_type = 'receipt'
	orders, count = get_orders(self, self.date, x_type)


	# Init
	total = 0
	for order in orders:
		total = total + order.amount_untaxed

	self.rec_tot = total

	if count != 0:
		self.serial_nr_first_rec = orders[0].x_serial_nr
		self.serial_nr_last_rec = orders[-1].x_serial_nr





	# Invoice

	# Get Orders
	x_type = 'invoice'
	orders, count = get_orders(self, self.date, x_type)


	# Init
	total = 0
	for order in orders:
		total = total + order.amount_untaxed
	self.inv_tot = total

	if count != 0:
		self.serial_nr_first_inv = orders[0].x_serial_nr
		self.serial_nr_last_inv = orders[-1].x_serial_nr





	# Ticket Receipt
	# Get Orders
	x_type = 'ticket_receipt'
	orders, count = get_orders(self, self.date, x_type)

	#print orders
	#print orders[0].x_serial_nr
	#print orders[-1].x_serial_nr

	# Init
	total = 0
	for order in orders:
		total = total + order.amount_untaxed
	self.tkr_tot = total

	if count != 0:
		self.serial_nr_first_tkr = orders[0].x_serial_nr
		self.serial_nr_last_tkr = orders[-1].x_serial_nr





	# Ticket Invoices

	# Get Orders
	x_type = 'ticket_invoice'
	orders, count = get_orders(self, self.date, x_type)

	# Init
	total = 0
	for order in orders:
		total = total + order.amount_untaxed
	self.tki_tot = total

	if count != 0:
		self.serial_nr_first_tki = orders[0].x_serial_nr
		self.serial_nr_last_tki = orders[-1].x_serial_nr





	# Advertisement

	# Get Orders
	x_type = 'advertisement'
	orders, count = get_orders(self, self.date, x_type)


	# Init
	total = 0
	for order in orders:
		total = total + order.amount_untaxed
	self.adv_tot = total

	if count != 0:
		self.serial_nr_first_adv = orders[0].x_serial_nr
		self.serial_nr_last_adv = orders[-1].x_serial_nr





	# Sale Notes

	# Get Orders
	x_type = 'sale_note'
	orders, count = get_orders(self, self.date, x_type)

	# Init
	total = 0
	for order in orders:
		total = total + order.amount_untaxed
	self.san_tot = total

	if count != 0:
		self.serial_nr_first_san = orders[0].x_serial_nr
		self.serial_nr_last_san = orders[-1].x_serial_nr





	# Totals Proof
	self.total_proof = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot + self.adv_tot + self.san_tot
	self.total_proof_wblack = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot 	#+ self.adv_tot + self.san_tot


# set_proof_totals




# ----------------------------------------------------------- Set Form ----------------------------

def set_form_totals(self):
	print()
	print('Set By Form')


	# Get Orders
	x_type = 'all'

	orders,count = get_orders(self, self.date, x_type)


	# Init
	cash_tot = 0 
	ame_tot = 0
	din_tot = 0
	mac_tot = 0
	mad_tot = 0
	vic_tot = 0
	vid_tot = 0


	# Loop
	for order in orders: 

		for pm_line in order.x_payment_method.pm_line_ids: 

			if pm_line.method == 'cash':
				cash_tot = cash_tot + pm_line.subtotal  

			elif pm_line.method == 'american_express':
				ame_tot = ame_tot + pm_line.subtotal  

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


	# Form
	self.cash_tot = cash_tot
	self.ame_tot = ame_tot
	self.din_tot = din_tot
	self.mac_tot = mac_tot
	self.mad_tot = mad_tot
	self.vic_tot = vic_tot
	self.vid_tot = vid_tot

# set_form_totals




# ----------------------------------------------------------- Get Orders --------------------------
@api.multi
def get_orders(self, date, x_type):
	#print
	#print 'Get Orders'
	#print date 


	count = 0 



	#DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
	DATETIME_FORMAT = "%Y-%m-%d"

	date_begin = date + ' 05:00:00'


	date_end_dt  = datetime.datetime.strptime(date, DATETIME_FORMAT) + datetime.timedelta(hours=24) + datetime.timedelta(hours=5,minutes=0)
	#print date_end_dt
	date_end = date_end_dt.strftime('%Y-%m-%d %H:%M')



	if x_type == 'all': 
		
		orders = self.env['sale.order'].search([
													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
											])


		count = self.env['sale.order'].search_count([
													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
											])



	else: 

		orders = self.env['sale.order'].search([
													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												order='x_serial_nr asc',
												#limit=1,
											)

		count = self.env['sale.order'].search_count([
													('state', '=', 'sale'),
													('date_order', '>=', date_begin),
													('date_order', '<', date_end),
													('x_type', '=', x_type),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)







	#print date_begin
	#print date_end
	#print orders  
	
	#return orders 
	return orders, count








# ----------------------------------------------------------- Funcs ------------------------------------------------------
#@api.multi
#def update_orders(self, date):
#	print 'jx'
#	print 'Get Orders'
#	orders = get_orders(self, date)
#	print orders
#	for order in orders: 
#		order.update_type()
		#print order.x_type 

