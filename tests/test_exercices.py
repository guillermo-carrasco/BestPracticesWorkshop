import unittest

from BestPracticesWorkshop import exercises

class ExercicesTest(unittest.TestCase):
    """Test all methods on the exercises module
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
            exercises.sum_list([1, 2, '3'])
        self.assertEqual(6, exercises.sum_list([1, 2, 3]))
        self.assertEqual(4, exercises.sum_list([-1, 2, 3]))

    def test_2_odd(self):
        """Testing odd method
        """
        with self.assertRaises(ValueError):
            exercises.odd('1')
        self.assertEqual(1, exercises.odd(1))
        self.assertEqual(3, exercises.odd(2))
