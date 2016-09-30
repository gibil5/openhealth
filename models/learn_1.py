from openerp import models, fields, api, _


class AModel(models.Model):
	#_name = 'a.model'
	_name = 'openhealth.learn'


	name = fields.Char(
			default='Name', 
			string='Name', 
			)

	a_field = fields.Char(
			default='A field', 
			string="A field"
			)

	a = fields.Integer(
			string="a"
			)

	b = fields.Integer(
			string="b"
			)

	c = fields.Integer(
			string="c"
			)


	def a_method(self):
			# self can be anywhere between 0 records and all records in the
			# database
			self.do_operation()

	def do_operation(self):
			print 'jx:self'
			print self # => a.model(1, 2, 3, 4, 5)
			print 'jx:records'
			for record in self:
				print record # => a.model(1), then a.model(2), then a.model(3), ...

	def do_msg(self):
			return {"msg" : "Message from Learn"}

	def do_55(self):
			print 'jx:debug'
			return 55
		


