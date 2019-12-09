# -*- coding: utf-8 -*-
"""
 	Marketing
 
 	Only Data model. No functions.

	Created: 				19 May 2018
 	Last up: 	 			 9 Dec 2019
"""
from __future__ import print_function
import datetime
from timeit import default_timer as timer
import collections
from openerp import models, fields, api
from . import mkt_funcs
from . import lib_marketing

class Marketing(models.Model):

	_inherit='openhealth.repo'

	_name = 'openhealth.marketing'

	_order = 'date_begin asc,name asc'



# ----------------------------------------------------------- QC ----------------------------------

	delta_patients = fields.Float(
			'Delta Pacientes',
		)

	delta_sales = fields.Float(
			'Delta Ventas',
		)

	delta_recos = fields.Float(
			'Delta Recos',
		)


	owner = fields.Selection(
			[
				('year', 'Year'),
				('month', 'Month'),
			],
		)




# ----------------------------------------------------------- Inheritable ------------------------------------------------------
	# Count
	total_count = fields.Integer(
			#'Total Ventas',
			#'Nr Ventas',
			'Nr Pacientes',
			readonly=True, 
		)



# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Patient Lines 
	patient_line = fields.One2many(
			'openhealth.patient.line', 
			'marketing_id', 
		)

	# Histo Lines 
	histo_line = fields.One2many(
			'openhealth.histo.line', 
			'marketing_id', 
		)

	# Media Lines 
	media_line = fields.One2many(
			'openhealth.media.line', 
			'marketing_id', 
		)

	# Country 
	country_line = fields.One2many(
			'openhealth.country.line', 
			'marketing_id', 
		)

	# City 
	city_line = fields.One2many(
			'openhealth.city.line', 
			'marketing_id', 
		)

	# District 
	district_line = fields.One2many(
			'openhealth.district.line', 
			'marketing_id', 
		)




# ----------------------------------------------------------- Counts ------------------------------
	patient_budget_count = fields.Integer(
			'Nr Presupuestos', 
		)

	patient_sale_count = fields.Integer(
			'Nr Ventas', 
		)

	patient_consu_count = fields.Integer(
			'Nr Consultas', 
		)

	patient_reco_count = fields.Integer(
			'Nr Recomendaciones', 
		)

	patient_proc_count = fields.Integer(
			'Nr Procedimientos', 
		)



# ----------------------------------------------------------- Fields - Stats ----------------------
	# Percentages - Float 


	# Age 
	age_undefined_per = fields.Float(
			'Error %',
			readonly=True,
			digits=(16,1), 
		)

	# Sex 
	sex_male_per = fields.Float(
			'M %',
			readonly=True, 
			digits=(16,1), 
		)

	sex_female_per = fields.Float(
			'F %',
			readonly=True, 
			digits=(16,1), 
		)

	sex_undefined_per = fields.Float(
			'Error %',
			readonly=True, 
			digits=(16,1), 
		)



	# First Contact 
	how_u_per = fields.Float(
			'No Definido %',
			readonly=True, 
			digits=(16,1), 
		)

	how_none_per = fields.Float(
			'Ninguno %',
			readonly=True, 
			digits=(16,1), 
		)

	how_reco_per = fields.Float(
			'Recomendación %',
			readonly=True, 
			digits=(16,1), 
		)

	how_tv_per = fields.Float(
			'Tv %',
			readonly=True, 
			digits=(16,1), 
		)

	how_radio_per = fields.Float(
			'Radio %',
			readonly=True, 
			digits=(16,1), 
		)

	how_inter_per = fields.Float(
			'Internet %',
			readonly=True, 
			digits=(16,1), 
		)

	how_web_per = fields.Float(
			'Web %',
			readonly=True, 
			digits=(16,1), 
		)

	how_mail_per = fields.Float(
			'Mail %',
			readonly=True, 
			digits=(16,1), 
		)



	# Education Level 
	edu_u_per = fields.Float(
			'No Definido %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_fir_per = fields.Float(
			'Primaria %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_sec_per = fields.Float(
			'Secundaria %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_tec_per = fields.Float(
			'Instituto %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_uni_per = fields.Float(
			'Universidad %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_mas_per = fields.Float(
			'Posgrado %',
			readonly=True, 
			digits=(16,1), 
		)


	# Vip 
	vip_true_per = fields.Float(
			'Vip Si %',
			readonly=True, 
			digits=(16,1), 
		)

	vip_false_per = fields.Float(
			'Vip No %',
			readonly=True, 
			digits=(16,1), 
		)



	# Age
	age_mean = fields.Float(
			'Edad Promedio',
			readonly=True, 

			digits=(16,1), 
		)

	age_max = fields.Integer(
			'Edad Max',
			readonly=True, 
		)

	age_min = fields.Integer(
			'Edad Min',
			readonly=True, 
		)

	age_undefined = fields.Integer(
			#'Edad Ind',
			'Edad Error',
			readonly=True, 
		)



	# Sex
	sex_male = fields.Integer(
			'Sexo M',
			readonly=True, 
		)

	sex_female = fields.Integer(
			'Sexo F',
			readonly=True, 
		)

	sex_undefined = fields.Integer(
			'Sexo Error',
			readonly=True, 	
		)



	# First Contact 
	how_u = fields.Integer(
			'No Definido',
			readonly=True, 
		)

	how_none = fields.Integer(
			'Pri Ninguno',
			readonly=True, 
		)

	how_reco = fields.Integer(
			'Pri Recomendación',
			readonly=True, 
		)

	how_tv = fields.Integer(
			'Pri Tv',
			readonly=True, 
		)

	how_radio = fields.Integer(
			'Pri Radio',
			readonly=True, 
		)

	how_inter = fields.Integer(
			'Pri Internet',
			readonly=True, 
		)

	how_web = fields.Integer(
			'Pri Web',
			readonly=True, 
		)

	how_mail = fields.Integer(
			'Pri Mail',
			readonly=True, 
		)



	# Education
	edu_u = fields.Integer(
			#'Edu Indefinido',
			'No Definido',
			readonly=True, 
		)

	edu_fir = fields.Integer(
			'Edu Primaria',
			readonly=True, 
		)

	edu_sec = fields.Integer(
			'Edu Secundaria',
			readonly=True, 
		)
	
	edu_tec = fields.Integer(
			'Edu Instituto',
			readonly=True, 
		)
	
	edu_uni = fields.Integer(
			'Edu Universidad',
			readonly=True, 
		)
	
	edu_mas = fields.Integer(
			'Edu Posgrado',
			readonly=True, 
		)

	# Vip 
	vip_true = fields.Integer(
			'Vip Si',
			readonly=True, 
		)

	vip_false = fields.Integer(
			'Vip No',
			readonly=True, 
		)

