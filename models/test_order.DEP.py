



# ----------------------------------------------------------- Test - Init -------------------------
# Test - Init
#@api.multi
def test_init(self, patient_id, partner_id, doctor_id, treatment_id, pl_id):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Order - Test Init'

	#self.test_reset()


	# Create Order
	order = self.env['sale.order'].create({
												'partner_id': 	partner_id,
												'patient': 		patient_id,
												'state':		'draft',
												'x_doctor': 	doctor_id,
												'pricelist_id': pl_id,
												'treatment': 	treatment_id,
											})

	# Create Order Lines


	# Tuples - Short Name + Manual price
	tup_arr = [
						('con_med',	0),  					# Consultation
						('con_med',	100),  					# Consultation
						('con_med',	200),  					# Consultation
						('con_gyn', 200),  					# Consultation
						('acneclean', -1),  				# Product
						('vip_card', -1),  					# Product
						('quick_neck_hands_rejuvenation_1',	-1), 	# Quick
						('co2_nec_rn1_one',	-1), 			# Co2
						('exc_bel_alo_15m_one',	-1),		# Exc
						('ipl_bel_dep_15m_six',	-1), 		# Ipl
						('ndy_bol_ema_15m_six',	-1),		# Ndyag
						('bot_1zo_rfa_one',	-1), 			# Medical
						('car_bod_rfa_30m_six',	-1), 		# Cosmeto
				]



	# Init
	#price_manual = 0
	#price_applied = 0
	price_applied = -1
	reco_id = False


	# Create
	for tup in tup_arr:

		name_short = tup[0]
		price_manual = tup[1]

		# Prints
		#print tup
		#print name_short
		#print price_manual

		# Create
		creates.create_order_lines_micro(order, name_short, price_manual, price_applied, reco_id)

	return [order]

# test_init




# ----------------------------------------------------------- Reset -------------------------------
# Test - Reset
#@api.multi
def test_reset(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Order - Reset'
	self.x_payment_method.unlink()
	#self.x_dni = ''
	#self.x_ruc = ''
	self.state = 'draft'			# This works
