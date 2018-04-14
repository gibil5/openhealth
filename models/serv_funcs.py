# -*- coding: utf-8 -*-
#
# 	*** Service Funcs
# 
# Created: 				 20 Jun 2017
#

from openerp import models, fields, api


# Product 
@api.multi
def product(self):

	self.service = self.env['product.template'].search([	
														('x_treatment', '=', self.laser),	
														('x_zone', '=', self.zone),	
														('x_pathology', '=', self.pathology),
														('x_time', '=', self.time),	
												])


# Product M22
@api.multi
def product_m22(self):

	self.service = self.env['product.template'].search([	
														('x_treatment', '=', self.laser),	
														('x_zone', '=', self.zone),	
														('x_pathology', '=', self.pathology),
														('x_time', '=', self.time),	
														('x_sessions', '=', self.nr_sessions)
												])

# Medical 
@api.multi
def product_medical(self):

	self.service = self.env['product.template'].search([	
															('x_treatment', '=', self.x_treatment),	
															('x_sessions', '=', self.sessions)
												])





