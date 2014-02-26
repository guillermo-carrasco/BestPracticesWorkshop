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
        """
        DNA = "ATATATCCCGGCG"
        self.assertEqual("CGCCGGGATATAT", exercises.reverse_complement(DNA, as_string=True))

    def test_2_search(self):
        """Testing search method
        """
        text = "Will you find the word find two times?"
        self.assertEqual(2, len(exercises.search('find', text)))

    def test_3_extract_kmers(self):
        """Testing extract K-mers function
        """
        res = {'AC', 'CT', 'GA', 'GT', 'TG'}
        self.assertEqual(res, exercises.extract_kmers(2, 'ACTGTGAC'))

    def test_4_most_frequent_kmer(self):
        """Testing most_frequent_kmer method
        """
        # On this DNA string, TTTT and GGGG are the most frequent 4-mers if not
        # checking for reverse complement, because both appear 2 times. If looking
        # for reverse complement, AAAA and TTTT are the most frequent ones.
        DNA = "AACCTTTTGACATTTTCGCCAAAAGGGGG"
        self.assertEqual(['TTTT', 'GGGG'], exercises.most_frequent_kmer(DNA, 4))
        self.assertEqual(['AAAA', 'TTTT'], exercises.most_frequent_kmer(DNA, 4, reverse=True))
