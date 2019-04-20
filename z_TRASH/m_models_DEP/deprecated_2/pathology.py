from openerp import models, fields, api
from datetime import datetime

import jxvars



	

class Pathology(models.Model):
	_name = 'openhealth.pathology'
	#_inherit = 'product.template'
	
	
	_co2_han_list = [
			('stains',	'Manchas'),	
			('scar',	'Cicatriz'),
			('wart',	'Verruga'),
			('rejuvenation_hands',	'Rejuvenecimiento'),
			('none',''),
			]
			

	name = fields.Selection(
			selection =_co2_han_list,
			default='stains',	
			)
	
	service_co2 = fields.Many2one('openhealth.service.co2',
			ondelete='cascade', 
			#string="", 
			string="Servicio Co2", 
			)