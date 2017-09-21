from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

import odooselenium


webdriver = Firefox()
ui = odooselenium.OdooUI(
    webdriver,
    base_url=u'http://localhost:8069',
)



# Log in.
ui.login('myusername', 'mypassword', 'mydatabase')

# Navigate to "Accounting / Customers".
ui.go_to_module('Accounting')
ui.go_to_view('Customers')

# Toggle list view.
assert ui.get_url_fragments()['view_type'] == u'kanban'
list_view_button = webdriver.find_element(
    By.CSS_SELECTOR,
    ".oe_vm_switch_list")
with ui.wait_for_ajax_load():
    list_view_button.click()
assert ui.get_url_fragments()['view_type'] == u'list'
# Click "Create" button.
create_button = webdriver.find_element(
    By.XPATH,
    "//button["
    "@data-bt-testing-model_name='res.partner' and "
    "@data-bt-testing-name='oe_list_add']")
with ui.wait_for_ajax_load():
    create_button.click()

# Fill then submit the form.
name_field = webdriver.find_element(
    By.XPATH,
    "//input["
    "@data-bt-testing-model_name='res.partner' and "
    "@data-bt-testing-name='name']")
name_field.send_keys('Sample customer')
save_button = webdriver.find_element(
    By.XPATH,
    "//button["
    "@data-bt-testing-model_name='res.partner' and "
    "@data-bt-testing-name='oe_form_button_save']"
)
with ui.wait_for_ajax_load():
    save_button.click()

