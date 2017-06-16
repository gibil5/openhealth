# -*- coding: utf-8 -*-




class TestModelPartner(common.TransactionCase):

	def test_some_action(self):


		#record = self.env['model.a'].create({'field': 'value'})

		name = 'Javier Revilla'

		record = self.env['res.partner'].create({

												'name': name, 
											})



		#record.some_action()

		#self.assertEqual(
		#	record.field,
		#	expected_field_value)


