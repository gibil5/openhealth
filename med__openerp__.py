# -*- coding: utf-8 -*-
{
	'name': "Open Health - SERVICE ORIENTED - MED",

	'summary': """
		ERP system, for the Chavarri Clinic. Contains ALL the Data Model. Encapsulates the Business logic in Classes and Libraries. Inherits OeHealth. 
	""",

	'description': """

		17 Sep 2019

		Contains:
			- All External Dependencies,
			- All Models,
			- All Users,
			- All Views,
			- All Data,
			- No Security.


		Remember Robert C. Martin:
			- Respect the Law of Demeter: avoid Train Wreckages.
			- Do not mix Data and Business Rules. Encapsulate Business Rules. 
			- Three layered model: Odoo Active Data - Customized Class with BR - General purpose Library.
			- Handle Exceptions.
			- The Database should not contain BR. Kill computes.

		Always clean your System: 
			- Procurement Orders, 
			- Stock Moves,
			- Computes,
			- Products Consumables.

		Deprecated: Ooor, Testcafe, Auto-backup, Inventory. 

		Created:        11 Sep 2016
		Last up:        10 Sep 2018 

		---

		External:
			- Oehealth 
			- Base multi image

		Python Libs:
			- Unidecode
			- pysftp

	""",

	'author': "DataMetrics",

	'website': "http://jrevilla.com/",
	
	'category': 'Object Oriented',
	
	'version': '3.0',

	'depends': ['base', 'oehealth', 'base_multi_image'],
	#'depends': ['base', 'oehealth', 'base_multi_image', 'account'],

	'data': [


# ----------------------------------------------------------- Legacy - Products - Only for Lima ------------------------------------------------------
		# Products

		#'data/categs/base_data_categs_prods.xml',
		#'data/allergies/allergy.xml',

		#'data/prods/odoo_data_products.xml',
		#'data/prods/odoo_data_products_new.xml',
		#'data/prods/odoo_data_services_consult.xml',
		#'data/prods/odoo_data_services_co2.xml',
		#'data/prods/odoo_data_services_exc.xml',
		#'data/prods/odoo_data_services_m22.xml',
		#'data/prods/odoo_data_services_med.xml',
		#'data/prods/odoo_data_services_cos.xml',
		#'data/prods/odoo_data_services_med_dep.xml',

		# Suppliers
		#'data/suppliers.xml',                          
		# Very Important - Account Invoice Dependance



# ----------------------------------------------------------- Users ------------------------------------------------------

		# Categs
		'data/categs/base_data_categs_partners.xml',

		# Users
		'data/users/base_data_users_generics.xml',                 # Important 
		
		'data/physicians/base_data_physicians.xml',                
		'data/physicians/base_data_physicians_inactive.xml',        
		
		'data/users/base_data_users_platform.xml',  
		'data/users/base_data_users_cash.xml',
		'data/users/base_data_users_account.xml',       

		'data/users/base_data_users_managers.xml',  

		'data/users/base_data_users_doctors.xml',
		'data/users/base_data_users_assistants.xml',    
		'data/users/base_data_users_directors.xml',  

		# Inactive
		'data/users/base_data_users_inactive.xml', 


		# Users Tacna
		'data/users/base_data_users_tacna.xml',



# ----------------------------------------------------------- Security - Users - First ------------------------------------------------------
		'security/openhealth_security.xml',             # Groups
		'security/openhealth_security_readers.xml',     # Important
		'security/openhealth_security_managers.xml',	# Important




# ----------------------------------------------------------- Configurator ------------------------------------------------------

		'views/configurators/configurator_emr.xml',         # Includes Menu



# ----------------------------------------------------------- Actions ------------------------------------------------------

		'views/patients/patient_actions.xml',




# ----------------------------------------------------------- Recent ------------------------------------------------------

		# Product Selector  - RSP
		'views/report_sale/report_sale_product.xml',
		'views/report_sale/item_counter.xml',


		# Account - Payments
		#'views/payment_method/payment_method_line.xml',
		'views/orders/payment_method/payment_method_line.xml',


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
		'views/base_actions.xml',                                       # Very important - All Actions should go here - Dependencies
		



# ----------------------------------------------------------- Reports ------------------------------------------------------

		# Patient
		'reports/patient/report_patient.xml',

		# Formats
		'reports/paper_format.xml',

		# Ticket - Electronic 
		'reports/report_layouts.xml',
		'reports/print_ticket_receipt_electronic.xml',



# ----------------------------------------------------------- Views - Actions ------------------------------------------------------

		'views/services/service_actions.xml',
		'views/services/service_search.xml',


# ----------------------------------------------------------- Views - First Level ------------------------------------------------------

		# Users
		'views/users/user.xml',
		'views/users/user_actions.xml',

		# Groups
		'views/users/group.xml',


		# Orders
		'views/orders/order.xml',
		'views/orders/order_tree.xml',
		'views/orders/order_actions.xml',
		'views/orders/order_search.xml',

		'views/orders/order_admin.xml',
		'views/orders/order_account.xml',

		'views/orders/order_report_nex.xml',                # Estado de Cuenta New


		# Payment methods 
		#'views/payment_method/payment_methods.xml',
		'views/orders/payment_method/payment_methods.xml',


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
		#'views/partners/partner.xml',
		#'views/partners/partner_actions.xml',
		'views/patients/partners/partner.xml',
		'views/patients/partners/partner_actions.xml',


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
		'views/patients/patient_legacy.xml',



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
		'views/reports/report_sale_actions.xml',            # With Menus


# ----------------------------------------------------------- Menus ------------------------------------------------------
		'views/menus/menus.xml',
		'views/menus/menus_dev.xml',
		'views/menus/menus_caja.xml',
		'views/menus/menus_marketing.xml',
		'views/menus/menus_management.xml',
		'views/menus/menus_account.xml',
		'views/menus/menus_products.xml',

		'views/menus/menus_oeh.xml',


# ----------------------------------------------------------- Security - Models - Last ------------------------------------------------------
		'security/ir.model.access.csv',
		
		'security/ir.rule.xml',                # Dep ?

	],

	'demo': [],

	# Static - Style Css 
	'css': ['static/src/css/jx.css'],   

	'js': [],
}
