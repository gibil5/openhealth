# -*- coding: utf-8 -*-

#from . import models


#from . import lib
from libs import *




# Account
#from . import account_line
#from . import account_contasis
from account import *




# Order 
#from . import order
#from . import order_line
#from . import product_selector
#from . import payment_method
#from . import payment_method_line
#from . import closing
#from . import card
#from . import order_report_nex			# Estado de Cuenta 
from order import *





#from . import partner
#from . import patient  
#from . import counter
#from . import company
from patient import *





# Management
#from . import mgt_line
#from . import doctor_line
#from . import family_line
#from . import sub_family_line
#from . import management_order_line
#from . import management 
from management import *






# Inheritable 
from . import medical
from . import line
from . import repo





# Electronic
from . import electronic_order
from . import electronic_line
from . import coder 
from . import texto


# Containers
from . import container
from . import corrector




# Marketing
from . import media_line
from . import marketing_recommendation_line
from . import marketing_order_line
from . import patient_line
from . import histo_line
from . import place_line
from . import marketing









# Reports
from . import report_order_line
from . import product_counter 
from . import report_sale_product











# EMR
from . import product
from . import product_product
from . import image		
from . import allergy  
from . import process 
from . import treatment 
from . import evaluation  
from . import appointment 
from . import consultation
#from . import recommendation    	# Deprecated 
from . import procedure
from . import control
from . import physician 
from . import session 
from . import session_med




# New
from . import product_pricelist_item






# Zones
from . import zone
from . import nexzone
from . import pathology





# Services 
from . import service
from . import service_co2
from . import service_excilite
from . import service_ipl
from . import service_ndyag
from . import service_medical
from . import service_quick
from . import service_vip
from . import service_cosmetology
from . import service_product
from . import service_consultation











#--------------
# DEPRECATED
#--------------
#from . import event
#from . import sale_report
#from . import sale_report_md
#from . import filesystem_directory
#from . import filesystem_file
#from . import account_line_contasis
#from . import report
#from . import report_sale






# Test
#from . import test

# Order 
#from . import ticket

# Cosmetology 
#from . import cosmetology				
#from . import cos_classes

# Legacy
#from . import legacy
#from . import legacy_manager
#from . import legacy_manager_patient
#from . import legacy_manager_order

#from . import data_analyzer

# Purchase 
#from . import purchase
#from . import purchase_order_line
#from . import account_invoice


# Stock 
#from . import stock_move
#from . import stock_min
#from . import stock_move_selector
#from . import kardex

