# -*- coding: utf-8 -*-
{
'name': "Open Health - Odoo9 - Object oriented - Refactorized - CodeClimate - SonarQube - Management - Functional - No black boxes - Patterns - Microservices - Testing",

'summary': """ ERP system for a Clinic. Inherits OeHealth. Contains ALL the Data Model. Business logic is in classes and libraries.

""",
'description': """

5 apr 2021

Created:        11 Sep 2016
Last up:        30 Mar 2021
(From 17 Mar 2018 - 13 963)

Using patterns:
	- Reduce inheritances.
	- Reduce singletons.
	- Introduce pubsubs.
	- Introduce containers.

Classes: 
	- Order (depends oeHealth)
	- Patient (free)
	- Treatment (free)
	- Management (free)
	- Management Doctor (free)
	
Contains:
	- All External Dependencies
	- All Models
	- All Users
	- All Views
	- All Security
	- All Data

External modules:
	- Spanish translation
	- Oehealth
	- Base multi image
	- Web Export View
	- Accounting and Finance. Adjust tax to zero

Python Libs:
	- Unidecode - dep
	- pysftp - dep
	- Numpy, Num2words, Pandas, QrCode

For PDF Reporting (tickets):
	- Install wkhtmltopdf (0.12.2 v). Other versions will not work.

For Tickets (right button printing):
	- On Chrome, install extension: PDF Viewer. Link it to Adobe Reader.

Deprecated services:
	- Ooor,
	- Testcafe,
	- Auto-backup,
	- Inventory.

Remember Robert C. Martin:
	- Respect the Law of Demeter: avoid Train Wreckages. When you see more than two dots, this needs fixing.
	- Do not mix the Data Model and Business Rules. Encapsulate Business Rules in a separate module.
	- Use Three layered model: Odoo Active Data - Customized Class with BR - General purpose Library.
	- Handle Exceptions.
	- The Database should not contain Business rules. Remove computes.

Always clean your System:
	- Remove Procurement Orders,
	- Remove Stock Moves,
	- Remove Products Consumables,
	- Remove Computes.

---

""",

'author': "jrevilla55@gmail.com",
'website': "http://jrevilla.com/",
'category': 'Object Oriented, Microservices',
'version': '5.0',
'depends': ['base', 'oehealth', 'base_multi_image'],
'data': [

# --------------------------------------------------------- Legacy - Products - Only for Lima -----
	# Products
	# Suppliers - Very Important - Account Invoice Dependance

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
	#'data/suppliers.xml',


# --------------------------------------------------------- Users --------------
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
	'security/openhealth_security_readers.xml',   	# Important
	'security/openhealth_security_managers.xml',

# ----------------------------------------------------------- Configurator ------------------------------------------------------
	#'views/configurators/configurator_emr.xml',         # Includes Menu

# ----------------------------------------------------------- Actions ------------------------------------------------------
	'views/patients/patient_actions.xml',

# ----------------------------------------------------------- Recent ------------------------------------------------------
	# Product Selector  - RSP
	'views/rsp/report_sale_product.xml',
	'views/rsp/item_counter.xml',


	# Account - Payments
	'views/orders/payment_method/payment_method_line.xml',


	# Account - Dep 
	#'views/account/account_line.xml',
	#'views/account/account_line_actions.xml',
	#'views/account/account_contasis_actions.xml',
	#'views/account/account_contasis.xml',


	# Electronic
	'views/electronic_old/electronic_order.xml',
	'views/electronic_old/electronic_line.xml',
	'views/containers/container.xml',

	# Electronic - From PL
	'views/electronic/account_line.xml',               # Min
	'views/electronic/account_contasis_actions.xml',   # Min
	'views/electronic/account_contasis.xml',           # Min
	'views/electronic/electronic_order.xml',           # Min
	'views/electronic/texto.xml',
	'views/electronic/electronic_actions.xml',
	'views/electronic/txt_line.xml',
	'views/electronic/electronic_container.xml',       # Min






	# Dep - Done In PL

	# Marketing - Dep
	#'views/marketing/patient_line_search.xml',
	#'views/marketing/patient_line.xml',
	#'views/marketing/patient_line_actions.xml',
	#'views/marketing/patient_line_pivot.xml',
	#'views/marketing/marketing_order_line.xml',
	#'views/marketing/marketing_reco_line.xml',
	#'views/marketing/media_line.xml',
	#'views/marketing/histogram.xml',
	#'views/marketing/place_actions.xml',
	#'views/marketing/place_pivot.xml',
	#'views/marketing/place.xml',
	#'views/marketing/marketing.xml',  # Dep
	#'views/marketing/marketing_pivot.xml',




	# Management - New
	'views/management/mgt_patient_line.xml',
	'views/management/management_order_line.xml',
	'views/management/management_productivity_day.xml',
	'views/management/management_trees.xml',
	'views/management/management_actions.xml',
	'views/management/management.xml',

	# Too complex
	'views/management/management_doctor_line.xml',		# too complex
	'views/management/management_doctor_daily.xml',	# too complex





	# Dep - Done In PL
	#'views/menus/menus_management.xml',
	#'views/menus/menus_rsp.xml',			# Dep PL
	#'views/menus/menus_marketing.xml', 	# Dep PL
	#'views/menus/menus_account.xml',  		# DEP PL

# ----------------------------------------------------------- Views - Base Actions ------------------------------------------------------
	# Base - Form and List Actions - Must be the first
	'views/base_actions.xml',                                       # Very important - All Actions should go here - Dependencies

# ----------------------------------------------------------- Reports -----------------------------
	# Patient
	'reports/patient/report_patient.xml',

	# Formats
	'reports/paper_format.xml',

	# Ticket - Electronic
	'reports/report_layouts.xml',
	'reports/print_ticket_receipt_electronic.xml',

# ----------------------------------------------------------- Views - First Level -----------------
	# Users
	'views/users/user.xml',
	'views/users/user_actions.xml',

	# Groups
	'views/users/group.xml',

	# Orders
	'views/orders/order_administrator.xml',
	'views/orders/order.xml',
	'views/orders/order_tree.xml',
	'views/orders/order_actions.xml',
	'views/orders/order_search.xml',
	'views/orders/order_admin.xml',
	'views/orders/order_account.xml',
	'views/orders/order_report_nex.xml',                # Estado de Cuenta New

	# Payment methods
	'views/orders/payment_method/payment_methods.xml',

	# Counters
	'views/counters/counter_actions.xml',
	'views/counters/counter.xml',

	# Companies
	'views/companies/company.xml',

	# Controls
	'views/controls/control.xml',
	'views/controls/control_admin.xml',

	# Images
	'views/images/image_view.xml',

	# Procedures
	'views/procedures/procedure_search.xml',
	'views/procedures/procedure_actions.xml',
	'views/procedures/procedure.xml',

	# Consultation
	'views/consultations/consultation_search.xml',
	'views/consultations/consultation_actions.xml',
	'views/consultations/consultation.xml',

	# Treatments
	'views/treatments/service_actions.xml',  	# Just a dummy
	'views/treatments/treatment.xml',
	'views/treatments/treatment_actions.xml',

	# Physicians
	'views/physicians/physician.xml',

	# Patients
	'views/patients/patient_origin.xml',
	'views/patients/patient.xml',
	'views/patients/patient_tree.xml',
	'views/patients/patient_search.xml',

	# Partners
	'views/patients/partners/partner_actions.xml',
	'views/patients/partners/partner.xml',



	# Products
	'views/products/product_actions.xml',
	
	'views/products/product_product.xml',
	'views/products/product_product_pl.xml',
	
	'views/products/product_template.xml',
	'views/products/product_template_2019.xml',



	# Cards
	'views/cards/card.xml',

# ----------------------------------------------------------- Views - Second ----------------------
	# Sessions
	'views/sessions/session.xml',
	'views/sessions/session_config_simple_1.xml',
	'views/sessions/session_config_simple_2.xml',
	'views/sessions/session_admin.xml',

	# Consultation - 2
	'views/consultations/consultation_diagnosis.xml',

	# Treatments - 2
	'views/treatments/treatment_orders.xml',
	'views/treatments/treatment_consultations.xml',
	'views/treatments/treatment_services.xml',
	'views/treatments/treatment_procedures.xml',
	'views/treatments/treatment_controls.xml', 	# Sab

	# Patients - 2
	'views/patients/patient_personal.xml',
	'views/patients/patient_control_docs.xml',
	'views/patients/patient_admin.xml',

# ----------------------------------------------------------- Closings ----------------------------
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
	'views/rsp/report_sale_actions.xml',

# ----------------------------------------------------------- Menus ------------------------------------------------------
	'views/menus/menus.xml',
	'views/menus/menus_dev.xml',
	'views/menus/menus_caja.xml',
	'views/menus/menus_products.xml',


	#'views/menus/prod_2019_actions.xml',
	'views/menus/menus_prods_2019.xml',


	'views/menus/menus_oeh.xml',
	'views/menus/menus_management.xml',
	'views/menus/menus_account.xml',

# ----------------------------------------------------------- Security - Models - Last ------------------------------------------------------
	'security/ir.model.access.csv',
	'security/ir.rule.xml',                # Dep ?
],
'demo': [],
# Static - Style Css
'css': ['static/src/css/jx.css'],
'js': [],
}
