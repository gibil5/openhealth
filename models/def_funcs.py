# -*- coding: utf-8 -*-

from openerp import models, fields, api



# ----------------------------------------------------------- Defaults ------------------------------------------------------

# Returns the Default Model Id 
@api.multi
def _get_default_id(self, x_type):

	#print 
	#print 'Get Default Id'
	#print x_type

	_h_vars = {
				'patient' : 	('oeh.medical.patient',		'REVILLA RONDON JOSE JAVIER'), 

				'doctor' : 		('oeh.medical.physician',	'Dr. Chavarri'), 

				#'product' : 	('product.product', 		'PROTECTOR SOLAR'), 
				'product' : 	('product.product', 		'TOKEN'), 
			}

	
	model = _h_vars[x_type][0]
	name = _h_vars[x_type][1]
	
	#print model
	#print name 

	obj = self.env[model].search([
									('name', '=', name), 
								],
								#order='write_date desc',
								limit=1,
							)
	#print obj

	return obj.id

# _get_default_id

