# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH - MIN
# 
#
###############################




{
	'name': "Open Health - MIN",

	'summary': """
		Extension for Odoo-oeHealth. 
		Treatments. 
	""",


	'description': """


		Last built: 15 Junio 2018 

		
		Stability by Design.

		Simplicity but Abstraction. 

		La Estabilidad se consigue por la disminución, no por el aumento. 
		Dieter Rams: Less but Better. 

		More Configuration and less programming. Near than zero hacking.  



		Laser - EMR - Min - Ama - Docean - Ooor - Github - Travis - Coverage - Proliant - Testcafe - User Stories - Auto Backup - Unit Testing - Less but Better - Fulcrum - Statistical - Machine Learning\n



		Created: 	 	11 Sep 2016
		
		Active for: 	17 months !!!		(Lu Feb 2018)

		Good Order is the Beginning of All Good Things. 
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
	'category': 'Health',
	'version': '1.0',




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


		# ----------------------------------------------------------- Deprecated ??? ------------------------------------------------------

		#'views/product_managers/product_manager.xml',
		#'views/menus/menus_kardex.xml',


		# ----------------------------------------------------------- Stock Moves - Deprecated ??? ------------------------------------------------------
		#'data/stock_move_data.xml',
		#'views/stock/stock_move.xml',
		#'views/stock/stock_move_selector.xml',
		#'views/stock/stock_move_all.xml',









		# ----------------------------------------------------------- Recent ------------------------------------------------------

		
		# Reports
		'views/product_selectors/product_selector.xml',
		'views/orders/order_report_nex.xml',
		'views/report_sale/report_sale_product.xml',
		'views/report_sale/report_sale.xml',
		'views/report_sale/item_counter.xml',



		# Accounting 
		'views/payment_methods/payment_method_line.xml',
		'views/account/account_line.xml',
		'views/account/account_contasis.xml',
		'views/menus/menus_account.xml',





		# Exceptions 
		#'views/patients/patient_exceptions.xml',





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



		# Commons 
		'views/menus/menus_openhealth.xml',
		'security/ir.model.access.csv',








		# ----------------------------------------------------------- Views - Base Actions ------------------------------------------------------

		# Base - Form and List Actions - Must be the first 
		'views/base.xml',										# Very important - All Actions should go here - Dependencies
		









		# ----------------------------------------------------------- Reports ------------------------------------------------------


		# Patient
		'reports/patient.xml',
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






		# Purchases
		'reports/report_purchasequotation.xml',























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





		# Users - With pw
		'data/users/base_data_users_platform.xml',	
		'data/users/base_data_users_cash.xml',		
		'data/users/base_data_users_doctors.xml',		
		'data/users/base_data_users_assistants.xml',	
		'data/users/base_data_users_staff.xml',		
		'data/users/base_data_users_almacen.xml',		
		'data/users/base_data_users_managers.xml',	


		'data/users/base_data_users_doctors_new.xml',		




		# Generics 
		'data/users/base_data_users_generics.xml',	





		# ----------------------------------------------------------- Security Rules ------------------------------------------------------
		'security/openhealth_security.xml',
		'security/openhealth_security_readers.xml',
		'security/ir.rule.xml',









		











		# ----------------------------------------------------------- Views ------------------------------------------------------


		# Purchases 
		'views/purchase/purchase.xml',


		# Stock 
		'views/stock/stock.xml',
		'views/stock/stock_inventory.xml',


		# Kardex
		'views/kardex/kardex.xml',








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
		'views/recommendations/recommendation.xml',


		# Treatments 
		'views/treatments/treatment.xml',



		# Cosmetologies
		'views/cosmetologies/cosmetology.xml',






		# Physicians 
		'views/physicians/physician.xml',


		

		# Patients 
		'views/patients/patient.xml',
		'views/patients/patient_search.xml',




		# Partners
		'views/partners/partner.xml',




		# Appointments
		'views/appointments/appointment.xml',


		# Products
		'views/products/product.xml',		


		# Cards 
		'views/cards/card.xml',



		# Style 
		'views/openhealth.xml',		






		# ----------------------------------------------------------- Views - Second Level ------------------------------------------------------

		# Sessions
		'views/sessions/session.xml',
		'views/sessions/session_config_manual.xml',
		'views/sessions/session_cos.xml',


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
		'views/services/service_quick.xml',
		'views/services/service_vip.xml',



		# Cosmetology
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


		# Patients - 2 
		'views/patients/patient_personal.xml',
		'views/patients/patient_control_docs.xml',
		'views/patients/patient_appointments.xml',
		'views/patients/patient_quick.xml',




		

		# Appointments - 2
		'views/appointments/calendar.xml',
		'views/appointments/appointment_cos.xml',


		# Closing 
		'reports/closing.xml',









		# ----------------------------------------------------------- Purchase ------------------------------------------------------
		'views/purchase/purchase_report.xml',			# Deprecated
		'views/purchase/purchase_report_view.xml',		# Deprecated 






		# ----------------------------------------------------------- Legacy ------------------------------------------------------
		'views/legacy/legacy.xml',
		'views/legacy/legacy_patient.xml',
		'views/legacy/legacy_manager.xml',
		'views/data/data_analyzer.xml',
		'views/legacy/legacy_manager_order.xml',
		'views/legacy/legacy_manager_patient.xml',
		'views/legacy/legacy_order.xml',

		'views/menus/menus_legacy.xml',



		






		# closings 
		'views/closings/closings.xml',




		# ----------------------------------------------------------- Stock Min ------------------------------------------------------
		'views/stock_min/stock_min_inventory.xml',
		'views/stock_min/stock_min_inventory_line.xml',





		# ----------------------------------------------------------- Products ------------------------------------------------------

		'data/prods/odoo_data_products.xml',	
		'data/prods/odoo_data_products_new.xml',	
		'data/prods/odoo_data_services_co2.xml',		
		'data/prods/odoo_data_services_exc.xml',		
		'data/prods/odoo_data_services_m22.xml',		
		'data/prods/odoo_data_services_med.xml',		
		'data/prods/odoo_data_services_consult.xml',	
		'data/prods/odoo_data_services_cos.xml',		





		# ----------------------------------------------------------- Reports ------------------------------------------------------
		# Sales 
		'views/reports/report_sale_pivots.xml',
		'views/reports/report_sale_graphs.xml',
		'views/reports/report_sale_favorites.xml',
		'views/reports/report_sale_search.xml',
		'views/reports/report_sale.xml',
		'views/reports/report_sale_months.xml',




		# ----------------------------------------------------------- Menus ------------------------------------------------------
		'views/menus/menus.xml',
		'views/menus/menus_reporting.xml',

	],




	# Only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],
	# Static - Style Css 
	'css': ['static/src/css/jx.css'],
	'js': [''],
}
