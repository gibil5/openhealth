from openerp import models, fields, api
#from datetime import datetime



class Partner(models.Model):
	
	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?	- Deprecated

	_inherit = 'res.partner'



	#x_owner = fields.Char(
	#						string='Owner', 
	#	)
	#x_sex = fields.Char(
	#						string='Sex', 
	#	)


