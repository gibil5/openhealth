

from openerp import models, fields, api


class PhysicianLine(models.Model):


	_inherit = 'oeh.medical.physician.line'  


	# Array containing different days name
	PHY_DAY = [
		('Monday', 'Lunes'),
		('Tuesday', 'Martes'),
		('Wednesday', 'Miercoles'),
		('Thursday', 'Jueves'),
		('Friday', 'Viernes'),
		('Saturday', 'Sabado'),
		('Sunday', 'Domingo'),
		]


	name = fields.Selection(
		PHY_DAY, 
		'Dias disponible', 
		required=True
	)

