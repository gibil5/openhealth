# -*- coding: utf-8 -*-
#
# 	Receipt 
# 
#

from openerp import models, fields, api

class Receipt(models.Model):

	_name = 'openhealth.receipt'

	_inherit='openhealth.sale_proof'




# ----------------------------------------------------------- Defaults ------------------------------------------------------

	@api.model
	def _get_default_serial_nr(self):

		print 'jx'
		print 'Get Default Serial Number'


		name = 'receipt'


		#counter = self.env['openhealth.counter'].search([('name', '=', serial_nr)])
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name), 
															],
																#order='write_date desc',
																limit=1,
															)

 		#print counter 
 		
		default_serial_nr = '13'


		if counter.total != False: 
			default_serial_nr = counter.total
			counter.increase()



		#print default_serial_nr
		
		return default_serial_nr




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name 
	name = fields.Char(
			string="Boleta #", 
		)

	# Family 
	family = fields.Selection(
			default='receipt', 
		)




	# Serial Number 
	serial_nr = fields.Char(
			#string="Nr de Serie", 
			default=_get_default_serial_nr, 
			#readonly=True, 
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
		#counter = self.env['openhealth.counter'].search([('name', '=', 'receipt')])
		#vals['serial_nr'] = counter.total
		#counter.increase()




		#Write your logic here
		res = super(Receipt, self).create(vals)
		#res = super(family.capitalize(), self).create(vals)
		#Write your logic here

		return res

