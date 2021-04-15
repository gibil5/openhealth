# -*- coding: utf-8 -*-
"""
 	Closing Proof

	Created: 			30 2019
	Last up: 	 		30 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

from . import lib

class ClosingProof(models.Model):
	"""
	Closing Proof
	"""
	_name = 'openhealth.closing.proof'



# ----------------------------------------------------------- Analyse ----------------------------
	def analyse(self):
		"""
		Analyse - Forms of payment - Build Totals
		"""
		print()
		print('CP - Analyse')


		# Receipt
		x_type = 'receipt'
		self.rec_tot, self.rec_serial_nr_first, self.rec_serial_nr_last = lib.get_gen_totals(self, self.date, x_type)


		# Invoice
		x_type = 'invoice'
		self.inv_tot, self.inv_serial_nr_first, self.inv_serial_nr_last = lib.get_gen_totals(self, self.date, x_type)


		# Ticket Receipt
		x_type = 'ticket_receipt'
		self.tkr_tot, self.tkr_serial_nr_first, self.tkr_serial_nr_last = lib.get_gen_totals(self, self.date, x_type)


		# Ticket Invoices
		x_type = 'ticket_invoice'
		self.tki_tot, self.tki_serial_nr_first, self.tki_serial_nr_last = lib.get_gen_totals(self, self.date, x_type)


		# Advertisement
		x_type = 'advertisement'
		self.adv_tot, self.adv_serial_nr_first, self.adv_serial_nr_last = lib.get_gen_totals(self, self.date, x_type)


		# Sale Notes
		x_type = 'sale_note'
		self.san_tot, self.san_serial_nr_first, self.san_serial_nr_last = lib.get_gen_totals(self, self.date, x_type)



		# Credit Notes

		# Get
		state = 'credit_note'
		orders, count = lib.get_orders_by_state(self, self.date, state)
		print(orders)
		print(count)


		# Init
		total = 0

		# Loop
		for order in orders:
			total = total + order.x_credit_note_amount


		# Assign
		self.crn_tot = total

		if count != 0:

			if count == 1:
				print('mark 0')
				self.crn_serial_nr_first = orders[0].x_serial_nr
				self.cnr_serial_nr_last = orders[0].x_serial_nr
				print(self.crn_serial_nr_first)
				print(self.cnr_serial_nr_last)

			else:
				print('mark 1')
				self.crn_serial_nr_first = orders[0].x_serial_nr
				self.cnr_serial_nr_last = orders[-1].x_serial_nr




		# Totals Proof
		self.total_proof = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot + self.adv_tot + self.san_tot - self.crn_tot
		print(self.total_proof)

		self.total_proof_wblack = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot 	#+ self.adv_tot + self.san_tot
		print(self.total_proof_wblack)


		print('mark 2')
		print(self.crn_serial_nr_first)
		print(self.cnr_serial_nr_last)
	# analyse






# ----------------------------------------------------------- Get Totals -----------------------
	def get_totals(self):
		"""
		Get Totals
		"""
		print()
		print('CP - Get Totals')

		print('mark 3')
		print(self.crn_serial_nr_first)
		print(self.cnr_serial_nr_last)

		return 	self.rec_tot, self.rec_serial_nr_first, self.rec_serial_nr_last, \
				self.inv_tot, self.inv_serial_nr_first, self.inv_serial_nr_last, \
				self.tkr_tot, self.tkr_serial_nr_first, self.tki_serial_nr_last, \
				self.tki_tot, self.tki_serial_nr_first, self.tki_serial_nr_last, \
				self.adv_tot, self.adv_serial_nr_first, self.adv_serial_nr_last, \
				self.san_tot, self.san_serial_nr_first, self.san_serial_nr_last, \
				self.crn_tot, self.crn_serial_nr_first, self.crn_serial_nr_last


# ----------------------------------------------------------- Fields -----------------------
	name = fields.Char()


	date = fields.Date(
			string="Fecha",
			default=fields.Date.today,
			#readonly=True,
			required=True,
		)



	# Totals
	total_proof = fields.Float()
	total_proof_wblack = fields.Float()



	# Receipt
	rec_tot = fields.Float()
	rec_serial_nr_first = fields.Char()
	rec_serial_nr_last = fields.Char()


	# Invoice
	inv_tot = fields.Float()
	serial_nr_first_inv = fields.Char()
	serial_nr_last_inv = fields.Char()



	# Ticket rreipt
	tkr_tot = fields.Float()
	tkr_serial_nr_first = fields.Char()
	tkr_serial_nr_last = fields.Char()


	# Ticket invoice
	tki_tot = fields.Float()
	tki_serial_nr_first = fields.Char()
	tki_serial_nr_last = fields.Char()



	# Advertisement
	adv_tot = fields.Float()
	adv_serial_nr_first = fields.Char()
	adv_serial_nr_last = fields.Char()



	# Sale Note
	san_tot = fields.Float()
	san_serial_nr_first = fields.Char()
	san_serial_nr_last = fields.Char()


	# Credit note
	crn_tot = fields.Float()
	crn_serial_nr_first = fields.Char()
	crn_serial_nr_last = fields.Char()



