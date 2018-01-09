# -*- coding: utf-8 -*-

#from . import models



# Base 
#from . import base  	- DEPRECATED ? 
#from . import test  	- DEPRECATED ?




# Base
from . import partner
from . import quotation

from . import patient  
from . import product



# Deprecated 
#from . import learn_1
#from . import quotation
#from . import pathology
#from . import therapist 




# After Travis
#from . import openhealth.models.appfuncs 
from . import appfuncs 
#from openhealth.models import appfuncs 





# Operational 

from . import closing


from . import card
from . import purchase
from . import purchase_order_line

#from . import purchase_po
#from . import purchase_rfq
#from . import purchase_line_rfq



from . import stock_picking 
from . import stock_move_selector
from . import stock_move
from . import stock_pack_operation 






from . import process 
from . import treatment 
from . import cosmetology				
from . import evaluation  


from . import physician 
from . import physician_line 


from . import consultation
from . import recommendation
from . import procedure
from . import session 
from . import session_med
from . import control




from . import image  			
#from . import image_full		# Deprecated ?
#from . import multi_image		# Deprecated 





#from . import zone_category
from . import zone


#from . import pathology_category
from . import pathology



from . import counter_raw


from . import service
from . import service_co2
from . import service_excilite
from . import service_ipl
from . import service_ndyag
from . import service_medical

from . import service_quick

from . import service_vip




from . import sale_make_invoice_advance





from . import order
from . import order_line


from . import account_invoice



#from . import oh_sale_report
from . import sale_report


#from . import sale_document
from . import sale_proof

from . import invoice
from . import receipt

from . import advertisement
from . import sale_note
from . import ticket_receipt
from . import ticket_invoice



from . import counter

from . import payment_method
from . import payment_method_line


from . import event 


from . import appointment 




# Cosmetology 	- Deprecated ? 
from . import consultation_cos
from . import procedure_cos
from . import session_cos
from . import service_cosmetology
from . import appointment_cos


