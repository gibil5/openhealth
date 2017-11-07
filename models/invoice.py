# -*- coding: utf-8 -*-
#
# 	Invoice 
# 
#
from openerp import models, fields, api

class Invoice(models.Model):
	
	_name = 'openhealth.invoice'

	_inherit='openhealth.sale_proof'



	name = fields.Char(
			string="Factura #", 
		)


	family = fields.Selection(
			default='invoice', 
		)





	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'Create Override'
		#print 
		#print vals
		#print 
	
		counter = self.env['openhealth.counter'].search([('name', '=', 'invoice')])		
		counter.increase()


		#Write your logic here
		res = super(Invoice, self).create(vals)
		#Write your logic here

		return res


