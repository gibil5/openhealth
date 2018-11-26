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

		'data/base_data_categs_partners.xml',			
		'data/base_data_categs_prods.xml',			


		# Users 
		'data/users/base_data_users_managers.xml',	 
		'data/users/base_data_users_staff.xml',		 
		'data/users/base_data_users_almacen.xml',		 
		'data/users/base_data_users_doctors.xml',		 
		'data/users/base_data_users_assistants.xml',	
		'data/users/base_data_users_platform.xml',	
		'data/users/base_data_users_cash.xml',		 




		# Products 
		'data/prods/odoo_data_products.xml',			 
		'data/prods/odoo_data_services_co2.xml',		
		'data/prods/odoo_data_services_exc.xml',		
		'data/prods/odoo_data_services_m22.xml',		
		'data/prods/odoo_data_services_med.xml',		
		'data/prods/odoo_data_services_cos.xml',		
		'data/prods/odoo_data_services_consult.xml',	


		# Doctors
		'data/base_data_physicians.xml',				





		# Pricelists 
		'data/pricelists.xml',							
		'data/pricelist_quick.xml',						
		'data/pricelist_quick_return.xml',						





		# Suppliers 
		'data/suppliers.xml',							



		],

	'demo': [],

	'css': [],

	'js': [''],

}


