'''
Testing openhealth

Created:    23 oct 2020
Last up:    23 oct 2020

Usage
    python test.py 
    python -m unittest -v discover -s tests
'''

import unittest

from mgt_funcs import averages_pure

# ------------------------------------------------------------------ Funcs -----
#def func(amo, nr):
#    return round(float(amo) / float(nr), 2) if nr else 0

func = lambda a, b : round(float(a) / float(b), 2)


# ------------------------------------------------------------------- Test -----
class TestSum(unittest.TestCase):

    #def __init__(self):
    #    print('init')

    @unittest.skip("skipping test")
    def test_vector_one_element(self):
        """
        Test a vector, one element
        """
        data = [(450, 3)]
        result = averages_pure(data)
        self.assertEqual(result, [150])

    @unittest.skip("skipping test")
    def test_vector_decimals(self):
        """
        Test a vector, with decimals
        """
        data = [(100, 7)]
        result = averages_pure(data)
        self.assertEqual(result, [14.29])

    @unittest.skip("skipping test")
    def test_func_external_lambda(self):
        """
        Test a vector, one element
        """
        data = [(450, 3)]
        result = averages_pure(data, func)
        self.assertEqual(result, [150])


    @unittest.skip("skipping test")
    def test_vector_two_elements(self):
        """
        Test a vector, two elements
        """
        data = [(1350, 2), (2950, 50)]
        result = averages_pure(data)
        self.assertEqual(result, [675, 59])


    def test_vector_tags(self):
        """
        Test a vector, with tags
        """
        data = [('tag_0', 1350, 2), ('tag_1', 2950, 50)]
        result = averages_pure(data)

        self.assertEqual(result, [('tag_0', 675), ('tag_1',59)])
        
        self.tag_0 = result[0][1]
        self.tag_1 = result[1][1]
        
        print(self.tag_0)
        print(self.tag_1)


    #def test_self_vars(self):
        #print(self.tag_0)
        #self.assertEqual(self.tag_0, 675)
        #self.assertEqual(self.tag_1, 59)



if __name__ == '__main__':

    unittest.main()



