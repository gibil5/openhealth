# -*- coding: utf-8 -*-
"""
 	Closing - 1st Level
 	Uses Closing Form and Closing Proof. 

	Created: 			18 Oct 2017
	Last up: 	 		20 Jan 2020

"""
from __future__ import print_function
from openerp import models, fields, api
from . import clos_funcs
from . import lib
from . import test_closing

class Closing(models.Model):
	"""
	Native class.
	Encapsulates Odoo services.
	"""
	_inherit = 'openhealth.closing'




# ----------------------------------------------------------- Getters - Ticket -----------------------

	def get_cash(self):
		return self.cash_tot
		#return self.cash_tot_wblack


	def get_american(self):
		return self.ame_tot


	def get_diners(self):
		return self.din_tot


	def get_master_credit(self):
		return self.mac_tot


	def get_master_debit(self):
		return self.mad_tot


	def get_visa_credit(self):
		return self.vic_tot


	def get_visa_debit(self):
		return self.vid_tot


	def get_total(self):
		return self.total_form
		#return self.total_form_wblack



	def get_bbva(self):
		return self.bbva_tot

	def get_inter(self):
		return self.interbank_tot

	def get_scotia(self):
		return self.scotiabank_tot

	def get_bcp(self):
		return self.bcp_tot




# ----------------------------------------------------- Relational - Counters ------------------------------------------------------------------

	# Closing Form
	closing_form = fields.Many2one(
			'openhealth.closing.form', 
			string='Forma de Pago',
		)

# ----------------------------------------------------------- Natives -----------------------
	total_banks = fields.Float(
			'Total Bancos',
		)


	bbva_tot = fields.Float(
			'BBVA',
		)

	interbank_tot = fields.Float(
			'Interbank',
		)

	scotiabank_tot = fields.Float(
			'Scotiabank',
		)

	bcp_tot = fields.Float(
			'BCP',
		)



# ----------------------------------------------------------- Update Totals -----------------------
	# Update Totals
	@api.multi
	def update_totals(self):
		"""
		Update Closing - Cierre de Caja
		Proof - Documentos de pago
		Form - Formas de pago
		"""
		print()
		print('2019 - Update Totals')


		# Reset
		self.reset()



# Proof Totals
		clos_funcs.set_proof_totals(self)



# Form Totals - Uses Closing Form

		# Create Closing Form
		self.closing_form = self.env["openhealth.closing.form"].create({
																			'name': 'Forma de Pago',
																			'date': self.date,
																	})
		# Analise
		self.closing_form.analyse()



		# Get Sub Totals
		self.cash_tot, self.ame_tot, self.din_tot, 	self.mac_tot, self.mad_tot, self.vic_tot, self.vid_tot, \
			self.bbva_tot, self.interbank_tot, self.scotiabank_tot, self.bcp_tot = self.closing_form.get_sub_totals()


		# Get Totals
		self.total_form, self.total_cash, self.total_cards, self.total_banks = self.closing_form.get_totals()




# Totals
		self.set_totals()



# Sub Totals
		#self.set_sub_totals() 	# Dep


	# update_totals



# ----------------------------------------------------------- Set Totals ---------------------------

	def set_totals(self):
		"""
		Set Totals
		"""
		print()
		print('2019 - Set Totals')


		# Get Orders
		x_type = 'all'
		orders, count = lib.get_orders(self, self.date, x_type)


		# Init
		amount_untaxed = 0
		count = 0

		# Loop
		for order in orders:
			amount_untaxed = amount_untaxed + order.amount_untaxed
			count = count + 1


		# Total
		self.total = amount_untaxed - self.crn_tot

	# set_totals



# ----------------------------------------------------------- Update ------------------------------
	# Update
	@api.multi
	def update(self):
		"""
		Build the Closing (Cierre de Caja). 
		For a given day.
		"""
		print()
		print('2019 - Update')

		self.update_totals()



