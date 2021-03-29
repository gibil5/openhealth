# -*- coding: utf-8 -*-
"""
 	Patient Line - Used by Marketing
 
 	Only Data model. No functions.

	Created: 				16 May 2018
 	Last up: 	 			29 mar 2021
"""
from openerp import models, fields, api
from openerp.addons.openhealth.models.patient import pat_vars
from openerp.addons.openhealth.models.product import prodvars

#from openerp.addons.openhealth.models.libs import eval_vars
#from openerp.addons.openhealth.models.commons.libs import eval_vars
from commons import eval_vars

#class PatientLine(models.Model):
class MktPatientLine(models.Model):
	
	_name = 'openhealth.patient.line'

	_order = 'date_create asc'


# ----------------------------------------------------------- First Contact ------------------------------------------------------
	
	# First Contact 
	first_contact = fields.Selection(

			selection = pat_vars._first_contact_list, 
		
			string = 'Primer contacto',
		)
	
	mea_recommendation = fields.Integer(
			'Pri Recomendación', 
		)

	mea_tv = fields.Integer(
			'Pri Tv', 
		)

	mea_radio = fields.Integer(
			'Pri Radio', 
		)

	mea_internet = fields.Integer(
			'Pri Internet', 
		)

	mea_website = fields.Integer(
			'Pri Website', 
		)

	mea_mail_campaign = fields.Integer(
			'Pri Mail', 
		)

	mea_how_none = fields.Integer(
			'Pri Ninguno', 
		)

	mea_how_u = fields.Integer(
			'Pri Ind', 
		)




# ----------------------------------------------------------- Stats - Required ------------------------------------------------------

	# Address
	country = fields.Char(
			'Pais', 
			required=True,
		)

	city = fields.Char(
			'Ciudad', 
			required=True,
		)

	district = fields.Char(
			'Distrito', 
			required=True,
		)


	# Sex 
	sex = fields.Selection(
			selection = pat_vars._sex_type_list, 
			string="Sexo",
			#required=False, 
			required=True,
		)

	mea_m = fields.Integer(
			'M', 
			required=True,
		)

	mea_f = fields.Integer(
			'F', 
			required=True,
		)

	mea_u = fields.Integer(
			'U', 
			required=True,
		)



	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment', 
			string="Tratamiento", 
		)


	# Consultation 
	consultation = fields.Many2one(
			'openhealth.consultation', 
			string="Consulta", 
		)



# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Marketing Id 
	marketing_id = fields.Many2one(
			'openhealth.marketing', 
			ondelete='cascade', 
		)



	# Sales
	#sale_line = fields.One2many(
	#		'openhealth.marketing.order.line', 
	#		'patient_line_sale_id',
	#	)


	# Budgets
	#budget_line = fields.One2many(
	#		'openhealth.marketing.order.line', 
	#		'patient_line_budget_id',
	#	)


	# Consus
	consu_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_consu_id',
		)

	# Products
	product_line = fields.One2many(
			'openhealth.marketing.order.line', 

			'patient_line_product_id',
		)

	# Procedures
	#procedure_line = fields.One2many(
	#		'openhealth.marketing.order.line', 
	#		'patient_line_proc_id',
	#		string="Procedimientos", 
	#	)

	# Vip Sales
	order_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_id',
		)

	# Vip Sales - With Vip Card
	order_line_vip = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_id_vip',
		)

	# Recommendations
	reco_line = fields.One2many(
			'openhealth.marketing.recom.line', 
			'patient_line_id',
			string="Recom.", 
		)



# ----------------------------------------------------------- Native ------------------------------------------------------

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





	# Marketing

	emr = fields.Char(
			'HC', 
		)

	phone_1 = fields.Char(
			'Tel 1', 
		)

	phone_2 = fields.Char(
			'Tel 2', 
		)

	email = fields.Char(
			'Email', 
		)

	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 						
			selection = eval_vars._chief_complaint_list, 
			#required=False, 
			#readonly=True, 
		)

	diagnosis = fields.Char(
			'Diagnóstico', 
		)

	budget_date = fields.Datetime(
			'Pres. Fecha', 
		)

	#budget_amount = fields.Float(
	budget_amount = fields.Char(
			'Pres. Monto', 
		)

	budget_flag = fields.Boolean(
			'Flag', 
		)

	budget_prod = fields.Char(
			'Pres. Proc.', 
		)




# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Date Created 
	date_create = fields.Datetime(
			string="Fecha de Creación", 
		)

	# Date Record 
	date_record = fields.Datetime(
			string="Fecha de Registro", 
			#string="Fecha creación", 
		)






# ----------------------------------------------------------- Reco ------------------------------------------------------
	# Nr Reco 
	nr_reco = fields.Integer(
			#'Nr Recomendaciones', 
			'Nr Recom', 
			#default=-1, 
		)



# ----------------------------------------------------------- Sales ------------------------------------------------------


	# Nr Budgets 
	nr_budget = fields.Integer(
			#'Nr Presupuestos', 
			'Nr Presupuestos pendientes', 
			#default=-1, 
		)




	# Nr Sales 
	nr_sale = fields.Integer(
			'Nr Ventas', 
			#default=-1, 
		)

	# Nr Consus 
	nr_consu = fields.Integer(
			'Nr Consultas', 
			#default=-1, 
		)



	# Nr Products 
	nr_products = fields.Integer(
			'Nr Productos', 
			#default=-1, 
		)



	# Nr Proc
	nr_proc = fields.Integer(
			'Nr Procedimientos', 
			#default=-1, 
		)




	# Nr lines Vip 
	nr_lines_vip = fields.Integer(
			#'Ventas Usando la tarjeta Vip', 
			'Compras Con Tarjeta Vip', 
			default=-1, 
		)





# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Date Vip card 
	vip_date = fields.Datetime(
			string="Fecha Vip", 
		)



	# Age 
	age = fields.Char(
			string = "Edad", 		
		)

	age_years = fields.Integer(
			string = "Edad", 		
			#default=0, 
			default=-1, 
		)

	dob = fields.Date(
			string="Fecha nacimiento",
			required=False, 
		)









	# Education 
	education = fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
		)

	mea_first = fields.Integer(
			'Edu Primaria', 
		)

	mea_second = fields.Integer(
			'Edu Secundaria', 
		)
	
	mea_technical = fields.Integer(
			'Edu Instituto', 
		)
	
	mea_university = fields.Integer(
			'Edu Universidad', 
		)
	
	mea_masterphd = fields.Integer(
			'Edu Posgrado', 
		)

	mea_edu_u = fields.Integer(
			'Edu Ind', 
		)
	




	# Vip 
	vip = fields.Boolean(
			string = 'Vip',
		)

	mea_vip = fields.Integer(
			'Vip', 
		)

	mea_vip_no = fields.Integer(
			'No Vip', 
		)




	# Function
	function = fields.Char(
			'Ocupación', 
		)

