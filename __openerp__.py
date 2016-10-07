# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
#   Last up: 2 Oct 2016
#

{
    'name': "openHealth",

    'summary': """
		Extension for Odoo-oeHealth. 
		Treatments. 
	""",

    'description': """

		Installed: 	 7 Sep 2016.\n 
		Upgraded: 	 5 Oct 2016.\n 
		\n

		This is my first extension for oeHealth.
		Completely independent and self-referecing.\n
		It provides the following objects:
            - Patients
            - Treatments
            - Evaluations
            - Consultations
            - Procedures
            - Controls 
            - Services
    """,

    'author': "DataMetrics",
	'website': "http://javier-revilla.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health',
    'version': '1.0',


    # any module necessary for this one to work correctly
    #'depends': ['base'],
    'depends': ['base', 'oehealth'],
    #'depends': ['base', 'oehealth', 'openextension'],
    #'depends': ['base', 'openextension'],




    # always loaded
    'data': [

		'views/openhealth.xml',

        
        # Generated
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
		
        
		
		
        # Learning 
        'views/learning/learn.xml',




        # Treatments 
		'views/treatments/treatment.xml',
		
		
		
		# Services
		#'views/service/service.xml',
		#'views/service/laserco2.xml',
		'views/service/service_co2.xml',
		'views/service/service_co2_zone.xml',



		# Invoices
		#'views/treatments/invoice.xml',

		
        # Patients 
        'views/patients/patient.xml',
		'views/patients/patient_personal.xml',
		'views/patients/patient_treatments.xml',
		'views/patients/patient_control_docs.xml',
		
        #'views/patients/patient_lab.xml',
		#'views/patients/patient_med.xml',



        # Evaluations
		#'views/evaluations/evaluation.xml',
		'views/evaluations/evaluation_oeh.xml',
		
		'views/evaluations/consultation.xml',
		'views/evaluations/consultation_first.xml',

		'views/evaluations/consultation_procedures.xml',

		'views/evaluations/consultation_services.xml',



		# jx_eval
		#'views/evaluations/jx_eval_co2.xml',
		#'views/evaluations/jx_eval_excilite.xml',
		#'views/evaluations/jx_eval_ipl.xml',
		#'views/evaluations/jx_eval_ndyag.xml',



		
        'views/evaluations/consultation_quotation.xml',        
		'views/evaluations/quotation.xml',
		'views/evaluations/order.xml',

        
		'views/evaluations/procedure.xml',



    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
	
	
	
	# Static - jx 
	#'js': ['static/src/js/widget_radio.js'],
	#'qweb': ['static/src/xml/widget_radio.xml'],
    #'css': ['static/src/css/my_css.css'],
	'css': ['static/src/css/jx.css'],
	
	
}
