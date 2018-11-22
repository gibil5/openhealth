

# 19 Aug 2018 


# ----------------------------------------------------------- Test Integration - Management ------------------------------------------------------

# Test - Integration 

def test_integration_management(self):

	print 
	print 'Test Integration management'

	report = self.env['openhealth.management'].search([
														#('name_short', '=', 'quick_neck_hands_rejuvenation_1'),
													],
													order='date_begin desc',
													limit=1,
												)
	print report
	print report.name 

	report.update()

	print 'End'

# test_integration_management






# ----------------------------------------------------------- Test Integration - Closing ------------------------------------------------------

# Test - Integration 

def test_integration_closing(self):

	print 
	print 'Test Integration Closing'

	report = self.env['openhealth.closing'].search([
														#('name_short', '=', 'quick_neck_hands_rejuvenation_1'),
													],
													order='date desc',
													limit=1,
												)
	print report
	print report.name 

	report.update_totals()

	print 'End'

# test_integration_closing




# ----------------------------------------------------------- Test Integration - Report Sale Product ------------------------------------------------------

# Test - Integration 

def test_integration_report_sale_product(self):

	print 
	print 'Test Integration RSP'

	report = self.env['openhealth.report.sale.product'].search([
																	#('name_short', '=', 'quick_neck_hands_rejuvenation_1'),
															],
															order='name desc',
															limit=1,
														)
	print report
	print report.name 

	report.update_report()

	print 'End'

# test_integration_report_sale_product




# 20 Aug 2018 

# ----------------------------------------------------------- Test Integration - Report ------------------------------------------------------

# Test - Integration - Report 
# Closing
# Report Sale Product 
# Management 

def test_integration_report(self, model, descriptor):

	print 
	print 'Test Integration Report'

	report = self.env[model].search([
														#('name_short', '=', 'quick_neck_hands_rejuvenation_1'),
													],
													order=descriptor +  ' desc',
													limit=1,
												)
	print report
	print report.name 
	print descriptor 

	report.update()

	print 'End'

# test_integration_report






# Reset 
#@api.multi 
#def reset(self):
def reset_treatment(self):

	# Important
	#self.patient.x_nothing = 'Nothing'

	# Numbers 
	#self.nr_invoices_cons = 0 
	#self.nr_invoices_pro = 0 

	# Add Procs 
	#self.add_procedures = False 





