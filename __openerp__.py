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

		Last built: 	3 December 2017 - Yey !

		Created: 	 	11 Sep 2016

		Active for: 	15 months !!!

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




	# Dependencies - Very important !
	# ------------------------------
	#'depends': ['base', 'oehealth'],
	'depends': ['base', 'oehealth', 'base_multi_image'],
	#'depends': ['base', 'oehealth', 'base_multi_image', 'mail', 'purchase'],


#'depends': ['mail','contacts'],





	# always loaded
	'data': [




		# ----------------------------------------------------------- Views - Actions ------------------------------------------------------
		'views/actions.xml',







		# ----------------------------------------------------------- Reports ------------------------------------------------------
		#'views/example_report.xml',
		#'views/order_report.xml',



		# Patient
		'reports/patient.xml',
		'reports/patient_consultation.xml',
		'reports/patient_sessions.xml',
		'reports/patient_controls.xml',


		# Closing 
		'reports/closing.xml',





		# Ticket 
		'reports/report_ticket_sale_proof.xml',

		'reports/report_ticket_sale_order.xml',
		'reports/report_ticket_invoice.xml',
		'reports/report_ticket_receipt.xml',





		# Sales 
		'views/reports/report_sale_search.xml',
		'views/reports/report_sale.xml',
		'views/reports/report_sale_doctors.xml',
		'views/reports/report_sale_months.xml',
		'views/reports/report_sale_months_platform.xml',
		'views/reports/report_sale_months_physician.xml',




		# Deprecated ? 
		#'views/reports/report_sale_months_phy_ala.xml',
		#'views/reports/report_sale_months_phy_can.xml',
		#'views/reports/report_sale_months_phy_esc.xml',
		#'views/reports/report_sale_months_phy_gon.xml',
		#'views/reports/report_sale_months_phy_mon.xml',
		#'views/reports/report_sale_months_phy_vas.xml',

		#'views/reports/oh_report_sale.xml',








		# ----------------------------------------------------------- Data ------------------------------------------------------

		# Check that data is not updated. All the time. 


		# Categs
		'data/base_data_categs.xml',			# check


		# Users 
		'data/users/base_data_users_managers.xml',	# check 
		'data/users/base_data_users_staff.xml',		# check 
		'data/users/base_data_users_almacen.xml',		# check 
		'data/users/base_data_users_doctors.xml',		# check 
		'data/users/base_data_users_assistants.xml',	# check
		'data/users/base_data_users_platform.xml',	# check
		'data/users/base_data_users_cash.xml',		# check 






		# Moved 

		# Products 
		'data/prods/odoo_data_products.xml',			# check 
		'data/prods/odoo_data_services_co2.xml',		# check
		'data/prods/odoo_data_services_exc.xml',		# check
		'data/prods/odoo_data_services_m22.xml',		# check
		'data/prods/odoo_data_services_med.xml',		# check
		'data/prods/odoo_data_services_cos.xml',		# check
		'data/prods/odoo_data_services_consult.xml',	# check


		# Doctors
		'data/base_data_physicians.xml',				# check





		# Pricelists 
		'data/pricelists.xml',							# check





		# Suppliers 
		'data/suppliers.xml',							# DEPRECATED - Very 
		#'data/supplier_services.xml',					# DEPRECATED - Very





		# Deprecated 
		#'data/base_data_patients.xml',	
		#'data/odoo_data_cards.xml',	
		#'views/base_data.xml',			









		# ----------------------------------------------------------- Security ------------------------------------------------------


		#'security/openhealth_security_oe.xml',		# DEPRECATED !!! 
		#'security/openhealth_security.xml',


		'security/openhealth_security_readers.xml',
		'security/openhealth_security_buf.xml',
		'security/ir.model.access.csv',
		'security/ir.rule.xml',


		






		# ----------------------------------------------------------- Views - Base ------------------------------------------------------

		# Base - Form and List Actions - Must be the first 
		'views/base.xml',			# Very important - All Actions should go here - Dependencies
		'views/other.xml',







		# ----------------------------------------------------------- Views ------------------------------------------------------



		# Purchases 
		#'views/purchase/purchase.xml',





		# Mail template - Deprecated 
		#'views/mail/rfq_send.xml',




		# Stock 
		'views/stock/stock.xml',
		'views/stock/stock_picking.xml',
		'views/stock/stock_move.xml',


		'data/stock_move_data.xml',
		#'views/stock/stock_move_selector.xml',








		# ----------------------------------------------------------- Views - First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',




		# Orders
		'views/orders/order_line.xml',
		'views/orders/order.xml',



		# Account invoice
		'views/account_invoices/account_invoice.xml',





		# Events 
		'views/orders/events.xml',






		# Counters 
		'views/counters/counter.xml',


		# Companies 
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
		#'views/sessions/session.xml',


		# Controls
		'views/controls/control.xml',




		# Images 
		#'views/images/image.xml',			# Deprecated ? 
		#'views/images/image_full.xml',		# Deprecated ? 
		
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






		# Cosmetologies		- Deprecated ?  - No !
		'views/cosmetologies/cosmetology.xml',






		# Physicians 
		'views/physicians/physician.xml',


		
		# Patients 
		'views/patients/patient.xml',



		# Partners
		'views/partners/partner.xml',





		# Quotations 
		'views/quotations/quotation.xml',






		# Appointments
		'views/appointments/appointment.xml',



		# Products
		'views/products/product.xml',		




		# Cards 
		'views/cards/card.xml',




		# closings 
		'views/closings/closings.xml',





		# Menus
		'views/menus/menus.xml',
		'views/menus/menus_reporting.xml',
		'views/menus/menus_reporting_pla.xml',
		'views/menus/menus_reporting_phy.xml',
		

		#'views/menus/menus_reporting_phy_ala.xml',
		
		'views/menus/menus_openhealth.xml',






		# Statics  
		# Style 
		'views/openhealth.xml',		






		# ----------------------------------------------------------- Views - Second Level ------------------------------------------------------

		# Sessions
		'views/sessions/session.xml',

		# Sessions - 2 
		#'views/sessions/session_med.xml',



		#'views/sessions/session_config_manual.xml',
		#'views/sessions/session_config_fractional.xml',
		#'views/sessions/session_measures.xml',

		
		#'views/sessions/session_cos.xml',





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


		# Deprecated ? - No !
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


