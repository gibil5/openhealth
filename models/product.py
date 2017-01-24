from openerp import models, fields, api
from datetime import datetime


#import jxvars
import prodvars


	

class Product(models.Model):
	#_name = 'openhealth.service'
	_inherit = 'product.template'





	# WTF ? 
	x_name_short = fields.Char()

	x_time = fields.Char()

	#state = fields.Char()






	# Before 
	x_date_updated = fields.Date(
			)

	x_date_created = fields.Date(
			)

	x_price_vip = fields.Float(
		#string = 'Precio VIP - nex',
	)


	x_family = fields.Selection(
		selection=prodvars._family_list,
	)	

	
	x_treatment = fields.Selection(
		selection=prodvars._treatment_list,
	)	



	#x_subtreatment = fields.Selection(
	#	selection=prodvars._subtreatment_list,
	#)	



	x_zone = fields.Selection(
		selection=prodvars._zone_list,
	)	
	
	x_pathology = fields.Selection(
		selection=prodvars._pathology_list,
	)





	#x_sessions = fields.Integer(
	x_sessions = fields.Char(
		#string = 'Sesiones',
		default="",
	)







