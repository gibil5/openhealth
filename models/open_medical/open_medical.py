"""
    Open Medical
    Created:    12 apr 2021 
    Last:       12 apr 2021     
"""
from __future__ import print_function
from openerp import models, fields, api



# Physician Management

class OeHealthPhysicianSpeciality(models.Model):
    _name = "oeh.medical.speciality"
    _order = 'name'
    #_sql_constraints = [
    #    ('code_uniq', 'unique (name)', 'The Medical Speciality code must be unique')]
    
    name = fields.Char('Description', size=128, help="ie, Addiction Psychiatry", required=True)
    code = fields.Char('Code', size=128, help="ie, ADP")



class OeHealthPhysicianDegree(models.Model):
    _name = "oeh.medical.degrees"
    #_sql_constraints = [
    #    ('full_name_uniq', 'unique (name)', 'The Medical Degree must be unique')]
    
    name = fields.Char('Degree', size=128, required=True)
    full_name =  fields.Char('Full Name', size=128)
    physician_ids = fields.Many2many('oeh.medical.physician', id1='degree_id', id2='physician_id', string='Physicians')



class OeHealthPhysicianLine(models.Model):
    _name = "oeh.medical.physician.line"
    _description = "Information about doctor availability"

    # Array containing different days name
    PHY_DAY = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ]

    name = fields.Selection(PHY_DAY, 'Available Day(s)', required=True)
    start_time = fields.Float ('Start Time (24h format)')
    end_time = fields.Float ('End Time (24h format)')
    physician_id = fields.Many2one('oeh.medical.physician', 'Physician', select=True, ondelete='cascade')



class OeHealthPhysician(models.Model):
    _name = "oeh.medical.physician"
    _description = "Information about the doctor"
    _inherits = {
        'hr.employee': 'employee_id',
    }
    #_defaults = {
    #    'consultancy_type':lambda *a: 'Residential',
    #    'is_pharmacist':lambda *a: False,
    #}

    #_sql_constraints = [
    #    ('code_oeh_physician_userid_uniq', 'unique (oeh_user_id)', "Selected 'Responsible' user is already assigned to another physician !")
    #]

    CONSULTATION_TYPE = [
        ('Residential', 'Residential'),
        ('Visiting', 'Visiting'),
        ('Other', 'Other'),
    ]

    employee_id = fields.Many2one('hr.employee', 'Related Employee', required=True, ondelete='cascade', help='Employee-related data of the physician')
    institution = fields.Many2one('oeh.medical.health.center', 'Institution', help="Institution where doctor works")
    code = fields.Char('Licence ID', size=128, help="Physician's License ID")
    speciality = fields.Many2one('oeh.medical.speciality', 'Speciality', help="Speciality Code")
    
    consultancy_type = fields.Selection(
        CONSULTATION_TYPE, 
        'Consultancy Type', 
        help="Type of Doctor's Consultancy",
        default='Residential'
    )
    
    consultancy_price = fields.Integer('Consultancy Charge', help="Physician's Consultancy price")

    available_lines = fields.One2many(
        'oeh.medical.physician.line', 
        'physician_id', 
        'Physician Availability', 
        required=True
    )

    #'info =  fields.text ('Extra info')

    degree_id = fields.Many2many(
        'oeh.medical.degrees', 
        id1='physician_id', 
        id2='degree_id', 
        string='Degrees',
        required=True
    )

    is_pharmacist = fields.Boolean('Pharmacist?')
    oeh_user_id = fields.Many2one('res.users', 'Responsible')

    #app_count = fields.function(_app_count, string="Appointments", type="integer")
    app_count = fields.Integer(
        string="Appointments", 
    	compute='_app_count',
    )
    @api.multi
    def _app_count(self):
        for record in self:
            record.app_count = 0


    #prescription_count = fields.function(_prescription_count, string="Prescriptions", type="integer")
    prescription_count = fields.Integer(
        string="Prescriptions", 
    	compute='_prescription_count',
    )
    @api.multi
    def _prescription_count(self):
        for record in self:
            record._prescription_count = 0



    #@api.multi
    #def onchange_state(self, state_id):
    #    if state_id:
    #        state = self.env['res.country.state'].browse(state_id)
    #        return {'value': {'country_id': state.country_id.id}}
    #    return {}

    #def onchange_address_id(self, cr, uid, ids, address, context=None):
    #    if address:
    #        address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
    #        return {'value': {'work_phone': address.phone, 'mobile_phone': address.mobile}}
    #    return {'value': {}}

    #def onchange_company(self, cr, uid, ids, company, context=None):
    #    address_id = False
    #    if company:
    #        company_id = self.pool.get('res.company').browse(cr, uid, company, context=context)
    #        address = self.pool.get('res.partner').address_get(cr, uid, [company_id.partner_id.id], ['default'])
    #        address_id = address and address['default'] or False
    #    return {'value': {'address_id': address_id}}

    #def onchange_user(self, cr, uid, ids, user_id, context=None):
    #    work_email = False
    #    if user_id:
    #        work_email = self.pool.get('res.users').browse(cr, uid, user_id, context=context).email
    #    return {'value': {'work_email': work_email}}



