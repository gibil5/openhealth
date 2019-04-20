from openerp import models, fields, api, _

class MyModel(models.Model):
	_name = 'a.model' 

	firstname = fields.Char(string="Firstname")

	def jx_fun():
		#print 'jx'

	def a_fun(self):
		self.do_something() 
		record_set = self
		record_set.do_something()

	def do_something(self):
		for record in self:
			#print record



