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

		21 Nov 2018

		Fulcrum - DEV - DOCEAN - PROLIANT
		
		Code without Tests is broken by design. Jacob Kaplan-Moss
		
		Zero Maintenance is Perfection. 

		My Goal is to achieve Complete Coverage. 

		Stability by Design. Simplicity by Abstraction. 

		La Estabilidad se consigue por la disminución no por el aumento. 
		Dieter Rams: Less but Better. 

		More configuration and less programming, near than zero hacking.  

		Good order is the beginning of all good things. 

		(From 17 Mar 2018 - 13 963)

		EMR - Min - Docean - Github - Travis - Coverage - Proliant - User Stories - Cron Pg Dump  - 
		Statistical - Machine Learning - Object Oriented - Fulcrum - Coverage Testing - Unit Testing - Electronic Billing - Name Constraints\n

		Deprecated: Ooor, Testcafe, Auto-backup, Inventory. 

		Created: 	 	11 Sep 2016
		Last up: 		10 Sep 2018 

		---


		Additional modules:
			- MRP (Manufacturing Ressource Planning). 
			- Purchase. 
			- Multi prices. 


		External:
			- Oehealth 
			- Base multi image
			- Auto backup

		Python:
			- Unidecode
			- pysftp

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



	# always
	'data': [


		# ----------------------------------------------------------- Actions ------------------------------------------------------
		'views/patients/patient_actions.xml',




		# ----------------------------------------------------------- Recent ------------------------------------------------------

		# Reports
		#'views/product_selectors/product_selector.xml',
		'views/products/product_selector.xml',

		
		#'views/report_sale/report_sale_product.xml',
		#'views/report_sale/item_counter.xml',
		'views/report_sale/report_sale_product.xml',
		'views/report_sale/item_counter.xml',




		# Accounting 
		'views/payment_method/payment_method_line.xml',




		'views/account/account_line.xml',
		'views/account/account_contasis.xml',
		'views/account/patient_line.xml',
		'views/account/patient_line_pivot.xml',



		# Marketing 
		'views/marketing/marketing_order_line.xml',
		'views/marketing/marketing_reco_line.xml',

		#'views/media/media_line.xml',
		'views/marketing/media_line.xml',
		
		#'views/histogram/histogram.xml',
		'views/marketing/histogram.xml',
		
		#'views/places/place.xml',
		'views/marketing/place.xml',
		
		'views/marketing/marketing.xml',
		'views/marketing/marketing_pivot.xml',




		# Electronic
		'views/electronic/electronic_order.xml',
		'views/electronic/electronic_line.xml',



		# Management 
		'views/management/management_family_line.xml',
		'views/management/management_order_line.xml',
		'views/management/management_doctor_line.xml',
		'views/management/management.xml',
		'views/management/management_actions.xml',
		


		# Coder 
		'views/coders/coder.xml',

		







		# ----------------------------------------------------------- Views - Base Actions ------------------------------------------------------

		# Base - Form and List Actions - Must be the first 
		#'views/base.xml',										# Very important - All Actions should go here - Dependencies
		'views/base_actions.xml',										# Very important - All Actions should go here - Dependencies
		






		# ----------------------------------------------------------- Reports ------------------------------------------------------

		# Patient
		#'reports/patient.xml',
		#'reports/report_patient.xml',
		'reports/patient/report_patient.xml',


		#'reports/patient_consultation.xml',
		#'reports/patient_sessions.xml',
		#'reports/patient_controls.xml',



		# Formats
		'reports/paper_format.xml',

		# Ticket - Electronic 
		'reports/report_layouts.xml',
		'reports/print_ticket_receipt_electronic.xml',



		# Ticket - Dep !
		#'reports/report_ticket_receipt.xml',
		#'reports/report_ticket_invoice.xml',

		# Ticket
		#'reports/report_ticket_invoice_nex.xml',
		#'reports/report_ticket_receipt_nex.xml',
		'reports/phys/report_ticket_invoice_nex.xml',
		'reports/phys/report_ticket_receipt_nex.xml',









		# ----------------------------------------------------------- Data ------------------------------------------------------

		# Check that data is not updated. All the time. 

		# Categs
		'data/base_data_categs_partners.xml',			
		'data/base_data_categs_prods.xml',			


		# Important 
		#'views/pathologies/pathology.xml',
		'data/pathologies/pathology.xml',

		'data/prods/zone/data_pathologies.xml',			
		'data/prods/zone/data_nexzones.xml',	

		# Zone
		'views/zones/zone.xml',

		'data/prods/zone/data_zones_quick.xml',			 
		'data/prods/zone/data_zones_co2.xml',			 
		'data/prods/zone/data_zones_excilite.xml',			 
		'data/prods/zone/data_zones_ipl.xml',			 
		'data/prods/zone/data_zones_ndyag.xml',			 


		# Allergy 
		#'views/allergies/allergy.xml',
		'data/allergies/allergy.xml',


		# Doctors
		'data/base_data_physicians.xml',				
		'data/base_data_physicians_inactive.xml',				
		'data/base_data_physicians_new.xml',				







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

		'data/users/base_data_users_test.xml',	




		# ----------------------------------------------------------- Data - Products ------------------------------------------------------

		'data/prods/odoo_data_products.xml',
		'data/prods/odoo_data_products_new.xml',
		'data/prods/odoo_data_products_dep.xml',			# Important

		'data/prods/odoo_data_services_co2.xml',
		'data/prods/odoo_data_services_exc.xml',
		'data/prods/odoo_data_services_m22.xml',
		'data/prods/odoo_data_services_med.xml',
		#'data/prods/odoo_data_services_med_dep.xml',
		'data/prods/odoo_data_services_consult.xml',
		'data/prods/odoo_data_services_cos.xml',
		#'data/prods/odoo_data_services_cos_dep.xml',




		# Pricelists - Vip
		'data/pricelists/pricelists.xml',
		
		# Pricelists - Deprecated ?
		#'data/pricelists/pricelist_items_co2.xml',
		#'data/pricelists/pricelist_items_ipl.xml',
		#'data/pricelists/pricelist_items_ndyag.xml',
		#'data/pricelists/pricelist_items_quick.xml',
		#'data/pricelists/pricelist_items_med_cos.xml',
		#'data/pricelists/pricelist_consultation.xml',
		#'data/pricelists/pricelist_products.xml',


		# Suppliers 
		#'data/suppliers.xml',							# DEPRECATED - Very 




# ----------------------------------------------------------- Views ------------------------------------------------------



		# ----------------------------------------------------------- Views - Actions ------------------------------------------------------
		'views/services/service_actions.xml',
		'views/services/service_search.xml',




		# ----------------------------------------------------------- Views - First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',


		# Groups 
		#'views/groups/groups.xml',



		# Orders
		'views/orders/order_actions.xml',
		'views/orders/order_search.xml',
		'views/orders/order_line.xml',
		'views/orders/order.xml',
		'views/orders/order_admin.xml',
		#'views/orders/order_report_nex.xml',				# Estado de Cuenta
		'views/orders/order_account.xml',				# Estado de Cuenta




		# Payment methods 
		'views/payment_method/payment_methods.xml',



		# Counters 
		'views/counters/counter.xml',


		# Companies 
		'views/companies/company.xml',


		# Controls
		'views/controls/control.xml',


		# Images 
		'views/images/image_view.xml',


		# Evaluations
		#'views/evaluations/evaluation.xml',


		# Services
		'views/services/service.xml',


		# Procedures
		'views/procedures/procedure.xml',


		# Consultation
		'views/consultations/consultation.xml',




		# Treatments 
		'views/treatments/treatment.xml',
		'views/treatments/treatment_actions.xml',


		# Physicians 
		'views/physicians/physician.xml',



		# Patients 
		'views/patients/patient.xml',
		'views/patients/patient_search.xml',



		# Containers 
		'views/containers/container.xml',
		'views/containers/texto.xml',
		'views/containers/corrector.xml',




		# Partners
		'views/partners/partner.xml',
		'views/partners/partner_actions.xml',


		# Appointments
		'views/appointments/appointment.xml',
		'views/appointments/appointment_actions.xml',



		# Products
		'views/products/product_template.xml',
		'views/products/product_actions.xml',
		'views/products/product_product.xml',
		
		#'views/products/product_category.xml',
		#'views/products/product_pricelist.xml',
		#'views/products/purchase_order.xml',	



		# Pricelist Items
		'views/pricelist_items/pricelist_item_actions.xml',
		'views/pricelist_items/pricelist_item.xml',




		# Cards 
		'views/cards/card.xml',














		# ----------------------------------------------------------- Views - Second Level ------------------------------------------------------

		# Sessions
		'views/sessions/session.xml',
		'views/sessions/session_config_simple.xml',
		'views/sessions/session_config_simple_2.xml',
		#'views/sessions/session_config_manual.xml',	# Dep



		# Evaluations - 2
		#'views/evaluations/evaluation_oeh.xml',



		# Services - 2  
		'views/services/service_product.xml',

		'views/services/service_co2.xml',
		'views/services/service_excilite.xml',
		'views/services/service_ipl.xml',
		'views/services/service_ndyag.xml',
		'views/services/service_quick.xml',		
		'views/services/service_medical.xml',
		'views/services/service_cosmetology.xml',
		#'views/services/service_vip.xml',			# Dep


		'views/services/zones/service_co2_zone.xml',
		'views/services/zones/service_excilite_zone.xml',
		'views/services/zones/service_ipl_zone.xml',
		'views/services/zones/service_ndyag_zone.xml',
		'views/services/zones/service_medical_zone.xml',
		'views/services/zones/service_cosmetology_zone.xml',






		# Procedures - 2  
		'views/procedures/procedure_controls.xml',
		'views/procedures/procedure_sessions.xml',		


		# Consultation - 2
		#'views/consultations/consultation_med.xml',	# Dep ?
		#'views/consultations/consultation_diagnosis.xml',
		

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






		# ----------------------------------------------------------- FileSystem Directory ------------------------------------------------------

		#'views/containers/filesystem_directory.xml',
		#'views/containers/filesystem_file.xml',







		# ----------------------------------------------------------- Closings ------------------------------------------------------
		# Closing 
		'views/closings/closings.xml',

		#'reports/closing.xml',
		'reports/closing/closing.xml',




		# ----------------------------------------------------------- Sale Reports ------------------------------------------------------
		'views/reports/report_sale_pivots.xml',
		'views/reports/report_sale_graphs.xml',
		'views/reports/report_sale_favorites.xml',
		'views/reports/report_sale_search.xml',
		'views/reports/report_sale.xml',
		'views/reports/report_sale_months.xml',



		# ----------------------------------------------------------- Security ------------------------------------------------------
		'security/openhealth_security.xml',
		'security/openhealth_security_readers.xml',		
		'security/ir.model.access.csv',
		'security/ir.rule.xml', 	# Dep 


		# ----------------------------------------------------------- Menus ------------------------------------------------------
		'views/menus/menus.xml',
		'views/menus/menus_products.xml',
		'views/menus/menus_caja.xml',
		'views/menus/menus_reporting.xml',
		'views/menus/menus_openhealth.xml',		
		'views/menus/menus_marketing.xml',		 
		'views/menus/menus_management.xml',		  
		'views/menus/menus_qc.xml',

		'views/menus/menus_account.xml',
	],




	# Only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],

	# Static - Style Css 
	'css': ['static/src/css/jx.css'],
	
	'js': [''],
}
