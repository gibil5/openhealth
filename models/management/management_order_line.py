# -*- coding: utf-8 -*-
#
# 	Management Order Line - Clean This !
# 
# 	Created: 			28 May 2018
# 	Last updated: 		 4 Nov 2018
#
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars
from openerp.addons.openhealth.models.emr import prodvars

class management_order_line(models.Model):
	
	_name = 'openhealth.management.order.line'
	
	_inherit='openhealth.line'

	_description = "Openhealth Management Order Line"








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




# ----------------------------------------------------------- Dep ? -----------------------------

	# Container  
	container_id = fields.Many2one(
			'openhealth.container', 
			ondelete='cascade',
		)


# ----------------------------------------------------------- Emitter - Dep ? ---------------------

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


	# Ubigeo
	ubigeo = fields.Char(
			'Ubigeo',
			default='150101', 
		)

	# Address
	address = fields.Char(
			'Address', 
			#default='Jr. Lima 150', 
			default='Av. La Merced 161', 
		)


	# Country
	country = fields.Char(
			'Country', 
			default='PE', 
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


	# Family 
	family = fields.Selection(
			string = "Familia", 	
			selection = [
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
			required=False, 
		)


	# Sub Family
	sub_family = fields.Char(
			string = "Sub-familia",
			selection=prodvars._treatment_list,
			required=False,
		)	

	# State 
	state = fields.Selection(
			selection = ord_vars._state_list, 
			string='Estado',	
			readonly=False,
			default='draft',
		)





# ----------------------------------------------------------- Actions ------------------------------------------------------
	
	# Update Fields
	@api.multi
	def update_fields(self):
		print()
		print('2018 - Update Fields - Order')


		# If Product 
		if self.product_id.type in ['product','consu']: 	# Products and Consumables 
			# Family 
			if self.product_id.x_family in ['kit']: 	# Kits 
				self.family = 'topical'
			else: 										# Vip and Topical 
				self.family = self.product_id.x_family
			# Sub family
			self.sub_family = 'product'


		# If Service 
		else: 
			# Family 
			self.family = self.product_id.x_family

			# Correct 
			if (self.product_id.x_family  == 'consultation'): 
				if self.price_unit  == 100: 
					self.family = 'consultation_100'			
				elif self.price_unit  == 0: 
					self.family = 'consultation_0'

			# Sub family 
			# Cosmetology 
			if self.product_id.x_family == 'cosmetology': 
				self.sub_family = 'cosmetology'

			# Medical, Other 
			else: 
				self.sub_family = self.product_id.x_treatment 

	# update_fields
