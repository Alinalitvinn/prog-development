import unittest
from main import bubble_sort

class TestFactorial(unittest.TestCase):
    def testfactorial(self):
        self.assertEqual(bubble_sort([5,8,2,0,4,1]), [0,1,2,4,5,8])
        self.assertEqual(bubble_sort([2,9,3,1]), [1,2,3,9])
        self.assertEqual(bubble_sort([5,0,4,6,3]), [0,3,4,5,6])

if __name__ == '__main__':
    unittest.main()