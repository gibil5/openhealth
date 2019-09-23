# -*- coding: utf-8 -*-
"""
 		PaymentMethod

 		Created: 			26 Aug 2016
		Last up: 	 		 2 Sep 2019
"""
from __future__ import print_function

from openerp import models, fields, api
from openerp import _
from openerp.exceptions import Warning as UserError
from . import pm_vars

class PaymentMethod(models.Model):
	"""
	Payment Method
	Several methods are possible:
		- ticket receipt, 
		- ticket invoice, 
		- advertissement, 
		- sale note,
	"""

	_name = 'openhealth.payment_method'



# ----------------------------------------------------------- Relational ------------------------------

	# Lines
	pm_line_ids = fields.One2many(
			
			'openhealth.payment_method_line',
			
			'payment_method',
			
			string="Pago #",
		)




# ----------------------------------------------------------- Locked ------------------------------
	# Total
	total = fields.Float(
			string='Total a pagar',
			required=True,
			states=pm_vars.READONLY_STATES,
		)


	# Saledoc
	saledoc = fields.Selection(
			string="Tipo",

			selection=pm_vars._sale_doc_type_list,
			
			states=pm_vars.READONLY_STATES,

			default='ticket_receipt',
		)



# ----------------------------------------------------------- Primitives --------------------------

	# Order
	order = fields.Many2one(
			'sale.order',
			string="Venta",
			ondelete='cascade',
			required=True,
			readonly=True,
		)

	# Date created
	date_created = fields.Datetime(
			string="Fecha",
		)

	# Partner
	partner = fields.Many2one(
			'res.partner',
			string="Cliente",
			required=True,
			readonly=True,
		)

	# Vspace
	vspace = fields.Char(
			' ',
			readonly=True
		)

	# Nr Payments
	nr_pm = fields.Char(
			default=2,
		)

	# Firm
	firm = fields.Char(
			'Razón social',
			readonly=True,
		)

	# Ruc
	ruc = fields.Char(
			'Ruc',
			readonly=True,
		)


# ----------------------------------------------------------- Admin - Editable --------------------

	# Confirmed
	confirmed = fields.Boolean(
			default=False,
			readonly=True,
			string="Confirmado",
		)

	# Editable
	editable = fields.Boolean(
			default=False,
			readonly=True,
			string="Editable",
		)


# ----------------------------------------------------------- Actions -----------------------------

	# go_back
	@api.multi
	def go_back(self):
		"""
		high level support for doing this and that.
		"""
		self.confirmed = True
		# Order
		self.order.state = 'sent'
		return self.order.open_myself()
	# go_back






# ----------------------------------------------------------- Computes ----------------------------

	# Total Paid
	pm_total = fields.Float(
			string='Total pagado',
			#required=True,
			default=0,

			compute="_compute_pm_total",
		)

	@api.multi
	def _compute_pm_total(self):
		for record in self:
			pm_total = 0
			for line in record.pm_line_ids:
				pm_total = pm_total + line.subtotal
			record.pm_total = pm_total




	# Balance
	balance = fields.Float(
			string='Saldo',
			readonly=True,
			default=0,

			compute="_compute_balance",
		)

	@api.multi
	def _compute_balance(self):
		#print
		#print 'Compute Balance'
		for record in self:
			record.balance = record.total - record.pm_total





	# Name - Used by Order
	name = fields.Char(
			string="Pagos",

			compute='_compute_name',
		)
	@api.multi
	def _compute_name(self):
		for record in self:
			record.name = 'PA-' + str(record.id).zfill(6)



	# State
	state = fields.Selection(
			selection=[
							('draft', 'Inicio'),
							('sale', 'Pagado'),
							('done', 'Completo'),
							('editable', 'e'),
						],
			string='Estado',
			default='draft',

			compute="_compute_state",
		)

	@api.multi
	def _compute_state(self):
		for record in self:
			record.state = 'draft'
			if record.balance == 0.0 and record.saledoc != False:
				record.state = 'sale'
			if record.confirmed:
				record.state = 'done'
			if record.editable:
				record.state = 'editable'





# ----------------------------------------------------------- Test ---------------------------
	def test_computes(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print(self.name)
		print(self.pm_total)
		print(self.balance)
		print(self.state)


	@api.multi
	def test(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Test')
		self.test_computes()
		#return self.test_actions()		# Dangerous


# ----------------------------------------------------------- On Changes ---------------------------
	# Pm Line Ids
	@api.onchange('pm_line_ids')
	def _onchange_pm_line_ids(self):
		#print
		#print 'On change - Pm Line'

		pm_total = 0
		ctr = 1
		for line in self.pm_line_ids:
			pm_total = pm_total + line.subtotal
			ctr = ctr + 1


		# Init
		self.balance = self.total - pm_total
		self.pm_total = pm_total
		self.nr_pm = ctr


		if self.balance < 0:
			# Raise Error
			msg = "Error: Subtotal incorrecto !"
			raise UserError(_(msg))

	# _onchange_pm_line_ids


	# On Sale Doc
	@api.onchange('saledoc')
	def _onchange_saledoc(self):
		#print
		#print 'On change - Saledoc'
		if self.balance == 0.0:
			self.state = 'sale'
	# _onchange_saledoc
