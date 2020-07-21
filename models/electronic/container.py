# -*- coding: utf-8 -*-
"""
	Container

	Created: 				30 Sep 2018
	Last mod: 				 4 Nov 2018
"""
from __future__ import print_function

from openerp import models, fields, api

class Container(models.Model):
	"""
	Electronic Containter
	"""
	_name = 'openhealth.container'

	_inherit='openhealth.django.interface'



