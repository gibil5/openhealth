"""
API endpoint Update Fast 

For fast updating of the Finance Report 

Should be 100% unit testable with pytest 
Completely decoupled from Odoos low level aspects (fields and db searches)
"""

# ------------------------------------ Example from the Percival Gregory book ------------------------------------------
@flask.route.gubbins 
def allocate_endpoint():     
    batches = SqlAlchemyRepository.list() 
    lines = [ 
        OrderLine ( l [ 'orderid' ], l [ 'sku' ], l [ 'qty' ]) 
            for l in request . params ... 
    ] 
    allocate(lines, batches) 
    session.commit() 
    return 201 


# ------------------------------------ API endpoint ------------------------------------------
#@flask.route.gubbins 
def update_fast():     

	#  Init vectors
    vectors = RepositoryVectors.list() 

	#  Init sales
    lines = update_sales(vector_obj, vector_sub)

    #allocate(lines, batches) 
    #session.commit() 
    #return 201 



# ----------------------------------------------------------- Update Fast ------
def update_sales(self, vector_obj, vector_sub):
	"""
	Update Sales Macros
	Responsibilites:
		- Clean
		- Get orders
		- Loop on sales - Line analysis
		- Update stats

    Called by: update_fast
	"""
	print()
	print('** Update Sales')

	# Clean
	self.reset_macro()

	# Get Orders
	if self.type_arr in ['all']:
		#orders, count = mgt_db.get_orders_filter_fast(self, self.date_begin, self.date_end)
		orders, count = ManagementDb.get_orders_filter_fast(self, self.date_begin, self.date_end)
	else:
		#orders, count = mgt_db.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)
		orders, count = ManagementDb.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)

	# Loop on sales
	tickets = 0
	for order in orders:
		tickets = tickets + 1

		# Filter Block
		if not order.x_block_flow:

			# If sale
			if order.state in ['sale']:

				# Line Analysis
				for line in order.order_line:
                    
                    # Dep !
					#self.line_analysis(line)

					mgt_funcs.line_analysis_type(line, vector_obj)
					mgt_funcs.line_analysis_sub(line, vector_sub)


			# If credit Note - Do Amount Flow
			elif order.state in ['credit_note']:
				self.credit_note_analysis(order)


# After the loop
# Analysis - Setters

	# Set Averages
	#self.set_averages()
	mgt_funcs.set_averages_vector(vector_obj)
	mgt_funcs.set_averages_vector(vector_sub)


# Data model 
	# Set Totals
	self.total_tickets = tickets
	self.total_amount, self.total_count = mgt_funcs.get_totals(vector_obj)

	# Set Percentages
	#mgt_funcs.set_percentages(self, total_amount)
	#results = mgt_funcs.percentages_pure(vector, self.total_amount)
	mgt_funcs.set_percentages_vector(vector_obj, self.total_amount)
	mgt_funcs.set_percentages_vector(vector_sub, self.total_amount)


	# Set Ratios
	#self.set_ratios()
	#mgt_funcs.set_ratios_vector(vector_obj)
	#mgt_funcs.set_ratios_vector(vector_sub)
	#mgt_funcs.set_ratios_vector(nr_consultations, nr_procedures, vector_obj)

	#self.ratio_pro_con = mgt_funcs.set_ratios_vector(vector_fam)
	self.ratio_pro_con = mgt_funcs.set_ratios_vector(vector_sub)


	# Set macro vectors 
	# Bridges
	mgt_bridge.set_totals(self, vector_obj)
	mgt_bridge.set_types(self, vector_obj)
	mgt_bridge.set_subfamilies(self, vector_sub)



	# Test
	print(_pre + 'Vectors - Test' + _pos)

	vecs = [vector_obj, vector_sub]

	for vector in vecs:
		for obj in vector:
		    print(obj.name)
		    print(obj.count)
		    print(obj.amount)
		    print(obj.average)
		    print(obj.percentage)
		    print()

# update_sales


