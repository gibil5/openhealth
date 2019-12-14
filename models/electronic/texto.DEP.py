# 13 Dec 2019

# -*- coding: utf-8 -*-
"""
#		Texto - In PL now
#
# 		Created: 		14 Oct 2016
# 		Last up: 		14 Oct 2018
"""

from openerp import models, fields, api
from openerp.exceptions import ValidationError
#from openerp.exceptions import Warning

class Texto(models.Model):
	"""
	high level support for doing this and that.
	"""

	_name = 'openhealth.texto'

	#_order = 'content asc'
	_order = 'name asc'



# ----------------------------------------------------------- Constraints - Sql -------------------
	_sql_constraints = [
							#('name_unique', 'unique(name)', 'SQL Warning: NAME must be unique !'),
							('name_unique',	'Check(1=1)', 'SQL Warning: NAME must be unique !'),

							#('content_unique',	'unique(content)', 	'SQL Warning: CONTENT must be unique !'),
						]



# ----------------------------------------------------------- Python ------------------------------

	# Check Name
	@api.constrains('name')
	def _check_name(self):

		for record in self:

			#if record.name == '0':
			#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)


			# Count
			if record.name != False:
				count = self.env['openhealth.texto'].search_count([
																	('name', '=', record.name),
											])
				if count > 1:
					raise ValidationError("Rec Error: NAME already exists: %s" % record.name)
					#raise Warning("Rec Error: NAME already exists: %s" % record.name)



		# all records passed the test, don't return anything





# ----------------------------------------------------------- Handles -----------------------------

	container_id = fields.Many2one(
			'openhealth.container',
			ondelete='cascade',
		)

	container_ref_id = fields.Many2one(
			'openhealth.container',
			ondelete='cascade',
		)




# ----------------------------------------------------------- Fields ------------------------------

	name = fields.Char()

	content = fields.Char()
