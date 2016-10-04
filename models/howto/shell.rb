Learn
------

Created: 	15 sep 2016
Last mod:	id. 



Shell 
./odoo.py shell -d chavarri-oehealth


self

self.name

self.env


self.env['res.partner']



#self.env['res.partner'].mapped('partner_id')



self.env['res.partner'].search([('name', 'like', 'J')])

self.env['res.country'].search([('name', 'like', 'Peru')])





http://localhost:8069/web#id=12&view_type=form&model=openextension.treatment&menu_id=1314&action=797
http://localhost:8069/web#id=14&view_type=form&model=openextension.treatment&menu_id=1314&action=797


self.env['openhealth.learn'].search([('name', 'like', 'B')])

self.env['openhealth.learn'].search([('name', 'like', 'J')]).do_operation()


self.env['openhealth.learn'].search([('name', 'like', 'J')]).write({'a': 1, 'b': 2, 'c': 3})

self.env['openhealth.learn'].search([('name', 'like', '')]).write({'a': 1, 'b': 2, 'c': 3})


self.env['res.partner'].filtered("partner_id.is_company")
self.env['res.partner'].filtered("company_type.is_company")


self.env['openhealth.learn'].search([('name', 'like', '')]).sorted()
self.env['openhealth.learn'].search([('name', 'like', '')]).sorted(key=lambda r: r.name)

self.env['openhealth.learn'].search([('name', 'like', '')]).mapped(lambda r: r.a + r.b)


self.env['openhealth.learn'].search([('name', 'like', '')]).mapped('name')



self.env['openhealth.learn'].search([('id','=','1')]).name




env['res.partner'].sudo().create({'name': "A Partner"})




self.env['openhealth.learn'].search([('name', 'like', '')]).search_count()






self.env['oeh.medical.patient'].search([('name', 'like', 'Ja')])

self.env['oeh.medical.patient'].search([('id', '=', '3025')])



self.env['oeh.medical.physician'].search([('name', 'like', 'Fe')])
self.env['oeh.medical.physician'].search([('id', '=', '1')])







self.env['openhealth.service'].search([('name', 'like', 'S')])












# not working
self.env['openhealth.learn'].search([('name', 'like', '')]).filtered(lambda r: r.name == user.name)

openhealth.learn(1, 2)

self.env['openhealth.learn'].do_operation()

self.env['openhealth.learn'].do_msg()








self.env.ref('base.group_public')

self.env.ref('openextension.treatment')




'default_patient': context.get('patient_id', False),









self.env['sale.order'].search_count([('name', 'like', '1')])

self.env['sale.order'].search([('name', 'like', '11')]).order_line.search([('name', 'like', 'CO')])
self.env['sale.order'].search([('name', 'like', '11')]).order_line.search([('id', '=', '3201')])
