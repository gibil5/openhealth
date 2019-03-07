# -*- coding: utf-8 -*-
{
	'name': "Open Health - SERVICE ORIENTED - ALIVE - WINTLIB - DOCEAN TEST ENV",

	'summary': "",

	'description': """

		7 Mar 2019

		Remember, it is just a Bigger game:
			- DEV = 9x9
			- TEST = 13 x 13
			- PROD = 19 x 19


		Go - Fulcrum - TRAVIS Quality Controlled - 2019

		Learn from Go, to build and maintain territory:
			- Build Eyes. Which are the arrangement of internal liberties.
			- Not too few. Not too much. Two is the good number. 
			- Watch for the Atari, that comes from nowhere. 
			- Build ladders and recognize when your token are captured.

		New Micro Services:
			- Management Reports. Productivity. 
			- Appointments. 
			- New Products. 

		Critical Use Cases: 
		- New patient wants a consultation. 
		- Existing patient wants to change Control Appointment. 
		  Dr has not created anything.


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
	
	'category': 'Object Oriented',
	
	'version': '2.0',

	'depends': ['base', 'oehealth', 'base_multi_image'],



	'data': [


# ----------------------------------------------------------- New ------------------------------------------------------
		'views/configurators/scheduler.xml',

		'views/configurators/configurator.xml',

		'views/configurators/configurator_emr.xml',

		'views/configurators/configurator_report.xml',



# ----------------------------------------------------------- Data - First ------------------------------------------------------

		# Check that data is not updated. All the time. 

		# Categs
		'data/categs/base_data_categs_partners.xml',			
		'data/categs/base_data_categs_prods.xml',			


		# Important 
		#'views/pathologies/pathology.xml',
		'data/pathologies/pathology.xml',

		'data/prods/zone/data_pathologies.xml',			
		'data/prods/zone/data_nexzones.xml',	

		# Zone
		#'views/zones/zone.xml',
		'views/zones/zone_actions.xml',

		'data/prods/zone/data_zones_quick.xml',			 
		'data/prods/zone/data_zones_co2.xml',			 
		'data/prods/zone/data_zones_excilite.xml',			 
		'data/prods/zone/data_zones_ipl.xml',			 
		'data/prods/zone/data_zones_ndyag.xml',			 


		# Allergy 
		#'views/allergies/allergy.xml',
		'data/allergies/allergy.xml',


		# Doctors
		'data/physicians/base_data_physicians.xml',				
		#'data/physicians/base_data_physicians_inactive.xml',		Dep ???
		'data/physicians/base_data_physicians_new.xml',				



		# Generics 
		'data/users/base_data_users_generics.xml',	


		# Users - With pw
		'data/users/base_data_users_platform.xml',	
		'data/users/base_data_users_platform_new.xml',	

		'data/users/base_data_users_cash.xml',		
		'data/users/base_data_users_doctors.xml',

		'data/users/base_data_users_assistants.xml',	
		
		'data/users/base_data_users_staff.xml',		
		'data/users/base_data_users_almacen.xml',		
		'data/users/base_data_users_managers.xml',	
		'data/users/base_data_users_doctors_new.xml',		

		#'data/users/base_data_users_test.xml',		Dep !!!



		# ----------------------------------------------------------- Data - Products ------------------------------------------------------

		'data/prods/odoo_data_products.xml',
		'data/prods/odoo_data_products_new.xml',
		'data/prods/odoo_data_products_dep.xml',			# Important

		'data/prods/odoo_data_products_new_20181212.xml',

		'data/prods/odoo_data_products_new_20190128.xml',	# New !

		'data/prods/odoo_data_products_credit_notes.xml',	# New !

		'data/prods/odoo_data_products_new_2019-03-06.xml',





		'data/prods/odoo_data_services_co2.xml',
		'data/prods/odoo_data_services_exc.xml',
		'data/prods/odoo_data_services_m22.xml',
		'data/prods/odoo_data_services_med.xml',		
		'data/prods/odoo_data_services_consult.xml',
		'data/prods/odoo_data_services_cos.xml',
		'data/prods/odoo_data_services_med_dep.xml',	# Dependance


		#'data/prods/odoo_data_services_cos_dep.xml', 	# Dependance ?
		#'data/prods/odoo_data_products_consu.xml',		# Deprecated




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
		'data/suppliers.xml',							# Very Important - Account Invoice Dependance









		# ----------------------------------------------------------- Actions ------------------------------------------------------
		'views/patients/patient_actions.xml',




		# ----------------------------------------------------------- Recent ------------------------------------------------------

		# Product Selector
		'views/product_selectors/product_selector.xml',



		# RSP
		'views/report_sale/report_sale_product.xml',
		'views/report_sale/item_counter.xml',



		# Account - Payments
		'views/payment_method/payment_method_line.xml',




		# Account
		'views/account/account_line.xml',
		'views/account/account_line_actions.xml',
		'views/account/account_contasis_actions.xml',
		'views/account/account_contasis.xml',





		# Account - Patients 					# Dep ???
		'views/account/patient_line.xml',
		'views/account/patient_line_pivot.xml',




		# Marketing 
		'views/marketing/marketing_order_line.xml',
		'views/marketing/marketing_reco_line.xml',
		'views/marketing/media_line.xml',
		'views/marketing/histogram.xml',
		#'views/places/place.xml',
		'views/marketing/place_actions.xml',
		'views/marketing/place_pivot.xml',
		'views/marketing/place.xml',
		'views/marketing/marketing.xml',
		'views/marketing/marketing_pivot.xml',



		# Electronic
		'views/electronic/electronic_order.xml',
		'views/electronic/electronic_line.xml',



		# Management 
		'views/management/management_day_line.xml',

		'views/management/management_day_doctor_line.xml',


		'views/management/management_family_line.xml',
		'views/management/management_subfamily_line.xml',
		'views/management/management_order_line.xml',
		'views/management/management_doctor_line.xml',

		'views/management/management_actions.xml',
		'views/management/management.xml',
		


		# Coder 
		'views/coders/coder.xml',

		





		# ----------------------------------------------------------- Views - Base Actions ------------------------------------------------------

		# Base - Form and List Actions - Must be the first
		
		'views/base_actions.xml',										# Very important - All Actions should go here - Dependencies
		






		# ----------------------------------------------------------- Reports ------------------------------------------------------

		# Patient
		#'reports/patient.xml',
		#'reports/report_patient.xml',
		#'reports/patient_consultation.xml',
		#'reports/patient_sessions.xml',
		#'reports/patient_controls.xml',
		'reports/patient/report_patient.xml',



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











# ----------------------------------------------------------- Views ------------------------------------------------------



		# ----------------------------------------------------------- Views - Actions ------------------------------------------------------
		'views/services/service_actions.xml',
		'views/services/service_search.xml',

		'views/appointments/appointment_actions.xml',
		'views/appointments/appointment_search.xml',



		# ----------------------------------------------------------- Views - First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',


		# Groups 
		#'views/groups/groups.xml',



		# Orders
		'views/orders/order.xml',
		'views/orders/order_tree.xml',

		'views/orders/order_actions.xml',
		'views/orders/order_search.xml',
		'views/orders/order_line.xml',
		'views/orders/order_admin.xml',
		#'views/orders/order_report_nex.xml',				# Estado de Cuenta
		'views/orders/order_account.xml',				# Estado de Cuenta New




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
		'views/containers/texto.xml',
		'views/containers/container.xml',
		'views/containers/corrector.xml',




		# Partners
		'views/partners/partner.xml',
		'views/partners/partner_actions.xml',


		# Appointments
		'views/appointments/appointment.xml',




		# Products Min
		'views/products/product_min.xml',




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






		# ----------------------------------------------------------- Views - Second ------------------------------------------------------

		# Sessions
		'views/sessions/session.xml',
		'views/sessions/session_config_simple.xml',
		'views/sessions/session_config_simple_2.xml',
		#'views/sessions/session_config_manual.xml',		# Dep



		# Evaluations - 2
		#'views/evaluations/evaluation_oeh.xml',			# Dep



		# Services - 2  
		'views/services/service_product.xml',

		'views/services/service_co2.xml',
		'views/services/service_excilite.xml',
		'views/services/service_ipl.xml',
		'views/services/service_ndyag.xml',
		'views/services/service_quick.xml',		
		'views/services/service_medical.xml',
		'views/services/service_cosmetology.xml',
		#'views/services/service_vip.xml',					# Dep


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
		#'views/consultations/consultation_med.xml',			# Dep ?
		'views/consultations/consultation_diagnosis.xml',
		

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
		'views/appointments/appointment_kanban.xml',






		# ----------------------------------------------------------- FileSystem - Dep ------------------------------------------------------

		#'views/containers/filesystem_directory.xml',	# Dep
		#'views/containers/filesystem_file.xml',		# Dep







		# ----------------------------------------------------------- Closings ------------------------------------------------------
		# Closing 
		'views/closings/closings.xml',
		'views/closings/closings_search.xml',


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
		'security/ir.rule.xml', 				# Dep 




# ----------------------------------------------------------- Menus ------------------------------------------------------
		'views/menus/menus.xml',

		'views/menus/menus_app.xml',

		'views/menus/menus_config.xml',

		'views/menus/menus_openhealth.xml',		


		'views/menus/menus_products.xml',
		'views/menus/menus_caja.xml',
		'views/menus/menus_reporting.xml',
		'views/menus/menus_marketing.xml',		 
		'views/menus/menus_management.xml',		  
		'views/menus/menus_qc.xml',
		'views/menus/menus_account.xml',

	],


	'demo': [],


	# Static - Style Css 
	'css': ['static/src/css/jx.css'],
	

	'js': [],
}


