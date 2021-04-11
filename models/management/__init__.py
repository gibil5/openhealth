# -*- coding: utf-8 -*-
from __future__ import absolute_import

# Import modules

# Management
from . import mgt_productivity_day
from . import mgt_order_line
from . import mgt_family_line
from . import mgt_subfamily_line
from . import mgt_day_line

#from . import management
from . import management_view
from . import management_controller
from . import management_tools
#from . import management_bridge


# Patient
from . import mgt_patient_line

# Doctor - Too complex 
# Isolate and Reduce inheritance
from . import mgt_doctor_day_line   # For doctor_line
from . import mgt_doctor_line      # Too complex 
from . import mgt_doctor_daily
