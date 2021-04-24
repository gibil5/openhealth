# -*- coding: utf-8 -*-
"""
	Ticket
	Created: 			09 Aug 2020
	Last up: 	 		09 Aug 2020
"""
from __future__ import print_function
from openerp import models, fields, api
from . import raw_funcs
from . import ticket_line

class Ticket(models.Model):
	"""
	Ticket tools 
	Used by - print_ticket_receipt_electronic
	"""
	_name = 'openhealth.ticket'
	#_order = 'write_date desc'
	_description = 'Ticket'


# ---------------------------------------------------- Ticket - Vars -----------
	name = fields.Char( string="Name", required=True, default='Ticket')

	# Configurator
	configurator = fields.Many2one(
		'openhealth.configurator.emr',
		string="Configurator",
		required=True,
		default=lambda self: raw_funcs.get_configurator(self.env['openhealth.configurator.emr']),
	)


# ---------------------------------------------------- Always the same -------------
	# Company
	def get_company(self, tag):
		"""
		Used by Ticket
		openhealth.report_ticket_receipt_electronic
		"""
		print('get_company')
		options = {
			'name' : self.configurator.company_name,
			'ruc' : self.configurator.ticket_company_ruc,
			'address' : self.configurator.ticket_company_address,
			'phone' : self.configurator.company_phone,
			'note' : self.configurator.ticket_note,
			'description' : self.configurator.ticket_company_address,
			'warning' : self.configurator.ticket_warning,
			'website' : self.configurator.company_website,
			'email' : self.configurator.company_email,
		}
		return options[tag]

	# Header
	def get_items_header(self, tag):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_items_header')
		if tag in ['items_header']:
			tag = 'items'
			value = 'header'
		obj = ticket_line.TicketLine(tag, value)
		line = obj.get_line_items()
		return line


# --------------------------------------------- Is function of the caller ------
	def get_ticket(self, tag, obj):
		"""
		Used by Ticket
		"""
		if tag == 'title':
			ret = obj.x_title
		elif tag == 'serial_nr':
			ret = obj.x_serial_nr
		return ret


	def get_ticket_line(self, tag, obj):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_ticket_line')
		#line = raw_funcs.get_ticket_raw_line(obj, tag)
		print(tag)

		if tag in ['Cliente']:
			value = obj.patient.name
		elif tag in ['DNI']:
			value = obj.x_id_doc
		elif tag in ['Direccion']:
			value = obj.patient.x_address
		elif tag in ['Fecha']:
			value = raw_funcs.get_date_corrected(obj.date_order)
		elif tag in ['Ticket']:
			value = obj.x_serial_nr

		obj = ticket_line.TicketLine(tag, value)

		line = obj.get_line()

		return line

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_raw_line(self, arg, obj):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_raw_line')
		print(arg)

		# Default
		tag = 'TOTAL S/.'
		#value = str(obj.get_amount_total())
		value = str(raw_funcs.get_amount_total(obj.x_amount_total, obj.pl_transfer_free))

		# Totals
		if arg in ['totals_net']:
			tag = 'OP. GRAVADAS S/.'
			#value = str(obj.get_total_net())
			value = str(raw_funcs.get_total_net(obj.x_amount_total, obj.pl_transfer_free))

		elif arg in ['totals_free']:
			tag = 'OP. GRATUITAS S/.'
			value = '0'

		elif arg in ['totals_exonerated']:
			tag = 'OP. EXONERADAS S/.'
			value = '0'

		elif arg in ['totals_unaffected']:
			tag = 'OP. INAFECTAS S/.'
			value = '0'

		elif arg in ['totals_tax']:
			tag = 'I.G.V. 18% S/.'
			#value = str(obj.get_total_tax())
			value = str(raw_funcs.get_total_tax(obj.x_amount_total, obj.pl_transfer_free))

		#elif arg in ['totals_total']:
		#	tag = 'TOTAL S/.'
		#	value = str(obj.get_amount_total())

		obj = ticket_line.TicketLine(tag, value)
		line = obj.get_line()
		return line

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_words_line(self, argument, obj):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_words_line')
		print(argument)

		# Words
		if argument in ['words_header']:
			tag = 'Son:'
			value = ''
		elif argument in ['words_soles']:
			tag = ''
			#value = str(obj.get_total_in_words())
			value = str(raw_funcs.get_total_in_words(obj.x_amount_total, obj.pl_transfer_free))
		elif argument in ['words_cents']:
			tag = ''
			#value = str(obj.get_total_cents())
			value = str(raw_funcs.get_total_cents(obj.x_amount_total, obj.pl_transfer_free))
		elif argument in ['words_footer']:
			tag = ''
			value = 'Soles'

		obj = ticket_line.TicketLine(tag, value)
		line = obj.get_line()
		return line
