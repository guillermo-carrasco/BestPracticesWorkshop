import unittest

from BestPracticesWorkshop import examples

class ExamplesTest(unittest.TestCase):
    """Test all methods on the examples module
    """

    def setUp(self):
        """This method is executed before all tests
        """
        pass

    def tearDown(self):
        """This method is executed after all tests
        """
        pass

    def test_1_sum_list(self):
        """Testing sum_list method
        """
        with self.assertRaises(ValueError):
            examples.sum_list([1, 2, '3'])
        self.assertEqual(6, examples.sum_list([1, 2, 3]))
        self.assertEqual(4, examples.sum_list([-1, 2, 3]))

    def test_2_odd(self):
        """Testing odd method
        """
        with self.assertRaises(ValueError):
            examples.odd('1')
        self.assertEqual(1, examples.odd(1))
        self.assertEqual(3, examples.odd(2))
