
	# Name 
	name = fields.Char(
		)


	# Name short
	name_short = fields.Char(
		)



	pathology = fields.Many2one(
			'openhealth.pathology', 
		)




	laser_quick = fields.Boolean(
		)

	laser_co2 = fields.Boolean(
		)

	laser_excilite = fields.Boolean(
		)

	laser_ipl = fields.Boolean(
		)

	laser_ndyag = fields.Boolean(
		)







	treatment = fields.Selection(
			[
				('laser_quick','Quick Laser'), 

				('laser_co2','Laser Co2'), 
				('laser_excilite','Laser Excilite'), 
				('laser_ipl','Laser Ipl'), 
				('laser_ndyag','Laser Ndyag'), 
			], 
		)



	# Service 
	#service = fields.Many2one(			
	#		'openhealth.service',
	#	)
