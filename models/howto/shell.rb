Learn
------

Created: 	15 sep 2016
Last mod:	id. 



Shell 
./odoo.py shell -d chavarri-oehealth


self

self.name

self.env



s= self.env['product.template'].search([  ('x_treatment', '=', 'hyaluronic_acid'), ('x_sessions', '=', '1') ])











self.env['res.partner']



#self.env['res.partner'].mapped('partner_id')



self.env['res.partner'].search([('name', 'like', 'J')])



self.env['product.pricelist'].search([('name', 'like', 'P')])
self.env['product.pricelist'].search([('name', '=', 'Public Pricelist')])






self.env['res.users']
self.env['res.users'].search([('name', 'like', 'J')])






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


self.env['oeh.medical.patient'].search([('name', '=', '')])
self.env['oeh.medical.patient'].search([('name', '=', 'NIZAMA CASTILLO EDICSON JIICHIRO')])
self.env['oeh.medical.patient'].search([('name', '=', 'REVILLA RONDON Jose Javier')])


NIZAMA CASTILLO EDICSON JIICHIRO
REVILLA RONDON Jose Javier




self.env['oeh.medical.physician'].search([('name', 'like', 'Fe')])
self.env['oeh.medical.physician'].search([('id', '=', '1')])







self.env['openhealth.service'].search([('name', 'like', 'S')])




self.env['product.template'].search([('x_treatment', 'like', 'laser_co2')])


#order='appointment_date desc',



self.env['product.template'].search([	('x_treatment', '=', 'laser_co2'),	('x_zone', '=', 'body_local'),	('x_pathology', '=', 'acne_sequels_1')])


self.env['product.template'].search([('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'body_local'),('list_price', '=', 50)]).name








self.env['openhealth.treatment']

self.env['openhealth.treatment'].search([('name', 'like', 'TR000016'),])

t = self.env['openhealth.treatment'].search([('id', '=', '16'),])

t = self.env['openhealth.treatment'].search([('id', '=', '02'),])








self.env['product.template']

self.env['product.template'].search([('x_zone', 'like', '1_hypodermic'),])



self.env['account.invoice.line']




self.env['product.template'].search([('type', 'like', 'service'),])

self.env['product.template'].search([('type', 'like', 'consumable'),])





self.env['product.template'].search([('x_treatment', 'like', 'co2'),('x_zone', 'like', 'hands')], limit=1)


self.env['product.template'].search([('x_treatment', 'like', 'hyaluronic_acid'),('x_zone', 'like', '1_hypodermic_repair')], limit=1)



p = self.env['product.template'].search([('x_treatment', 'like', 'hyaluronic_acid'),('x_zone', 'like', '1_hypodermic_repair')], limit=1)



p = self.env['product.template'].search([('x_name_short', 'like', 'co2_han_sta'),])






# not working
self.env['openhealth.learn'].search([('name', 'like', '')]).filtered(lambda r: r.name == user.name)

openhealth.learn(1, 2)

self.env['openhealth.learn'].do_operation()

self.env['openhealth.learn'].do_msg()







# Treatment 

self.env.ref('base.group_public')

self.env.ref('openextension.treatment')

t = self.env['openextension.treatment'].search([('chief_complaint', 'like', 'acne_active')], limit=1)



t = self.env['openextension.treatment'].search([	('chief_complaint', 'like', 'acne_active'), ('patient', 'like', 'Puga')	])


t = self.env['openextension.treatment'].search([	('chief_complaint', 'like', 'acne_active'), ('patient', 'like', 'Revilla')	])

t = self.env['openextension.treatment'].search([	('chief_complaint', 'like', 'acne_active'), ('patient', 'like', 'Revilla')],  order='start_date' )

t = self.env['openextension.treatment'].search([	('chief_complaint', 'like', 'acne_active'), ('patient', 'like', 'Revilla')],  order='start_date desc' )

t = self.env['openextension.treatment'].search([	('chief_complaint', 'like', 'acne_active'), ('patient', 'like', 'Revilla')],  order='start_date desc', limit=1 )


t = self.env['openextension.treatment'].search([  ('chief_complaint', 'like', 'acne_active'), ('patient', 'like', 'Revilla'),    ],  order='start_date desc', limit=1 )





'default_patient': context.get('patient_id', False),







self.env['sale.order']
self.env['sale.order'].search_count([('name', 'like', '1')])

self.env['sale.order'].search([('name', 'like', '11')]).order_line.search([('name', 'like', 'CO')])
self.env['sale.order'].search([('name', 'like', '11')]).order_line.search([('id', '=', '3201')])



o = self.env['sale.order'].search([('name', 'like', '103')])

o = self.env['sale.order'].search([('name', 'like', '109')])

o = self.env['sale.order'].search([('name', 'like', '119')])




o = self.env['sale.order'].search([('name', 'like', '182')])

o = self.env['sale.order'].search([('name', 'like', '184')])


o = self.env['sale.order'].search([('name', 'like', '191')])








o.order_line.create({ 'product_id': 4043, 'order_id': 89, 'name': 'hya_1hr_ref_one_nor' })

o.order_line.create({ 'product_id': 4136, 'order_id': 95, 'name': 'hya_1hr_ref_one_nor' })

o.order_line.create({ 'product_id': 4136, 'order_id': 95, 'name': 'ACIDO HIALURONICO - 1 Jeringa - REPAIR - Rejuvenecimiento Facial - 1 - Normal' })



o.order_line.create({ 'product_id': 4190, 'order_id': 105, 'name': 'lep_bac_acn_one_nor' })






self.env['product.template'].search([('x_name_short', 'like', 'hya_1hr_ref_one_nor'),])

p = self.env['product.template'].search([('x_name_short', 'like', 'lep_bac_acn_one_nor')])



pc = self.env['product.template'].search([('x_name_short', 'like', 'co2_nec_sca')])



self.env['openhealth.consultation'].search([('name', 'like', '93')])

self.env['res.partner'].search([('name','=','Yvan Puga')],limit=1)


self.env['openhealth.service.co2'].search([('name', 'like', '93')])










self.env['sale.order'].search([('state', 'like', 'draft')])

o = self.env['sale.order'].search([('state', 'like', 'draft')])


self.env['sale.order'].search([('customer', 'like', 'J')])












a = self.env['oeh.medical.appointment'].search([('name', 'like', '68')])

a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '26')])

