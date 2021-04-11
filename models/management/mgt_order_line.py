# -*- coding: utf-8 -*-
"""
	Management Order Line - Clean This !
	Added pylint validation in Atom

	Created: 			28 may 2018
	Last up: 	 		29 mar 2021
"""
from __future__ import absolute_import

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


from openerp.addons.openhealth.models.order import ord_vars

#from openerp.addons.openhealth.models.libs import lib
#from openerp.addons.openhealth.models.commons.libs import lib
from openerp.addons.openhealth.models.commons.libs import commons_lib as lib

from openerp.addons.openhealth.models.commons import prodvars


class MgtOrderLine(models.Model):
	"""
	Used by
		Management
			For Doctor Sales Report

		Account ?
			For Txt generation
	"""
	_name = 'openhealth.management.order.line' 
	_description = "Openhealth Management Order Line"


# -------------------------------------------------- Handles internal ----------
	# Management
	management_id = fields.Many2one(
			'openhealth.management',
			ondelete='cascade',
		)

	# Mgt Doctor line
	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',
			ondelete='cascade',
		)

	# Mgt Doctor Day
	doctor_day_id = fields.Many2one(
			'openhealth.management.day.doctor.line',
			ondelete='cascade',
		)

	# Mgt Sales TKR
	#management_tkr_id = fields.Many2one(
	#		'openhealth.management',
	#		ondelete='cascade',
	#	)


# -------------------------------------------------- Handles external ----------
	# Product Product
	product_id = fields.Many2one(
			'product.product',
			string='Producto',
			domain=[('sale_ok', '=', True)],
			change_default=True,
			ondelete='restrict',
		)

	# Account - Txt - Dep !
	#container_id = fields.Many2one(
	#		'openhealth.container',
	#		ondelete='cascade',
	#	)




# ----------------------------------------------------------- View -------------

# -------------------------------------------------- Inherited from line.py ----
	# Name
	name = fields.Char(
			string="Nombre",
		)

	# Date Created
	x_date_created = fields.Datetime(
			string='Fecha y Hora',
		)

	# Date Order
	date_order_date = fields.Datetime(
		'Fecha',
	)

	# Qty
	product_uom_qty = fields.Float(
			string='Cantidad',
			digits=dp.get_precision('Product Unit of Measure'),
			default=1.0,
			required=True,
		)



	# Unit
	price_unit = fields.Float(
			'Precio Unit.',
			digits=dp.get_precision('Product Price'),
			default=0.0,
			required=True,
		)

# ----------------------------------------------------------- Families ----------------------------

# ----------------------------------------------------------- 2019 !!! ---------
	# Family
	family = fields.Selection(
			string = "Familia",
			selection = [
							('gynecology',	'Ginecologia'),
							('echography',	'Ecografia'),
							('promotion',	'Promocion'),
							('credit_note',	'Notas de Credito'),
							('other',	'Otros'),
							('topical',	'Cremas'),
							('card',	'Tarjeta'),
							('kit',		'Kit'),
							('product',	'Producto'),
							('consultation',		'Consulta'),
							('consultation_gyn',	'Consulta Ginecológica'),
							('consultation_100',	'Consulta 100'),
							('consultation_0',		'Consulta Gratuita'),
							('procedure',	'Procedimiento'),
							('laser',		'Laser'),
							('cosmetology',	'Cosmiatría'),
							('medical',		'Tratamiento Médico'),
			],
			required=True,
		)

	# Sub Family
	sub_family = fields.Char(
			string = "Sub-familia",
			selection=prodvars._treatment_list,
			required=True,
		)



# ----------------------------------------------------------- Fields -----------
	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente",
		)

	# Doctor
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico",
		)

	# Serial Number
	serial_nr = fields.Char(
			'Serial Nr',
		)

	# Delta
	delta = fields.Integer(
			'Delta',
		)

	# State
	state = fields.Selection(
			selection = ord_vars._state_list,
			string='Estado',
			readonly=False,
			default='draft',
		)

