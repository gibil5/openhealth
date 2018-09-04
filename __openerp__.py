# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH - MIN
#
###############################

{
	'name': "Open Health - MIN",

	'summary': """
		Fulcrum 
	""",


	'description': """

		4 Sep 2018

		Fulcrum 
		
		Code without Tests is broken by design.
		My Goal is to achieve Complete Coverage. 

		Stability by Design. Simplicity by Abstraction. 

		La Estabilidad se consigue por la disminución no por el aumento. 
		Dieter Rams is Less but Better. 

		More configuration and less programming, near than zero hacking.  

		Good order is the beginning of all good things. 



		EMR - Min - Docean - Github - Travis - Coverage - Proliant - User Stories - Cron Pg Dump - Unit Testing - Less but Better 
		- Statistical - Machine Learning - Object Oriented - Fulcrum - Coverage Testing \n

		Deprecated: Ooor, Testcafe, Auto Backup. 

		Created: 	 	11 Sep 2016
		Last up: 		24 Aug 2018 

		---


		Additional modules:
			- MRP (Manufacturing Ressource Planning). 
			- Purchase. 


		External:
			- Oehealth. 
			- Base multi image. 
			- Auto backup. 

		Python:
			- Unidecode. 
			- pysftp.
	""",

	'author': "DataMetrics",
	
	'website': "http://jrevilla.com/",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
	# for the full list
	#'category': 'Health',
	
	'category': 'Object Oriented',
	
	'version': '2.0',


	# Dependencies - Very important !
	# ------------------------------
	'depends': ['base', 'oehealth', 'base_multi_image'],



	# always loaded
	'data': [


		# ----------------------------------------------------------- Deprecated ------------------------------------------------------

		#'views/reports/report_sale_months_platform.xml',
		#'views/reports/report_sale_months_physician.xml',
		#'views/reports/report_sale_doctors.xml',

		#'views/sale_documents/receipts.xml',
		#'views/sale_documents/invoices.xml',
		#'views/sale_documents/advertisements.xml',
		#'views/sale_documents/sale_notes.xml',
		#'views/sale_documents/ticket_receipts.xml',
		#'views/sale_documents/ticket_invoices.xml',

		# Mail template - Deprecated 
		#'views/mail/rfq_send.xml',

		# Account invoice
		#'views/account_invoices/account_invoice.xml',

		# Quotations 
		#'views/quotations/quotation.xml',

		#'data/prods/data_products_consu.xml',			 

		# Users - Inactive - With pw
		#'data/users/base_data_users_inactive.xml',	

		#'views/stock/stock_picking.xml',

		#'views/menus/menus_inventory.xml',

		#'data/base_data_physicians_lines.xml',			


		#'views/product_managers/product_manager.xml',
		#'views/menus/menus_kardex.xml',



		# ----------------------------------------------------------- Stock Moves - Deprecated ??? ------------------------------------------------------
		#'data/stock_move_data.xml',
		#'views/stock/stock_move.xml',
		#'views/stock/stock_move_selector.xml',
		#'views/stock/stock_move_all.xml',



		# ----------------------------------------------------------- Cosmetology - Deprecated ! ------------------------------------------------------

		# Cosmetologies
		#'views/cosmetologies/cosmetology.xml',
		#'views/sessions/session_cos.xml',
		#'views/procedures/procedure_cos.xml',
		#'views/procedures/procedure_cos_sessions.xml',		
		#'views/consultations/consultation_cos.xml',
		#'views/consultations/consultation_cos_first.xml',
		#'views/appointments/appointment_cos.xml',




		# ----------------------------------------------------------- Quick ------------------------------------------------------
		
		#'views/patients/patient_quick.xml',			# Deprecated ? 




		# ----------------------------------------------------------- Style ------------------------------------------------------

		#'views/openhealth.xml',		


		
		# ----------------------------------------------------------- Reservations ------------------------------------------------------
		
		#'views/treatments/treatment_reservations.xml',			# Deprecated 


		# ----------------------------------------------------------- Deprecated ------------------------------------------------------
		#'views/report_sale/report_sale.xml',





		# ----------------------------------------------------------- Actions ------------------------------------------------------
		'reports/patient.xml',
		'views/patients/patient_actions.xml',
		'views/menus/menus_account.xml',




		# ----------------------------------------------------------- Recent ------------------------------------------------------

		# Reports
		'views/product_selectors/product_selector.xml',
		'views/orders/order_report_nex.xml',				# Estado de Cuenta
		
		'views/report_sale/report_sale_product.xml',
		
		'views/report_sale/item_counter.xml',


		# Accounting 
		'views/payment_methods/payment_method_line.xml',
		'views/account/account_line.xml',
		'views/account/account_contasis.xml',


		# Marketing 
		'views/marketing/marketing_order_line.xml',
		'views/marketing/marketing_reco_line.xml',
		'views/media/media_line.xml',
		'views/histogram/histogram.xml',
		'views/places/place.xml',
		'views/account/patient_line.xml',
		'views/account/patient_line_pivot.xml',
		'views/marketing/marketing.xml',
		'views/marketing/marketing_pivot.xml',


		# Management 
		'views/management/management_family_line.xml',
		'views/management/management_order_line.xml',
		'views/management/management_doctor_line.xml',
		'views/management/management.xml',


		# Exceptions 
		#'views/patients/patient_exceptions.xml',





		# ----------------------------------------------------------- Views - Base Actions ------------------------------------------------------

		# Base - Form and List Actions - Must be the first 
		'views/base.xml',										# Very important - All Actions should go here - Dependencies
		






		# ----------------------------------------------------------- Reports ------------------------------------------------------

		# Patient
		'reports/patient_consultation.xml',
		'reports/patient_sessions.xml',
		'reports/patient_controls.xml',

		# Formats
		'reports/paper_format.xml',

		# Ticket 
		'reports/report_ticket_invoice.xml',
		'reports/report_ticket_receipt.xml',
		
		# New Tickets 
		'reports/report_ticket_receipt_nex.xml',
		'reports/report_ticket_invoice_nex.xml',








		# ----------------------------------------------------------- Data ------------------------------------------------------

		# Check that data is not updated. All the time. 

		# Categs
		'data/base_data_categs_partners.xml',			
		'data/base_data_categs_prods.xml',			

		# Important 
		'views/pathologies/pathology.xml',
		'data/prods/data_pathologies.xml',			
		'data/prods/data_nexzones.xml',	

		# Zone
		'views/zones/zone.xml',
		'data/prods/data_zones_quick.xml',			 
		'data/prods/data_zones_co2.xml',			 
		'data/prods/data_zones_excilite.xml',			 
		'data/prods/data_zones_ipl.xml',			 
		'data/prods/data_zones_ndyag.xml',			 


		# Allergy 
		'views/allergies/allergy.xml',


		# Doctors
		'data/base_data_physicians.xml',				
		'data/base_data_physicians_inactive.xml',				
		'data/base_data_physicians_new.xml',				

		# Pricelists 
		'data/pricelists.xml',							
		'data/pricelist_quick.xml',						

		# Suppliers 
		'data/suppliers.xml',							# DEPRECATED - Very 

		# Generics 
		'data/users/base_data_users_generics.xml',	


		# Users - With pw
		'data/users/base_data_users_platform.xml',	
		'data/users/base_data_users_cash.xml',		
		'data/users/base_data_users_doctors.xml',

		'data/users/base_data_users_assistants.xml',	
		
		'data/users/base_data_users_staff.xml',		
		'data/users/base_data_users_almacen.xml',		
		'data/users/base_data_users_managers.xml',	
		'data/users/base_data_users_doctors_new.xml',		




		# ----------------------------------------------------------- Data - Products ------------------------------------------------------

		'data/prods/odoo_data_products.xml',
		'data/prods/odoo_data_products_new.xml',

		'data/prods/odoo_data_services_co2.xml',
		'data/prods/odoo_data_services_exc.xml',
		'data/prods/odoo_data_services_m22.xml',
		'data/prods/odoo_data_services_med.xml',
		'data/prods/odoo_data_services_consult.xml',
		'data/prods/odoo_data_services_cos.xml',








# ----------------------------------------------------------- Views ------------------------------------------------------


		# ----------------------------------------------------------- Views - Actions ------------------------------------------------------
		'views/services/service_actions.xml',
		
		'views/services/service_search.xml',




		# ----------------------------------------------------------- Views - First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',


		# Groups 
		'views/groups/groups.xml',


		# Orders
		'views/orders/order_line.xml',
		'views/orders/order.xml',
		'views/orders/order_admin.xml',
		'views/orders/order_search.xml',


		# Payment methods 
		'views/payment_methods/payment_methods.xml',


		# Counters 
		'views/counters/counter.xml',


		# Companies 
		'views/companies/company.xml',


		# Controls
		'views/controls/control.xml',


		# Images 
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
		#'views/recommendations/recommendation.xml',


		# Treatments 
		'views/treatments/treatment.xml',
		'views/treatments/treatment_actions.xml',


		# Physicians 
		'views/physicians/physician.xml',



		# Patients 
		'views/patients/patient.xml',


		'views/patients/patient_search.xml',



		# Partners
		'views/partners/partner.xml',
		'views/partners/partner_actions.xml',


		# Appointments
		'views/appointments/appointment.xml',
		'views/appointments/appointment_actions.xml',


		# Products
		'views/products/product.xml',		
		'views/products/product_actions.xml',		


		# Cards 
		'views/cards/card.xml',





		# Stock 
		'views/stock/stock.xml',
		'views/stock/stock_inventory.xml',








		# ----------------------------------------------------------- Views - Second Level ------------------------------------------------------

		# Sessions
		'views/sessions/session.xml',
		
		'views/sessions/session_config_simple.xml',
		'views/sessions/session_config_simple_2.xml',
		
		#'views/sessions/session_config_manual.xml',



		# Evaluations - 2
		'views/evaluations/evaluation_oeh.xml',



		# Services - 2  
		'views/services/service_product.xml',

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
		
		'views/services/service_quick.xml',

		'views/services/service_cosmetology.xml',
		'views/services/service_cosmetology_zone.xml',


		#'views/services/service_vip.xml',








		# Procedures - 2  
		'views/procedures/procedure_controls.xml',
		'views/procedures/procedure_sessions.xml',		


		# Consultation - 2
		'views/consultations/consultation_med.xml',
		'views/consultations/consultation_med_first.xml',
		

		# Treatments - 2 
		'views/treatments/treatment_appointments.xml',
		'views/treatments/treatment_orders.xml',
		'views/treatments/treatment_consultations.xml',
		'views/treatments/treatment_services.xml',
		'views/treatments/treatment_procedures.xml',
		'views/treatments/treatment_sessions.xml',
		'views/treatments/treatment_controls.xml',
		

		# Patients - 2 
		'views/patients/patient_personal.xml',
		'views/patients/patient_control_docs.xml',
		#'views/patients/patient_appointments.xml',

		# Appointments - 2
		'views/appointments/calendar.xml',








		# ----------------------------------------------------------- Purchase - Deprecated ------------------------------------------------------

		# Purchases 
		#'views/purchase/purchase.xml',
		#'reports/report_purchasequotation.xml',
		#'views/purchase/purchase_report.xml',			# Deprecated ? 
		#'views/purchase/purchase_report_view.xml',		# Deprecated ?



		# ----------------------------------------------------------- Legacy - Deprecated ------------------------------------------------------
		#'views/legacy/legacy.xml',
		#'views/legacy/legacy_patient.xml',
		#'views/legacy/legacy_manager.xml',
		#'views/data/data_analyzer.xml',
		#'views/legacy/legacy_manager_order.xml',
		#'views/legacy/legacy_manager_patient.xml',
		#'views/legacy/legacy_order.xml',
		#'views/menus/menus_legacy.xml',



		# ----------------------------------------------------------- Stock Min - Deprecated ------------------------------------------------------
		#'views/stock_min/stock_min_inventory.xml',
		#'views/stock_min/stock_min_inventory_line.xml',

		# Kardex
		#'views/kardex/kardex.xml',







		# ----------------------------------------------------------- Quality Control ------------------------------------------------------
		'views/menus/menus_qc.xml',




		# ----------------------------------------------------------- Closings ------------------------------------------------------
		# Closing 
		'views/closings/closings.xml',
		'reports/closing.xml',



		# ----------------------------------------------------------- Sale Reports ------------------------------------------------------
		'views/reports/report_sale_pivots.xml',
		'views/reports/report_sale_graphs.xml',
		'views/reports/report_sale_favorites.xml',
		'views/reports/report_sale_search.xml',
		'views/reports/report_sale.xml',

		'views/reports/report_sale_months.xml',
		#'views/reports/report_sale_days.xml',




		# ----------------------------------------------------------- Menus ------------------------------------------------------
		'views/menus/menus.xml',
		'views/menus/menus_reporting.xml',
		'views/menus/menus_openhealth.xml',



		# ----------------------------------------------------------- Security ------------------------------------------------------
		'security/openhealth_security.xml',
		'security/openhealth_security_readers.xml',
		'security/ir.rule.xml',

		'security/ir.model.access.csv',
	],




	# Only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],

	# Static - Style Css 
	'css': ['static/src/css/jx.css'],
	
	'js': [''],
}
