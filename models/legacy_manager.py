# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Patient Legacy Manager
# 

# Created: 				24 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api




class LegacyManager(models.Model):


	#_order = 'write_date desc'

	_description = 'Legacy Manager'



	_inherit = 'openhealth.legacy'

	#_name = 'openhealth.patient.legacy'
	_name = 'openhealth.legacy.manager'







# ----------------------------------------------------------- Primitives ------------------------------------------------------

	name = fields.Char(
			#string='Nombre',
			#required=True, 
		)





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi 
	def update_patients(self):

		print 'jx'
		print 'Update Patients'






