# -*- coding: utf-8 -*-
"""
	Management - Data model

	Using: vectors and functional programming.

	Created: 			28 may 2018
	Last up: 			 6 dec 2020
"""
from __future__ import print_function
from openerp import models, fields
from . import mgt_vars

# ------------------------------------------------------------------- Class ----
class Management(models.Model):
	"""
	Contains only methods.
	"""
	_name = 'openhealth.management'
	
	_inherit = 'openhealth.management_fields'


# ----------------------------------------------------------- Relational --------------------------

# ------------------------------------------------------------- One2many -------
	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'management_id',
		)

	# Sales
	sale_line_tkr = fields.One2many(
			'openhealth.management.order.line',
			'management_tkr_id',
		)

	# Family
	family_line = fields.One2many(
			'openhealth.management.family.line',
			'management_id',
		)

	# Sub_family
	sub_family_line = fields.One2many(
			'openhealth.management.sub_family.line',
			'management_id',
		)

	# Daily
	day_line = fields.One2many(
			'openhealth.management.day.line',
			'management_id',
		)

	# Doctor line - For Update Daily
	doctor_line = fields.One2many(
			'openhealth.management.doctor.line',
			'management_id',
		)

	# Doctor Day
	doctor_daily = fields.One2many(
			'doctor.daily',
			'management_id',
		)

	# Productivity
	productivity_day = fields.One2many(
			'productivity.day',
			'management_id',
		)

	# Patient
	patient_line = fields.One2many(
			'openhealth.management.patient.line',
			'management_id',
		)

# ------------------------------------------------------------- Many2one -------
	# Report Sale Product
	report_sale_product = fields.Many2one(
			'openhealth.report.sale.product'
		)

# ----------------------------------------------------------- Configurator -----
	# Default Configurator
	def _get_default_configurator(self):
		return self.env['openhealth.configurator.emr'].search([('x_type', 'in', ['emr']),], limit=1,)

	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			default=_get_default_configurator,
		)



# ----------------------------------------------------------- PL - Natives -----
	mode = fields.Selection([('normal', 'Normal'),
							('test', 'Test'),
							#('legacy', 'Legacy'),
							],
		default='normal',
		required=True,
	)

	# All Year Max and Min
	pl_max = fields.Boolean('Max')

	pl_min = fields.Boolean('Min')

# ----------------------------------------------------------- PL - Natives -----
	# New Procedures

	# Echography
	nr_echo = fields.Integer(
			'Nr Ecografia',
		)
	amo_echo = fields.Float(
			'Monto Ecografia',
		)
	per_amo_echo = fields.Float(
			'% Monto Ecografia',
		)
	avg_echo = fields.Float(
			'Precio Prom. Ecografia',
		)

	# Gynecology
	nr_gyn = fields.Integer(
			'Nr Ginecologia',
		)
	amo_gyn = fields.Float(
			'Monto Ginecologia',
		)
	per_amo_gyn = fields.Float(
			'% Monto Ginecologia',
		)
	avg_gyn = fields.Float(
			'Precio Prom. Ginecologia',
		)

	# Promotions
	nr_prom = fields.Integer(
			'Nr Promocion',
		)
	amo_prom = fields.Float(
			'Monto Promocion',
		)
	per_amo_prom = fields.Float(
			'% Monto Promocion',
		)
	avg_prom = fields.Float(
			'Precio Prom. Promocion',
		)

# ----------------------------------------------------------- PL Natives -------
	# Credit Notes
	per_amo_credit_notes = fields.Float(
		)

	# Consultations
	nr_sub_con_med = fields.Integer(
			'Nr Cons Med',
		)

	amo_sub_con_med = fields.Float(
			'Monto Cons Med',
		)

	per_amo_sub_con_med = fields.Float(
			'% Monto Cons Med',
		)

	# Gynecology
	nr_sub_con_gyn = fields.Integer(
			'Nr Cons Gin',
		)

	amo_sub_con_gyn = fields.Float(
			'Monto Cons Gin',
		)

	per_amo_sub_con_gyn = fields.Float(
			'% Monto Cons Gin',
		)

	# Chavarri Brand
	nr_sub_con_cha = fields.Integer(
			'Nr Cons Dr. Chav',
		)

	amo_sub_con_cha = fields.Float(
			'Monto Cons Dr. Chav',
		)

	per_amo_sub_con_cha = fields.Float(
			'% Monto Sub Cons Dr. Chav',
		)

	# Families and Sub Families
	per_amo_families = fields.Float(
			'% Monto Familias',
		)

	per_amo_subfamilies = fields.Float(
			'% Monto Sub Familias',
		)

	#per_amo_subfamilies_products = fields.Float(
	#		'% Monto Sub Familias Productos',
	#	)

	#per_amo_subfamilies_procedures = fields.Float(
	#		'% Monto Sub Familias Procedimientos',
	#	)


	rsp_count = fields.Integer(
			'RSP Nr',
		)

	rsp_total = fields.Float(
			'RSP Monto',
		)

	rsp_count_delta = fields.Integer(
			'RSP Nr Delta',
		)

	rsp_total_delta = fields.Float(
			'RSP Total Delta',
		)

