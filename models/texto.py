# -*- coding: utf-8 -*-
#
#		Texto
# 
# 		Created: 		14 Oct 2016
# 		Last up: 		14 Oct 2018
#
from openerp import models, fields, api

from openerp.exceptions import ValidationError


class Texto(models.Model):
	
	_name = 'openhealth.texto'



# ----------------------------------------------------------- Constraints - Sql ------------------------------------------------------

	_sql_constraints = [
							('name_unique',		'unique(name)', 	'SQL Warning: NAME must be unique !'),
							('content_unique',	'unique(content)', 	'SQL Warning: CONTENT must be unique !'),
						]     


# ----------------------------------------------------------- Python ------------------------------------------------------
	
	# Check Name  
	@api.constrains('name')
	def _check_name(self):

		#if False: 
		if True: 
			for record in self:
		
				#if record.name == '0':
				#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)

		
				# Count 
				if record.name != False: 
					count = self.env['openhealth.texto'].search_count([
																		('name', '=', record.name),
												])
					if count > 1: 
						raise ValidationError("Rec Warning: NAME already exists: %s" % record.name)

		
			# all records passed the test, don't return anything




# ----------------------------------------------------------- Fields ------------------------------------------------------
	
	name = fields.Char()


	content = fields.Char()


	container_id = fields.Many2one(
			'openhealth.container', 		
			ondelete='cascade', 
		)
