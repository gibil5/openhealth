# -*- coding: utf-8 -*-
{
    'name': "Open Health - SERVICE ORIENTED - MIN",

    'summary': """
            Minimalist version
    """,

    'description': """
        Contains:
            - All Models,
            - All Dependencies,
            - All Data,
            - No Views
            - No Security
    """,

    'author': "",

    'website': "",
    
    'category': '',
    
    'version': '',

    'depends': ['base', 'oehealth', 'base_multi_image'],

    
    'data': [


        # Users
        'data/physicians/base_data_physicians.xml',                 # Aggregates all
        'data/physicians/base_data_physicians_inactive.xml',        
        'data/users/base_data_users_platform.xml',  
        'data/users/base_data_users_cash.xml',
        'data/users/base_data_users_account.xml',       
        'data/users/base_data_users_managers.xml',  
        'data/users/base_data_users_doctors.xml',
        'data/users/base_data_users_assistants.xml',    


        # Data
        'data/categs/base_data_categs_prods.xml',
        'data/allergies/allergy.xml',
        'data/prods/odoo_data_products.xml',
        'data/prods/odoo_data_products_new.xml',            # Has integrated the following
        'data/prods/odoo_data_services_consult.xml',
        'data/prods/odoo_data_services_co2.xml',
        'data/prods/odoo_data_services_exc.xml',
        'data/prods/odoo_data_services_m22.xml',
        'data/prods/odoo_data_services_med.xml',
        'data/prods/odoo_data_services_cos.xml',
        'data/prods/odoo_data_services_med_dep.xml',    # Dependance


        # Pricelists - Vip
        'data/pricelists/pricelists.xml',
        

        # Dep
        #'data/suppliers.xml',                          # Very Important - Account Invoice Dependance
        'data/users/base_data_users_inactive.xml', 



# ----------------------------------------------------------- Views ------------------------------------------------------


        #'views/min/patient.xml',
        #'views/min/patient_personal.xml',


        #'views/min/treatment.xml',
        #'views/min/treatment_services.xml',
        

        #'views/min/order.xml',

        #'views/min/account_contasis.xml',


        #'views/min/configurator_emr.xml',
    ],

    
    'demo': [],

    'css': [],

    'js': [],
}