# ----------------------------------------------------------- PL - Admin -------
	admin_mode = fields.Boolean()

	nr_products_stats = fields.Integer()

	nr_consultations_stats = fields.Integer()

	nr_procedures_stats = fields.Integer()


# ----------------------------------------------------------- Fields -----------
	# Type Array
	type_arr = fields.Selection(
			selection=mgt_vars._type_arr_list,
			string='Type Array',
			required=True,
			#default='ticket_receipt,ticket_invoice',
			default='all',
		)

	state_arr = fields.Selection(
			selection=mgt_vars._state_arr_list,
		)

# ----------------------------------------------------------- PL - Fields ------
	# Owner
	owner = fields.Selection(
			[
				('month', 'Month'),
				('year', 'Year'),
				('account', 'Account'),
				('aggregate', 'Aggregate'),
			],
			default='month',
			required=True,
		)

	month = fields.Selection(
			selection=mgt_vars._month_order_list,
			string='Mes',
			#required=True,
		)

# ----------------------------------------------------------- QC ---------------
	year = fields.Selection(
			selection=mgt_vars._year_order_list,
			string='Año',
			default='2020',
			required=True,
		)

	delta_fast = fields.Float(
			'Delta Fast',
		)

	delta_doctor = fields.Float(
			'Delta Doctor',
		)

# -------------------------------------------------------------------------------------------------
# Functional vars
# -------------------------------------------------------------------------------------------------

	vec_amount = fields.Float(
		'Todos',
	)
	vec_count = fields.Integer(
		'.',
	)

	vec_products_amount = fields.Float(
		'Productos',
	)
	vec_products_count = fields.Integer(
		'.',
	)

	vec_services_amount = fields.Float(
		'Servicios',
	)
	vec_services_count = fields.Integer(
		'.',
	)


	# Sub
	vec_co2_amount = fields.Float(
		'Co2',
	)
	vec_co2_count = fields.Integer(
		'.',
	)

	vec_exc_amount = fields.Float(
		'Exc',
	)
	vec_exc_count = fields.Integer(
		'.',
	)

	vec_ipl_amount = fields.Float(
		'Ipl',
	)
	vec_ipl_count = fields.Integer(
		'.',
	)

	vec_ndy_amount = fields.Float(
		'Ndyag',
	)
	vec_ndy_count = fields.Integer(
		'.',
	)

	vec_qui_amount = fields.Float(
		'Quick',
	)
	vec_qui_count = fields.Integer(
		'.',
	)


	# Medical
	vec_med_amount = fields.Float(
		'Medical',
	)
	vec_med_count = fields.Integer(
		'.',
	)

	vec_cos_amount = fields.Float(
		'Cosmeto',
	)
	vec_cos_count = fields.Integer(
		'.',
	)

	vec_gyn_amount = fields.Float(
		'Gyn',
	)
	vec_gyn_count = fields.Integer(
		'.',
	)

	vec_ech_amount = fields.Float(
		'Echo',
	)
	vec_ech_count = fields.Integer(
		'.',
	)

	vec_pro_amount = fields.Float(
		'Promo',
	)
	vec_pro_count = fields.Integer(
		'.',
	)

	# Prod
	vec_top_amount = fields.Float(
		'Topical',
	)
	vec_top_count = fields.Integer(
		'.',
	)

	vec_vip_amount = fields.Float(
		'Vip',
	)
	vec_vip_count = fields.Integer(
		'.',
	)

	vec_kit_amount = fields.Float(
		'Kit',
	)
	vec_kit_count = fields.Integer(
		'.',
	)
