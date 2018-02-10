import unittest

from checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout_single_with_specialoffer(self):
        self.assertEqual(checkout('2B'), 45)

    def test_checkout_single(self):
        self.assertEqual(checkout('3B'), 75)


    def test_checkout_double(self):
        self.assertEqual(checkout('3B 1A'), 75+50)

    def test_checkout_with_error(self):
        self.assertEqual(checkout('3B 1A 19F'), -1)

    def test_checkout_with_alldata(self):
        self.assertEqual(checkout('1A 1B 1C 1D 1E'), -1)

if __name__ == '__main__':
    unittest.main()
