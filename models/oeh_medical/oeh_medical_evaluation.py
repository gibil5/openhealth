##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from openerp.osv import osv, fields

class OeHealthPatientEvaluation(osv.osv):
    _name = 'oeh.medical.evaluation'
    _description = "Patient Evaluation"

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

    _columns = {
        'name': fields.char('Evaluation #',size=64, readonly=True, required=True),
        'patient': fields.many2one('oeh.medical.patient','Patient', help="Patient Name", required=True),
        'doctor': fields.many2one('oeh.medical.physician','Physician', help="Current primary care / family doctor", domain=[('is_pharmacist','=',False)], required=True),
        'appointment': fields.many2one('oeh.medical.appointment','Appointment #'),
        'evaluation_start_date': fields.datetime('Evalution Date', required=True),
        'evaluation_end_date': fields.datetime('Evalution End Date'),
        'derived_from': fields.many2one('oeh.medical.physician','Physician who escalated the case'),
        'derived_to': fields.many2one('oeh.medical.physician','Physician to whom escalated'),
        'evaluation_type': fields.selection(EVALUATION_TYPE, 'Evaluation Type', required=True, select=True),
        'chief_complaint': fields.char('Chief Complaint', size=128, help='Chief Complaint'),
        'notes_complaint': fields.text('Complaint details'),
        'glycemia': fields.float('Glycemia', help="Last blood glucose level. It can be approximative."),
        'hba1c': fields.float('Glycated Hemoglobin', help="Last Glycated Hb level. It can be approximative."),
        'cholesterol_total': fields.integer ('Last Cholesterol',help="Last cholesterol reading. It can be approximative"),
        'hdl': fields.integer('Last HDL',help="Last HDL Cholesterol reading. It can be approximative"),
        'ldl': fields.integer('Last LDL',help="Last LDL Cholesterol reading. It can be approximative"),
        'tag': fields.integer('Last TAGs',help="Triacylglycerols (triglicerides) level. It can be approximative"),
        'systolic': fields.integer('Systolic Pressure'),
        'diastolic': fields.integer('Diastolic Pressure'),
        'bpm': fields.integer('Heart Rate',help="Heart rate expressed in beats per minute"),
        'respiratory_rate': fields.integer('Respiratory Rate',help="Respiratory rate expressed in breaths per minute"),
        'osat': fields.integer('Oxygen Saturation',help="Oxygen Saturation (arterial)."),
        'malnutrition': fields.boolean('Malnutrition', help="Check this box if the patient show signs of malnutrition. If not associated to a disease, please encode the correspondent disease on the patient disease history. For example, Moderate protein-energy malnutrition, E44.0 in ICD-10 encoding"),
        'dehydration': fields.boolean('Dehydration', help="Check this box if the patient show signs of dehydration. If not associated to a disease, please encode the correspondent disease on the patient disease history. For example, Volume Depletion, E86 in ICD-10 encoding"),
        'temperature': fields.float('Temperature (celsius)'),
        'weight': fields.float('Weight (kg)'),
        'height': fields.float('Height (cm)'),
        'bmi': fields.float('Body Mass Index (BMI)'),
        'head_circumference': fields.float('Head Circumference',help="Head circumference"),
        'abdominal_circ': fields.float('Abdominal Circumference'),
        'edema': fields.boolean('Edema', help="Please also encode the correspondent disease on the patient disease history. For example,  R60.1 in ICD-10 encoding"),
        'petechiae': fields.boolean('Petechiae'),
        'hematoma': fields.boolean('Hematomas'),
        'cyanosis': fields.boolean('Cyanosis', help="If not associated to a disease, please encode it on the patient disease history. For example,  R23.0 in ICD-10 encoding"),
        'acropachy': fields.boolean('Acropachy', help="Check if the patient shows acropachy / clubbing"),
        'nystagmus': fields.boolean('Nystagmus', help="If not associated to a disease, please encode it on the patient disease history. For example,  H55 in ICD-10 encoding"),
        'miosis': fields.boolean('Miosis', help="If not associated to a disease, please encode it on the patient disease history. For example,  H57.0 in ICD-10 encoding" ),
        'mydriasis': fields.boolean('Mydriasis', help="If not associated to a disease, please encode it on the patient disease history. For example,  H57.0 in ICD-10 encoding"),
        'cough': fields.boolean('Cough', help="If not associated to a disease, please encode it on the patient disease history."),
        'palpebral_ptosis': fields.boolean ('Palpebral Ptosis', help="If not associated to a disease, please encode it on the patient disease history"),
        'arritmia': fields.boolean('Arritmias', help="If not associated to a disease, please encode it on the patient disease history"),
        'heart_murmurs': fields.boolean('Heart Murmurs'),
        'heart_extra_sounds': fields.boolean('Heart Extra Sounds', help="If not associated to a disease, please encode it on the patient disease history"),
        'jugular_engorgement': fields.boolean('Tremor', help="If not associated to a disease, please encode it on the patient disease history"),
        'ascites': fields.boolean('Ascites', help="If not associated to a disease, please encode it on the patient disease history"),
        'lung_adventitious_sounds': fields.boolean('Lung Adventitious sounds', help="Crackles, wheezes, ronchus.."),
        'bronchophony': fields.boolean('Bronchophony'),
        'increased_fremitus': fields.boolean('Increased Fremitus'),
        'decreased_fremitus': fields.boolean('Decreased Fremitus'),
        'jaundice': fields.boolean('Jaundice', help="If not associated to a disease, please encode it on the patient disease history"),
        'lynphadenitis': fields.boolean('Linphadenitis', help="If not associated to a disease, please encode it on the patient disease history"),
        'breast_lump': fields.boolean('Breast Lumps'),
        'breast_asymmetry': fields.boolean('Breast Asymmetry'),
        'nipple_inversion': fields.boolean('Nipple Inversion'),
        'nipple_discharge': fields.boolean('Nipple Discharge'),
        'peau_dorange': fields.boolean('Peau d orange',help="Check if the patient has prominent pores in the skin of the breast" ),
        'gynecomastia': fields.boolean('Gynecomastia'),
        'masses': fields.boolean('Masses', help="Check when there are findings of masses / tumors / lumps"),
        'hypotonia': fields.boolean('Hypotonia', help="Please also encode the correspondent disease on the patient disease history."),
        'hypertonia': fields.boolean('Hypertonia', help="Please also encode the correspondent disease on the patient disease history."),
        'pressure_ulcers': fields.boolean('Pressure Ulcers', help="Check when Decubitus / Pressure ulcers are present"),
        'goiter': fields.boolean('Goiter'),
        'alopecia': fields.boolean('Alopecia', help="Check when alopecia - including androgenic - is present"),
        'xerosis': fields.boolean('Xerosis'),
        'erithema': fields.boolean('Erithema', help="Please also encode the correspondent disease on the patient disease history."),
        'loc': fields.integer('Level of Consciousness', help="Level of Consciousness - on Glasgow Coma Scale :  1=coma - 15=normal"),
        'loc_eyes': fields.integer('Level of Consciousness - Eyes', help="Eyes Response - Glasgow Coma Scale - 1 to 4"),
        'loc_verbal': fields.integer('Level of Consciousness - Verbal', help="Verbal Response - Glasgow Coma Scale - 1 to 5"),
        'loc_motor': fields.integer('Level of Consciousness - Motor', help="Motor Response - Glasgow Coma Scale - 1 to 6"),
        'violent': fields.boolean ('Violent Behaviour', help="Check this box if the patient is agressive or violent at the moment"),
        'mood': fields.selection(MOOD, 'Mood', select=True),
        'indication': fields.many2one('oeh.medical.pathology','Indication',help="Choose a disease for this medicament from the disease list. It can be an existing disease of the patient or a prophylactic."),
        'orientation': fields.boolean('Orientation', help="Check this box if the patient is disoriented in time and/or space"),
        'memory': fields.boolean('Memory', help="Check this box if the patient has problems in short or long term memory"),
        'knowledge_current_events': fields.boolean('Knowledge of Current Events', help="Check this box if the patient can not respond to public notorious events"),
        'judgment': fields.boolean('Jugdment', help="Check this box if the patient can not interpret basic scenario solutions"),
        'abstraction': fields.boolean('Abstraction', help="Check this box if the patient presents abnormalities in abstract reasoning"),
        'vocabulary': fields.boolean('Vocabulary', help="Check this box if the patient lacks basic intelectual capacity, when she/he can not describe elementary objects"),
        'calculation_ability': fields.boolean('Calculation Ability',help="Check this box if the patient can not do simple arithmetic problems"),
        'object_recognition': fields.boolean('Object Recognition', help="Check this box if the patient suffers from any sort of gnosia disorders, such as agnosia, prosopagnosia ..."),
        'praxis': fields.boolean('Praxis', help="Check this box if the patient is unable to make voluntary movements"),
        'info_diagnosis': fields.text('Presumptive Diagnosis'),
        'directions': fields.text('Plan'),
        'symptom_pain': fields.boolean('Pain'),
        'symptom_pain_intensity': fields.integer('Pain intensity', help="Pain intensity from 0 (no pain) to 10 (worst possible pain)"),
        'symptom_arthralgia': fields.boolean('Arthralgia'),
        'symptom_myalgia': fields.boolean('Myalgia'),
        'symptom_abdominal_pain': fields.boolean('Abdominal Pain'),
        'symptom_cervical_pain': fields.boolean('Cervical Pain'),
        'symptom_thoracic_pain': fields.boolean('Thoracic Pain'),
        'symptom_lumbar_pain': fields.boolean('Lumbar Pain'),
        'symptom_pelvic_pain': fields.boolean('Pelvic Pain'),
        'symptom_headache': fields.boolean('Headache'),
        'symptom_odynophagia': fields.boolean('Odynophagia'),
        'symptom_sore_throat': fields.boolean('Sore throat'),
        'symptom_otalgia': fields.boolean('Otalgia'),
        'symptom_tinnitus': fields.boolean('Tinnitus'),
        'symptom_ear_discharge': fields.boolean('Ear Discharge'),
        'symptom_hoarseness': fields.boolean('Hoarseness'),
        'symptom_chest_pain': fields.boolean('Chest Pain'),
        'symptom_chest_pain_excercise': fields.boolean('Chest Pain on excercise only'),
        'symptom_orthostatic_hypotension': fields.boolean('Orthostatic hypotension', help="If not associated to a disease,please encode it on the patient disease history. For example,  I95.1 in ICD-10 encoding"),
        'symptom_astenia': fields.boolean('Astenia'),
        'symptom_anorexia': fields.boolean('Anorexia'),
        'symptom_weight_change': fields.boolean('Sudden weight change'),
        'symptom_abdominal_distension': fields.boolean('Abdominal Distension'),
        'symptom_hemoptysis': fields.boolean('Hemoptysis'),
        'symptom_hematemesis': fields.boolean('Hematemesis'),
        'symptom_epistaxis': fields.boolean('Epistaxis'),
        'symptom_gingival_bleeding': fields.boolean('Gingival Bleeding'),
        'symptom_rinorrhea': fields.boolean('Rinorrhea'),
        'symptom_nausea': fields.boolean('Nausea'),
        'symptom_vomiting': fields.boolean('Vomiting'),
        'symptom_dysphagia': fields.boolean('Dysphagia'),
        'symptom_polydipsia': fields.boolean('Polydipsia'),
        'symptom_polyphagia': fields.boolean('Polyphagia'),
        'symptom_polyuria': fields.boolean('Polyuria'),
        'symptom_nocturia': fields.boolean('Nocturia'),
        'symptom_vesical_tenesmus': fields.boolean('Vesical Tenesmus'),
        'symptom_pollakiuria': fields.boolean('Pollakiuiria'),
        'symptom_dysuria': fields.boolean('Dysuria'),
        'symptom_stress': fields.boolean('Stressed-out'),
        'symptom_mood_swings': fields.boolean('Mood Swings'),
        'symptom_pruritus': fields.boolean('Pruritus'),
        'symptom_insomnia': fields.boolean('Insomnia'),
        'symptom_disturb_sleep': fields.boolean('Disturbed Sleep'),
        'symptom_dyspnea': fields.boolean('Dyspnea'),
        'symptom_orthopnea': fields.boolean('Orthopnea'),
        'symptom_amnesia': fields.boolean('Amnesia'),
        'symptom_paresthesia': fields.boolean('Paresthesia'),
        'symptom_paralysis': fields.boolean('Paralysis'),
        'symptom_syncope': fields.boolean('Syncope'),
        'symptom_dizziness': fields.boolean('Dizziness'),
        'symptom_vertigo': fields.boolean('Vertigo'),
        'symptom_eye_glasses': fields.boolean('Eye glasses',help="Eye glasses or contact lenses"),
        'symptom_blurry_vision': fields.boolean('Blurry vision'),
        'symptom_diplopia': fields.boolean('Diplopia'),
        'symptom_photophobia': fields.boolean('Photophobia'),
        'symptom_dysmenorrhea': fields.boolean('Dysmenorrhea'),
        'symptom_amenorrhea': fields.boolean('Amenorrhea'),
        'symptom_metrorrhagia': fields.boolean('Metrorrhagia'),
        'symptom_menorrhagia': fields.boolean('Menorrhagia'),
        'symptom_vaginal_discharge': fields.boolean('Vaginal Discharge'),
        'symptom_urethral_discharge': fields.boolean('Urethral Discharge'),
        'symptom_diarrhea': fields.boolean('Diarrhea'),
        'symptom_constipation': fields.boolean('Constipation'),
        'symptom_rectal_tenesmus': fields.boolean('Rectal Tenesmus'),
        'symptom_melena': fields.boolean('Melena'),
        'symptom_proctorrhagia': fields.boolean('Proctorrhagia'),
        'symptom_xerostomia': fields.boolean('Xerostomia'),
        'symptom_sexual_dysfunction': fields.boolean('Sexual Dysfunction'),
        'notes': fields.text('Notes'),
    }
    _defaults = {
        'loc_eyes': lambda *a: 4,
        'loc_verbal': lambda *a: 5,
        'loc_motor': lambda *a: 6,
        'evaluation_type': lambda *a: 'Pre-arraganged Appointment',
        'name': lambda obj, cr, uid, context: '/',
        'doctor': _get_physician,
    }

    def create(self, cr, uid, vals, context=None):
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'oeh.medical.evaluation') or '/'
        return super(OeHealthPatientEvaluation, self).create(cr, uid, vals, context=context)

    def onchange_height_weight(self, cr, uid, ids, height, weight):
        if height:
            v = {'bmi': weight / ((height/100)**2)}
        else:
            v = {'bmi': 0}
        return {'value': v}

    def onchange_loc(self, cr, uid, ids, loc_motor, loc_eyes, loc_verbal):
        v = {'loc': loc_motor + loc_eyes + loc_verbal}
        return {'value': v}

# Inheriting Patient module to add "Evaluation" screen reference
class OeHealthPatient(osv.osv):
    _inherit='oeh.medical.patient'
    _columns = {
        'evaluation_ids': fields.one2many('oeh.medical.evaluation','patient','Evaluation'),
    }

# Inheriting Appointment module to add "Evaluation" screen reference
class OeHealthAppointment(osv.osv):
    _inherit='oeh.medical.appointment'
    _columns = {
        'evaluation_ids': fields.one2many('oeh.medical.evaluation','appointment','Evaluation', readonly=True,states={'Scheduled': [('readonly', False)]}),
    }