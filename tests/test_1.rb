

require 'watir'


# URL 
b = Watir::Browser.start 'localhost:8069'



l = b.link text: 'Odoo9-min'
l.click

t = b.text_field id: 'login'
t.set 'jrevilla55@gmail.com'

t = b.text_field id: 'password'
t.set 'atojatojcha'

btn = b.button value: 'Log in'
btn.click





s = b.span text: 'Caja'
s.click


btn = b.button text: 'Create'
btn.click





s = b.span class: 'jx_partner_id'
t = s.text_field class: 'ui-autocomplete-input'
t.set 'REVILLA RONDON JOSE JAVIER'




l = b.link text: 'Add an item'
l.click
d = b.div class: 'oe_form_field_one2many'
t = d.text_field class: 'ui-autocomplete-input'
t.set 'token'




btn = b.button text: 'Save'
btn.click










