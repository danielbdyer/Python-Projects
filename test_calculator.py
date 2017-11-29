import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_can_create_calculator_object(self):
        self.assertNotEqual(self.calculator,None)

    def test_can_add_numbers(self):
        self.assertEqual(6,self.calculator.add(4,2))
        print("4 plus 2 equals... RETURNED ANSWER: " + str(self.calculator.add(4,2)))

    def test_can_subtract_numbers(self):
        self.assertEqual(2,self.calculator.sub(4,2))
        print("4 minus 2 equals... RETURNED ANSWER: " + str(self.calculator.sub(4,2)))

    def test_can_multiply_numbers(self):
        self.assertEqual(8,self.calculator.mult(4,2))
        print("4 times 2 equals... RETURNED ANSWER: " + str(self.calculator.mult(4,2)))

    def test_can_divide_numbers(self):
        self.assertEqual(2,self.calculator.div(4,2))
        print("4 divided by 2 equals... RETURNED ANSWER: " + str(self.calculator.div(4,2)))

    def test_can_return_modulo(self):
        self.assertEqual("2R1",self.calculator.div(5,2))
        print("5 divided by 2 equals... RETURNED ANSWER: " + str(self.calculator.div(5,2)))

    def test_can_factorialize_numbers(self):
        self.assertEqual(self.calculator.fact(4),24)
        print("4 factorialized equals... RETURNED ANSWER: " + str(self.calculator.fact(4)))

unittest.main(verbosity=2)
