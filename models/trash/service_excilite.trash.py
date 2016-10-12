	belly = fields.Selection(
			selection = exc._belly_list, 
			string="Abdomen", 
			default='',	
			)

	areolas = fields.Selection(
			selection = exc._areolas_list, 
			string="Ariolas", 
			default='',	
			)
			
	armpits = fields.Selection(
			selection = exc._armpits_list, 
			string="Axilas", 
			default='',	
			)
			
_belly_list = [
		('vitiligo',	'Vitiligo'),	
		('psoriasis',	'Psoriasis'),
		('alopecia',	'Alopecias'),
		
		('none',''),
		]

_areolas_list = [
		('vitiligo',	'Vitiligo'),	
		('psoriasis',	'Psoriasis'),
		('alopecia',	'Alopecias'),
		
		('none',''),
		]
		
_armpits_list = [
		('vitiligo',	'Vitiligo'),	
		('psoriasis',	'Psoriasis'),
		('alopecia',	'Alopecias'),
		
		('none',''),
		]