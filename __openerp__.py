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

		Laser - EMR - Min - Ama - Docean - Ooor - Github - Travis - Coverage - Proliant\n

		Last built: 	10 October 2017 - Yey !

		Created: 	 	10 Sep 2016

		Active for: 	12 months !

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
	#'depends': ['base', 'oehealth'],
	'depends': ['base', 'oehealth', 'base_multi_image'],





	# always loaded
	'data': [

		'views/actions.xml',






		# ----------------------------------------------------------- Reporting ------------------------------------------------------
		#'views/example_report.xml',
		#'views/order_report.xml',

		'reports/patient.xml',
		'reports/patient_consultation.xml',
		'reports/patient_sessions.xml',
		'reports/patient_controls.xml',





		'views/reports/report_sale_search.xml',
		'views/reports/report_sale.xml',
		'views/reports/report_sale_doctors.xml',


		'views/reports/report_sale_months.xml',
		'views/reports/report_sale_months_platform.xml',


		'views/reports/report_sale_months_physician.xml',

		#'views/reports/report_sale_months_phy_ala.xml',
		#'views/reports/report_sale_months_phy_can.xml',
		#'views/reports/report_sale_months_phy_esc.xml',
		#'views/reports/report_sale_months_phy_gon.xml',
		#'views/reports/report_sale_months_phy_mon.xml',
		#'views/reports/report_sale_months_phy_vas.xml',

		

		#'views/reports/oh_report_sale.xml',






		# ----------------------------------------------------------- Security ------------------------------------------------------
		'data/base_data_categs.xml',





		'data/base_data_users_managers.xml',
		'data/base_data_users_staff.xml',

		'data/base_data_users_almacen.xml',

		'data/base_data_users_doctors.xml',
		'data/base_data_users_assistants.xml',
		
		'data/base_data_users_platform.xml',
		'data/base_data_users_cash.xml',




		'data/base_data_patients.xml',




		'security/openhealth_security_oe.xml',

		#'security/openhealth_security.xml',
		'security/openhealth_security_buf.xml',

		

		

		'security/ir.model.access.csv',
		'security/ir.rule.xml',


		




		# ----------------------------------------------------------- Base ------------------------------------------------------

		# Base - Form and List Actions - Must be the first 
		'views/base.xml',			# Very important - All Actions should go here - Dependencies
		'views/other.xml',






		# ----------------------------------------------------------- DATA ------------------------------------------------------

		# Doctors
		'data/base_data_physicians.xml',
		

		# Products 
		'data/odoo_data_products.xml',
		'data/odoo_data_services_co2.xml',
		'data/odoo_data_services_exc.xml',
		'data/odoo_data_services_m22.xml',
		'data/odoo_data_services_med.xml',
		'data/odoo_data_services_cos.xml',
		'data/odoo_data_services_consult.xml',




		# Pricelists 
		'data/products_pricelist.xml',


		# Vip cards
		'data/base_data_patients.xml',	
		'data/odoo_data_cards.xml',	







		#'views/base_data.xml',			# Deprecated 

		# ----------------------------------------------------------- First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',




		# Orders
		'views/orders/order_line.xml',
		
		'views/orders/order.xml',
		#'views/orders/payment_methods.xml',
		#'views/orders/events.xml',



		'views/counters/counter.xml',


		'views/companies/company.xml',





		# DEPRECATED 
		#'views/sale_documents/sale_documents.xml',



		# Sale Documents
		'views/sale_documents/payment_methods.xml',
		'views/sale_documents/payment_method_line.xml',
		
		'views/sale_documents/receipts.xml',
		'views/sale_documents/invoices.xml',
		'views/sale_documents/advertisements.xml',
		'views/sale_documents/sale_notes.xml',
		'views/sale_documents/ticket_receipts.xml',
		'views/sale_documents/ticket_invoices.xml',




		# Sessions
		'views/sessions/session.xml',


		# Controls
		'views/controls/control.xml',


		# Images 
		#'views/images/image.xml',
		#'views/images/image_full.xml',
		
		'views/images/image_view.xml',




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




		# Cosmetologies		- Deprecated ? 
		#'views/cosmetologies/cosmetology.xml',



		# Physicians 
		'views/physicians/physician.xml',



		# Patients 
		'views/patients/patient.xml',




		# Partners
		'views/partners/partner.xml',





		# Appointments
		'views/appointments/appointment.xml',



		# Products
		'views/products/product.xml',		




		# Cards 
		'views/cards/card.xml',





		# Menus
		'views/menus/menus.xml',
		'views/menus/menus_reporting.xml',
		'views/menus/menus_reporting_pla.xml',

		#'views/menus/menus_reporting_phy.xml',
		#'views/menus/menus_reporting_phy_ala.xml',
		
		'views/menus/menus_openhealth.xml',






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
		#'views/services/service_cosmetology.xml',
		#'views/services/service_cosmetology_zone.xml',





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
		#'views/cosmetologies/cosmetology_services.xml',
		#'views/cosmetologies/cosmetology_orders.xml',
		#'views/cosmetologies/cosmetology_procedures.xml',
		#'views/cosmetologies/cosmetology_sessions.xml',
		#'views/cosmetologies/cosmetology_appointments.xml',
		#'views/cosmetologies/cosmetology_consultations.xml',
		#'views/cosmetologies/cosmetology_reservations.xml',




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
	
	
	

	# Static - CSS - STYLE
	'css': ['static/src/css/jx.css'],

	#'js': ['static/src/js/progressbar.js'],

}


