# -*- coding: utf-8 -*-
#
# 	Advertisement 
# 
from openerp import models, fields, api

class Advertisement(models.Model):
	
	_name = 'openhealth.advertisement'

	_inherit='openhealth.sale_proof'



	# ----------------------------------------------------------- Defaults ------------------------------------------------------
	@api.model
	def _get_default_serial_nr(self):

		print 'jx'
		print 'Get Default Serial Number - Advertisement'

		name = 'advertisement'
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name), 
															],
																#order='write_date desc',
																limit=1,
														)
		default_serial_nr = '13'

		if counter.total != False: 
			default_serial_nr = counter.total
			counter.increase()

		return default_serial_nr


	# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Serial Number 
	serial_nr = fields.Char(
			default=_get_default_serial_nr, 
		)


	name = fields.Char(
			string="Canje #", 
		)


	family = fields.Selection(
			default='advertisement', 
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
	

		# Counter - Deprecated 
		#counter = self.env['openhealth.counter'].search([('name', '=', 'advertisement')])		
		#vals['serial_nr'] = counter.total
		#counter.increase()



		#Write your logic here
		res = super(Advertisement, self).create(vals)
		#Write your logic here

		return res

		