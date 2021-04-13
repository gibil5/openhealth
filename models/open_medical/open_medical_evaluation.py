"""
    Open Evaluation
    Created:    12 apr 2021 
    Last:       12 apr 2021
"""

from openerp import models, api, fields

class OeHealthPatientEvaluation(models.Model):
    _name = 'oeh.medical.evaluation'
    _description = "Patient Evaluation"
    #_defaults = {
    #    'loc_eyes': lambda *a: 4,
    #    'loc_verbal': lambda *a: 5,
    #    'loc_motor': lambda *a: 6,
    #    'evaluation_type': lambda *a: 'Pre-arraganged Appointment',
    #    'name': lambda obj, cr, uid, context: '/',
    #    'doctor': _get_physician,
    #}

    EVALUATION_TYPE = [
        ('Ambulatory', 'Ambulatory'),
        ('Emergency', 'Emergency'),
        ('Inpatient Admission', 'Inpatient Admission'),
        ('Pre-arraganged Appointment', 'Pre-arraganged Appointment'),
        ('Periodic Control', 'Periodic Control'),
        ('Phone Call', 'Phone Call'),
        ('Telemedicine', 'Telemedicine'),
    ]

    MOOD = [
        ('Normal', 'Normal'),
        ('Sad', 'Sad'),
        ('Fear', 'Fear'),
        ('Rage', 'Rage'),
        ('Happy', 'Happy'),
        ('Disgust', 'Disgust'),
        ('Euphoria', 'Euphoria'),
        ('Flat', 'Flat'),
    ]

    name = fields.Char('Evaluation #',size=64, readonly=True, required=True)
    patient = fields.Many2one('oeh.medical.patient','Patient', help="Patient Name", required=True)
    doctor = fields.Many2one('oeh.medical.physician','Physician', help="Current primary care / family doctor", domain=[('is_pharmacist','=',False)], required=True)
    appointment = fields.Many2one('oeh.medical.appointment','Appointment #')
    evaluation_start_date = fields.Datetime('Evalution Date', required=True)
    evaluation_end_date = fields.Datetime('Evalution End Date')
    derived_from = fields.Many2one('oeh.medical.physician','Physician who escalated the case')
    derived_to = fields.Many2one('oeh.medical.physician','Physician to whom escalated')
    evaluation_type = fields.Selection(EVALUATION_TYPE, 'Evaluation Type', required=True, select=True)
    chief_complaint = fields.Char('Chief Complaint', size=128, help='Chief Complaint')
    notes_complaint = fields.Text('Complaint details')
    glycemia = fields.Float('Glycemia', help="Last blood glucose level. It can be approximative.")
    hba1c = fields.Float('Glycated Hemoglobin', help="Last Glycated Hb level. It can be approximative.")
    cholesterol_total = fields.Integer ('Last Cholesterol',help="Last cholesterol reading. It can be approximative")
    hdl = fields.Integer('Last HDL',help="Last HDL Cholesterol reading. It can be approximative")
    ldl = fields.Integer('Last LDL',help="Last LDL Cholesterol reading. It can be approximative")
    tag = fields.Integer('Last TAGs',help="Triacylglycerols (triglicerides) level. It can be approximative")
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    bpm = fields.Integer('Heart Rate',help="Heart rate expressed in beats per minute")
    respiratory_rate = fields.Integer('Respiratory Rate',help="Respiratory rate expressed in breaths per minute")
    osat = fields.Integer('Oxygen Saturation',help="Oxygen Saturation (arterial).")
    malnutrition = fields.Boolean('Malnutrition', help="Check this box if the patient show signs of malnutrition. If not associated to a disease, please encode the correspondent disease on the patient disease history. For example, Moderate protein-energy malnutrition, E44.0 in ICD-10 encoding")
    dehydration = fields.Boolean('Dehydration', help="Check this box if the patient show signs of dehydration. If not associated to a disease, please encode the correspondent disease on the patient disease history. For example, Volume Depletion, E86 in ICD-10 encoding")
    temperature = fields.Float('Temperature (celsius)')
    weight = fields.Float('Weight (kg)')
    height = fields.Float('Height (cm)')
    bmi = fields.Float('Body Mass Index (BMI)')
    head_circumference = fields.Float('Head Circumference',help="Head circumference")
    abdominal_circ = fields.Float('Abdominal Circumference')
    edema = fields.Boolean('Edema', help="Please also encode the correspondent disease on the patient disease history. For example,  R60.1 in ICD-10 encoding")
    petechiae = fields.Boolean('Petechiae')
    hematoma = fields.Boolean('Hematomas')
    cyanosis = fields.Boolean('Cyanosis', help="If not associated to a disease, please encode it on the patient disease history. For example,  R23.0 in ICD-10 encoding")
    acropachy = fields.Boolean('Acropachy', help="Check if the patient shows acropachy / clubbing")
    nystagmus = fields.Boolean('Nystagmus', help="If not associated to a disease, please encode it on the patient disease history. For example,  H55 in ICD-10 encoding")
    miosis = fields.Boolean('Miosis', help="If not associated to a disease, please encode it on the patient disease history. For example,  H57.0 in ICD-10 encoding" )
    mydriasis = fields.Boolean('Mydriasis', help="If not associated to a disease, please encode it on the patient disease history. For example,  H57.0 in ICD-10 encoding")
    cough = fields.Boolean('Cough', help="If not associated to a disease, please encode it on the patient disease history.")
    palpebral_ptosis = fields.Boolean ('Palpebral Ptosis', help="If not associated to a disease, please encode it on the patient disease history")
    arritmia = fields.Boolean('Arritmias', help="If not associated to a disease, please encode it on the patient disease history")
    heart_murmurs = fields.Boolean('Heart Murmurs')
    heart_extra_sounds = fields.Boolean('Heart Extra Sounds', help="If not associated to a disease, please encode it on the patient disease history")
    jugular_engorgement = fields.Boolean('Tremor', help="If not associated to a disease, please encode it on the patient disease history")
    ascites = fields.Boolean('Ascites', help="If not associated to a disease, please encode it on the patient disease history")
    lung_adventitious_sounds = fields.Boolean('Lung Adventitious sounds', help="Crackles, wheezes, ronchus..")
    bronchophony = fields.Boolean('Bronchophony')
    increased_fremitus = fields.Boolean('Increased Fremitus')
    decreased_fremitus = fields.Boolean('Decreased Fremitus')
    jaundice = fields.Boolean('Jaundice', help="If not associated to a disease, please encode it on the patient disease history")
    lynphadenitis = fields.Boolean('Linphadenitis', help="If not associated to a disease, please encode it on the patient disease history")
    breast_lump = fields.Boolean('Breast Lumps')
    breast_asymmetry = fields.Boolean('Breast Asymmetry')
    nipple_inversion = fields.Boolean('Nipple Inversion')
    nipple_discharge = fields.Boolean('Nipple Discharge')
    peau_dorange = fields.Boolean('Peau d orange',help="Check if the patient has prominent pores in the skin of the breast" )
    gynecomastia = fields.Boolean('Gynecomastia')
    masses = fields.Boolean('Masses', help="Check when there are findings of masses / tumors / lumps")
    hypotonia = fields.Boolean('Hypotonia', help="Please also encode the correspondent disease on the patient disease history.")
    hypertonia = fields.Boolean('Hypertonia', help="Please also encode the correspondent disease on the patient disease history.")
    pressure_ulcers = fields.Boolean('Pressure Ulcers', help="Check when Decubitus / Pressure ulcers are present")
    goiter = fields.Boolean('Goiter')
    alopecia = fields.Boolean('Alopecia', help="Check when alopecia - including androgenic - is present")
    xerosis = fields.Boolean('Xerosis')
    erithema = fields.Boolean('Erithema', help="Please also encode the correspondent disease on the patient disease history.")
    loc = fields.Integer('Level of Consciousness', help="Level of Consciousness - on Glasgow Coma Scale :  1=coma - 15=normal")
    loc_eyes = fields.Integer('Level of Consciousness - Eyes', help="Eyes Response - Glasgow Coma Scale - 1 to 4")
    loc_verbal = fields.Integer('Level of Consciousness - Verbal', help="Verbal Response - Glasgow Coma Scale - 1 to 5")
    loc_motor = fields.Integer('Level of Consciousness - Motor', help="Motor Response - Glasgow Coma Scale - 1 to 6")
    violent = fields.Boolean ('Violent Behaviour', help="Check this box if the patient is agressive or violent at the moment")
    mood = fields.Selection(MOOD, 'Mood', select=True)
    indication = fields.Many2one('oeh.medical.pathology','Indication',help="Choose a disease for this medicament from the disease list. It can be an existing disease of the patient or a prophylactic.")
    orientation = fields.Boolean('Orientation', help="Check this box if the patient is disoriented in time and/or space")
    memory = fields.Boolean('Memory', help="Check this box if the patient has problems in short or long term memory")
    knowledge_current_events = fields.Boolean('Knowledge of Current Events', help="Check this box if the patient can not respond to public notorious events")
    judgment = fields.Boolean('Jugdment', help="Check this box if the patient can not interpret basic scenario solutions")
    abstraction = fields.Boolean('Abstraction', help="Check this box if the patient presents abnormalities in abstract reasoning")
    vocabulary = fields.Boolean('Vocabulary', help="Check this box if the patient lacks basic intelectual capacity, when she/he can not describe elementary objects")
    calculation_ability = fields.Boolean('Calculation Ability',help="Check this box if the patient can not do simple arithmetic problems")
    object_recognition = fields.Boolean('Object Recognition', help="Check this box if the patient suffers from any sort of gnosia disorders, such as agnosia, prosopagnosia ...")
    praxis = fields.Boolean('Praxis', help="Check this box if the patient is unable to make voluntary movements")
    info_diagnosis = fields.Text('Presumptive Diagnosis')
    directions = fields.Text('Plan')

    symptom_pain = fields.Boolean('Pain')
    symptom_pain_intensity = fields.Integer('Pain intensity', help="Pain intensity from 0 (no pain) to 10 (worst possible pain)")
    symptom_arthralgia = fields.Boolean('Arthralgia')
    symptom_myalgia = fields.Boolean('Myalgia')
    symptom_abdominal_pain = fields.Boolean('Abdominal Pain')
    symptom_cervical_pain = fields.Boolean('Cervical Pain')
    symptom_thoracic_pain = fields.Boolean('Thoracic Pain')
    symptom_lumbar_pain = fields.Boolean('Lumbar Pain')
    symptom_pelvic_pain = fields.Boolean('Pelvic Pain')
    symptom_headache = fields.Boolean('Headache')
    symptom_odynophagia = fields.Boolean('Odynophagia')
    symptom_sore_throat = fields.Boolean('sore throat')
    symptom_otalgia = fields.Boolean('Otalgia')
    symptom_tinnitus = fields.Boolean('Tinnitus')
    symptom_ear_discharge = fields.Boolean('Ear Discharge')
    symptom_hoarseness = fields.Boolean('Hoarseness')
    symptom_chest_pain = fields.Boolean('Chest Pain')
    symptom_chest_pain_excercise = fields.Boolean('Chest Pain on excercise only')
    symptom_orthostatic_hypotension = fields.Boolean('Orthostatic hypotension', help="If not associated to a disease,please encode it on the patient disease history. For example,  I95.1 in ICD-10 encoding")
    symptom_astenia = fields.Boolean('Astenia')
    symptom_anorexia = fields.Boolean('Anorexia')
    symptom_weight_change = fields.Boolean('sudden weight change')
    symptom_abdominal_distension = fields.Boolean('Abdominal Distension')
    symptom_hemoptysis = fields.Boolean('Hemoptysis')
    symptom_hematemesis = fields.Boolean('Hematemesis')
    symptom_epistaxis = fields.Boolean('Epistaxis')
    symptom_gingival_bleeding = fields.Boolean('Gingival Bleeding')
    symptom_rinorrhea = fields.Boolean('Rinorrhea')
    symptom_nausea = fields.Boolean('Nausea')
    symptom_vomiting = fields.Boolean('Vomiting')
    symptom_dysphagia = fields.Boolean('Dysphagia')
    symptom_polydipsia = fields.Boolean('Polydipsia')
    symptom_polyphagia = fields.Boolean('Polyphagia')
    symptom_polyuria = fields.Boolean('Polyuria')
    symptom_nocturia = fields.Boolean('Nocturia')
    symptom_vesical_tenesmus = fields.Boolean('Vesical Tenesmus')
    symptom_pollakiuria = fields.Boolean('Pollakiuiria')
    symptom_dysuria = fields.Boolean('Dysuria')
    symptom_stress = fields.Boolean('stressed-out')
    symptom_mood_swings = fields.Boolean('Mood Swings')
    symptom_pruritus = fields.Boolean('Pruritus')
    symptom_insomnia = fields.Boolean('Insomnia')
    symptom_disturb_sleep = fields.Boolean('Disturbed Sleep')
    symptom_dyspnea = fields.Boolean('Dyspnea')
    symptom_orthopnea = fields.Boolean('Orthopnea')
    symptom_amnesia = fields.Boolean('Amnesia')
    symptom_paresthesia = fields.Boolean('Paresthesia')
    symptom_paralysis = fields.Boolean('Paralysis')
    symptom_syncope = fields.Boolean('syncope')
    symptom_dizziness = fields.Boolean('Dizziness')
    symptom_vertigo = fields.Boolean('Vertigo')
    symptom_eye_glasses = fields.Boolean('Eye glasses',help="Eye glasses or contact lenses")
    symptom_blurry_vision = fields.Boolean('Blurry vision')
    symptom_diplopia = fields.Boolean('Diplopia')
    symptom_photophobia = fields.Boolean('Photophobia')
    symptom_dysmenorrhea = fields.Boolean('Dysmenorrhea')
    symptom_amenorrhea = fields.Boolean('Amenorrhea')
    symptom_metrorrhagia = fields.Boolean('Metrorrhagia')
    symptom_menorrhagia = fields.Boolean('Menorrhagia')
    symptom_vaginal_discharge = fields.Boolean('Vaginal Discharge')
    symptom_urethral_discharge = fields.Boolean('Urethral Discharge')
    symptom_diarrhea = fields.Boolean('Diarrhea')
    symptom_constipation = fields.Boolean('Constipation')
    symptom_rectal_tenesmus = fields.Boolean('Rectal Tenesmus')
    symptom_melena = fields.Boolean('Melena')
    symptom_proctorrhagia = fields.Boolean('Proctorrhagia')
    symptom_xerostomia = fields.Boolean('Xerostomia')
    symptom_sexual_dysfunction = fields.Boolean('sexual Dysfunction')
    notes = fields.Text('Notes')


    # Automatically detect logged in physician
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

    #def create(self, cr, uid, vals, context=None):
    #    if vals.get('name','/')=='/':
    #        vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.evaluation') or '/'
    #    return super(OeHealthPatientEvaluation, self).create(cr, uid, vals, context=context)

    #def onchange_height_weight(self, cr, uid, ids, height, weight):
    #    if height:
    #        v = {'bmi': weight / ((height/100)**2)}
    #    else:
    #        v = {'bmi': 0}
    #    return {'value': v}

    #def onchange_loc(self, cr, uid, ids, loc_motor, loc_eyes, loc_verbal):
    #    v = {'loc': loc_motor + loc_eyes + loc_verbal}
    #    return {'value': v}


# Inheriting Patient module to add "Evaluation" screen reference
class OeHealthPatient(models.Model):
    _inherit='oeh.medical.patient'

    evaluation_ids = fields.One2many('oeh.medical.evaluation', 'patient', 'Evaluation')


# Inheriting Appointment module to add "Evaluation" screen reference
class OeHealthAppointment(models.Model):
    _inherit='oeh.medical.appointment'

    evaluation_ids = fields.One2many('oeh.medical.evaluation', 'appointment', 'Evaluation', readonly=True, states={'Scheduled': [('readonly', False)]})


