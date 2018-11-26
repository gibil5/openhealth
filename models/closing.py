# -*- coding: utf-8 -*-
#
# 	Closing 
# 
# Created: 			18 Oct 2017
# Last up: 	 		18 Aug 2018
#
import datetime
from openerp import models, fields, api
from . import clos_funcs

class Closing(models.Model):	
	#_inherit='sale.closing'
	_name = 'openhealth.closing'
	


# ----------------------------------------------------------- Test ------------------------------------------------------

	test_target = fields.Boolean(
			string="Test Target", 
		)



# ----------------------------------------------------------- Dates ------------------------------------------------------
	
	# Dates
	date = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)



# ----------------------------------------------------------- Totals - Absolute ------------------------------------------------------

	# Total
	total = fields.Float(
			'Total',
			default = 0, 
		)



# ----------------------------------------------------------- Totals - Partials ------------------------------------------------------

# Total Proof 
	total_proof = fields.Float(
			'Total Documentos de pago',
			default = 0, 
		)

	total_proof_wblack = fields.Float(					# Without sale_notes and advertisements
			'Total Documentos de pago - NSF',
			default = 0, 
		)

# Total Form 
	total_form = fields.Float(
			'Total Formas de pago',
			default = 0, 
		)

	total_form_wblack = fields.Float(
			'Total Formas de pago - NSF',
			default = 0, 
		)

# Total Cards 
	total_cards = fields.Float(
			'Total Tarjetas',
			default = 0, 
		)

# Total Cash 
	total_cash = fields.Float(
			'Total Cash',
			default = 0, 
		)


# ----------------------------------------------------------- Serial numbers ------------------------------------------------------

# Serial numbers 
	serial_nr_first_tkr = fields.Char(
			string="De:", 
		)	
	
	serial_nr_last_tkr = fields.Char(
			string="A:", 
		)

	serial_nr_first_tki = fields.Char(
			string="De:", 
		)
	
	serial_nr_last_tki = fields.Char(
			string="A:", 
		)

	serial_nr_first_rec = fields.Char(
			string="De:", 
		)	

	serial_nr_last_rec = fields.Char(
			string="A:", 
		)

	serial_nr_first_inv = fields.Char(
			string="De:", 
		)	

	serial_nr_last_inv = fields.Char(
			string="A:", 
		)

	serial_nr_first_adv = fields.Char(
			string="De:", 
		)	

	serial_nr_last_adv = fields.Char(
			string="A:", 
		)

	serial_nr_first_san = fields.Char(
			string="De:", 
		)	
	serial_nr_last_san = fields.Char(
			string="A:", 
		)



# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_totals(self):  

		#print
		#print 'Update Totals'



# Total 
		x_type = 'all'
		orders,count = clos_funcs.get_orders(self, self.date, x_type)
		amount_untaxed = 0 
		count = 0 
		for order in orders: 
			
			#order.update_type()				# Deprecated 
			
			amount_untaxed = amount_untaxed + order.amount_untaxed 
			count = count + 1
		self.total = amount_untaxed



# Proof 
		# Receipts
		x_type = 'receipt'
		
		orders,count = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.rec_tot = total

		if count != 0: 
			self.serial_nr_first_rec = orders[0].x_serial_nr
			self.serial_nr_last_rec = orders[-1].x_serial_nr



		# Invoices
		x_type = 'invoice'
		
		orders,count = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.inv_tot = total

		if count != 0: 
			self.serial_nr_first_inv = orders[0].x_serial_nr
			self.serial_nr_last_inv = orders[-1].x_serial_nr



		# Ticket Receipts
		x_type = 'ticket_receipt'
		
		
		orders,count = clos_funcs.get_orders(self, self.date, x_type)
		
		#print orders
		#print orders[0].x_serial_nr
		#print orders[-1].x_serial_nr

		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.tkr_tot = total

		if count != 0: 
			self.serial_nr_first_tkr = orders[0].x_serial_nr
			self.serial_nr_last_tkr = orders[-1].x_serial_nr



		# Ticket Invoices
		x_type = 'ticket_invoice'
		
		orders,count = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.tki_tot = total

		if count != 0: 
			self.serial_nr_first_tki = orders[0].x_serial_nr
			self.serial_nr_last_tki = orders[-1].x_serial_nr




		# Advertisement
		x_type = 'advertisement'
		
		orders,count = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.adv_tot = total

		if count != 0: 
			self.serial_nr_first_adv = orders[0].x_serial_nr
			self.serial_nr_last_adv = orders[-1].x_serial_nr



		# Sale notes 
		x_type = 'sale_note'
		
		orders,count = clos_funcs.get_orders(self, self.date, x_type)
		
		total = 0 
		for order in orders: 
			total = total + order.amount_untaxed 
		self.san_tot = total

		if count != 0: 
			self.serial_nr_first_san = orders[0].x_serial_nr
			self.serial_nr_last_san = orders[-1].x_serial_nr



		# Total Proof 
		self.total_proof = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot + self.adv_tot + self.san_tot
		self.total_proof_wblack = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot 	#+ self.adv_tot + self.san_tot






