# -*- coding: utf-8 -*-
"""
	Mgt Db - Dep !
        Database search and count for the models:
            SaleOrder

	Created: 			26 oct 2020
	Last up: 			12 dec 2020

	Interface
		get_orders_filter_fast
		get_orders_filter
"""
from __future__ import print_function
import datetime

from openerp import models

# ------------------------------------------------------------- Constants ------
_DATE_FORMAT = "%Y-%m-%d"
_DATE_HOUR_FORMAT = "%Y-%m-%d %H:%M"
_MODEL_SALE = "sale.order"