# -------------------------------------------------------------------------------------------------
# Appointment Management

class OeHealthAppointment(models.Model):
    _name = 'oeh.medical.appointment'
    _description = 'Appointment'
    _order = "appointment_date desc"

    #_inherit = ['mail.thread', 'ir.needaction_mixin']      # odoo 9
    #_inherit = ['mail.thread', 'mail.activity.mixin']      # odoo 11
    _inherit = ['mail.thread']


    #_defaults = {
    #       'urgency_level': lambda *a: 'Normal',
    #       'name': lambda obj, cr, uid, context: '/',
    #       'appointment_date': datetime.datetime.now(),
    #       'duration':lambda obj, cr, uid, context: 1,
    #       'patient_status':lambda *a: 'Inpatient',
    #       'doctor': _get_physician,
    #       'state': lambda *a: 'Scheduled',
    #    }

    URGENCY_LEVEL = [
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
        ('Medical Emergency', 'Medical Emergency'),
    ]

    PATIENT_STATUS = [
        ('Ambulatory', 'Ambulatory'),
        ('Outpatient', 'Outpatient'),
        ('Inpatient', 'Inpatient'),
    ]

    APPOINTMENT_STATUS = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Invoiced', 'Invoiced'),
    ]

    name = fields.Char('Appointment #', size=64, readonly=True, required=True)
    patient = fields.Many2one('oeh.medical.patient', 'Patient', help="Patient Name", required=True, readonly=True, states={'Scheduled': [('readonly', False)]})
    doctor = fields.Many2one('oeh.medical.physician', 'Physician', help="Current primary care / family doctor", domain=[('is_pharmacist', '=', False)], required=True, readonly=True, states={'Scheduled': [('readonly', False)]})
    appointment_date = fields.Datetime('Appointment Date', required=True, readonly=True, states={'Scheduled': [('readonly', False)]})
    duration = fields.Integer('Duration (Hours)', readonly=True, states={'Scheduled': [('readonly', False)]})
    institution = fields.Many2one('oeh.medical.health.center', 'Health Center', help="Medical Center", readonly=True, states={'Scheduled': [('readonly', False)]})
    urgency_level = fields.Selection(URGENCY_LEVEL, 'Urgency Level', readonly=True, states={'Scheduled': [('readonly', False)]})
    comments = fields.Text('Comments', readonly=True, states={'Scheduled': [('readonly', False)]})
    patient_status = fields.Selection(PATIENT_STATUS, 'Patient Status', readonly=True, states={'Scheduled': [('readonly', False)]})
    state = fields.Selection(APPOINTMENT_STATUS, 'State', readonly=True)

    #appointment_end = fields.function(_get_appointment_end, method=True, type="datetime", store=True, string='Appointment End Date', readonly=True, states={'Scheduled': [('readonly', False)]})
    appointment_end = fields.Datetime(
        string="Appointment End", 
    	compute='_get_appointment_end',
    )
    @api.multi
    def _get_appointment_end(self):
        for record in self:
            record.app_count = 0


    #def create(self, cr, uid, vals, context=None):
    #    if vals.get('doctor') and vals.get('appointment_date'):
    #        self.check_physician_availability(cr, uid,vals.get('doctor'),vals.get('appointment_date'))
    #    if vals.get('name', '/')=='/':
    #        vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.appointment') or '/'
    #    return super(OeHealthAppointment, self).create(cr, uid, vals, context=context)

    #def check_physician_availability(self,cr,uid,doctor,appointment_date):
    #    return available





# -------------------------------------------------------------------------------------------------
# Prescription Management


