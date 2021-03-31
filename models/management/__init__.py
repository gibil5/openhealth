# -*- coding: utf-8 -*-

# Import modules

# Management
from . import mgt_productivity_day
from . import mgt_order_line
from . import mgt_family_line
from . import mgt_subfamily_line
from . import mgt_day_line
from . import management

# Patient
from . import mgt_patient_line

# Doctor - Too complex 
# Isolate and Reduce inheritance
from . import mgt_doctor_day_line   # For doctor_line
from . import mgt_doctor_line      # Too complex 
from . import mgt_doctor_daily
