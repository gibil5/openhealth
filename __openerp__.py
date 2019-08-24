# -*- coding: utf-8 -*-
{
	'name': "Open Health - SERVICE ORIENTED",

	'summary': "",

	'description': """

		23 Aug 2019

		Remember, Hunter and Westerman:
			- Step 1 - New Thinking: Avoid the 7 Value Traps.

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
	'version': '3.0',

	'depends': ['base', 'oehealth', 'base_multi_image'],

	'data': [







# ----------------------------------------------------------- Data - First ------------------------------------------------------

		# Check that data is not updated. All the time. 

		# Categs
		'data/categs/base_data_categs_partners.xml',			
		'data/categs/base_data_categs_prods.xml',			

		# Allergy 
		'data/allergies/allergy.xml',

		# Doctors
		'data/physicians/base_data_physicians.xml',				
		'data/physicians/base_data_physicians_new.xml',
		'data/physicians/base_data_physicians_inactive.xml',		

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



		# ----------------------------------------------------------- Data - Products ------------------------------------------------------

		'data/prods/odoo_data_products.xml',

		'data/prods/odoo_data_products_new.xml',			# Has integrated the following

		#'data/prods/odoo_data_products_dep.xml',			# Dep
		#'data/prods/odoo_data_products_new_20181212.xml',	# Dep
		#'data/prods/odoo_data_products_new_20190128.xml',	# Dep 
		#'data/prods/odoo_data_products_new_2019-03-06.xml',	# Dep
		#'data/prods/odoo_data_products_credit_notes.xml',	# Dep




		'data/prods/odoo_data_services_co2.xml',
		'data/prods/odoo_data_services_exc.xml',
		'data/prods/odoo_data_services_m22.xml',
		'data/prods/odoo_data_services_med.xml',		
		'data/prods/odoo_data_services_consult.xml',
		'data/prods/odoo_data_services_cos.xml',
		'data/prods/odoo_data_services_med_dep.xml',	# Dependance

		# Pricelists - Vip
		'data/pricelists/pricelists.xml',
		
		# Suppliers 
		'data/suppliers.xml',							# Very Important - Account Invoice Dependance



# ----------------------------------------------------------- Security - First ------------------------------------------------------
		'security/openhealth_security.xml',				# Groups
		'security/openhealth_security_readers.xml',





# ----------------------------------------------------------- Configurators ------------------------------------------------------
		'views/configurators/scheduler.xml',
		'views/configurators/configurator.xml',
		'views/configurators/configurator_emr.xml',			# Includes Menu
		'views/configurators/configurator_report.xml',



# ----------------------------------------------------------- Actions ------------------------------------------------------

		'views/patients/patient_actions.xml',




# ----------------------------------------------------------- Recent ------------------------------------------------------

		# Product Selector  
		'views/report_sale/report_sale_product.xml',
		'views/report_sale/item_counter.xml',


		# Account - Payments
		'views/payment_method/payment_method_line.xml',


		# Account
		'views/account/account_line.xml',
		'views/account/account_line_actions.xml',
		'views/account/account_contasis_actions.xml',
		'views/account/account_contasis.xml',


		# Marketing 
		'views/marketing/patient_line_search.xml',
		'views/marketing/patient_line.xml',
		'views/marketing/patient_line_actions.xml',
		'views/marketing/patient_line_pivot.xml',

		'views/marketing/marketing_order_line.xml',
		'views/marketing/marketing_reco_line.xml',
		'views/marketing/media_line.xml',
		'views/marketing/histogram.xml',
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


		'views/management/management_trees.xml',
		'views/management/management_actions.xml',
		'views/management/management.xml',
		



# ----------------------------------------------------------- Views - Base Actions ------------------------------------------------------

		# Base - Form and List Actions - Must be the first
		'views/base_actions.xml',										# Very important - All Actions should go here - Dependencies
		



# ----------------------------------------------------------- Reports ------------------------------------------------------

		# Patient
		'reports/patient/report_patient.xml',

		# Formats
		'reports/paper_format.xml',

		# Ticket - Electronic 
		'reports/report_layouts.xml',
		'reports/print_ticket_receipt_electronic.xml',

		# Ticket
		'reports/phys/report_ticket_invoice_nex.xml',
		'reports/phys/report_ticket_receipt_nex.xml',



# ----------------------------------------------------------- Views - Actions ------------------------------------------------------

		'views/services/service_actions.xml',
		'views/services/service_search.xml',



# ----------------------------------------------------------- Views - First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',


		# Orders
		'views/orders/order.xml',
		'views/orders/order_tree.xml',
		'views/orders/order_actions.xml',
		'views/orders/order_search.xml',
		'views/orders/order_admin.xml',
		'views/orders/order_report_nex.xml',				# Estado de Cuenta New


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


		# Products
		'views/products/product_actions.xml',
		'views/products/product_product.xml',

		'views/products/product_template.xml',


		# Cards 
		'views/cards/card.xml',



# ----------------------------------------------------------- Views - Second ------------------------------------------------------

		# Sessions
		'views/sessions/session.xml',
		'views/sessions/session_config_simple.xml',
		'views/sessions/session_config_simple_2.xml',


		# Services - 2  
		'views/services/service_product.xml',

		'views/services/service_co2.xml',
		'views/services/service_excilite.xml',
		'views/services/service_ipl.xml',
		'views/services/service_ndyag.xml',
		'views/services/service_quick.xml',		
		'views/services/service_medical.xml',
		'views/services/service_cosmetology.xml',


		# Consultation - 2
		'views/consultations/consultation_diagnosis.xml',
		

		# Treatments - 2 
		'views/treatments/treatment_orders.xml',
		'views/treatments/treatment_consultations.xml',
		'views/treatments/treatment_procedures.xml',
		'views/treatments/treatment_sessions.xml',
		'views/treatments/treatment_controls.xml',
		

		# Patients - 2 
		'views/patients/patient_personal.xml',
		'views/patients/patient_control_docs.xml',



# ----------------------------------------------------------- Closings ------------------------------------------------------
		# Closing 
		'views/closings/closings.xml',
		'views/closings/closings_search.xml',
		'reports/closing/closing.xml',


# ----------------------------------------------------------- Sale Reports ------------------------------------------------------
		'views/reports/report_sale_pivots.xml',
		'views/reports/report_sale_graphs.xml',
		'views/reports/report_sale_favorites.xml',
		'views/reports/report_sale_search.xml',
		'views/reports/report_sale.xml',
		'views/reports/report_sale_actions.xml',			# With Menus





# ----------------------------------------------------------- Menus ------------------------------------------------------
		'views/menus/menus.xml',
		#'views/menus/menus_openhealth.xml',		# Dep
		'views/menus/menus_caja.xml',
		'views/menus/menus_marketing.xml',
		'views/menus/menus_management.xml',
		'views/menus/menus_account.xml',



# ----------------------------------------------------------- Security - Models - Last ------------------------------------------------------
		#'security/ir.model.access.csv',
		#'security/ir.rule.xml', 				# Dep 

	],
	'demo': [],
	# Static - Style Css 
	'css': ['static/src/css/jx.css'],	

	'js': [],
}
