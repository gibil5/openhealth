"""
    Open Pathology

    Created:    12 apr 2021 
    Last:       13 apr 2021     
"""

from __future__ import print_function
from openerp import models, fields, api



# Medicaments Configuration

class OeHealthDoseUnit(models.Model):
    _name = "oeh.medical.dose.unit"
    _description = "Medical Dose Unit"

    name = fields.Char('Unit', size=32, required=True)
    desc = fields.Char('Description', size=64)


class OeHealthDrugRoute(models.Model):
    _name = "oeh.medical.drug.route"
    _description = "Medical Drug Route"

    name = fields.Char('Route', size=64, required=True)
    code = fields.Char('Code', size=32)


class OeHealthDrugForm(models.Model):
    _name = "oeh.medical.drug.form"
    _description = "Medical Dose Form"

    name = fields.Char('Form', size=64, required=True)
    code = fields.Char('Code', size=32)


class OeHealthDosage (models.Model):
    _name = "oeh.medical.dosage"
    _description = "Medicines Dosage"

    name = fields.Char('Frequency', size=256, help='Common dosage frequency')
    code = fields.Char('Code', size=64, help='Dosage Code, such as SNOMED, 229798009 = 3 times per day')
    abbreviation = fields.Char('Abbreviation', size=64, help='Dosage abbreviation, such as tid in the US or tds in the UK')


# Medicines
class OeHealthMedicines(models.Model):
    _name = 'oeh.medical.medicines'
    _description = "Information about the medicines"
    _inherits = {
        'product.product': 'product_id',
    }

    MEDICAMENT_TYPE = [
        ('Medicine', 'Medicine'),
        ('Vaccine', 'Vaccine'),
    ]


    product_id = fields.Many2one('product.product', 'Related Product', required=True, ondelete='cascade', help='Product-related data of the medicines')

    therapeutic_action = fields.Char('Therapeutic effect', size=128, help="Therapeutic action")

    composition = fields.Text('Composition', help="Components")

    indications = fields.Text('Indication', help="Indications")

    dosage = fields.Text('Dosage Instructions', help="Dosage / Indications")

    overdosage = fields.Text('Overdosage', help="Overdosage")

    pregnancy_warning = fields.Boolean('Pregnancy Warning', help="Check when the drug can not be taken during pregnancy or lactancy")

    pregnancy = fields.Text('Pregnancy and Lactancy', help="Warnings for Pregnant Women")

    adverse_reaction = fields.Text('Adverse Reactions')

    storage = fields.Text('Storage Conditions')

    info = fields.Text('Extra Info')

    medicament_type = fields.Selection(MEDICAMENT_TYPE, 'Medicament Type')



# Medicaments Configuration

#class OeHealthDoseUnit(osv.osv):
#    _name = "oeh.medical.dose.unit"
#    _description = "Medical Dose Unit"
#    _columns = {
#        'name': fields.char('Unit', size=32, required=True),
#        'desc': fields.char('Description', size=64),
#    }

#class OeHealthDrugRoute(osv.osv):
#    _name = "oeh.medical.drug.route"
#    _description = "Medical Drug Route"
#    _columns = {
#        'name': fields.char('Route', size=64, required=True),
#        'code': fields.char('Code', size=32),
#    }

#class OeHealthDrugForm(osv.osv):
#    _name = "oeh.medical.drug.form"
#    _description = "Medical Dose Form"
#    _columns = {
#        'name': fields.char('Form', size=64, required=True),
#        'code': fields.char('Code', size=32),
#    }

#class OeHealthDosage(osv.osv):
#    _name = "oeh.medical.dosage"
#    _description = "Medicines Dosage"
#    _columns = {
#        'name': fields.char('Frequency', size=256, help='Common dosage frequency'),
#        'code': fields.char('Code', size=64, help='Dosage Code, such as SNOMED, 229798009 = 3 times per day'),
#        'abbreviation' : fields.char('Abbreviation', size=64, help='Dosage abbreviation, such as tid in the US or tds in the UK'),
#    }
