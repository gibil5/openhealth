# -*- coding: utf-8 -*-

from datetime import datetime,tzinfo,timedelta

from openerp import models, fields, api




#------------------------------------------------ Buttons ---------------------------------------------------


# Create procedure 
@api.multi
def create_procedure_go(self):

	print 'Create Procedure Go'
		
	name = 'name'
	patient = self.patient.id
	doctor = self.physician.id
	treatment = self.id
		
		
	chief_complaint = self.chief_complaint



	GMT = Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")



	ret = 0



	for line in self.sale_ids.order_line:
			
			
		#if (not line.procedure_created) and (self.consultation_ids.order):


		#if not line.procedure_created:				
		#if self.nr_procedures == 0:
		
		if self.nr_procedures < self.sale_ids.nr_lines:

			#line.procedure_created = True
				
			product = line.product_id.id
				
			ret = self.procedure_ids.create({
											'patient':patient,
											'doctor':doctor,
											'chief_complaint':chief_complaint,
											'treatment':treatment,										
											'product':product,

											'evaluation_start_date':evaluation_start_date,
									})
			#print ret 


	#print 
	
	return ret	




# Button - Procedure 

@api.multi
def open_procedure_current(self):  

	patient_id = self.patient.id
	doctor_id = self.physician.id

	#chief_complaint = self.chief_complaint
		
	treatment_id = self.id 

	return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Procedure Current',

			# Window action 
			'res_model': 'openhealth.procedure',

			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			'target': 'current',

			'context':   {
				'search_default_treatment': treatment_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_treatment': treatment_id,
				
				#'default_chief_complaint': chief_complaint,
				
			}
	}











#------------------------------------------------ Time ---------------------------------------------------

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name