# ------------------------------------------------------ Electronic - Dep ? ----
	# Receptor
	receptor = fields.Char(
			string='Receptor',
			required=True,
		)

	id_doc_type = fields.Char(
			string='Doc Id Tipo',
			default=".",
			required=True,
		)

	id_doc_type_code = fields.Char(
			string='Codigo',
			default=".",
			required=True,
		)

	id_doc = fields.Char(
			'Doc Id',
			default=".",
		)

	# Order
	x_type = fields.Char(
			'Tipo',
		)

	type_code = fields.Char(
			'Codigo',
		)

	currency_code = fields.Char(
			'Moneda',
			default="PEN",
		)

# ----------------------------------------------------------- Account Txt ------
	# Firm
	firm = fields.Char(
			'Firm',
			default='SERVICIOS MÉDICOS ESTÉTICOS S.A.C',
		)

	# Ruc
	ruc = fields.Char(
			'Ruc',
			default='20523424221',
		)

	# Address
	address = fields.Char(
			'Address',
			#default='Jr. Lima 150',
			default='Av. La Merced 161',
		)

	# Ubigeo
	ubigeo = fields.Char(
			'Ubigeo',
			default='150101',
		)

	# Country
	country = fields.Char(
			'Country',
			default='PE',
		)


# ----------------------------------------------------- Computes ---------------

	@api.multi
	def _compute_amount(self):
		for line in self:
			price_unit = line.price_unit
			unit_net, unit_tax = lib.get_net_tax(price_unit)
			total = price_unit * line.product_uom_qty
			net, tax = lib.get_net_tax(total)
			line.update({
				'price_total': total,
				'price_subtotal': total,
				'price_net': net,
				'price_tax': tax,
				'price_unit_net': unit_net,
			})

	# Total
	price_total = fields.Float(
			string='Total',
			readonly=True,
			store=True,

			compute='_compute_amount',
		)

	# Subtotal
	price_subtotal = fields.Float(
			string='Subtotal',
			readonly=True,
			store=True,

			compute='_compute_amount',
		)


# ----------------------------------------------------- Static methods ----------
	# Create
	@staticmethod
	def create_oh(order, line, doctor, management):
		#print('Class method - create')
		#print(line)
		#print(line.product_id)
		#print(line.product_id.name)

		# init
		env = management.env['openhealth.management.order.line']

		# Receptor and id_doc
		# invoice
		if order.x_type in ['ticket_invoice', 'invoice']:
			receptor = order.patient.x_firm.upper()
			id_doc = order.patient.x_ruc
			id_doc_type = 'ruc'
			id_doc_type_code = '6'
		# receipt
		else:
			receptor = order.patient.name
			id_doc = order.patient.x_id_doc
			id_doc_type = order.patient.x_id_doc_type
			id_doc_type_code = order.patient.x_id_doc_type_code

		# Price
		price_unit = line.price_unit

		# Families
		family = line.product_id.get_family()
		sub_family = line.product_id.get_subsubfamily()

		# Create
		order_line = env.create({
									# Receptor
									'receptor': 	receptor,

									# Id Doc
									'id_doc': 				id_doc,
									'id_doc_type': 			id_doc_type,
									'id_doc_type_code': 	id_doc_type_code,

									# Order
									'name': order.name,
									'patient': 		order.patient.id,
									'doctor': order.x_doctor.id,
									'serial_nr': order.x_serial_nr,
									'date_order_date': order.date_order,
									'x_date_created': order.date_order,

									# Type of Sale
									'type_code': 	order.x_type_code,
									'x_type': 		order.x_type,

									# State
									'state': order.state,

									# Handles
									'doctor_id': doctor.id,
									'management_id': management.id,

									# Line
									'product_id': 			line.product_id.id,
									'product_uom_qty': 		line.product_uom_qty,

									# Price
									'price_unit': 			price_unit,

									# Families
									'family': family,
									'sub_family': sub_family,
		})
		return order_line
