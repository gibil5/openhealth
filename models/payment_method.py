# -*- coding: utf-8 -*-
#
# 		PaymentMethod 
#
# 		Created: 			26 Aug 2016
# 		Last up: 	 		31 Aug 2018
#
from openerp import models, fields, api
import pm_vars
from openerp import _
from openerp.exceptions import Warning
import pat_vars

class PaymentMethod(models.Model):

	_name = 'openhealth.payment_method'


# ----------------------------------------------------------- Id Doc - Deperecated ! ------------------------------------------------------

	# Id Doc 
	#id_doc = fields.Char(
	#		'Nr. Doc.', 
	#		required=True, 
	#		readonly=True, 
	#	)

	# Id Document Type 
	#id_doc_type = fields.Selection(
	#		selection = pat_vars._id_doc_type_list, 
	#		string='Tipo de documento', 
	#		required=True, 
	#		readonly=True, 
	#	)


	# DNI 
	#dni = fields.Char(
	#		'DNI', 
	#		states=pm_vars.READONLY_STATES, 
	#	)


	# Firm 
	firm = fields.Char(
			'Razón social',
			#states=pm_vars.READONLY_STATES, 
			readonly=True, 
		)


	# Ruc
	ruc = fields.Char(
			'Ruc', 
			#states=pm_vars.READONLY_STATES, 
			readonly=True, 
		)



# ----------------------------------------------------------- On Change ------------------------------------------------------
	
	# Onchange Pm Line Ids 
	@api.onchange('pm_line_ids')
	def _onchange_pm_line_ids(self):
		print 
		print 'On change - Line'

		pm_total = 0
		ctr = 1
		for line in self.pm_line_ids:
			pm_total = pm_total + line.subtotal
			ctr = ctr + 1 
		
		#self.balance = self.total - pm_total 
		
		self.balance = self.total - pm_total 
		self.pm_total = pm_total
		self.nr_pm = ctr
	
		if self.balance < 0: 
			
			# Raise Error 
			msg = "Error: Subtotal incorrecto !"
			raise Warning(_(msg))
	
	# _onchange_pm_line_ids



# ----------------------------------------------------------- Paid ------------------------------------------------------

	# Total Paid
	pm_total = fields.Float(
			string = 'Total pagado', 
			#required=True, 
			default=0, 

			compute="_compute_pm_total",
		)

	@api.multi
	#@api.depends('total', 'pm_total')
	def _compute_pm_total(self):
		print 
		print 'Compute Pm Total'

		for record in self:

			pm_total = 0

			for line in record.pm_line_ids:

				pm_total = pm_total + line.subtotal

			record.pm_total = pm_total
			



	# Balance 
	balance = fields.Float(
			string = 'Saldo',  
			readonly=True, 
			default=0, 

			compute="_compute_balance",
		)

	@api.multi
	#@api.depends('total', 'pm_total')
	def _compute_balance(self):		
		print 
		print 'Compute Balance'

		for record in self:
			record.balance = record.total - record.pm_total




# ----------------------------------------------------------- Locked ------------------------------------------------------
	# Lines 
	pm_line_ids = fields.One2many(
			'openhealth.payment_method_line',
			'payment_method',
			string="Pago #", 
			
			#states=READONLY_STATES, 
		)


	# Total 
	total = fields.Float(
			string = 'Total a pagar', 
			required=True, 

			states=pm_vars.READONLY_STATES, 			
		)




	# Saledoc 
	saledoc = fields.Selection(
			string="Tipo", 
			selection=pm_vars._sale_doc_type_list, 

			states=pm_vars.READONLY_STATES, 
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
		#self.order.x_dni = self.dni
		#self.order.x_ruc = self.ruc

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

			#required=True,
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


	# On change Sale Doc 
	@api.onchange('saledoc')
	def _onchange_saledoc(self):
		#print 
		#print 'On change - Saledoc'
		if self.balance == 0.0:
			self.state = 'sale'
	# _onchange_saledoc



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


# ----------------------------------------------------------- CRUD ------------------------------------------------------
	# Write 
	@api.multi
	def write(self,vals):
		#print
		#print 'Payment Method  - Write'
		#print vals


		# Update Partner - Dni, Ruc, Firm 
		#if 'dni' in vals: 
		#	dni = vals['dni']
		#	self.partner.x_dni = dni 

		#if 'ruc' in vals: 
		#	ruc = vals['ruc']
		#	self.partner.x_ruc = ruc 

		#if 'firm' in vals: 
		#	firm = vals['firm']
		#	self.partner.x_firm = firm 


		#Write your logic here
		res = super(PaymentMethod, self).write(vals)
		#Write your logic here

		return res
	# write 
