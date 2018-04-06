



# 5 Apr 2018


# ----------------------------------------------------------- Computes ------------------------------------------------------

	# Total 
	total = fields.Char(
			string="Total", 
		
			#compute='_compute_total', 
		)

	#@api.multi
	#@api.depends()
	#def _compute_total(self):		
	#	for record in self:
	#		if record.prefix != False:
	#			if record.separator != False: 
	#				record.total = record.prefix  +  record.separator  +  str(record.value).zfill(record.padding)
	#			else:
	#				record.total = record.prefix  +  str(record.value).zfill(record.padding)