# Form
		# Payment methods 
		x_type = 'all'
		orders,count = clos_funcs.get_orders(self, self.date, x_type)


		cash_tot = 0 
		#cash_tot_wblack = 0 

		ame_tot = 0 
		din_tot = 0 
		mac_tot = 0 
		mad_tot = 0 
		vic_tot = 0 
		vid_tot = 0 

		#cuo_tot = 0 



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



				#elif pm_line.method == 'cuota_perfecta':
				#	cuo_tot = cuo_tot + pm_line.subtotal  






		self.cash_tot = cash_tot
		self.ame_tot = ame_tot
		self.din_tot = din_tot
		self.mac_tot = mac_tot
		self.mad_tot = mad_tot
		self.vic_tot = vic_tot
		self.vid_tot = vid_tot
		#self.cuo_tot = cuo_tot




		self.total_form = self.cash_tot + self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot 		#+ self.cuo_tot 

		self.total_form_wblack = self.total_proof_wblack


		self.cash_tot_wblack = self.cash_tot - (self.total_form - self.total_form_wblack)






		self.total_cards = self.ame_tot + self.din_tot + self.mac_tot + self.mad_tot + self.vic_tot + self.vid_tot 						#+ self.cuo_tot 

		self.total_cash = self.cash_tot





# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
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


	# Other 
	vspace = fields.Char(
			' ', 
			readonly=True
		)






# ----------------------------------------------------------- Totals - Partials ------------------------------------------------------

# Form of payment 

	# Cash  
	cash_tot = fields.Float(
			'Efectivo',
			default = 0, 
		)

	cash_tot_wblack = fields.Float(					# Without sale notes and advertisements
			'Efectivo - NSF',
			default = 0, 
		)


	# American Express 
	ame_tot = fields.Float(
			'American Express',
			default = 0, 
		)


	# Diners 
	din_tot = fields.Float(
			'Diners',
			default = 0, 
		)


	# Master - Credito
	mac_tot = fields.Float(
			'Mastercard - Crédito',
			default = 0, 
		)


	# Master - Depbito 
	mad_tot = fields.Float(
			'Mastercard - Débito',
			default = 0, 
		)


	# Visa - Credito 
	vic_tot = fields.Float(
			'Visa - Crédito',
			default = 0, 
		)


	# Visa - Debito 
	vid_tot = fields.Float(
			'Visa - Débito',
			default = 0, 
		)



# Proof of payment 
	
	# Receipts  
	rec_tot = fields.Float(
			'Boletas',
			default = 0, 
		)

	# Invoices  
	inv_tot = fields.Float(
			'Facturas',
			default = 0, 
		)

	# Ticket Invoices  
	tki_tot = fields.Float(
			'Tickets Factura',
			default = 0, 
		)

	# Ticket Receipts 
	tkr_tot = fields.Float(
			'Tickets Boleta',
			default = 0, 
		)

	# Advetisements 
	adv_tot = fields.Float(
			'Canjes Publicidad',
			default = 0, 
		)

	# Sale Notes 
	san_tot = fields.Float(
			'Canjes NV',
			default = 0, 	
		)




# ----------------------------------------------------------- Update ------------------------------------------------------
	# Update 
	@api.multi
	def update(self):  
		#print 'Closing - Update'
		self.update_totals()