class OeHealthPrescriptions(models.Model):
    _name = 'oeh.medical.prescription'
    _description = 'Prescriptions'
    #_defaults = {
    #    'date': datetime.datetime.now(),
    #    'name': lambda obj, cr, uid, context: '/',
    #    'state': lambda *a: 'Draft',
    #    'doctor': _get_physician,
    #}

    STATES = [
        ('Draft', 'Draft'),
        ('Invoiced', 'Invoiced'),
        ('Sent to Pharmacy', 'Sent to Pharmacy'),
    ]

    #def _get_physician(self, cr, uid, context=None):
    #    """Return default physician value"""
    #    therapist_id = []
    #    therapist_obj = self.pool.get('oeh.medical.physician')
    #    domain = [('oeh_user_id', '=', uid)]
    #    user_ids = therapist_obj.search(cr, uid, domain, context=context)
    #    if user_ids:
    #        return user_ids[0] or False
    #    else:
    #        return False

    name = fields.Char('Prescription #',size=64, readonly=True, required=True)
    patient = fields.Many2one('oeh.medical.patient','Patient', help="Patient Name",required=True, readonly=True, states={'Draft': [('readonly', False)]})
    doctor = fields.Many2one('oeh.medical.physician','Physician', domain=[('is_pharmacist','=',False)], help="Current primary care / family doctor", required=True, readonly=True, states={'Draft': [('readonly', False)]})
    pharmacy = fields.Many2one('oeh.medical.health.center.pharmacy', 'Pharmacy', readonly=True,states={'Draft': [('readonly', False)]})
    date = fields.Datetime('Prescription Date', readonly=True,states={'Draft': [('readonly', False)]})
    info = fields.Text('Prescription Notes', readonly=True, states={'Draft': [('readonly', False)]})
    prescription_line = fields.One2many('oeh.medical.prescription.line', 'prescription_id', 'Prescription Lines', readonly=True, states={'Draft': [('readonly', False)]})
    state = fields.Selection(STATES, 'State',readonly=True)



class OeHealthPrescriptionLines(models.Model):
    _name = 'oeh.medical.prescription.line'
    _description = 'Prescription Lines'
    #_defaults = {
    #    'qty': lambda *a: 1.0,
    #}

    FREQUENCY_UNIT = [
        ('Seconds', 'Seconds'),
        ('Minutes', 'Minutes'),
        ('Hours', 'Hours'),
        ('Days', 'Days'),
        ('Weeks', 'Weeks'),
        ('When Required', 'When Required'),
    ]

    DURATION_UNIT = [
        ('Minutes', 'Minutes'),
        ('Hours', 'Hours'),
        ('Days', 'Days'),
        ('Months', 'Months'),
        ('Years', 'Years'),
        ('Indefinite', 'Indefinite'),
    ]


    prescription_id = fields.Many2one('oeh.medical.prescription', 'Prescription Reference', required=True, ondelete='cascade', select=True)
    name = fields.Many2one('oeh.medical.medicines','Medicines',help="Prescribed Medicines",domain=[('medicament_type','=','Medicine')], required=True)
    indication = fields.Many2one('oeh.medical.pathology','Indication',help="Choose a disease for this medicament from the disease list. It can be an existing disease of the patient or a prophylactic.")
    dose = fields.Integer('Dose',help="Amount of medicines (eg, 250 mg ) each time the patient takes it")
    qty = fields.Integer('x',help="Quantity of units (eg, 2 capsules) of the medicament")

    # Orphans
    common_dosage = fields.Many2one(
        'oeh.medical.dosage',
        'Frequency',
        help="Common / standard dosage frequency for this medicines", 
        required=True
    )
    dose_unit = fields.Many2one(
        'oeh.medical.dose.unit',
        'Dose Unit', 
        help="Unit of measure for the medication to be taken",
        required=True
    )
    dose_route = fields.Many2one('oeh.medical.drug.route','Administration Route',help="HL7 or other standard drug administration route code.")
    dose_form = fields.Many2one('oeh.medical.drug.form','Form',help="Drug form, such as tablet or gel")
    
    frequency = fields.Integer('Frequency')
    frequency_unit = fields.Selection(FREQUENCY_UNIT, 'Unit', select=True)
    admin_times = fields.Char('Admin hours', size=128, help='Suggested administration hours. For example, at 08:00, 13:00 and 18:00 can be encoded like 08 13 18')
    duration = fields.Integer('Treatment duration')
    duration_period = fields.Selection(DURATION_UNIT, 'Treatment period',help="Period that the patient must take the medication. in minutes, hours, days, months, years or indefinately", select=True)
    start_treatment = fields.Datetime('Start of treatment')
    end_treatment = fields.Datetime('End of treatment')
    info = fields.Text('Comment')
    patient = fields.Many2one('oeh.medical.patient','Patient', help="Patient Name")





