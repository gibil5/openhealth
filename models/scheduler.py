# -*- coding: utf-8 -*-
#
#
# 	Scheduler 
# 
# Created: 				21 Mar 2018
# Last updated: 	 	id


from openerp import models, fields, api

class scheduler(models.Model):
	
	#_inherit='sale.order'

	_name = 'openhealth.scheduler'
	


# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Create Closing  
	#@api.multi
	#def create_closing(self):  
	#def schedule_backup(self, cr, user, context={}):
	def create_closing(self, cr, user, context={}):

		#self.create_closing()
		

		print 'jx'
		print 'Create closing'

		today = '2018-03-21'

		#closings = self.env['openhealth.closing'].search([
																												
		#													('date', '=', today),

		#									])
		print closings


		print 'out'

