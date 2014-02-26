import unittest

from BestPracticesWorkshop import exercises

class ExercisesTest(unittest.TestCase):
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

    def test_1_reverse_complement(self):
        """Testing reverse_complement function

        Return the reverse complement of the given DNA sequence.
        """
        self.assertTrue(False)

    def test_2_search(self):
        """Testing search method

        Returns a list containing the indexes of all matches of pattern in text.
        It also count overlapping matches.
        """
        self.assertTrue(False)

    def test_3_extract_kmers(self):
        """Testing extract K-mers function

        Returns a set of all k-mers in DNA.
        """
        self.assertTrue(False)

    def test_4_most_frequent_kmer(self):
        """Testing most_frequent_kmer method

        Returns a list containing the list of most frequent k-mer(s) in DNA. If
        reverse=True, will also count the reverse complement of the k-mer.
        """
        self.assertTrue(False)
