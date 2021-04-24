##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from openerp.osv import osv, fields

# Insurance Types

class OeHealthInsuranceType(osv.osv):
    _name = 'oeh.medical.insurance.type'
    _description = "Insurance Types"
    _columns = {
        'name':fields.char('Types', size=256,required=True),
    }
    _sql_constraints = [
            ('name_uniq', 'unique (name)', 'The insurance type must be unique')]

# Insurances

class OeHealthInsurance(osv.osv):
    _name = 'oeh.medical.insurance'
    _description = "Insurances"
    _inherits={
        'res.partner': 'partner_id',
    }

    STATE = [
                ('Draft','Draft'),
                ('Active','Active'),
                ('Expired','Expired'),
            ]

    _columns = {
        'partner_id': fields.many2one('res.partner','Related Partner', required=True,ondelete='cascade', help='Partner-related data of the insurance company'),
        'ins_no': fields.char('Insurance #', size=64,required=True),
        'patient': fields.many2one('oeh.medical.patient','Patient',required=True),
        'start_date': fields.date('Start Date',required=True),
        'exp_date': fields.date('Expiration date',required=True),
        'ins_type': fields.many2one('oeh.medical.insurance.type','Insurance Type', required=True),
        'info': fields.text ('Extra Info'),
        'state': fields.selection(STATE, 'State',readonly=True, copy=False,help="Status of insurance"),
    }
    _defaults={
            'is_insurance_company': True,
            'state':'Draft',
    }

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['ins_no','name'], context)
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
