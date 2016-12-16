# -*- coding: utf-8 -*-


from openerp import models, fields, api

class Partner(models.Model):

	_inherit = 'res.partner'


	vspace = fields.Char(
			' ', 
			readonly=True
			)



# ----------------------------------------------------------- Indexes ------------------------------------------------------
	
	#patient = fields.Many2one(
	#		'oeh.medical.patient',
	#		string="Patient id", 

	#		ondelete='cascade', 
	#		)




# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):

		print 
		print 'jx'
		print 'Res Partner - Create - Override'
		print 
		print vals
		print 


		print 
		print 'type: ', vals['type']
		
		print 'name: ', vals['name']


		#vals['type'] = 'other'
		#print vals['type']


		print 

		# Return 
		res = super(Partner, self).create(vals)

		return res
