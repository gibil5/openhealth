import unittest2


def fun(x):
	return x + 1




class MyTest(unittest2.TestCase):
	def test(self):
		self.assertEqual(fun(3), 4)

class LearningCase(unittest2.TestCase):
	def test_starting_out(self):
		self.assertEqual(1, 1)



def main():
	unittest2.main()

if __name__ == "__main__":
	main()
