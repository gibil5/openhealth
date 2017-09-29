# -*- coding: utf-8 -*-
#
# 	*** Service Funcs
# 
# Created: 				 20 Jun 2017
# Last updated: 	 	 Id.

from openerp import models, fields, api



@api.multi
def product(self):

	self.service = self.env['product.template'].search([	
													('x_treatment', '=', self.laser),	
													('x_zone', '=', self.zone),	
													('x_pathology', '=', self.pathology),


													('x_time', '=', self.time),	

													#('x_sessions', '=', self.nr_sessions)
												])

	#return product 



@api.multi
def product_m22(self):

	self.service = self.env['product.template'].search([	
													('x_treatment', '=', self.laser),	
													('x_zone', '=', self.zone),	
													('x_pathology', '=', self.pathology),


													('x_time', '=', self.time),	

													('x_sessions', '=', self.nr_sessions)
												])

	#return product 





@api.multi
def product_medical(self):

	print 'jx'
	print self.x_treatment
	print self.sessions
	print 

	self.service = self.env['product.template'].search([	
													('x_treatment', '=', self.x_treatment),	
													
													#('x_zone', '=', self.zone),	
													#('x_pathology', '=', self.pathology),

													('x_sessions', '=', self.sessions)

													#('x_time', '=', self.time),	
												])

	#return product 




