#import unittest2

import odooselenium


class SampleTestCase(odooselenium.TestCase):

    def configure(self, **kwargs):
        """Override this method to alter settings... if necessary."""
        kwargs.setdefault('url', 'http://localhost:8069')
        kwargs.setdefault('username', 'admin')
        kwargs.setdefault('password', 'admin')
        kwargs.setdefault('dbname', 'test')
        super(SampleTestCase, self).configure(kwargs)

    def test_ui(self):
        # self.ui is instance of odooselenium.OdooUI.
        self.ui.go_to_module('Accounting')
        # self.webdriver is Selenium's webdriver.
        self.webdriver.find_element_by_css_selector('body')



def main():
    #unittest2.main()
    print 'jx'
    tc = SampleTestCase
    tc.configure()
    #tc.test_ui()


if __name__ == "__main__":
    main()
