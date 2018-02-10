import unittest

from checkout import checkout


class TestCheckout(unittest.TestCase):

    def test_checkout_with_moreF(self):
        self.assertEqual(checkout('FFFFFFFFFFFF'), (12 / 3 * 2) * 10)

    def test_checkout_with_double_special_offer(self):
        self.assertEqual(checkout('AAAAAAAAAAAAA'), 530)

    def test_checkout_with_single(self):
        self.assertEqual(checkout('ABCDE'), 50 + 30 + 20 + 15 + 40)

    def test_checkout_with_free_1(self):
        self.assertEqual(checkout('EEEEE'), 5 * 40)

    def test_checkout_with_free(self):
        self.assertEqual(checkout('EEEEEBBB'), 5 * 40 + 30)

    def test_checkout_with_free_special(self):
        self.assertEqual(checkout('EEEEEBBBB'), 5 * 40 + 45)

    def test_checkout_with_double_special_offer(self):
        #self.assertEqual(checkout('XXX'), 90 * 3)
        self.assertEqual(checkout('XXX'), 45)

    def test_checkout_illegal(self):
        self.assertEqual(checkout('ABCa'), -1)

    def test_checkout_illegal_lower(self):
        self.assertEqual(checkout('AxA'), -1)

    def test_checkout_single(self):
        self.assertEqual(checkout('BBB'), 75)

    def test_checkout_single_with_specialoffer(self):
        self.assertEqual(checkout('ABCDCBAABCABBAAA'), 200 + (2 * 50) + (45 * 2) + 30 + 3 * 20 + 15)

    #

    def test_ckeckout_all(self):
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('C'), 20)
        self.assertEqual(checkout('D'), 15)
        self.assertEqual(checkout('E'), 40)
        self.assertEqual(checkout('F'), 10)
        self.assertEqual(checkout('G'), 20)
        self.assertEqual(checkout('H'), 10)
        self.assertEqual(checkout('I'), 35)
        self.assertEqual(checkout('J'), 60)
        self.assertEqual(checkout('K'), 80)
        self.assertEqual(checkout('L'), 90)
        self.assertEqual(checkout('M'), 15)
        self.assertEqual(checkout('N'), 40)
        self.assertEqual(checkout('O'), 10)
        self.assertEqual(checkout('P'), 50)
        self.assertEqual(checkout('Q'), 30)
        self.assertEqual(checkout('R'), 50)
        self.assertEqual(checkout('S'), 30)
        self.assertEqual(checkout('T'), 20)
        self.assertEqual(checkout('U'), 40)
        self.assertEqual(checkout('V'), 50)
        self.assertEqual(checkout('W'), 20)
        self.assertEqual(checkout('X'), 90)
        self.assertEqual(checkout('Y'), 10)
        self.assertEqual(checkout('Z'), 50)

    def test_checkout_A(self):
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout('AAA'), 130)
        self.assertEqual(checkout('AAAa'), -1)
        self.assertEqual(checkout('AAAAA'), 200)
        self.assertEqual(checkout('AAAAAAAA'), 200 + 130)
        self.assertEqual(checkout('AAAAAAAAA'), 200 + 130 + 50)

    def test_checkout_B(self):
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('BB'), 45)
        self.assertEqual(checkout('BBB'), 45 + 30)

    def test_checkout_E(self):
        self.assertEqual(checkout('EE'), 40 * 2)
        self.assertEqual(checkout('EEB'), 40 * 2)
        self.assertEqual(checkout('EEBB'), 40 * 2 + 30)

    def test_checkout_F(self):
        self.assertEqual(checkout('FF'), 10 * 2)
        self.assertEqual(checkout('FFF'), 10 * 2)

    def test_checkout_H(self):
        self.assertEqual(checkout('H'), 10)
        self.assertEqual(checkout('HHHHH'), 45)
        self.assertEqual(checkout('HHHHHHHHHH'), 80)
        self.assertEqual(checkout('HHHHHHHHHHHHHHH'), 80 + 45)
        self.assertEqual(checkout('HHHHHHHHHHHHHHHH'), 80 + 45 + 10)

    def test_checkout_K(self):
        self.assertEqual(checkout('K'), 80)
        self.assertEqual(checkout('KK'), 150)

    def test_checkout_N(self):
        self.assertEqual(checkout('NNN'), 40 * 3)
        self.assertEqual(checkout('NNNM'), 40 * 3)
        self.assertEqual(checkout('NNNMM'), 40 * 3 + 15)

    def test_checkout_P(self):
        self.assertEqual(checkout('P'), 50)
        self.assertEqual(checkout('PPPPP'), 200)
        self.assertEqual(checkout('PPPPPP'), 250)

    def test_checkout_Q(self):
        self.assertEqual(checkout('Q'), 30)
        self.assertEqual(checkout('QQQ'), 80)
        self.assertEqual(checkout('QQQQ'), 80 + 30)

    def test_checkout_R(self):
        self.assertEqual(checkout('R'), 50)
        self.assertEqual(checkout('RRR'), 50 * 3)
        self.assertEqual(checkout('RRRQ'), 50 * 3)
        self.assertEqual(checkout('RRRQQQ'), 50 * 3 + (2 * 30))
        self.assertEqual(checkout('RRRQQQQ'), 50 * 3 + 80)

    def test_checkout_U(self):
        self.assertEqual(checkout('U'), 40)
        self.assertEqual(checkout('UUU'), 40 * 3)
        self.assertEqual(checkout('UUUU'), 40 * 3)


    def test_checkout_V(self):
        self.assertEqual(checkout('V'), 50)
        self.assertEqual(checkout('VV'), 90)
        self.assertEqual(checkout('VVV'), 130)
        self.assertEqual(checkout('VVVVV'), 130 + 90)
        self.assertEqual(checkout('VVVVVV'), 130 + 130)
        self.assertEqual(checkout('VVVVVVV'), 130 + 130 + 50)


    def test_checkout_space(self):
        self.assertEqual(checkout(''), 0)


    def test_checkout_group(self):
        self.assertEqual(checkout('SSS'), 45)
        self.assertEqual(checkout('XYZSST'), 90)
        self.assertEqual(checkout('TTTTTT'), 90)
        self.assertEqual(checkout('TTTTTTT'), 90 + 20)
        #self.assertEqual(checkout('ZZZZZZZ'), 90 + 21)
        self.assertEqual(checkout('TTTZZZZ'), 90 + 20)
        self.assertEqual(checkout('ZZZZZZZ'), 90 + 21)
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
