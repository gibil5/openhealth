# -*- coding: utf-8 -*-
#
# 	Minimal 
# 


{
	'name': "Open Health - MIN",

	
	'summary': """
	""",


	'description': """

		MINIMAL

		---
			
			
	""",

	'author': "",

	'website': "",

	'category': '',

	'version': '',

	'depends': ['base', 'oehealth', 'base_multi_image'],

	'data': [

		'data/base_data_categs_partners.xml',			# check
		'data/base_data_categs_prods.xml',			# check


		# Users 
		'data/users/base_data_users_managers.xml',	# check 
		'data/users/base_data_users_staff.xml',		# check 
		'data/users/base_data_users_almacen.xml',		# check 
		'data/users/base_data_users_doctors.xml',		# check 
		'data/users/base_data_users_assistants.xml',	# check
		'data/users/base_data_users_platform.xml',	# check
		'data/users/base_data_users_cash.xml',		# check 




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
		'data/pricelists.xml',							
		'data/pricelist_quick.xml',						
		'data/pricelist_quick_return.xml',						





		# Suppliers 
		'data/suppliers.xml',							# DEPRECATED - Very 



		],

	'demo': [],

	'css': [],

	#'js': ['static/src/js/progressbar.js'],

}


