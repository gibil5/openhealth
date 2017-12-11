
require 'watir'

Watir::Browser.new



# Url 
b = Watir::Browser.start 'localhost:8069'




# Field 
t = b.text_field id: 'entry_1000000'
t.exists?
t.set 'REVILLA RONDON JOSE JAVIER'
t.value



# Lists 
s = b.select_list id: 'entry_1000001'
s.select 'Ruby'
s.selected_options



# Radios 
r = b.radio value: 'A gem'
r.exists?
r.set
r.set?



# Checkbox 
c = b.checkbox value: '1.9.2'
c.exists?
c.set
c.set?



# Button
btn = b.button value: 'Submit'
btn.exists?
btn.click


# Link 
l = b.link text: 'Google Forms'
l.exists?
l.click