# -------------------------------------------------------------------------------------------------
# Patient Management
#jx

class OeHealthGenetics(models.Model):
    _name = 'oeh.medical.genetics'
    _description = "Information about the genetics risks"

    DOMINANCE = [
        ('Dominant','Dominant'),
        ('Recessive','Recessive'),
    ]
    
    name = fields.Char('Official Symbol', size=16)
    long_name = fields.Char('Official Long Name', size=256)
    gene_id = fields.Char('Gene ID', size=8, help="Default code from NCBI Entrez database.")
    chromosome = fields.Char('Affected Chromosome', size=2, help="Name of the affected chromosome")
    location = fields.Char('Location', size=32, help="Locus of the chromosome")
    dominance = fields.Selection(DOMINANCE, 'Dominance', select=True)
    info = fields.Text('Information', size=128, help="Name of the protein(s) affected")

    
class OeHealthEthnicGroups(models.Model):
    _name = 'oeh.medical.ethnicity'
    _description = "Ethnic Groups"
    #_sql_constraints = [
    #        ('name_uniq', 'unique (name)', 'The ethnic group must be unique !')]

    name = fields.Char('Ethnic Groups', size=256,required=True)



class OeHealthFamily(models.Model):
    _name = 'oeh.medical.patient.family'

    FAMILY_RELATION = [
            ('Father', 'Father'),
            ('Mother', 'Mother'),
            ('Brother', 'Brother'),
            ('Sister', 'Sister'),
            ('Wife', 'Wife'),
            ('Husband', 'Husband'),
            ('Grand Father', 'Grand Father'),
            ('Grand Mother', 'Grand Mother'),
            ('Aunt', 'Aunt'),
            ('Uncle', 'Uncle'),
            ('Nephew', 'Nephew'),
            ('Niece', 'Niece'),
            ('Cousin', 'Cousin'),
            ('Relative', 'Relative'),
            ('Other', 'Other'),
    ]

    name = fields.Char(size=256, string='Name', required=True, help='Family Member Name')
    relation = fields.Selection(FAMILY_RELATION, 'Relation', help="Family Relation", select=True)
    age = fields.Integer(string='Age', help='Family Member Age')
    deceased = fields.Boolean ('Deceased?', help="Mark if the family member has died")
    patient_id = fields.Many2one('oeh.medical.patient', 'Patient', required=True, ondelete='cascade', select=True)



