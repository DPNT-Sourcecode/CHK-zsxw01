import unittest

from checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout_single_with_specialoffer(self):
        self.assertEqual(checkout('ABCDCBAABCABBAAA'), 505)

    def test_checkout_single(self):
        self.assertEqual(checkout('BBB'), 75)

    def test_checkout_illegal(self):
        self.assertEqual(checkout('B'), -1)

    def test_checkout_double(self):
        self.assertEqual(checkout('BBAB'), 75+50)

    def test_checkout_with_error(self):
        self.assertEqual(checkout('BBABFFFFFF'), -1)

    def test_checkout_with_alldata(self):
        self.assertEqual(checkout('ABCD'), 50+30+20+15)

    def test_checkout_with_alldata_special(self):
        self.assertEqual(checkout('BB'), 45)
        self.assertEqual(checkout('AAA'), 130)
        self.assertEqual(checkout('AAABB'), 130+45)

    def test_checkout_with_alldata_special_and_no(self):
        self.assertEqual(checkout('AAAABBBDDDD'), 130+50+45+30+(4*15))

    def test_checkout_with_alldata_10(self):
        self.assertEqual(checkout('AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDD'), (3*130+50)+(5*45)+10*20+10*15)

if __name__ == '__main__':
    unittest.main()
