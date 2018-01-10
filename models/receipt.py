# -*- coding: utf-8 -*-
#
# 	Receipt 
# 
#
from openerp import models, fields, api

class Receipt(models.Model):

	_name = 'openhealth.receipt'

	_inherit='openhealth.sale_proof'



	name = fields.Char(
			string="Boleta #", 
		)


	family = fields.Selection(
			default='receipt', 
		)





	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'Receipt - Create Override'
		#print 
		#print vals
		#print 
	


		# Counter 
		counter = self.env['openhealth.counter'].search([('name', '=', 'receipt')])

		vals['serial_nr'] = counter.total

		counter.increase()



		#Write your logic here
		res = super(Receipt, self).create(vals)
		#res = super(family.capitalize(), self).create(vals)
		#Write your logic here

		return res

