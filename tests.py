import unittest
from A1 import *
from A2 import *


class TestStringMethods(unittest.TestCase):

    def test_zero_repo(self):
        f = True
        try:
            make_api_call(1, 4)
        except:
            f = False
        self.assertTrue(f)

    def test_to_date_less_than_from_date(self):
        f = True
        try:
            create_df('2021-10-17', '2021-08-18')
        except:
            f = False

        self.assertTrue(f)

    def test_incorrect_format(self):
        try:
            create_df('asdasd', '2021-08-18')
        except:
            f = False
        self.assertTrue(f)


if __name__ == '__main__':
    unittest.main()
