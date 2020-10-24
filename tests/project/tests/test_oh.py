'''
Testing openhealth

Created:    23 oct 2020
Last up:    23 oct 2020

Usage
    python test.py 
    python -m unittest -v discover -s tests
'''

import unittest

#from ../../../models/management/lib/mgt_funcs import set_averages
#from models.management.lib.mgt_funcs import set_averages
from mgt_funcs import set_averages_pure


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can average
        """
        #data = [(150, 1)]
        #data = [(300, 2)]
        data = [(450, 3)]

        result = set_averages_pure(data)

        self.assertEqual(result, 150)


if __name__ == '__main__':
    unittest.main()

