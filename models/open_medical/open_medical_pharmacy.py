"""
    Open Pharmacy
    Created:    12 apr 2021 
    Last:       12 apr 2021     
"""

from __future__ import print_function
import datetime
from openerp import models, fields, api

# Pharmacy Management


class OeHealthPharmacy(models.Model):
    _name = 'oeh.medical.health.center.pharmacy'
    _description = "Information about the pharmacy"
    _inherits={
        'res.partner': 'partner_id',
    }
    #_defaults={
    #    'is_pharmacy': lambda *a: True,
    #    'is_company': lambda *a: True
    #}

    partner_id = fields.Many2one('res.partner', 'Related Partner', required=True,ondelete='cascade', help='Partner-related data of the hospitals')

    pharmacist_name = fields.Many2one('oeh.medical.physician','Pharmacist Name', domain=[('is_pharmacist','=',True)], required=True)

    institution = fields.Many2one ('oeh.medical.health.center','Health Center')

    pharmacy_lines = fields.One2many('oeh.medical.health.center.pharmacy.line', 'pharmacy_id', 'Pharmacy Lines')

    info = fields.Text('Extra Information')

    #@api.multi
    #def onchange_state(self, state_id):
    #    if state_id:
    #        state = self.env['res.country.state'].browse(state_id)
    #        return {'value': {'country_id': state.country_id.id}}
    #    return {}


class OeHealthPharmacyLines(models.Model):
    _name = 'oeh.medical.health.center.pharmacy.line'
    _description = 'Pharmacy Lines'
    #_defaults={
    #    'state': lambda *a: 'Draft',
    #}

    STATES = [
        ('Draft', 'Draft'),
        ('Invoiced', 'Invoiced'),
    ]

    name = fields.Many2one('oeh.medical.prescription', 'Prescription #', required=True, ondelete='cascade', readonly=True, states={'Draft': [('readonly', False)]})
    patient = fields.Many2one('oeh.medical.patient','Patient', help="Patient Name", required=True, readonly=True, states={'Draft': [('readonly', False)]})
    doctor = fields.Many2one('oeh.medical.physician','Physician', help="Current primary care / family doctor", domain=[('is_pharmacist','=',False)], readonly=True, states={'Draft': [('readonly', False)]})
    prescription_lines = fields.One2many('oeh.medical.health.center.pharmacy.prescription.line', 'prescription_id', 'Prescription Lines', readonly=True, states={'Draft': [('readonly', False)]})
    pharmacy_id = fields.Many2one('oeh.medical.health.center.pharmacy', 'Pharmacy Reference', readonly=True, states={'Draft': [('readonly', False)]})

    #amount_total = fields.Function(_amount_all, digits_compute=dp.get_precision('Account'), string='Total', store=True, multi='sums', help="The total amount.")
    amount_total = fields.Float(
        #digits_compute=dp.get_precision('Account'), 
        string='Total', 
        #store=True, 
        #multi='sums', 
        #help="The total amount.",
    	compute='_amount_all',
    )
    @api.multi
    def _amount_all(self):
        for record in self:
            record.complete_name = 5.55

    pricelist_id = fields.Many2one('product.pricelist', 'Pricelist', help="Pricelist for current prescription", readonly=True, states={'Draft': [('readonly', False)]})

    #currency_id = fields.related('pricelist_id', 'currency_id', type="Many2one", relation="res.currency", string="Currency", readonly=True)
    currency_id = fields.Many2one(
        "res.currency", 
        #'pricelist_id', 
        #'currency_id', 
        #string="Currency", 
        #readonly=True
    )

    info = fields.Text('Extra Information', readonly=True, states={'Draft': [('readonly', False)]})
    state = fields.Selection(STATES, 'State',readonly=True)

    #def _amount_all(self, cr, uid, ids, field_name=None, arg=None, context=None):
    #    res = {}
    #    for order in self.browse(cr, uid, ids, context=context):
    #        res[order.id] = {
    #            'amount_total': 0.0,
    #        }
    #        val = 0.0
    #        for line in order.prescription_lines:
    #            val += line.price_subtotal
    #        res[order.id]['amount_total'] = val
    #    return res


    # Fetching prescription lines values
    #def onchange_prescription_id(self, cr, uid, ids, prescription_id=False,context=None):
    #    return True

    #def button_compute(self, cr, uid, ids,context=None):
    #    return True

    # Create Prescription invoice

    #def _default_account(self,cr,uid,ids,context=None):
    #    return True

    #def action_prescription_invoice_create(self, cr, uid, ids, context=None):
    #    return True

    # Preventing deletion of a prescription which is not in draft state
    #def unlink(self, cr, uid, ids, context=None):
    #    return True


class OeHealthPharmacyMedicineLines(models.Model):
    _name = 'oeh.medical.health.center.pharmacy.prescription.line'
    _description = 'Pharmacy Medicine Lines'
    #_defaults={
    #    'price_unit': lambda *a: 0.0,
    #    'price_subtotal': lambda *a: 0.0,
    #}

    name = fields.Many2one('oeh.medical.medicines','Medicines',help="Prescribed Medicines",domain=[('medicament_type','=','Medicine')], required=True)
    indication = fields.Many2one('oeh.medical.pathology','Indication',help="Choose a disease for this medicament from the disease list. It can be an existing disease of the patient or a prophylactic.")
    qty = fields.Integer('Prescribed Qty',help="Quantity of units (eg, 2 capsules) of the medicament")
    actual_qty = fields.Integer('Actual Qty Given', help="Actual quantity given to the patient")
    prescription_id = fields.Many2one('oeh.medical.health.center.pharmacy.line', 'Pharmacy Prescription Reference')
    price_unit = fields.Float('Unit Price', required=True,
        #digits_compute= dp.get_precision('Product Price')
    )
    
    #price_subtotal = fields.Function(_amount_line, string='Subtotal', 
        #digits_compute= dp.get_precision('Account')
    #),
    price_subtotal = fields.Float(
        string='Subtotal', 
        #digits_compute= dp.get_precision('Account')
    	compute='_amount_line',
    )
    @api.multi
    def _amount_line(self):
        for record in self:
            record.complete_name = 5.55


    #def _amount_line(self, cr, uid, ids, field_name, arg, context=None):
    #    res = {}
    #    if context is None:
    #        context = {}
    #    for line in self.browse(cr, uid, ids, context=context):
    #        price = line.price_unit * line.actual_qty
    #        res[line.id] = price
    #    return res


    # Autopopulate selected medicine values
    #def onchange_medicine_id(self, cr, uid, ids, medicine=False,context=None):
    #    if context is None:
    #        context = {}
    #    result = {}
    #    if medicine:
    #        med_obj = self.pool.get('oeh.medical.medicines')
    #        med_price_ids1 = med_obj.search(cr, uid, [('id', '=', medicine)], context=context)
    #        if med_price_ids1:
    #            for med_id in med_obj.browse(cr, uid, med_price_ids1, context=context):
    #                result['price_unit'] = med_id.lst_price
    #    return {'value': result}

    # Change subtotal pricing
    #def onchange_qty_and_price(self, cr, uid, ids, qty=False,price_unit=False,context=None):
    #    if context is None:
    #        context = {}
    #    result = {}
    #    if qty and price_unit:
    #        result['price_subtotal'] = price_unit * qty
    #    return {'value': result}
