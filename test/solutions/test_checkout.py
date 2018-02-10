import unittest

from checkout import checkout


class TestCheckout(unittest.TestCase):

    def test_checkout_with_2F(self):
        self.assertEqual(checkout('FF'), 10*2)

    def test_checkout_with_3F(self):
        self.assertEqual(checkout('FFF'), 10*2)

    def test_checkout_with_moreF(self):
        self.assertEqual(checkout('FFFFFFFFFFFF'), (12/3*2) * 10)

    def test_checkout_with_double_special_offer(self):
        self.assertEqual(checkout('AAAAAAAAAAAAA'), 530)

    def test_checkout_with_single(self):
        self.assertEqual(checkout('ABCDE'), 50+30+20+15+40)

    def test_checkout_with_free_1(self):
        self.assertEqual(checkout('EEEEE'), 5*40)

    def test_checkout_with_free(self):
        self.assertEqual(checkout('EEEEEBBB'), 5*40+30)

    def test_checkout_with_free_special(self):
        self.assertEqual(checkout('EEEEEBBBB'), 5*40+45)

    def test_checkout_with_double_special_offer(self):
        self.assertEqual(checkout('XXX'), -1)

    def test_checkout_illegal(self):
        self.assertEqual(checkout('ABCa'), -1)

    def test_checkout_illegal_lower(self):
        self.assertEqual(checkout('AxA'), -1)

    def test_checkout_single(self):
        self.assertEqual(checkout('BBB'), 75)



    def test_checkout_single_with_specialoffer(self):
        self.assertEqual(checkout('ABCDCBAABCABBAAA'), 200+(2*50)+(45*2)+30+3*20+15)
    #

    #

    #
    # def test_checkout_space(self):
    #     self.assertEqual(checkout(''), 0)
    #
    # def test_checkout_double(self):
    #     self.assertEqual(checkout('BBAB'), 75+50)
    #
    # def test_checkout_with_error(self):
    #     self.assertEqual(checkout('BBABFFFFFF'), -1)
    #
    # def test_checkout_with_alldata(self):
    #     self.assertEqual(checkout('ABCD'), 50+30+20+15)
    #
    # def test_checkout_with_alldata_special(self):
    #     self.assertEqual(checkout('BB'), 45)
    #     self.assertEqual(checkout('AAA'), 130)
    #     self.assertEqual(checkout('AAABB'), 130+45)
    #
    # def test_checkout_with_alldata_special_and_no(self):
    #     self.assertEqual(checkout('AAAABBBDDDD'), 130+50+45+30+(4*15))
    #
    # def test_checkout_with_alldata_10(self):
    #     self.assertEqual(checkout('AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDD'), (3*130+50)+(5*45)+10*20+10*15)

if __name__ == '__main__':
    unittest.main()
