# -*- coding: utf-8 -*-
"""
 	Closing
	
	Only the Data Model - Not functions. 

	Created: 			18 Oct 2017
	Last up: 	 		30 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
#from . import clos_funcs
from . import ord_vars

class Closing(models.Model):
	"""
	Closing for the days sales - Cierre de Caja. 
	"""
	_name = 'openhealth.closing'
	_description = 'Closing'
	#_order = 'name desc'



# ----------------------------------------------------------- Macros ------------------------------
# Proof of payment

	# Credit Notes
	crn_tot = fields.Float(
			'Notas de Crédito',
			default=0,
		)



	# Ticket Receipts
	tkr_tot = fields.Float(
			#'Tickets Boleta',
			'Boleta Electronica',
			default=0,
		)

	# Ticket Invoices
	tki_tot = fields.Float(
			#'Tickets Factura',
			'Factura Electronica',
			default=0,
		)

	# Receipts
	rec_tot = fields.Float(
			'Boletas',
			default=0,
		)

	# Invoices
	inv_tot = fields.Float(
			'Facturas',
			default=0,
		)

	# Advertisements
	adv_tot = fields.Float(
			'Canjes Publicidad',
			default=0,
		)

	# Sale Notes
	san_tot = fields.Float(
			'Canjes NV',
			default=0,
		)




# ----------------------------------------------------------- Natives -----------------------------

	# Type
	x_type = fields.Char()



	# Dates
	date = fields.Date(
			string="Fecha",
			default=fields.Date.today,
			#readonly=True,
			required=True,
		)

	# Total
	total = fields.Float(
			'Total',
			default=0,
		)

	# Vspace
	vspace = fields.Char(
			' ',
			readonly=True
		)


	# Month
	month = fields.Selection(
			selection=ord_vars._month_order_list,
			string='Mes',
			#required=True,
			readonly=True,
		)

	# Year
	year = fields.Char(
			string='Año',
			#required=True,
			readonly=True,
		)



# ----------------------------------------------------------- Partials ----------------------------

	# Total Proof
	total_proof = fields.Float(
			'Total Documentos de pago',
			default=0,
		)

	total_proof_wblack = fields.Float(					# Without sale_notes and advertisements
			'Total Documentos de pago - NSF',
			default=0,
		)


	# Total Form
	total_form = fields.Float(
			'Total Formas de pago',
			default=0,
		)

	total_form_wblack = fields.Float(
			'Total Formas de pago - NSF',
			default=0,
		)


	# Total Cards
	total_cards = fields.Float(
			'Total Tarjetas',
			default=0,
		)


	# Total Cash
	total_cash = fields.Float(
			'Total Cash',
			default=0,
		)



# ----------------------------------------------------------- Serial numbers ----------------------

# Serial numbers

	serial_nr_first_crn = fields.Char(
			string="De:",
		)

	serial_nr_last_crn = fields.Char(
			string="A:",
		)



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



# ----------------------------------------------------------- Partials ----------------------------

# Form of payment

	# Cash
	cash_tot = fields.Float(
			'Efectivo',
			default=0,
		)

	cash_tot_wblack = fields.Float(					# Without sale notes and advertisements
			'Efectivo - NSF',
			default=0,
		)

	# American Express
	ame_tot = fields.Float(
			'American Express',
			default=0,
		)

	# Diners
	din_tot = fields.Float(
			'Diners',
			default=0,
		)

	# Master - Credito
	mac_tot = fields.Float(
			'Mastercard - Crédito',
			default=0,
		)

	# Master - Debito
	mad_tot = fields.Float(
			'Mastercard - Débito',
			default=0,
		)

	# Visa - Credito
	vic_tot = fields.Float(
			'Visa - Crédito',
			default=0,
		)

	# Visa - Debito
	vid_tot = fields.Float(
			'Visa - Débito',
			default=0,
		)




# ----------------------------------------------------------- Computes ----------------------------
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




# ----------------------------------------------------------- Print -------------------------------
	@api.multi
	def print_closing(self):
		"""
		Print Closing
		"""
		print('')
		print('Print Closing')
		name = "openhealth.report_closing_view"            
		action = self.env['report'].get_action(self, name)
		return action
