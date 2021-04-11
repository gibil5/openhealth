# -*- coding: utf-8 -*-
"""
		*** Test Funcs

		Give low-level services. To Treatment.

		Used by:	test_treatment.py

		Created: 			17 Jul 2019
		Last up: 	 		22 Jul 2019
"""
from __future__ import print_function
import sys
import os

# ----------------------------------------------- Test Funcs ----------------------------------------------------------
def disablePrint():
	"""
	Disable Print
	"""
	sys.stdout = open(os.devnull, 'w')

def enablePrint():
	"""
	Enable Print
	"""
	sys.stdout = sys.__stdout__
