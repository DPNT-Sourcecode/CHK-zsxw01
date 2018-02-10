"""

Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+


Notes:
 - For any illegal input return -1

In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items

"""
from collections import Counter

DICT_PRICE = dict(A=50, B=30, C=20, D=15, E=40)

DICT_SPECIAL_OFFER = dict(A=dict(qty=3, price=130),
                          B=dict(qty=2, price=45))


DICT_FREE_ITEM_OFFER = dict(E=dict(qty=2, free_items=[dict(B=dict(qty=1))]))

def _clean_from_free(skus_counter):
    """
    function to clean obj.
    :param skus_counter:
    :return:
    """
    print 'skus_counter init'
    print skus_counter
    for item in skus_counter:
        if item in DICT_FREE_ITEM_OFFER:
            free_item_qty = DICT_FREE_ITEM_OFFER[item]['qty']
            mult = skus_counter[item]/free_item_qty


            for free_item in DICT_FREE_ITEM_OFFER[item]['free_items']:
                for item_2 in skus_counter:
                    print '=====>>>>>'
                    print item_2
                    print free_item
                    print item_2 in free_item
                    print '=====>>>>>'
                    if item_2 in free_item:
                         clean_qty = mult * free_item[item_2]['qty']
                         print clean_qty
                         print skus_counter[item_2]['qty']

                         if skus_counter[item_2]['qty'] < clean_qty:
                             print 'ooo'
                    # #
                    #      skus_counter[item_2]['qty'] = 0  else \
                    #          skus_counter[item_2]['qty'] - clean_qty

    print 'skus_counter end'
    print skus_counter
    return skus_counter





def chunk_string(s, n):
    return [s[i:i+n] for i in range(len(s)-n+1)]
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    result = 0
    skus_counter = Counter(chunk_string(skus, 1))
    #

    skus_counter = _clean_from_free(skus_counter)

    for item in skus_counter:

        qty = skus_counter[item]
        special_offer_qty = None

        # check if item has special offers.
        if item in DICT_SPECIAL_OFFER:
            special_offer_price = DICT_SPECIAL_OFFER[item]['price']
            special_offer_qty = DICT_SPECIAL_OFFER[item]['qty']

            # I use / as I have integer => 5/2 = 2
            result += qty / special_offer_qty * special_offer_price

        # check NO special offers => uses %
        if item in DICT_PRICE:
            price = DICT_PRICE[item]

            # check % with special_offer_qty
            if special_offer_qty:
                result += qty % special_offer_qty * price
            else:
                result += qty * price

        else:
            return -1

    #print result
    return result
