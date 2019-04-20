

#receipt_id, order_id, patient_id, doctor_id, total = order_funcs.create_document_go(self, 'receipt')
@api.multi 
def create_document_go(self, type_doc):

		#print 
		#print 'Create'

		order_id = self.id 
		patient_id = self.patient.id
		doctor_id = self.x_doctor.id		
		total = self.amount_total
		

		if type_doc == 'receipt':
			document_id = create_receipt_go(self)

		elif type_doc == 'invoice':
			document_id = create_invoice_go()

		elif type_doc == 'advertisement':
			document_id = create_advertisement_go()


		#print document_id
		
		return (document_id, order_id, patient_id, doctor_id, total)






@api.multi 
def create_receipt_go(self):

		# Search 
		receipt_id = self.env['openhealth.receipt'].search([
													#('order','=',order_id),													
													('order','=',self.id),													
												]).id

		# Create 
		if receipt_id == False:
			receipt = self.env['openhealth.receipt'].create(
													{
														#'order': order_id,
														#'patient': patient_id,	
														#'doctor': doctor_id,	
														#'total': total, 

														'order': self.id,
														'patient': self.patient.id,	
														'doctor': self.x_doctor.id,	
														'total': self.amount_total, 
													})
			receipt_id = receipt.id 




		self.receipt = receipt_id

		return (receipt_id)





@api.multi 
def create_invoice_go(self):

	#print 



@api.multi 
def create_advertisement_go(self):

	#print 