class OeHealthPatient(models.Model):
    _name = 'oeh.medical.patient'
    _inherits = {
        'res.partner': 'partner_id',
    }
    #_defaults={
    #        'ref': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.patient'),
    #        'is_patient': True
    #    }
    #_sql_constraints = [
    #    ('code_oeh_patient_userid_uniq', 'unique (oeh_patient_user_id)', "Selected 'Responsible' user is already assigned to another patient !")
    #]

    MARITAL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
        ('Separated', 'Separated'),
    ]

    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    BLOOD_TYPE = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]

    RH = [
        ('+', '+'),
        ('-', '-'),
    ]


    partner_id = fields.Many2one('res.partner', 'Related Partner', required=True, ondelete='cascade', help='Partner-related data of the patient')

    family = fields.One2many('oeh.medical.patient.family', 'patient_id', 'Family')

    ssn = fields.Char(size=256, string='SSN')

    current_insurance = fields.Many2one('oeh.medical.insurance', "Insurance", domain="[('patient', '=', active_id)('state', '=', 'Active')]", help="Insurance information. You may choose from the different insurances belonging to the patient")

    doctor = fields.Many2one('oeh.medical.physician', 'Family Physician', help="Current primary care physician / family doctor", domain=[('is_pharmacist', '=', False)])

    dob = fields.Datetime('Date of Birth')

    sex = fields.Selection(SEX, 'Sex', select=True)

    marital_status = fields.Selection(MARITAL_STATUS, 'Marital Status')

    blood_type = fields.Selection(BLOOD_TYPE, 'Blood Type')

    rh = fields.Selection(RH, 'Rh')

    identification_code = fields.Char('Patient ID', size=256, help='Patient Identifier provided by the Health Center', readonly=True)

    ethnic_group = fields.Many2one('oeh.medical.ethnicity', 'Ethnic group')

    critical_info = fields.Text('Important disease, allergy or procedures information', help="Write any important information on the patient's disease, surgeries, allergies, ...")

    general_info = fields.Text('General Information', help="General information about the patient")

    genetic_risks = fields.Many2many('oeh.medical.genetics', 'oeh_genetic_risks_rel', 'patient_id', 'genetic_risk_id', 'Genetic Risks')

    deceased = fields.Boolean('Patient Deceased ?', help="Mark if the patient has died")

    dod = fields.Datetime('Date of Death')

    cod = fields.Many2one('oeh.medical.pathology', 'Cause of Death')

    oeh_patient_user_id = fields.Many2one('res.users', 'Responsible')

    prescription_line = fields.One2many('oeh.medical.prescription.line', 'patient', 'Medicines', readonly=True)

    #app_count = fields.function(_app_count, string="Appointments", type="integer")
    #prescription_count = fields.function(_prescription_count, string="Prescriptions", type="integer")
    #admission_count = fields.function(_admission_count, string="Admission / Discharge", type="integer")
    #vaccine_count = fields.function(_vaccine_count, string="Vaccines", type="integer")
    #invoice_count = fields.function(_invoice_count, string="Invoices", type="integer")
    #age = fields.function(_patient_age, method=True, type='char', size=32, string='Patient Age', help="It shows the age of the patient in years(y) months(m) and days(d).\nIf the patient has died, the age shown is the age at time of death, the age corresponding to the date on the death certificate. It will show also \"deceased\" on the field")

    #app_count = fields.function(_app_count, string="Appointments", type="integer")
    app_count = fields.Integer(
        string="Appointments", 
    	compute='_app_count',
    )
    @api.multi
    def _app_count(self):
        for record in self:
            record.app_count = 0

    
    #prescription_count = fields.function(_prescription_count, string="Prescriptions", type="integer")
    prescription_count = fields.Integer(
        string="Prescriptions", 
    	compute='_prescription_count',
    )
    @api.multi
    def _prescription_count(self):
        for record in self:
            record._prescription_count = 0

    
    
    #admission_count = fields.function(_admission_count, string="Admission / Discharge", type="integer")
    admission_count = fields.Integer(
        string="Admission / Discharge", 
        compute='_admission_count',
    )   
    @api.multi
    def _admission_count(self):
        for record in self:
            record._admission_count = 0
    
    
    #vaccine_count = fields.function(_vaccine_count, string="Vaccines", type="integer")
    vaccine_count = fields.Integer(
        string="Vaccines", 
    	compute='_vaccine_count',
        )   
    @api.multi
    def _vaccine_count(self):
        for record in self:
            record.vaccine_count = 0
    
    
    #invoice_count = fields.function(_invoice_count, string="Invoices", type="integer")
    invoice_count = fields.Integer(
        string="Invoices", 
    	compute='_invoice_count',
        )   
    @api.multi
    def _invoice_count(self):
        for record in self:
            record.invoice_count = 0



    #age = fields.function(_patient_age, method=True, type='char', size=32, string='Patient Age', help="It shows the age of the patient in years(y) months(m) and days(d).\nIf the patient has died, the age shown is the age at time of death, the age corresponding to the date on the death certificate. It will show also \"deceased\" on the field")
    age = fields.Char(
        string="Patient Age", 
    	compute='_patient_age',
    )
    @api.multi
    def _patient_age(self):
        for record in self:
            record.ageage = '0'



    #def create(self, cr, uid, vals, context=None):
    #    sequence = unicode (self.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.patient'))
    #    vals['identification_code'] = sequence
    #    return super(OeHealthPatient, self).create(cr, uid, vals, context=context)

    #def print_patient_label(self, cr, uid, ids, context=None):
    #    '''
    #    This function prints the patient label
    #    '''
    #    assert len(ids) == 1, 'This option should only be used for a single id at a time'
    #    return self.pool['report'].get_action(cr, uid, ids, 'oehealth.report_patient_label', context=context)

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}

