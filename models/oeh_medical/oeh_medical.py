##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from openerp import pooler, tools, api
from openerp.osv import osv, fields
import datetime
from openerp.tools.translate import _
from datetime import timedelta

import pytz
from openerp import SUPERUSER_ID

# Family Management

class OeHealthFamily(osv.osv):
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

    _columns = {
        'name': fields.char(size=256, string='Name', required=True, help='Family Member Name'),
        'relation': fields.selection(FAMILY_RELATION, 'Relation', help="Family Relation", select=True),
        'age': fields.integer(string='Age', help='Family Member Age'),
        'deceased': fields.boolean ('Deceased?',help="Mark if the family member has died"),
        'patient_id': fields.many2one('oeh.medical.patient', 'Patient', required=True, ondelete='cascade', select=True),
    }

# Patient Management

class OeHealthPatient(osv.osv):
    _name='oeh.medical.patient'
    _inherits={
        'res.partner': 'partner_id',
    }

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
        ('+','+'),
        ('-','-'),
    ]

    def _app_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_apps = self.pool.get('oeh.medical.appointment')
        for pa in self.browse(cr, uid, ids, context=context):
            domain = [('patient', '=', pa.id)]
            app_ids = oe_apps.search(cr, uid, domain, context=context)
            apps = oe_apps.browse(cr, uid, app_ids, context=context)
            app_count = 0
            for ap in apps:
                app_count+=1
            result[pa.id] = app_count
        return result

    def _prescription_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_pres = self.pool.get('oeh.medical.prescription')
        for pa in self.browse(cr, uid, ids, context=context):
            domain = [('patient', '=', pa.id)]
            pres_ids = oe_pres.search(cr, uid, domain, context=context)
            pres = oe_pres.browse(cr, uid, pres_ids, context=context)
            pres_count = 0
            for pr in pres:
                pres_count+=1
            result[pa.id] = pres_count
        return result

    def _admission_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_admission = self.pool.get('oeh.medical.inpatient')
        for adm in self.browse(cr, uid, ids, context=context):
            domain = [('patient', '=', adm.id)]
            admission_ids = oe_admission.search(cr, uid, domain, context=context)
            admissions = oe_admission.browse(cr, uid, admission_ids, context=context)
            admission_count = 0
            for ad in admissions:
                admission_count+=1
            result[adm.id] = admission_count
        return result

    def _vaccine_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_vac = self.pool.get('oeh.medical.vaccines')
        for va in self.browse(cr, uid, ids, context=context):
            domain = [('patient', '=', va.id)]
            vec_ids = oe_vac.search(cr, uid, domain, context=context)
            vecs = oe_vac.browse(cr, uid, vec_ids, context=context)
            vecs_count = 0
            for pr in vecs:
                vecs_count+=1
            result[va.id] = vecs_count
        return result

    def _invoice_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_invoice = self.pool.get('account.invoice')
        for inv in self.browse(cr, uid, ids, context=context):
            domain = [('partner_id', '=', inv.partner_id.id)]
            invoice_ids = oe_invoice.search(cr, uid, domain, context=context)
            invoices = oe_invoice.browse(cr, uid, invoice_ids, context=context)
            invoice_count = 0
            for inv_id in invoices:
                invoice_count+=1
            result[inv.id] = invoice_count
        return result

    def _patient_age(self, cr, uid, ids, name, arg, context={}):
        def compute_age_from_dates (patient_dob,patient_deceased,patient_dod):
            now=datetime.datetime.now()
            if (patient_dob):
                dob=datetime.datetime.strptime(patient_dob,'%Y-%m-%d')
                if patient_deceased :
                    dod=datetime.datetime.strptime(patient_dod,'%Y-%m-%d')
                    delta= dod - dob
                    deceased=" (deceased)"
                    years_months_days = str(delta.days // 365)+" years "+ str(delta.days%365)+" days" + deceased
                else:
                    delta= now - dob
                    years_months_days = str(delta.days // 365)+" years "+ str(delta.days%365)+" days"
            else:
                years_months_days = "No DoB !"

            return years_months_days
        result={}
        for patient_data in self.browse(cr, uid, ids, context=context):
            result[patient_data.id] = compute_age_from_dates (patient_data.dob,patient_data.deceased,patient_data.dod)
        return result

    _columns = {
            'partner_id': fields.many2one('res.partner', 'Related Partner', required=True,ondelete='cascade', help='Partner-related data of the patient'),
            'family': fields.one2many('oeh.medical.patient.family', 'patient_id', 'Family'),
            'ssn': fields.char(size=256, string='SSN'),
            'current_insurance': fields.many2one ('oeh.medical.insurance',"Insurance", domain="[('patient','=',active_id),('state','=','Active')]",help="Insurance information. You may choose from the different insurances belonging to the patient"),
            'doctor': fields.many2one('oeh.medical.physician', 'Family Physician', help="Current primary care physician / family doctor", domain=[('is_pharmacist','=',False)]),
            'dob': fields.date ('Date of Birth'),
            'age': fields.function(_patient_age, method=True, type='char', size=32, string='Patient Age',help="It shows the age of the patient in years(y), months(m) and days(d).\nIf the patient has died, the age shown is the age at time of death, the age corresponding to the date on the death certificate. It will show also \"deceased\" on the field"),
            'sex': fields.selection(SEX, 'Sex', select=True),
            'marital_status': fields.selection(MARITAL_STATUS, 'Marital Status'),
            'blood_type': fields.selection(BLOOD_TYPE, 'Blood Type'),
            'rh': fields.selection(RH, 'Rh'),
            'identification_code': fields.char('Patient ID',size=256, help='Patient Identifier provided by the Health Center',readonly=True),
            'ethnic_group' : fields.many2one ('oeh.medical.ethnicity','Ethnic group'),
            'critical_info' : fields.text ('Important disease, allergy or procedures information',help="Write any important information on the patient's disease, surgeries, allergies, ..."),
            'general_info': fields.text ('General Information',help="General information about the patient"),
            'genetic_risks' : fields.many2many('oeh.medical.genetics','oeh_genetic_risks_rel','patient_id','genetic_risk_id','Genetic Risks'),
            'deceased': fields.boolean ('Patient Deceased ?',help="Mark if the patient has died"),
            'dod': fields.date('Date of Death'),
            'cod': fields.many2one('oeh.medical.pathology', 'Cause of Death'),
            'app_count': fields.function(_app_count, string="Appointments", type="integer"),
            'prescription_count': fields.function(_prescription_count, string="Prescriptions", type="integer"),
            'admission_count': fields.function(_admission_count, string="Admission / Discharge", type="integer"),
            'vaccine_count': fields.function(_vaccine_count, string="Vaccines", type="integer"),
            'invoice_count': fields.function(_invoice_count, string="Invoices", type="integer"),
            'oeh_patient_user_id': fields.many2one('res.users', 'Responsible'),
            'prescription_line': fields.one2many('oeh.medical.prescription.line', 'patient', 'Medicines', readonly=True),
        }

    _defaults={
            'ref': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.patient'),
            'is_patient': True
        }
    _sql_constraints = [
        ('code_oeh_patient_userid_uniq', 'unique (oeh_patient_user_id)', "Selected 'Responsible' user is already assigned to another patient !")
    ]

    def create(self, cr, uid, vals, context=None):
        sequence = unicode (self.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.patient'))
        vals['identification_code'] = sequence
        return super(OeHealthPatient, self).create(cr, uid, vals, context=context)

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}

    def print_patient_label(self, cr, uid, ids, context=None):
        '''
        This function prints the patient label
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        return self.pool['report'].get_action(cr, uid, ids, 'oehealth.report_patient_label', context=context)

# Physician Management

class OeHealthPhysicianSpeciality(osv.osv):
    _name = "oeh.medical.speciality"
    _columns = {
        'name' :fields.char ('Description', size=128, help="ie, Addiction Psychiatry",required=True),
        'code' : fields.char ('Code', size=128, help="ie, ADP"),
    }
    _order = 'name'
    _sql_constraints = [
        ('code_uniq', 'unique (name)', 'The Medical Speciality code must be unique')]


class OeHealthPhysicianDegree(osv.osv):
    _name = "oeh.medical.degrees"
    _columns = {
        'name' :fields.char ('Degree', size=128, required=True),
        'full_name' : fields.char ('Full Name', size=128),
        'physician_ids': fields.many2many('oeh.medical.physician', id1='degree_id', id2='physician_id', string='Physicians'),
    }
    _sql_constraints = [
        ('full_name_uniq', 'unique (name)', 'The Medical Degree must be unique')]

class OeHealthPhysician (osv.osv):
    _name = "oeh.medical.physician"
    _description = "Information about the doctor"
    _inherits={
        'hr.employee': 'employee_id',
    }

    CONSULTATION_TYPE = [
        ('Residential', 'Residential'),
        ('Visiting', 'Visiting'),
        ('Other', 'Other'),
        ]

    def _app_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_apps = self.pool.get('oeh.medical.appointment')
        for pa in self.browse(cr, uid, ids, context=context):
            domain = [('doctor', '=', pa.id)]
            app_ids = oe_apps.search(cr, uid, domain, context=context)
            apps = oe_apps.browse(cr, uid, app_ids, context=context)
            app_count = 0
            for ap in apps:
                app_count+=1
            result[pa.id] = app_count
        return result

    def _prescription_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_pres = self.pool.get('oeh.medical.prescription')
        for pa in self.browse(cr, uid, ids, context=context):
            domain = [('doctor', '=', pa.id)]
            pres_ids = oe_pres.search(cr, uid, domain, context=context)
            pres = oe_pres.browse(cr, uid, pres_ids, context=context)
            pres_count = 0
            for pr in pres:
                pres_count+=1
            result[pa.id] = pres_count
        return result

    _columns = {
        'employee_id': fields.many2one('hr.employee', 'Related Employee', required=True,ondelete='cascade', help='Employee-related data of the physician'),
        'institution': fields.many2one('oeh.medical.health.center','Institution',help="Institution where doctor works"),
        'code': fields.char('Licence ID', size=128, help="Physician's License ID"),
        'speciality': fields.many2one('oeh.medical.speciality','Speciality', help="Speciality Code"),
        'consultancy_type': fields.selection(CONSULTATION_TYPE, 'Consultancy Type', help="Type of Doctor's Consultancy"),
        'consultancy_price': fields.integer('Consultancy Charge', help="Physician's Consultancy price"),
        'available_lines': fields.one2many('oeh.medical.physician.line', 'physician_id', 'Physician Availability'),
        #'info' : fields.text ('Extra info'),
        'degree_id': fields.many2many('oeh.medical.degrees', id1='physician_id', id2='degree_id', string='Degrees'),
        'app_count': fields.function(_app_count, string="Appointments", type="integer"),
        'prescription_count': fields.function(_prescription_count, string="Prescriptions", type="integer"),
        'is_pharmacist': fields.boolean('Pharmacist?'),
        'oeh_user_id': fields.many2one('res.users', 'Responsible'),
    }
    _defaults = {
        'consultancy_type':lambda *a: 'Residential',
        'is_pharmacist':lambda *a: False,
    }
    _sql_constraints = [
        ('code_oeh_physician_userid_uniq', 'unique (oeh_user_id)', "Selected 'Responsible' user is already assigned to another physician !")
    ]

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'work_phone': address.phone, 'mobile_phone': address.mobile}}
        return {'value': {}}

    def onchange_company(self, cr, uid, ids, company, context=None):
        address_id = False
        if company:
            company_id = self.pool.get('res.company').browse(cr, uid, company, context=context)
            address = self.pool.get('res.partner').address_get(cr, uid, [company_id.partner_id.id], ['default'])
            address_id = address and address['default'] or False
        return {'value': {'address_id': address_id}}

    def onchange_user(self, cr, uid, ids, user_id, context=None):
        work_email = False
        if user_id:
            work_email = self.pool.get('res.users').browse(cr, uid, user_id, context=context).email
        return {'value': {'work_email': work_email}}

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if not ids:
            return True
        if isinstance(ids, (int, long)):
            ids = [ids]

        if 'name' in vals:
           vals['name_related'] = vals['name']
        return super(OeHealthPhysician, self).write(cr, uid, ids, vals, context=context)

class OeHealthPhysicianLine (osv.osv):

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

    _name = "oeh.medical.physician.line"
    _description = "Information about doctor availability"
    _columns = {
        'name': fields.selection(PHY_DAY, 'Available Day(s)', required=True),
        'start_time' : fields.float ('Start Time (24h format)'),
        'end_time' : fields.float ('End Time (24h format)'),
        'physician_id': fields.many2one('oeh.medical.physician', 'Physician',select=True,ondelete='cascade'),
    }

# Appointment Management

class OeHealthAppointment(osv.osv):
    _name = 'oeh.medical.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

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

    # Automatically detect logged in physician
    def _get_physician(self, cr, uid, context=None):
        """Return default physician value"""
        therapist_id = []
        therapist_obj = self.pool.get('oeh.medical.physician')
        domain = [('oeh_user_id', '=', uid)]
        user_ids = therapist_obj.search(cr, uid, domain, context=context)
        if user_ids:
            return user_ids[0] or False
        else:
            return False

    # Calculating Appointment End date
    def _get_appointment_end(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for apm in self.browse(cr, uid, ids, context=context):
            end_date = False
            duration = 1
            if apm.duration:
                duration = apm.duration
            if apm.appointment_date:
                end_date = datetime.datetime.strptime(apm.appointment_date, "%Y-%m-%d %H:%M:%S") + timedelta(hours=duration)
            res[apm.id] = end_date
        return res

    _columns = {
        'name': fields.char ('Appointment #',size=64, readonly=True, required=True),
        'patient': fields.many2one ('oeh.medical.patient','Patient', help="Patient Name",required=True, readonly=True,states={'Scheduled': [('readonly', False)]}),
        'doctor': fields.many2one('oeh.medical.physician','Physician', help="Current primary care / family doctor", domain=[('is_pharmacist','=',False)], required=True, readonly=True,states={'Scheduled': [('readonly', False)]}),
        'appointment_date': fields.datetime('Appointment Date',required=True, readonly=True,states={'Scheduled': [('readonly', False)]}),
        'appointment_end': fields.function(_get_appointment_end, method=True, type="datetime", store=True, string='Appointment End Date', readonly=True,states={'Scheduled': [('readonly', False)]}),
        'duration': fields.integer('Duration (Hours)', readonly=True,states={'Scheduled': [('readonly', False)]}),
        'institution': fields.many2one ('oeh.medical.health.center','Health Center',help="Medical Center", readonly=True,states={'Scheduled': [('readonly', False)]}),
        'urgency_level': fields.selection(URGENCY_LEVEL, 'Urgency Level', readonly=True,states={'Scheduled': [('readonly', False)]}),
        'comments': fields.text ('Comments', readonly=True,states={'Scheduled': [('readonly', False)]}),
        'patient_status': fields.selection(PATIENT_STATUS, 'Patient Status', readonly=True,states={'Scheduled': [('readonly', False)]}),
        'state': fields.selection(APPOINTMENT_STATUS, 'State',readonly=True),
        }
    _order = "appointment_date desc"
    _defaults = {
           'urgency_level': lambda *a: 'Normal',
           'name': lambda obj, cr, uid, context: '/',
           'appointment_date': datetime.datetime.now(),
           'duration':lambda obj, cr, uid, context: 1,
           'patient_status':lambda *a: 'Inpatient',
           'doctor': _get_physician,
           'state': lambda *a: 'Scheduled',
        }

    def create(self, cr, uid, vals, context=None):
        if vals.get('doctor') and vals.get('appointment_date'):
            self.check_physician_availability(cr, uid,vals.get('doctor'),vals.get('appointment_date'))
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.appointment') or '/'
        return super(OeHealthAppointment, self).create(cr, uid, vals, context=context)

    def check_physician_availability(self,cr,uid,doctor,appointment_date):
        available = False
        DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        patient_line_obj = self.pool.get('oeh.medical.physician.line')

        #check if doctor is working on selected day of the week
        selected_day = datetime.datetime.strptime(appointment_date, DATETIME_FORMAT).strftime('%A')
        print str(selected_day)

        if selected_day:
            avail_day_ids = patient_line_obj.search(cr, uid, [('name', '=', str(selected_day)),('physician_id', '=', doctor)])
            if not avail_day_ids:
                raise osv.except_osv(_('Not Available'), _('Physician is not available on selected day'))
            else:
                for av_day in patient_line_obj.browse(cr,uid,avail_day_ids):
                    #get selected day's start and end time

                    phy_start_time = self.get_time_string(av_day.start_time).split(':')
                    phy_end_time = self.get_time_string(av_day.end_time).split(':')

                    user_pool = self.pool.get('res.users')
                    user = user_pool.browse(cr, SUPERUSER_ID, uid)
                    tz = pytz.timezone(user.partner_id.tz) or pytz.utc

                    # get localized dates
                    appointment_date = pytz.utc.localize(datetime.datetime.strptime(appointment_date, DATETIME_FORMAT)).astimezone(tz)
                    #print "App Real time: " + str(appointment_date)

                    t1 = datetime.time(int(phy_start_time[0]),int(phy_start_time[1]),0)
                    t3 = datetime.time(int(phy_end_time[0]),int(phy_end_time[1]),0)

                    #get appointment hour and minute
                    #app_time = datetime.datetime.strptime(appointment_date,DATETIME_FORMAT)
                    t2 = datetime.time(appointment_date.hour,appointment_date.minute,0)

                    print str(t2)
                    if not (t2 > t1 and t2 < t3):
                        raise osv.except_osv(_('Not Available'), _('Physician is not available on selected time'))
                    else:
                        available = True
        return available


    def get_time_string(self,duration):
        result =''
        currentHours = int(duration // 1)
        currentMinutes =int(round(duration % 1 * 60))
        if(currentHours <= 9):
            currentHours = "0" + str(currentHours)
        if(currentMinutes <= 9):
            currentMinutes = "0" + str(currentMinutes)
        result = str(currentHours)+":"+str(currentMinutes)
        return result

    def _default_account(self,cr,uid,ids,context=None):
        journal_ids = self.pool.get('account.journal').search(cr,uid,[('type', '=', 'sale')],context=context, limit=1)
        journal = self.pool.get('account.journal').browse(cr, uid, journal_ids, context=context)
        return journal.default_credit_account_id.id

    def action_appointment_invoice_create(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        invoice_obj = self.pool.get("account.invoice")
        invoice_line_obj = self.pool.get("account.invoice.line")
        inv_ids = []

        for acc in self.browse(cr, uid, ids, context=context):
            # Create Invoice
            if acc.patient:
                curr_invoice = {
                    'partner_id': acc.patient.partner_id.id,
                    'account_id': acc.patient.partner_id.property_account_receivable_id.id,
                    'patient': acc.patient.id,
                    'state': 'draft',
                    'type':'out_invoice',
                    'date_invoice':acc.appointment_date,
                    'origin': "Appointment # : " + acc.name,
                }

                inv_ids = invoice_obj.create(cr, uid, curr_invoice, context)
                self.write(cr, uid, [acc.id], {'state': 'Invoiced'})

                if inv_ids:
                    prd_account_id = self._default_account(cr,uid,ids,context)
                    # Create Invoice line
                    curr_invoice_line = {
                        'name':"Consultancy invoice for " + acc.name,
                        'price_unit':acc.doctor.consultancy_price,
                        'quantity':1,
                        'account_id':prd_account_id,
                        'invoice_id':inv_ids,
                    }

                    inv_line_ids = invoice_line_obj.create(cr, uid, curr_invoice_line, context)

        return {
                'domain': "[('id','=', " + str(inv_ids) + ")]",
                'name': 'Appointment Invoice',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'account.invoice',
                'type': 'ir.actions.act_window'
        }

    def set_to_completed(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'Completed'}, context=context)


# Prescription Management

class OeHealthPrescriptions(osv.osv):
    _name = 'oeh.medical.prescription'
    _description = 'Prescriptions'

    STATES = [
        ('Draft', 'Draft'),
        ('Invoiced', 'Invoiced'),
        ('Sent to Pharmacy', 'Sent to Pharmacy'),
    ]

    def _get_physician(self, cr, uid, context=None):
        """Return default physician value"""
        therapist_id = []
        therapist_obj = self.pool.get('oeh.medical.physician')
        domain = [('oeh_user_id', '=', uid)]
        user_ids = therapist_obj.search(cr, uid, domain, context=context)
        if user_ids:
            return user_ids[0] or False
        else:
            return False

    _columns = {
       'name': fields.char('Prescription #',size=64, readonly=True, required=True),
       'patient': fields.many2one('oeh.medical.patient','Patient', help="Patient Name",required=True, readonly=True, states={'Draft': [('readonly', False)]}),
       'doctor': fields.many2one('oeh.medical.physician','Physician', domain=[('is_pharmacist','=',False)], help="Current primary care / family doctor", required=True, readonly=True, states={'Draft': [('readonly', False)]}),
       'pharmacy': fields.many2one('oeh.medical.health.center.pharmacy', 'Pharmacy', readonly=True,states={'Draft': [('readonly', False)]}),
       'date': fields.datetime('Prescription Date', readonly=True,states={'Draft': [('readonly', False)]}),
       'info': fields.text('Prescription Notes', readonly=True, states={'Draft': [('readonly', False)]}),
       'prescription_line': fields.one2many('oeh.medical.prescription.line', 'prescription_id', 'Prescription Lines', readonly=True, states={'Draft': [('readonly', False)]}),
       'state': fields.selection(STATES, 'State',readonly=True),
    }
    _defaults = {
        'date': datetime.datetime.now(),
        'name': lambda obj, cr, uid, context: '/',
        'state': lambda *a: 'Draft',
        'doctor': _get_physician,
    }

    def create(self, cr, uid, vals, context=None):
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.prescription') or '/'
        return super(OeHealthPrescriptions, self).create(cr, uid, vals, context=context)

    def _default_account(self,cr,uid,ids,context=None):
        journal_ids = self.pool.get('account.journal').search(cr,uid,[('type', '=', 'sale')],context=context, limit=1)
        journal = self.pool.get('account.journal').browse(cr, uid, journal_ids, context=context)
        return journal.default_credit_account_id.id

    def action_prescription_invoice_create(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        invoice_obj = self.pool.get("account.invoice")
        invoice_line_obj = self.pool.get("account.invoice.line")
        inv_ids = []

        for pres in self.browse(cr, uid, ids, context=context):
            # Create Invoice
            if pres.patient:
                curr_invoice = {
                    'partner_id': pres.patient.partner_id.id,
                    'account_id': pres.patient.partner_id.property_account_receivable_id.id,
                    'patient': pres.patient.id,
                    'state': 'draft',
                    'type':'out_invoice',
                    'date_invoice':pres.date,
                    'origin': "Prescription# : " + pres.name,
                }

                inv_ids = invoice_obj.create(cr, uid, curr_invoice, context)
                self.write(cr, uid, [pres.id], {'state': 'Invoiced'})

                if inv_ids:
                    prd_account_id = self._default_account(cr,uid,ids,context)
                    if pres.prescription_line:
                        for ps in pres.prescription_line:

                            # Create Invoice line
                            curr_invoice_line = {
                                'name':ps.name.product_id.name,
                                'product_id':ps.name.product_id.id,
                                'price_unit':ps.name.product_id.list_price,
                                'quantity':ps.qty,
                                'account_id':prd_account_id,
                                'invoice_id':inv_ids,
                            }

                            inv_line_ids = invoice_line_obj.create(cr, uid, curr_invoice_line, context)

                            #invoice_obj.button_compute(cr, uid, [inv_ids], context=context, set_total=('type' in ('in_invoice', 'in_refund')))

        return {
                'domain': "[('id','=', " + str(inv_ids) + ")]",
                'name': 'Prescription Invoice',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'account.invoice',
                'type': 'ir.actions.act_window'
        }

    # Preventing deletion of a prescription which is not in draft state
    def unlink(self, cr, uid, ids, context=None):
        stat = self.read(cr, uid, ids, ['state'], context=context)
        unlink_ids = []
        for t in stat:
            if t['state'] in ('Draft'):
                unlink_ids.append(t['id'])
            else:
                raise osv.except_osv(_('Invalid Action!'), _('You can not delete a prescription which is not in "Draft" state !!'))
        osv.osv.unlink(self, cr, uid, unlink_ids, context=context)
        return True

    def action_prescription_send_to_pharmacy(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        pharmacy_obj = self.pool.get("oeh.medical.health.center.pharmacy.line")
        pharmacy_line_obj = self.pool.get("oeh.medical.health.center.pharmacy.prescription.line")
        res = {}
        for pres in self.browse(cr, uid, ids, context=context):
            if not pres.pharmacy:
                raise osv.except_osv(_('Warning'), _('No pharmacy selected !!'))
            else:
                curr_pres = {
                    'name': pres.id,
                    'patient': pres.patient.id,
                    'doctor': pres.doctor.id,
                    'pharmacy_id': pres.pharmacy.id,
                }
                phy_ids = pharmacy_obj.create(cr, uid, curr_pres, context)

                if phy_ids:
                    if pres.prescription_line:
                        for ps in pres.prescription_line:

                            # Create Prescription line
                            curr_pres_line = {
                                'name': ps.name.id,
                                'indication': ps.indication.id,
                                'price_unit': ps.name.product_id.list_price,
                                'qty': ps.qty,
                                'actual_qty': ps.qty,
                                'prescription_id': phy_ids,
                                'state': 'Draft',
                            }

                            phy_line_ids = pharmacy_line_obj.create(cr, uid, curr_pres_line, context)
                            pharmacy_obj.button_compute(cr, uid, [phy_ids], context=context)

                res = self.write(cr, uid, [pres.id], {'state': 'Sent to Pharmacy'})

        return res


class OeHealthPrescriptionLines(osv.osv):
    _name = 'oeh.medical.prescription.line'
    _description = 'Prescription Lines'

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

    _columns = {
        'prescription_id': fields.many2one('oeh.medical.prescription', 'Prescription Reference', required=True, ondelete='cascade', select=True),
        'name': fields.many2one('oeh.medical.medicines','Medicines',help="Prescribed Medicines",domain=[('medicament_type','=','Medicine')], required=True),
        'indication': fields.many2one('oeh.medical.pathology','Indication',help="Choose a disease for this medicament from the disease list. It can be an existing disease of the patient or a prophylactic."),
        'dose': fields.integer('Dose',help="Amount of medicines (eg, 250 mg ) each time the patient takes it"),
        'dose_unit': fields.many2one('oeh.medical.dose.unit','Dose Unit', help="Unit of measure for the medication to be taken"),
        'dose_route': fields.many2one('oeh.medical.drug.route','Administration Route',help="HL7 or other standard drug administration route code."),
        'dose_form' : fields.many2one('oeh.medical.drug.form','Form',help="Drug form, such as tablet or gel"),
        'qty': fields.integer('x',help="Quantity of units (eg, 2 capsules) of the medicament"),
        'common_dosage': fields.many2one('oeh.medical.dosage','Frequency',help="Common / standard dosage frequency for this medicines"),
        'frequency': fields.integer('Frequency'),
        'frequency_unit': fields.selection(FREQUENCY_UNIT, 'Unit', select=True),
        'admin_times': fields.char('Admin hours', size=128, help='Suggested administration hours. For example, at 08:00, 13:00 and 18:00 can be encoded like 08 13 18'),
        'duration': fields.integer('Treatment duration'),
        'duration_period': fields.selection(DURATION_UNIT, 'Treatment period',help="Period that the patient must take the medication. in minutes, hours, days, months, years or indefinately", select=True),
        'start_treatment': fields.datetime('Start of treatment'),
        'end_treatment': fields.datetime('End of treatment'),
        'info': fields.text('Comment'),
        'patient': fields.many2one('oeh.medical.patient','Patient', help="Patient Name"),
    }
    _defaults = {
        'qty': lambda *a: 1.0,
    }

# Vaccines Management

class OeHealthVaccines(osv.osv):
    _name = 'oeh.medical.vaccines'
    _description = 'Vaccines'

    def _get_physician(self, cr, uid, context=None):
        """Return default physician value"""
        therapist_id = []
        therapist_obj = self.pool.get('oeh.medical.physician')
        domain = [('oeh_user_id', '=', uid)]
        user_ids = therapist_obj.search(cr, uid, domain, context=context)
        if user_ids:
            return user_ids[0] or False
        else:
            return False

    _columns = {
       'name': fields.many2one('oeh.medical.medicines','Vaccine', domain=[('medicament_type','=','Vaccine')], required=True),
       'patient': fields.many2one('oeh.medical.patient','Patient', help="Patient Name", required=True),
       'doctor': fields.many2one('oeh.medical.physician','Physician', domain=[('is_pharmacist','=',False)], help="Current primary care / family doctor", required=True),
       'date': fields.datetime('Date', required=True),
       'institution': fields.many2one('oeh.medical.health.center','Institution',help="Health Center where the patient is being or was vaccinated"),
       'dose': fields.integer('Dose #'),
       'info': fields.text('Observation'),
    }
    _defaults = {
        'date': datetime.datetime.now(),
        'dose': lambda *a: 1,
        'doctor': _get_physician,
    }

    def onchange_patient(self, cr, uid, ids, patient, context=None):
        if patient:
            dose = 0
            query = _("select max(dose) from oeh_medical_vaccines where patient=%s") % (str(patient))
            cr.execute(query)
            val = cr.fetchone()
            if val and val[0]:
                dose = int(val[0]) + 1
            else:
                dose = 1
            return {'value': {'dose': dose}}
        return {'value': {}}



