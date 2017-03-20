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


		Clínica Chavarri - EMPTY\n

		Laser - EMR (Electronic Medical Records)\n

		Last built: 	17 Mar 2017

		Created: 	 	7 Sep 2016

		Active: 		7 months.

		---




		This is my first extension for oeHealth.
		Completely independent and self-referecing.\n
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
			
			
	""",

	'author': "DataMetrics",
	'website': "http://jrevilla.com/",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
	# for the full list
	'category': 'Health',
	'version': '1.0',




	# Very important !!!
	# --------------
	'depends': ['base', 'oehealth'],





	# always loaded
	'data': [



	],
	# only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],
	
	
	
	# Static - jx 

	#'js': ['static/src/js/widget_radio.js'],
	#'qweb': ['static/src/xml/widget_radio.xml'],
	#'css': ['static/src/css/my_css.css'],



}


