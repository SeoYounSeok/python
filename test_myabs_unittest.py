import unittest
from code import myabs

class TestMyAbs(unittest.TestCase):

    def test_return_itself_with_positive_param(self):
        self.assertEqual(myabs(5),5)
    def test_return_positive_wtih_negative_param(self):
        self.assertEqual(myabs(-7), 7)

# self.assertEqual(a,b): 테스트 에러
# asswert a == b : 에러 
