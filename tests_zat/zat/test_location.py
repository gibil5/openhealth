

# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase

class test_location(TransactionCase):

	def setUp(self):
		super(test_location, self).setUp()
		self.LocationObj = self.env['stock.location']

	def test_location(self):
		record = self.LocationObj.search([('name','=','Stock')])
		self.assertEqual(record.id,1)
