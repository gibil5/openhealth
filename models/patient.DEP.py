





# ----------------------------------------------------------- Quality control ------------------------------------------------------

	# QC - Number of clones  
	x_nr_clones = fields.Integer(
			"QC - Nrc",

			#compute="_compute_x_nr_clones",
	)
	#@api.multi
	#def _compute_x_nr_clones(self):
	#	for record in self:
	#		record.x_nr_clones = self.env['oeh.medical.patient'].search_count([
	#																			('name','=', record.name),
	#																		])
	#		if record.x_nr_clones > 1:
	#			record.x_flag = 'error'
	#		else:
	#			record.x_flag = ''




	# QC - Lowcase
	x_lowcase = fields.Boolean(
			"QC - Low",

			#compute="_compute_x_lowcase",
	)
	#@api.multi
	#def _compute_x_lowcase(self):
	#	for record in self:
	#		if record.name != record.name.upper():
	#			record.x_lowcase = True
	#			record.x_flag = 'error'
	#		else:
	#			record.x_lowcase = False




	# Spaced 		- ?
	x_spaced = fields.Boolean(
		string="Spaced",
		default=False, 

		#compute='_compute_spaced', 
	)

	#@api.multi
	#@api.depends('name')
	#def _compute_spaced(self):
	#	for record in self:
	#		if record.name[0] == ' ':
	#			record.x_spaced = True






