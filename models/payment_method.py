# -*- coding: utf-8 -*-
#
# 	PaymentMethod 
#
# 	Created: 			26 Aug 2016
# 	Last up: 	 		26 Aug 2018
#
from openerp import models, fields, api

from . import pm_vars

class PaymentMethod(models.Model):
	
	#_inherit='openhealth.sale_document'

	_name = 'openhealth.payment_method'


# ----------------------------------------------------------- Admin - Editable ------------------------------------------------------

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


	# For Admin Editing 
	@api.multi
	def state_force(self):  
		if self.state == 'done': 
			self.editable = True
			self.confirmed = False
		elif self.state == 'editable': 
			self.editable = False
			self.confirmed = True


# ----------------------------------------------------------- Locked ------------------------------------------------------

	# States 
	READONLY_STATES = {
		'draft': 		[('readonly', False)], 
		'sale': 		[('readonly', False)], 
		'done': 		[('readonly', True)], 	
		'editable': 	[('readonly', False)], 	
	}


	# Lines 
	pm_line_ids = fields.One2many(
			'openhealth.payment_method_line',
			'payment_method',
			string="Pago #", 
			
			states=READONLY_STATES, 
		)


	# Total 
	total = fields.Float(
			string = 'Total a pagar', 
			required=True, 

			states=READONLY_STATES, 			
		)


	# Saledoc 
	saledoc = fields.Selection(
			string="Tipo", 
			selection=pm_vars._sale_doc_type_list, 

			states=READONLY_STATES, 
		)



	# DNI 
	dni = fields.Char(
			'DNI', 

			states=READONLY_STATES, 
		)


	# Firm 
	firm = fields.Char(
			'Razón social',

			states=READONLY_STATES, 
		)


	# Ruc
	ruc = fields.Char(
			'Ruc', 

			states=READONLY_STATES, 
		)



# ----------------------------------------------------------- Computes ------------------------------------------------------

	# Name - Used by Order
	name = fields.Char(
			string="Pagos", 

			compute='_compute_name', 
		)
	@api.multi
	def _compute_name(self):
		#print 
		#print 'Compute Name'
		for record in self:
			record.name = 'PA-' + str(record.id).zfill(6)


	# state 
	state = fields.Selection(
			selection = [
							('draft', 'Inicio'),
							('sale', 'Pagado'),
							('done', 'Completo'),
							('editable', 	'e'),
						], 
			string='Estado',	
			default='draft',

			compute="_compute_state",
		)

	@api.multi
	#@api.depends('state')
	def _compute_state(self):
		#print 
		#print 'Compute State'
		for record in self:
			record.state = 'draft'
			if record.balance == 0.0		and		record.saledoc != False:
				record.state = 'sale'
			if record.confirmed:
				record.state = 'done'
			if record.editable:
				record.state = 'editable'


	# Balance 
	balance = fields.Float(
			string = 'Saldo',  
			readonly=True, 
			default=0, 
		)


	# Nr Payments
	nr_pm = fields.Char(
			default=2, 
		)


# ----------------------------------------------------------- Actions ------------------------------------------------------
	# go_back
	@api.multi 
	def go_back(self):
		#print
		#print 'PM - Go Back'

		self.confirmed = True 
		# Order
		self.order.state = 'sent'
		self.order.x_dni = self.dni
		self.order.x_ruc = self.ruc

		return self.order.open_myself() 
	# go_back


# ----------------------------------------------------------- Primitives ------------------------------------------------------

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
			required=True, 
			#states=READONLY_STATES, 
		)

	# Partner 
	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 
			required=True, 
			readonly=True, 
		)

	# Vspace 
	vspace = fields.Char(
			' ', 
			readonly=True
		)


# ----------------------------------------------------------- Onchanges ------------------------------------------------------

	# Onchange Pm Line Ids 
	@api.onchange('pm_line_ids')
	def _onchange_pm_line_ids(self):
		#print 
		#print 'On change - Line'
		pm_total = 0
		ctr = 1
		for line in self.pm_line_ids:
				pm_total = pm_total + line.subtotal
				ctr = ctr + 1 
		self.balance = self.total - pm_total 
		self.nr_pm = ctr
	# _onchange_pm_line_ids


	# On change Sale Doc 
	@api.onchange('saledoc')
	def _onchange_saledoc(self):
		#print 
		#print 'On change - Saledoc'
		if self.balance == 0.0:
			self.state = 'sale'
	# _onchange_saledoc



# ----------------------------------------------------------- CRUD ------------------------------------------------------
	# Write 
	@api.multi
	def write(self,vals):
		#print
		#print 'Payment Method  - Write'
		#print vals


		# Update Partner - Dni, Ruc, Firm 
		if 'dni' in vals: 
			dni = vals['dni']
			self.partner.x_dni = dni 

		if 'ruc' in vals: 
			ruc = vals['ruc']
			self.partner.x_ruc = ruc 

		if 'firm' in vals: 
			firm = vals['firm']
			self.partner.x_firm = firm 


		#Write your logic here
		res = super(PaymentMethod, self).write(vals)
		#Write your logic here

		return res
	# write 
