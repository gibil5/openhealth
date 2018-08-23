

# 6 Jan 2017


	#name = 'name'
	#treatment = False
	#cosmetology = False
	#if process == 'treatment':
	#	treatment = self.id
	#if process == 'cosmetology':
	#	cosmetology = self.id








																#('patient', 'like', self.patient.name),		
																#('doctor', 'like', self.physician.name), 	
																#('x_type', 'like', 'procedure'), 



	#print appointment
	#print appointment.state

	# Change App state 
	#appointment.state = 'completed'

	#print appointment.state




	#for line in self.order_pro_ids.order_line:



	# Chief complaint 
	#for sale in self.order_ids:
	#	chief_complaint = sale.x_chief_complaint
	#	#print 'chief_complaint:', chief_complaint


				#if self.nr_procedures < self.order_pro_ids.nr_lines:

					#product = self.env['product.product'].search([




					#product = product_template.id




																#'product':product,






# 12 Apr 2018

			#print service
			#print target_line




			#ret = order.x_create_order_lines_target(target_line)
			#ret = order.x_create_order_lines_target(target_line, price_manual)



# 16 Aug 2018 

	# Recommendations
	#if rec_set != False: 
	for reco in rec_set: 

		print 'Gotcha !'
		
		#target_line = service.service.x_name_short
		#price_manual = service.price_manual
		#price_applied = service.price_applied
		#ret = order.x_create_order_lines_target(target_line, price_manual, price_applied)
		#service.state = 'budget'

		# Init 
		reco_id = reco.id
		name_short = reco.service.x_name_short		
		price_manual = reco.price_manual
		price_applied = reco.price_applied

		ret = order.x_create_order_lines_target(name_short, price_manual, price_applied, reco_id)


		# Update state 
		reco.state = 'budget'

	return 0

# create_order_lines






def create_procedure_go(self, app_date_str, subtype, product_id):

	# Loop - Create Procedures 
	#ret = 0
	#for order in self.order_pro_ids:
		#if order.state == 'sale' 	and 	not order.x_procedure_created: 
			# Update 
			#order.x_procedure_created = True
			# Loop
			#for line in order.order_line:
	# Init 
	#product_product = line.product_id
	#product_product = product_id


