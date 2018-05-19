# -*- coding: utf-8 -*-
#
# 	Report Marketing
# 
# Created: 				19 Mayo 2018
#

from openerp import models, fields, api

import datetime
import resap_funcs
import acc_funcs

#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import collections


class Marketing(models.Model):

	#_inherit='sale.closing'

	_name = 'openhealth.marketing'

	#_order = 'create_date desc'
	#_order = 'date_begin asc'
	_order = 'date_begin asc,name asc'



