##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from openerp import pooler, tools, api
from openerp.osv import osv, fields


# Medicines
class OeHealthMedicines(osv.osv):
    _name = 'oeh.medical.medicines'
    _description = "Information about the medicines"
    _inherits={
        'product.product': 'product_id',
    }

    MEDICAMENT_TYPE = [
                ('Medicine', 'Medicine'),
                ('Vaccine', 'Vaccine'),
            ]
    _columns = {
            'product_id': fields.many2one('product.product', 'Related Product', required=True,ondelete='cascade', help='Product-related data of the medicines'),
            'therapeutic_action' : fields.char('Therapeutic effect', size=128, help="Therapeutic action"),
            'composition': fields.text('Composition',help="Components"),
            'indications': fields.text('Indication',help="Indications"),
            'dosage': fields.text('Dosage Instructions',help="Dosage / Indications"),
            'overdosage': fields.text('Overdosage',help="Overdosage"),
            'pregnancy_warning': fields.boolean('Pregnancy Warning', help="Check when the drug can not be taken during pregnancy or lactancy"),
            'pregnancy': fields.text('Pregnancy and Lactancy',help="Warnings for Pregnant Women"),
            'adverse_reaction': fields.text('Adverse Reactions'),
            'storage': fields.text('Storage Conditions'),
            'info': fields.text('Extra Info'),
            'medicament_type': fields.selection(MEDICAMENT_TYPE, 'Medicament Type'),
        }

# Medicaments Configuration

class OeHealthDoseUnit(osv.osv):
    _name = "oeh.medical.dose.unit"
    _description = "Medical Dose Unit"
    _columns = {
        'name': fields.char('Unit',size=32,required=True),
        'desc': fields.char('Description',size=64),
    }

class OeHealthDrugRoute(osv.osv):
    _name = "oeh.medical.drug.route"
    _description = "Medical Drug Route"
    _columns = {
        'name': fields.char('Route',size=64, required=True),
        'code': fields.char('Code',size=32),
    }

class OeHealthDrugForm(osv.osv):
    _name = "oeh.medical.drug.form"
    _description = "Medical Dose Form"
    _columns = {
        'name': fields.char('Form',size=64,required=True),
        'code': fields.char('Code',size=32),
    }

class OeHealthDosage (osv.osv):
    _name = "oeh.medical.dosage"
    _description = "Medicines Dosage"
    _columns = {
        'name': fields.char('Frequency', size=256, help='Common dosage frequency'),
        'code': fields.char('Code', size=64, help='Dosage Code, such as SNOMED, 229798009 = 3 times per day'),
        'abbreviation' : fields.char('Abbreviation', size=64, help='Dosage abbreviation, such as tid in the US or tds in the UK'),
    }