"""
    Open Insurance
    Created:    12 apr 2021 
    Last:       12 apr 2021     
"""
from __future__ import print_function
from openerp import models, fields, api


# Insurance Types
class OeHealthInsuranceType(models.Model):
    _name = 'oeh.medical.insurance.type'
    _description = "Insurance Types"
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The insurance type must be unique')
    ]

    name = fields.Char('Types', size=256, required=True)


# Insurances
class OeHealthInsurance(models.Model):
    _name = 'oeh.medical.insurance'
    _description = "Insurances"
    _inherits = {
        'res.partner': 'partner_id',
    }
    #_defaults={
    #        'is_insurance_company': True,
    #        'state':'Draft',
    #}

    STATE = [
        ('Draft', 'Draft'),
        ('Active', 'Active'),
        ('Expired', 'Expired'),
    ]

    partner_id = fields.Many2one('res.partner', 'Related Partner', required=True, ondelete='cascade', help='Partner-related data of the insurance company')
    ins_no = fields.Char('Insurance #', size=64, reqired=True)
    patient = fields.Many2one('oeh.medical.patient', 'Patient', reqired=True)
    start_date = fields.Datetime('Start Date', reqired=True)
    exp_date = fields.Datetime('Expiration date', reqired=True)
    ins_type = fields.Many2one('oeh.medical.insurance.type', 'Insurance Type', required=True)
    info = fields.Text('Extra Info')
    state = fields.Selection(STATE, 'State', readonly=True, copy=False, help="Status of insurance")

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['ins_no', 'name'], context)
        res = []
        for record in reads:
            name = record['name']
            if record['ins_no']:
                name = "[" + record['ins_no'] + '] ' + name
            res.append((record['id'], name))
        return res

    def make_active(self, cr, uid, ids, context=None):
        if not context:
            return False
        self.write(cr, uid, ids, {'state': 'Active'}, context=context)
        return True
