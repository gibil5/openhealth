# -*- coding: utf-8 -*-
"""
	Management - Data model

	SRP
		Responsibility of this class: 
		Create a data model for the Management report.

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
	_order = 'date_begin desc'
	#_inherit = 'openhealth.management_fields'  # Dep !


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


# ----------------------------------------------------------- Repo -------------
	# Name 
	name = fields.Char(
			string="Nombre", 		
			required=True, 
		)

	# Amount Total Year
	total_amount_year = fields.Float(
			'Monto Total Año',
			default=0,
		)

	# Dates
	date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
			required=True,
		)

	date_end = fields.Date(
			string="Fecha Fin",
			default=fields.Date.today,
			required=True,
		)

	# Amount
	total_amount = fields.Float(
			#'Total Monto',
			#'Total',
			'Monto Total',
			readonly=True,
			default=0,
		)

	# Date Test
	date_test = fields.Datetime(
			string="Fecha Test", 
		)

	# Percentage Total Amount Year
	per_amo_total = fields.Float(
			'Porc Monto Año',
		)

	# State
	state = fields.Selection(			
			selection=[
							('stable', 'Estable'),
							('unstable', 'Inestable'),
			],
			string='Estado',
			#readonly=False,
			default='unstable',
			#index=True,
		)


	# Spacing
	vspace = fields.Char(
			' ', 
			readonly=True
		)

# ----------------------------------------------------------- Totals -----------
	# Sales
	total_count = fields.Integer(
			'Nr Ventas',
			readonly=True,
		)

	# Ticket
	total_tickets = fields.Integer(
			'Nr Tickets',
			readonly=True,
		)

	# Ratios
	ratio_pro_con = fields.Float(
			'Ratio (proc/con) %',
		)

# ----------------------------------------------------------- Percentages -------------------------
	per_amo_products = fields.Float(
			'% Monto Productos',
		)

	per_amo_consultations = fields.Float(
			'% Monto Consultas',
		)

	per_amo_procedures = fields.Float(
			'% Monto Procedimientos',
		)

	per_amo_other = fields.Float(
			'Porc Monto',
		)

	per_nr_products = fields.Float(
			'Porc Nr',
		)

	per_nr_consultations = fields.Float(
			'Porc Nr',
		)

	per_nr_procedures = fields.Float(
			'Porc Nr',
		)

	per_nr_other = fields.Float(
			'Porc Nr',
		)

	per_amo_co2 = fields.Float(
			'% Monto Co2',
		)

	per_amo_exc = fields.Float(
			'% Monto Exc',
		)

	per_amo_ipl = fields.Float(
			'% Monto Ipl',
		)

	per_amo_ndyag = fields.Float(
			'% Monto Ndyag',
		)

	per_amo_quick = fields.Float(
			'% Monto Quick',
		)

	per_amo_medical = fields.Float(
			'% Monto TM',
		)

	per_amo_cosmetology = fields.Float(
			'% Monto Cosmiatria',
		)

	per_amo_topical = fields.Float(
			'% Monto Cremas',
		)

	per_amo_card = fields.Float(
			'% Monto Vip',
		)

	per_amo_kit = fields.Float(
			'% Monto Kits',
		)

# ----------------------------------------------------------- Amounts -----------------------------

	amo_products = fields.Float(
			'Monto Productos',
		)

	amo_procedures = fields.Float(
			'Monto Procedimientos',
		)

	amo_consultations = fields.Float(
			'Monto Consultas',
		)

	amo_other = fields.Float(
			'Monto Otros',
		)

	amo_credit_notes = fields.Float(
			'Monto Notas de Credito',
		)

	amo_co2 = fields.Float(
			'Monto Co2',
		)

	amo_exc = fields.Float(
			'Monto Exc',
		)

	amo_ipl = fields.Float(
			'Monto Ipl',
		)

	amo_ndyag = fields.Float(
			'Monto Ndyag',
		)

	amo_quick = fields.Float(
			'Monto Quick',
		)

	amo_medical = fields.Float(
			'Monto TM',
		)

	amo_cosmetology = fields.Float(
			'Monto Cosmiatria',
		)

	amo_services = fields.Float(
			'Monto Servicios',
		)

	amo_topical = fields.Integer(
			'Monto Cremas',
		)

	amo_card = fields.Integer(
			'Monto Vip',
		)

	amo_kit = fields.Integer(
			'Monto Kits',
		)

# ----------------------------------------------------------- Numbers ----------
	nr_procedures = fields.Integer(
			'Nr Procs',
		)

	nr_consultations = fields.Integer(
			'Nr Consultas',
		)

	nr_products = fields.Integer(
			'Nr Productos',
		)

	nr_other = fields.Integer(
			'Nr Otros',
		)

	nr_credit_notes = fields.Integer(
			'Nr Notas de Credito',
		)

	# Procedures
	nr_co2 = fields.Integer(
			'Nr Co2',
		)

	nr_exc = fields.Integer(
			'Nr Exc',
		)

	nr_ipl = fields.Integer(
			'Nr Ipl',
		)

	nr_ndyag = fields.Integer(
			'Nr Ndyag',
		)

	nr_quick = fields.Integer(
			'Nr Quick',
		)

	nr_medical = fields.Integer(
			'Nr TM',
		)

	nr_cosmetology = fields.Integer(
			'Nr Cosmiatria',
		)

	# Nr Services
	nr_services = fields.Integer(
			'Nr Servicios',
		)

	# Prods
	nr_topical = fields.Integer(
			'Nr Cremas',
		)

	nr_card = fields.Integer(
			'Nr Vip',
		)

	nr_kit = fields.Integer(
			'Nr Kits',
		)

# ----------------------------------------------------------- Avg --------------
	avg_other = fields.Float(
			'Precio Prom. Otros',
		)

	avg_products = fields.Float(
			'Precio Prom. Productos',
		)

	avg_consultations = fields.Float(
			'Precio Prom. Consultas',
		)

	avg_procedures = fields.Float(
			'Precio Prom. Procedimientos',
		)

	avg_services = fields.Float(
			'Precio Prom. Servicios',
		)

	# Products
	avg_topical = fields.Float(
			'Precio Prom. Cremas',
		)

	avg_card = fields.Float(
			'Precio Prom. Vip',
		)

	avg_kit = fields.Float(
			'Precio Prom. Kits',
		)

	# Procedures
	avg_co2 = fields.Float(
			'Precio Prom. Co2',
		)

	avg_exc = fields.Float(
			'Precio Prom. Exc',
		)

	avg_ipl = fields.Float(
			'Precio Prom. Ipl',
		)

	avg_ndyag = fields.Float(
			'Precio Prom. Ndyag',
		)

	avg_quick = fields.Float(
			'Precio Prom. Quick',
		)

	avg_medical = fields.Float(
			'Precio Prom. TM',
		)

	avg_cosmetology = fields.Float(
			'Precio Prom. Cosmiatria',
		)

