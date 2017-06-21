#import os
#import re
#import sys
#import subprocess
#import openerp

import unittest2

from openerp.tests import common
#from openerp.tests.common import TransactionCase
#from openerp import tests
#from openerp import sql_db
#import openerp


# export OPENERP_SERVER=/Users/gibil/Virtualenvs/Odoo9-min/odoo/jx_config.cfg


def fun(x):
	return x + 1


class MyTest(unittest2.TestCase):
	def test(self):
		self.assertEqual(fun(3), 4)

class LearningCase(unittest2.TestCase):
	def test_starting_out(self):
		self.assertEqual(1, 1)



class TestModelPartner(common.TransactionCase):
#class TestModelPartner(tests.common.TransactionCase):
#class TestModelPartner(TransactionCase):
	def test_some_action(self):

		_logger.debug("Debug message")

		#record = self.env['model.a'].create({'field': 'value'})

		#name = 'Javier Revilla'

		#record = self.env['res.partner'].create({
		#											'name': name, 
		#									})

		self.assertEqual(1, 1)




def main():
	unittest2.main()

if __name__ == "__main__":
	main()
