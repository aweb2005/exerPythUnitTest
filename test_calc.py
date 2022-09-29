import unittest
import calc


class TestCalc(unittest.TestCase):
#all tests must start with test_ or they will not run even if you don't see an error
    def test_add(self):
        #result = calc.add(10,5)
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
        #all three lines are considered 1 test not 3 because all under one def

    def test_subtract(self):
        #result = calc.add(10,5)
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)

    def test_multiply(self):
        #result = calc.add(10,5)
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)

    def test_divide(self):
        #result = calc.add(10,5)
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)
        self.assertEqual(calc.divide(5,2),2.5) #using to make sure we didn't do floor division instead of regular division

        #self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()







