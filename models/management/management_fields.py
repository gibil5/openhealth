# -*- coding: utf-8 -*-
"""
	Management Fields

	Created: 			28 nov 2020
	Last up: 			28 nov 2020
"""
from openerp import models, fields, api

class ManagementFields(models.Model):
	"""
	Contains the model fields.
	"""
	_name = 'openhealth.management_fields'
	_inherit = 'openhealth.repo'
	_order = 'date_begin desc'

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
