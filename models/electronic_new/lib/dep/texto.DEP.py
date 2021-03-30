# 13 Dec 2019


# ----------------------------------------------------------- Constraints - Sql - Dep -------------------
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


	container_ref_id = fields.Many2one(
			'openhealth.container',
			ondelete='cascade',
		)

