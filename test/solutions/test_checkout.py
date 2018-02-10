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
        self.assertEqual(checkout('1A 1B 1C 1D'), 50+30+20+15)

    def test_checkout_with_alldata_special(self):
        self.assertEqual(checkout('2B'), 45)
        self.assertEqual(checkout('3A'), 130)
        self.assertEqual(checkout('3A 2B'), 130+45)

    def test_checkout_with_alldata_special_and_no(self):
        self.assertEqual(checkout('4A 3B 19D'), 130+50+45+30+(19*15))

if __name__ == '__main__':
    unittest.main()
