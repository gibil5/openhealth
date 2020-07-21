# -*- coding: utf-8 -*-
"""
		payment method line

	 	Created: 			 2016
		Last up: 	 		 2 Sep 2019
"""
from openerp import models, fields, api
from . import pm_vars
from openerp.addons.openhealth.models.libs import acc_lib

class payment_method_line(models.Model):
	"""
	Payment Method Line
	Allow different forms of payment.
	"""
	_name = 'openhealth.payment_method_line'

	_order = 'date_time asc'


# ----------------------------------------------------------- Relational --------------------------
	# Payment Method

	#payment_method = fields.Char()

	payment_method = fields.Many2one(
			'openhealth.payment_method',
			ondelete='cascade',
			required=False,
		)




	# Account - Contabilidad
	account_id = fields.Many2one(
			'openhealth.account.contasis',
			ondelete='cascade',
		)




# ----------------------------------------------------------- Method --------------------------------
	# Method
	method = fields.Selection(

			selection=pm_vars._payment_method_list,

			string="Forma de Pago",
			default="cash",
			required=True,
		)




# ----------------------------------------------------------- Important ---------------------------
	# Subtotal
	subtotal = fields.Float(
			string='Subtotal',
			#default=self.balance,
			required=True,
		)






# ----------------------------------------------------------- Meta --------------------------------

	# Date
	date_char = fields.Char(
			string="Fecha",
		)

	# Time
	time_char = fields.Char(
			string="Hora",
		)

	# State
	state = fields.Selection(
			selection=pm_vars._state_list,
			string="Estado",
		)


	# Document
	document = fields.Char(
			string="Documento",
		)

	document_type = fields.Char(
			string="Tipo Doc",
		)



	# Other
	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Nombre",
		)

	serial_nr = fields.Char(
			string="Nr. de serie",
		)

	x_type = fields.Selection(
			[
				('receipt', 'Boleta'),
				('invoice', 'Factura'),
				('advertisement', 'Canje Publicidad'),
				('sale_note', 'Canje NV'),
				('ticket_receipt', 'Ticket Boleta'),
				('ticket_invoice', 'Ticket Factura'),
			],
			string='Tipo',
		)

	date_time = fields.Datetime(
			#string="Fecha",
			string="Fecha y Hora",
		)


# ----------------------------------------------------------- Primitives --------------------------

	# Name
	name = fields.Char(
			string="#",
			required=True,
		)

	# Currency
	currency = fields.Char(
			string="Moneda",
			default="S/.",
		)

	# Vspace
	vspace = fields.Char(
			' ',
			readonly=True
			)



# ----------------------------------------------------------- Actions -----------------------------

	# Update Fields
	@api.multi
	def update_fields(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'PM Line - Update'

		# Dates
		#date_time_corr, date_time_str = acc_funcs.correct_time(self, self.date_time, -5)
		date_time_corr, date_time_str = acc_lib.AccFuncs.correct_time(self.date_time, -5)

		self.date_char = date_time_str.split()[0]
		self.time_char = date_time_str.split()[1]

	# update_fields
