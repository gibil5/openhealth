# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH - MIN
# 
#

{
	'name': "Open Health - MIN",

	'summary': """
		Extension for Odoo-oeHealth. 
		Treatments. 
	""",

	'description': """

		EMR (Electronic Medical Records) for Laser\n
		Clinica Chavarri\n


		Built: 	23 Jan 2017.\n 

		Installed: 	 	7 Sep 2016.\n 
		Active: 4 months.\n
		---
		\n



		This is my first extension for oeHealth.
		Completely independent and self-referecing.\n
		It provides the following objects:
			- Patients,
			- Treatments,
			- Evaluations,
			- Consultations,
			- Procedures,
			- Controls,
			- Sessions,
			- Services,
			- Orders,
			- Appointments,
			- Calendar, 
			
			
	""",

	'author': "DataMetrics",
	'website': "http://jrevilla.com/",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
	# for the full list
	'category': 'Health',
	'version': '1.0',




	# Very important !!!
	# --------------
	# any module necessary for this one to work correctly
	#'depends': ['base'],
	#'depends': ['base', 'oehealth', 'openextension'],
	#'depends': ['base', 'openextension'],
	#'depends': ['base', 'oehealth'],





	#'depends': ['base', 'oehealth', 'openextension', 'openhealth-patient'],
	#'depends': ['base', 'oehealth', 'openhealth-patient'],

	'depends': ['base', 'oehealth'],





	# always loaded
	'data': [


# ----------------------------------------------------------- Generated ------------------------------------------------------
		#'views/views.xml',
		#'views/templates.xml',
		


# ----------------------------------------------------------- Deprecated ------------------------------------------------------

		# Learning 
		#'views/learning/learn.xml',	- Deprecated
		#'views/evaluations/consultation_procedures.xml',
		# Invoices
		#'views/treatments/invoice.xml',

		# jx_eval
		#'views/evaluations/jx_eval_co2.xml',
		#'views/evaluations/jx_eval_excilite.xml',
		#'views/evaluations/jx_eval_ipl.xml',
		#'views/evaluations/jx_eval_ndyag.xml',



		#'views/evaluations/consultation_quotation.xml',        
		#'views/evaluations/quotation.xml',



		


		# Doctors
		#'views/doctors/doctor.xml',

		# Partners 
		#'views/partners/partner.xml',


		# Open Extension
		#'views/treatments/treatment_oex.xml',



		#'views/treatments/treatment_sales.xml',
		#'views/treatments/treatment_quotations.xml',


		#'views/patients/patient_lab.xml',
		#'views/patients/patient_med.xml',



		#'views/consultations/consultation_services.xml',		
		#'views/consultations/consultation_order_lines.xml',

		
		# Templates
		#'views/templates/template.xml',	# Template - Change Title





	],
	# only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],
	
	
	
	# Static - jx 
	#'js': ['static/src/js/widget_radio.js'],
	#'qweb': ['static/src/xml/widget_radio.xml'],
	#'css': ['static/src/css/my_css.css'],


	# CSS - This is it.
	'css': ['static/src/css/jx.css'],

}