# ----------------------------------------------------------- Reset ------------------------------
	@api.multi
	def reset(self):
		"""
		Reset
		"""
		print()
		print('2019 - Reset')


		# Relational
		self.closing_form.unlink()
		#self.closing_proof.unlink()


		# Totals
		self.total = 0
		self.total_cash = 0
		self.total_banks = 0
		self.total_cards = 0
		self.total_form = 0

		self.total_proof = 0





		# Sub Totals - Proof
		self.crn_tot = 0

		self.tkr_tot = 0
		self.tki_tot = 0

		self.rec_tot = 0
		self.inv_tot = 0

		self.adv_tot = 0
		self.san_tot = 0


		# Serial Numbers - Proof
		self.serial_nr_first_crn = ''
		self.serial_nr_last_crn = ''

		# Ticket
		self.serial_nr_first_tkr = ""
		self.serial_nr_last_tkr = ""
		self.serial_nr_first_tki = ""
		self.serial_nr_last_tki = ""

		# Paper
		self.serial_nr_first_rec = ""
		self.serial_nr_last_rec = ""
		self.serial_nr_first_inv = ""
		self.serial_nr_last_inv = ""


		# Other
		self.serial_nr_first_adv = ""
		self.serial_nr_last_adv = ""
		self.serial_nr_first_san = ""
		self.serial_nr_last_san = ""



		# Subtotals - Form

		# Cash
		self.cash_tot = 0
		self.cash_tot_wblack = 0

		# Cards
		self.ame_tot = 0
		self.din_tot = 0
		self.mac_tot = 0
		self.mad_tot = 0
		self.vic_tot = 0
		self.vid_tot = 0

		# Banks
		self.bbva_tot = 0
		self.interbank_tot = 0
		self.scotiabank_tot = 0
		self.bcp_tot = 0




# ----------------------------------------------------------- Test ------------------------------
	@api.multi
	def test(self):
		"""
		Test
		"""
		print()
		print('2019 - Test')


		# Patient
		patient_name = 'REVILLA RONDON JOSE JAVIER'

		partner = self.env['res.partner'].search([
													('name', '=', patient_name),
												],
												#order='appointment_date desc',
												limit=1,)
		partner_id = partner.id
		print(partner)
		print(partner_id)



		# Patient
		patient = self.env['oeh.medical.patient'].search([
													('name', '=', patient_name),
												],
												#order='appointment_date desc',
												limit=1,)
		patient_id = patient.id
		print(patient)
		print(patient_id)



		# Doctor
		doctor_name = 'Dr. Chavarri'
		doctor = self.env['oeh.medical.physician'].search([
															('name', '=', doctor_name),
												],
												#order='appointment_date desc',
												limit=1,)
		doctor_id = doctor.id
		print(doctor)
		print(doctor_id)



		# Order Consultation - Receipt
		#x_type = 'ticket_receipt'
		#order = test_closing.create_order_con(self, partner, patient, doctor, x_type)
		#print(order)


		par_arr = [
						('ticket_receipt',	'cash'),
						('ticket_invoice',	'bcp'), 
						('ticket_receipt',	'american_express'),


						#('receipt',			'american_express'), 
						#('invoice',			'credit_master'), 

						#'advertisement',
						#'sale_note',
		]

		#method = 'cash'
		#method = 'bcp'
		#method = 'american_express'


		# Create Order Consultations
		#for x_type in x_type_arr:
		for par in par_arr:
			print(par)

			x_type = par[0]
			method = par[1]

			order = test_closing.create_order_con(self, partner, patient, doctor, x_type, method)
			print(order)


# ----------------------------------------------------------- Clean ------------------------------
	@api.multi
	def clean(self):
		"""
		Clean
		"""
		print()
		print('2019 - Clean')


		# Patient
		patient_name = 'REVILLA RONDON JOSE JAVIER'

		patient = self.env['oeh.medical.patient'].search([
													('name', '=', patient_name),
												],
												#order='appointment_date desc',
												limit=1,)
		patient_id = patient.id
		print(patient)
		print(patient_id)



		# Orders
		orders = self.env['sale.order'].search([
															('patient', '=', patient.name),

															('state', 'in', ['sale']),
												],
												order='date_order desc',
												limit=10,
												)

		print(orders)


		# Loop
		for order in orders:
			order.remove_myself_force()




