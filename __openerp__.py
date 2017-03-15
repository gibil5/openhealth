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
	'depends': ['base', 'oehealth'],





	# always loaded
	'data': [



		# ----------------------------------------------------------- Security ------------------------------------------------------
		
		# Important !!!
		'security/ir.model.access.csv',
		'security/ir.rule.xml',





		# ----------------------------------------------------------- Forms and Menus ------------------------------------------------------

		# Base - Form and List Actions - Must be the first 
		'views/base.xml',		# Dependencies - Actions 




		'views/other.xml',



		
		# Orders
		'views/orders/order.xml',
		'views/orders/order_line.xml',

		'views/orders/payment_methods.xml',
		
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
		'views/sessions/session_configuration.xml',

		'views/sessions/session_cos.xml',
		'views/sessions/session_med.xml',

		'views/sessions/session_measures.xml',





		# Controls
		'views/controls/control.xml',
		#'views/controls/control_protocols.xml',


		# Evaluations
		'views/evaluations/evaluation.xml',
		'views/evaluations/evaluation_oeh.xml',


		# Products
		'views/products/product.xml',		
		'views/products/product_excilite.xml',
		'views/products/product_ipl.xml',
		'views/products/product_ndyag.xml',
		'views/products/product_medical.xml',

		

		# Services
		'views/services/service.xml',
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




		# Procedures
		'views/procedures/procedure.xml',
		'views/procedures/procedure_controls.xml',
		'views/procedures/procedure_sessions.xml',		

		#'views/procedures/procedure_appointment.xml',
		#'views/procedures/procedure_controls_appointment.xml',
		#'views/procedures/procedure_configuration.xml',

		'views/procedures/procedure_cos.xml',
		'views/procedures/procedure_cos_sessions.xml',		






		# Consultation
		'views/consultations/consultation.xml',

		'views/consultations/consultation_med.xml',
		#'views/consultations/consultation_first.xml',
		'views/consultations/consultation_med_first.xml',

		#'views/consultations/consultation_order.xml',
		#'views/consultations/consultation_appointment.xml',
		#'views/consultations/consultation_services_co2.xml',
		#'views/consultations/consultation_services_ipl.xml',
		#'views/consultations/consultation_services_excilite.xml',
		#'views/consultations/consultation_services_ndyag.xml',
		#'views/consultations/consultation_medical_treatment.xml',


		'views/consultations/consultation_cos.xml',
		'views/consultations/consultation_cos_first.xml',






		# Treatments 
		'views/treatments/treatment.xml',
		'views/treatments/treatment_consultations.xml',


		'views/treatments/treatment_orders.xml',
		

		'views/treatments/treatment_procedures.xml',
		'views/treatments/treatment_appointments.xml',
		'views/treatments/treatment_reservations.xml',
		'views/treatments/treatment_sessions.xml',
		'views/treatments/treatment_controls.xml',
		'views/treatments/treatment_services.xml',





		# Cosmetologies
		'views/cosmetologies/cosmetology.xml',
		'views/cosmetologies/cosmetology_services.xml',
		'views/cosmetologies/cosmetology_orders.xml',
		'views/cosmetologies/cosmetology_procedures.xml',
		'views/cosmetologies/cosmetology_sessions.xml',
		'views/cosmetologies/cosmetology_appointments.xml',
		'views/cosmetologies/cosmetology_consultations.xml',


		'views/cosmetologies/cosmetology_reservations.xml',




		# Therapists 
		#'views/therapists/therapist.xml',



		# Physicians 
		'views/physicians/physician.xml',




		# Patients 
		'views/patients/patient.xml',
		'views/patients/patient_personal.xml',
		'views/patients/patient_treatments.xml',
		'views/patients/patient_control_docs.xml',
		'views/patients/patient_appointments.xml',

		'views/patients/patient_cosmetologies.xml',



		# Appointments
		'views/appointments/appointment.xml',

		'views/appointments/calendar.xml',

		'views/appointments/appointment_cos.xml',



		# Menus
		'views/menus.xml',




		# Static - Stylesheet 
		'views/openhealth.xml',		

	],


	# only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],
	
	
	

	# Static - CSS - This is it.
	'css': ['static/src/css/jx.css'],
}


