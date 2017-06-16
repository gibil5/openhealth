# -*- coding: utf-8 -*-



#class TestModelA(common.TransactionCase):
#    def test_some_action(self):
#        record = self.env['model.a'].create({'field': 'value'})
#        record.some_action()
#        self.assertEqual(
#            record.field,
#            expected_field_value)




class TestProduct(common.TransactionCase):

	def test_some_action(self):
    
		name = 'Prod 1'
		product = self.env['product.template'].create({
								#'field': 'value',
								#'field': 'value',
								'name': name,
								})
    
	#record.some_action()
    
	#self.assertEqual(
	#    record.field,
	#    expected_field_value)









