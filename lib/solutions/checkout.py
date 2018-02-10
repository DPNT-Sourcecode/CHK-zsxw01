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


# TODO: this should be move in a 'constants.py' and/or create model with these values - INIT

DICT_PRICE = dict(A=50, B=30, C=20, D=15, E=40, F=10, G=20, H=10, I=35, J=60, K=80, L=90, M=15, N=40, O=10,
                  P=50, Q=30, R=50, S=30, T=20, U=40, V=50, W=20, X=90, Y=10, Z=50)

DICT_SPECIAL_OFFER_1 = dict(A=dict(qty=5, price=200),
                            H=dict(qty=10, price=80),
                            V=dict(qty=3, price=130))

DICT_SPECIAL_OFFER = dict(A=dict(qty=3, price=130),
                          B=dict(qty=2, price=45),
                          H=dict(qty=5, price=45),
                          K=dict(qty=2, price=150),
                          P=dict(qty=5, price=200),
                          Q=dict(qty=3, price=80),
                          V=dict(qty=2, price=90),
                          )


DICT_FREE_ITEM_OFFER = dict(E=dict(qty=2, free_items=[dict(B=dict(qty=1))]),
                            F=dict(qty=3, free_items=[dict(F=dict(qty=1))]),
                            N=dict(qty=3, free_items=[dict(M=dict(qty=1))]),
                            R=dict(qty=3, free_items=[dict(Q=dict(qty=1))]),
                            U=dict(qty=4, free_items=[dict(U=dict(qty=1))]))

# TODO: this should be move in a 'constants.py' and/or create model with these values - END

def _clean_from_free(skus_counter):
    """
    function to clean obj.
    :param skus_counter:
    :return:
    """
    # check if the item is in DICT_FREE_ITEM_OFFER.
    for item in skus_counter:
        if item in DICT_FREE_ITEM_OFFER:
            # calculate how many items to get free.
            free_item_qty = DICT_FREE_ITEM_OFFER[item]['qty']
            mult = skus_counter[item]/free_item_qty

            # check if my skus_counter I've items to get free.
            for free_item in DICT_FREE_ITEM_OFFER[item]['free_items']:
                for item_2 in skus_counter:
                    if item_2 in free_item:
                        clean_qty = mult * free_item[item_2]['qty']
                        skus_counter[item_2] = 0 if skus_counter[item_2] < clean_qty else skus_counter[item_2] - clean_qty

    return skus_counter


def _calc_special_offer(skus_counter, result, dict_special_offer):
    for item in skus_counter:

        qty = skus_counter[item]

        # check if item has special offers.
        if item in dict_special_offer:
            special_offer_price = dict_special_offer[item]['price']
            special_offer_qty = dict_special_offer[item]['qty']

            # I use / as I have integer => 5/2 = 2
            no_pack = (qty / special_offer_qty)
            result += no_pack * special_offer_price

            skus_counter[item] -= no_pack * special_offer_qty

    return skus_counter, result


def chunk_string(s, n):
    """
    Create a group of letters/number giving a string.
    """
    return [s[i:i+n] for i in range(len(s)-n+1)]


def checkout(skus):

    result = 0
    skus_counter = Counter(chunk_string(skus, 1))

    # call f(x) to get objects free.
    skus_counter = _clean_from_free(skus_counter)

    # call f(xt) to calc_special offer
    skus_counter, result = _calc_special_offer(skus_counter, result, DICT_SPECIAL_OFFER_1)
    skus_counter, result = _calc_special_offer(skus_counter, result, DICT_SPECIAL_OFFER)

    # call the calc for other items.
    for item in skus_counter:
        qty = skus_counter[item]
        special_offer_qty = None

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

    return result
