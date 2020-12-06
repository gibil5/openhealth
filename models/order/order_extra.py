# -*- coding: utf-8 -*-
"""
	Order - Extra

	Created: 			 6 dec 2020
	Last up: 			 6 dec 2020
"""
from __future__ import print_function
from openerp import models, fields, api
from . import ord_funcs
from . import raw_funcs

class OrderExtra(models.Model):
	"""
    Order extra.
    Everything that does not fit in a tight model.
	"""
	_inherit = 'sale.order'


# ----------------------------------------------------------- Checksum ----------------------------
	# Checksum
	x_checksum = fields.Float(
			'Checksum',
			readonly=True,
			default=5,
		)

	# Checksum Func
	@api.multi
	def checksum(self):
		"""
		Checksum
		"""
		#obj = check_order.CheckOrder()

		#self.check_payment_method()
		self.x_pm_total = raw_funcs.check_payment_method(self.x_payment_method.pm_line_ids)

		delta = int(self.amount_total) - int(self.x_pm_total)
		if delta != 0:
			self.x_checksum = 1
		else:
			self.x_checksum = 0


	# Pm Total
	x_pm_total = fields.Float(
			'Total MP',
			readonly=True,
		)

# ---------------------------------------------- Credit Note - Block Flow -------------------------
	# Block Flow
	@api.multi
	def block_flow(self):
		"""
		Used by Credit Notes
		"""
		print()
		print('Block Flow')
		if self.state in ['credit_note']:
			self.x_block_flow = True
			self.x_credit_note_owner.x_block_flow = True
		elif self.state in ['sale']:
			self.x_block_flow = True

	# Unblock Flow
	@api.multi
	def unblock_flow(self):
		"""
		Used by Credit Notes
		"""
		print()
		print('Unblock Flow')
		if self.state in ['credit_note']:
			self.x_block_flow = False
			self.x_credit_note_owner.x_block_flow = False

# ---------------------------------------------- Credit Note - Update -----------------------------
	# Update CN
	@api.multi
	def update_credit_note(self):
		"""
		Update Credit note
		"""
		print()
		print('Update CN')
		print(self.x_credit_note_type)

		if self.state in ['credit_note']:
			self.x_credit_note_owner_amount = self.x_credit_note_owner.amount_total
			self.order_line.unlink()
			name = self.x_credit_note_type
			# Search
			product = self.env['product.product'].search([
															('x_name_short', 'in', [name]),
															],
															#order='date_begin asc',
															limit=1,
														)
			print(product)
			product_id = product.id
			print(product_id)
			line = self.order_line.create({
											'product_id': product_id,
											'price_unit': self.x_credit_note_amount,
											'product_uom_qty': 1,
											'order_id': self.id,
										})
	# update_credit_note


# ----------------------------------------------------- Admin --------------------------
	@api.multi
	def correct_serial_number(self):
		"""
		Correct Serial Number - Admin only
		"""
		print()
		print('correct_serial_number')
		self.x_serial_nr = ord_funcs.get_serial_nr(self.x_type, self.x_counter_value, self.state)

# ----------------------------------------------------- Fixers --------------------------
	@api.multi
	def fix_treatment(self):
		"""
		Fix Treatment
		"""
		print()
		print('Fix Treatment')
		fixer = fix_treatment.FixTreatment(self.env['openhealth.treatment'], self.patient.id, self.x_doctor.id)
		fixer.fix()


# ----------------------------------------------------------- Remove and Reset ------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset order
		"""
		self.x_payment_method.unlink()
		self.state = 'draft'

	# Remove - Protected for Sales
	@api.multi
	def remove_myself(self):
		"""
		Remove myself
		"""
		if self.state in ['credit_note']:
			#raise UserError("Advertencia: La Nota de Crédito va a ser eliminada del sistema !")
			self.reset()
			self.unlink()
		else:
			#raise UserError("Advertencia: La Venta va a ser convertida en Presupuesto !")
			self.reset()

	# Remove Force
	@api.multi
	def remove_myself_force(self):
		"""
		high level support for doing this and that.
		"""
		self.reset()
		self.unlink()
