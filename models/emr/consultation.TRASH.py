# 2 Oct 2019

#from . import app_vars

	#_inherit = ['openhealth.base', 'oeh.medical.evaluation']

	#----------------------------------------------------------- Deprecated ------------------------------------------------------------

	# Appointments 
	#appointment_ids = fields.One2many(
	#		'oeh.medical.appointment', 

	#		'consultation', 
	#		string = "Citas", 
	#		required=True, 
	#	)

	# Number of appointments
	#nr_apps = fields.Integer(
	#			string="Citas",
	#			compute="_compute_nr_apps",
	#)

	#@api.multi
	#def _compute_nr_apps(self):
	#	for record in self:
	#		ctr = 0 
	#		for a in record.appointment_ids:
	#			ctr = ctr + 1		
	#		record.nr_apps = ctr











	#service_co2_ids = fields.Char()
	#service_excilite_ids = fields.Char()
	#service_ipl_ids = fields.Char()
	#service_ndyag_ids = fields.Char()
	#service_medical_ids = fields.Char()
	#service_ids = fields.Char()

	# Target 
	#x_target = fields.Selection(
	#		string="Target", 
	#		selection = app_vars._target_list, 
	#		default="doctor", 
			#required=True, 
	#	)

	# Owner 
	#owner_type = fields.Char(
	#		default = 'consultation',
	#	)

	#evaluation_type = fields.Selection(
	#		default = 'Pre-arraganged Appointment', 
	#		)
