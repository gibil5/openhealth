import unittest
import calc

class TestCalc(unittest.TestCase):

	def test_add_a(self):

		calc_a = calc.Calc()
	
		self.assertEqual(calc_a.add(2, 3), 5)
		#self.assertEqual(calc_a.add(2, 3), 4)


if __name__ == '__main__':
		
	unittest.main()

