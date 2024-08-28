def calculator_add(a, b):
    return a + b

# Przykład dodawania
result = calculator_add(3, 3)
print(result)



import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator_add(3, 3), 6)
        self.assertEqual(calculator_add(-1, 1), 0)
        self.assertEqual(calculator_add(-1, -1), -2)
        self.assertEqual(calculator_add(0, 0), 0)
        self.assertEqual(calculator_add(100, 200), 300)

if __name__ == '__main__':
    unittest.main()