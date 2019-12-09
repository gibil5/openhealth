# -*- coding: utf-8 -*-
#
# 	Management Order Line - Clean This !
# 
# 	Created: 			28 May 2018
# 	Last updated: 		 9 Dec 2019
#
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars
from openerp.addons.openhealth.models.emr import prodvars

import openerp.addons.decimal_precision as dp

class management_order_line(models.Model):
	"""
	Used by 
		Management 
			For Doctor Sales Report
		Account
			For Txt generation
	"""
	#_inherit='openhealth.line'

	_name = 'openhealth.management.order.line'

	_description = "Openhealth Management Order Line"



# ----------------------------------------------------------- Inherited from line.py ------------------------------------------------------
	# Name 
	name = fields.Char(
			string="Nombre", 		
			#required=True, 
		)


	# Date Created 
	x_date_created = fields.Datetime(
			#string='Fecha', 
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


	# Product Product 
	product_id = fields.Many2one(
			
			'product.product', 
			
			string='Producto', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 			
			#required=True, 
		)


	# Total 
	price_total = fields.Float(
			string='Total', 
			readonly=True, 
			store=True, 

			compute='_compute_amount', 
		)


	# Compute - Total and Subtotal 
	@api.multi
	#@api.depends('product_uom_qty', 'price_unit')
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
				#'price_unit_tax': unit_tax,
			})


	# Subtotal 
	price_subtotal = fields.Float(
			string='Subtotal', 
			readonly=True, 
			store=True, 

			compute='_compute_amount', 
		)
	

	# Unit 
	price_unit = fields.Float(
			'Precio Unit.', 
			digits=dp.get_precision('Product Price'), 
			default=0.0, 
			required=True, 
		)


# ----------------------------------------------------------- Families ------------------------------------------------------


# ----------------------------------------------------------- 2019 !!! -------------------------------------
	# Family 
	family = fields.Selection(

			string = "Familia - 9 Dec", 	

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

			#required=False, 
			required=True, 
		)



	# Sub Family
	sub_family = fields.Char(
			string = "Sub-familia - 9 Dec",
			selection=prodvars._treatment_list,

			#required=False,
			required=True, 
		)	



# ----------------------------------------------------------- Handles -----------------------------

	# Management 
	management_id = fields.Many2one(
			'openhealth.management',
			ondelete='cascade',
		)

	# Doctor 
	doctor_id = fields.Many2one(			
			'openhealth.management.doctor.line',
			ondelete='cascade', 			
		)

	# Doctor Day
	doctor_day_id = fields.Many2one(			
			'openhealth.management.day.doctor.line',
			ondelete='cascade', 			
		)




	# Sales TKR
	management_tkr_id = fields.Many2one(			
			'openhealth.management',
			ondelete='cascade',		
		)



	# Account - Txt
	container_id = fields.Many2one(
			'openhealth.container', 
			ondelete='cascade',
		)





# ----------------------------------------------------------- Fields ------------------------------------------------------

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



# ----------------------------------------------------------- Electronic - Dep ? ------------------------------------------------------

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

			#required=True, 
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




# ----------------------------------------------------------- Account Txt ---------------------

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