a = self.env['oeh.medical.appointment'].search([('appointment_date', '=', '2016-11-26')])


a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '26')], limit=1)



a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '16-11-26')], limit=1)

a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '16-11-26'), ('doctor_id', '=', '1'),])



a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '16-12-6'), ('doctor', 'like', 'Chavarri'),])

a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '16-12-6'), ('patient', 'like', 'Revilla'),])


a = self.env['oeh.medical.appointment'].search([ 	('patient', 'like', 'Revilla'),		('doctor', 'like', 'Chavarri'), 		])

a = self.env['oeh.medical.appointment'].search([ 	('patient', 'like', 'Revilla'),		('doctor', 'like', 'Chavarri'), 	('appointment_date', 'like', '2016-12-06 15:30:00')	])




a = self.env['oeh.medical.appointment'].search([ 	('patient', 'like', 'Revilla'),		('doctor', 'like', 'Chavarri'), 		], limit=1)


a = self.env['oeh.medical.appointment'].search([ 	('patient', 'like', 'Revilla'),		('doctor', 'like', 'Chavarri'), 	('x_type', 'like', 'consultation'), 		])

a = self.env['oeh.medical.appointment'].search([ 	('patient', 'like', 'Revilla'),		('doctor', 'like', 'Chavarri'), 	('x_type', 'like', 'consultation'), 		], order='appointment_date desc', limit=1)



a = self.env['oeh.medical.appointment'].search([ 	('patient', 'like', 'Revilla'),		('doctor', 'like', 'Chavarri'), 	('x_type', 'like', 'consultation'), ('appointment_date', 'like', '2016-12-06 15:30:00')		])




a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', appointment_date_str), ('doctor', '=', doctor_name), ('x_type', '=', x_type), ])


a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', appointment_date_str), ])
														 	])

a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '16-12-23'), ])




a = self.env['oeh.medical.appointment'].search([ ('patient', 'like', 'REVILLA Javier'),	('x_therapist', 'like', 'Eulalia'), ('x_type', 'like', 'procedure'), ], order='appointment_date desc', limit=1)




a = self.env['oeh.medical.appointment'].search([ ('appointment_date', 'like', '17-03-02'), ('patient', 'like', 'REVILLA Javier'),	('x_therapist', 'like', 'Eulalia'), ('x_type', 'like', 'procedure'), ], order='appointment_date desc', limit=1)


a = self.env['oeh.medical.appointment'].search([ ('appointment_date', 'like', '2017-03-02 16:00:00'), ('patient', 'like', 'REVILLA Javier'),	('x_therapist', 'like', 'Eulalia'), ('x_type', 'like', 'procedure'), ], order='appointment_date desc', limit=1)


a = self.env['oeh.medical.appointment'].search([ ('appointment_date', 'like', '2017-03-02 '), ('patient', 'like', 'REVILLA Javier'),	('x_therapist', 'like', 'Eulalia'), ('x_type', 'like', 'procedure'), ], order='appointment_date desc', limit=1)


a = self.env['oeh.medical.appointment'].search([ ('appointment_date', 'like', '2017-03-02 17:17:36'), ('patient', 'like', 'REVILLA Javier'),	('x_therapist', 'like', 'Eulalia'), ('x_type', 'like', 'procedure'), ], order='appointment_date desc', limit=1)








ret = a.write({'consultation': 65,})



