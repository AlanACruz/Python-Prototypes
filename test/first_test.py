import unittest

class TestSum(unittest.TestCase):

    def test_sum_array(self):

        # given 
        expected = 6
        arrayValues = [1, 2, 3]

        # then
        actual = sum(arrayValues) 

        # assert
        self.assertEqual(actual, expected, "Should be 6")

    def test_sum_tuple(self):
        
        # given 
        expected = 6
        tupleValues = (1, 2, 3)

        # then
        actual = sum(tupleValues) 

        # assert
        self.assertEqual(actual, expected, "Should be 6")

if __name__ == '__main__':
    unittest.main()