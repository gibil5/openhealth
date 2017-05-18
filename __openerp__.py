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

		Clínica Chavarri\n

		Laser - EMR - Min - Ama - Docean\n

		Last built: 	18 May 2017

		Created: 	 	7 Sep 2016

		Active for: 		9 months.

		---



		This is my first extension for oeHealth.

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
			- ...
			
			
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
	#'depends': ['base', 'oehealth'],
	'depends': ['base', 'oehealth'],





	# always loaded
	'data': [

		'views/actions.xml',






		# ----------------------------------------------------------- Reporting ------------------------------------------------------
		#'views/example_report.xml',
		'views/order_report.xml',







		# ----------------------------------------------------------- Security ------------------------------------------------------
		'security/ir.model.access.csv',
		'security/ir.rule.xml',





		'data/base_data_users.xml',
		'security/openhealth_security.xml',




		# ----------------------------------------------------------- Base ------------------------------------------------------

		# Base - Form and List Actions - Must be the first 
		'views/base.xml',		# Dependencies - Actions 
		'views/other.xml',




		# ----------------------------------------------------------- DATA ------------------------------------------------------
		'data/base_data_physicians.xml',
		
		'data/odoo_data_products.xml',
		
		'data/odoo_data_services_co2.xml',
		'data/odoo_data_services_exc.xml',
		'data/odoo_data_services_m22.xml',
		'data/odoo_data_services_med.xml',
		'data/odoo_data_services_cos.xml',
		
		'data/odoo_data_services_consult.xml',



		#'views/base_data.xml',




		# ----------------------------------------------------------- First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',




		# Orders
		'views/orders/order_line.xml',
		
		'views/orders/order.xml',
		#'views/orders/payment_methods.xml',
		'views/orders/events.xml',




		# Sale Documents
		'views/sale_documents/sale_documents.xml',

		'views/sale_documents/receipts.xml',
		'views/sale_documents/invoices.xml',
		
		'views/sale_documents/advertisements.xml',
		'views/sale_documents/sale_notes.xml',
		'views/sale_documents/ticket_receipts.xml',
		'views/sale_documents/ticket_invoices.xml',
		'views/sale_documents/payment_methods.xml',



		# Sessions
		'views/sessions/session.xml',


		# Controls
		'views/controls/control.xml',


		# Evaluations
		'views/evaluations/evaluation.xml',




		# Services
		'views/services/service.xml',


		# Procedures
		'views/procedures/procedure.xml',



		# Consultation
		'views/consultations/consultation.xml',




		# Recommendation
		'views/recommendations/recommendation.xml',





		# Treatments 
		'views/treatments/treatment.xml',




		# Cosmetologies
		'views/cosmetologies/cosmetology.xml',


		# Physicians 
		'views/physicians/physician.xml',

		# Patients 
		'views/patients/patient.xml',




		# Appointments
		'views/appointments/appointment.xml',



		# Products
		'views/products/product.xml',		



		# Menus
		'views/menus.xml',






		# Statics  
		# Style 
		'views/openhealth.xml',		






		# ----------------------------------------------------------- Second Level ------------------------------------------------------

		# Sessions - 2 
		'views/sessions/session_med.xml',
		'views/sessions/session_configuration.xml',
		'views/sessions/session_cos.xml',
		'views/sessions/session_measures.xml',



		# Evaluations - 2
		'views/evaluations/evaluation_oeh.xml',




		# Services - 2  
		'views/services/service_co2.xml',
		'views/services/service_co2_zone.xml',
		'views/services/service_excilite.xml',
		'views/services/service_excilite_zone.xml',
		'views/services/service_ipl.xml',
		'views/services/service_ipl_zone.xml',
		'views/services/service_ndyag.xml',
		'views/services/service_ndyag_zone.xml',
		'views/services/service_medical.xml',
		'views/services/service_medical_zone.xml',
		'views/services/service_cosmetology.xml',
		'views/services/service_cosmetology_zone.xml',





		# Procedures - 2  
		'views/procedures/procedure_controls.xml',
		'views/procedures/procedure_sessions.xml',		
		'views/procedures/procedure_cos.xml',
		'views/procedures/procedure_cos_sessions.xml',		



		# Consultation - 2
		'views/consultations/consultation_med.xml',
		'views/consultations/consultation_med_first.xml',
		'views/consultations/consultation_cos.xml',
		'views/consultations/consultation_cos_first.xml',



		# Treatments - 2 
		'views/treatments/treatment_consultations.xml',
		'views/treatments/treatment_orders.xml',
		'views/treatments/treatment_procedures.xml',
		'views/treatments/treatment_appointments.xml',
		'views/treatments/treatment_reservations.xml',
		'views/treatments/treatment_sessions.xml',
		'views/treatments/treatment_controls.xml',
		'views/treatments/treatment_services.xml',





		# Cosmetologies - 2 
		'views/cosmetologies/cosmetology_services.xml',
		'views/cosmetologies/cosmetology_orders.xml',
		'views/cosmetologies/cosmetology_procedures.xml',
		'views/cosmetologies/cosmetology_sessions.xml',
		'views/cosmetologies/cosmetology_appointments.xml',
		'views/cosmetologies/cosmetology_consultations.xml',
		'views/cosmetologies/cosmetology_reservations.xml',



		# Patients - 2 
		'views/patients/patient_personal.xml',
		'views/patients/patient_treatments.xml',
		'views/patients/patient_control_docs.xml',
		'views/patients/patient_appointments.xml',
		'views/patients/patient_cosmetologies.xml',



		# Appointments - 2
		'views/appointments/calendar.xml',
		'views/appointments/appointment_cos.xml',


		],





	'data_jx': [

	],




	# only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],
	
	
	

	# Static - CSS - This is it.
	'css': ['static/src/css/jx.css'],

	#'js': ['static/src/js/progressbar.js'],

}


