'''
Testing openhealth

Created:    23 oct 2020
Last up:     3 apr 2021

We should have:
    Unit tests: a lot 
    Service tests: some 
    End-to-end: a few 

Very important !
Every error should be caught, using an exception. 

Usage
    #python test.py 
    #python -m unittest -v discover -s tests
    
    From outside:
    cd /Users/gibil/cellar/github/openhealth/tests/project
    python -m unittest discover tests

    From inside:
    cd /Users/gibil/cellar/github/openhealth/tests/project/tests
    python -m unittest      # Explores the unittest testcase
    python -m unittest discover         # Explores the unittest testcase
    python test.py          # Executes the main
'''
import unittest
from mgt_funcs import averages_pure, averages_pure_tag


# ------------------------------------------------------------------ Funcs -----
#def func(amo, nr):
#    return round(float(amo) / float(nr), 2) if nr else 0
#func = lambda a, b : round(float(a) / float(b), 2)
func = lambda a, b : round(float(a) / float(b), 4)

_pre = '\n\n----------------------------------------------- '
_pos = ' -----'


# ---------------------------------------------------------- Test Averages -----
class TestAveragesPure(unittest.TestCase):
    """
    Unit test 
    mgt_funcs - averages_pure, averages_pure_tag
    """
    #@unittest.skip("skipping test")
    def test_func_external_lambda(self):
        """
        Test an external func
        """
        print(_pre + 'test_func_external_lambda' + _pos)
        data = [(100, 7)]
        print(data)
        result = averages_pure(data, func)
        print(result)
        self.assertEqual(result, [14.2857])

    #@unittest.skip("skipping test")
    def test_vector_tags(self):
        """
        Test a vector, with tags
        """
        print(_pre + 'test_vector_tags' + _pos)
        data = [('tag_0', 1350, 2), ('tag_1', 2950, 50)]
        print(data)
        result = averages_pure_tag(data)
        print(result)
        self.assertEqual(result, [('tag_0', 675), ('tag_1',59)])
        #self.tag_0 = result[0][1]
        #self.tag_1 = result[1][1]
        #print(self.tag_0)
        #print(self.tag_1)

    #@unittest.skip("skipping test")
    def test_vector_one_element(self):
        """
        Test a vector, one element
        """
        print(_pre + 'test_vector_one_element' + _pos)
        data = [(450, 3)]
        print(data)
        result = averages_pure(data)
        print(result)
        self.assertEqual(result, [150])

    #@unittest.skip("skipping test")
    def test_vector_decimals(self):
        """
        Test a vector, with decimals
        """
        print(_pre + 'test_vector_decimals' + _pos)
        data = [(100, 7)]
        print(data)
        result = averages_pure(data)
        print(result)
        self.assertEqual(result, [14.29])

    #@unittest.skip("skipping test")
    def test_vector_two_elements(self):
        """
        Test a vector, two elements
        """
        print(_pre + 'test_vector_two_elements' + _pos)
        data = [(1350, 2), (2950, 50)]
        print(data)
        result = averages_pure(data)
        print(result)
        self.assertEqual(result, [675, 59])





if __name__ == '__main__':
    print('Main')
    unittest.main()



