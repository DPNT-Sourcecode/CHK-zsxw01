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

DICT_PRICE = dict(A=50, B=30, C=20, D=15)

DICT_SPECIAL_OFFER = dict(A=dict(qty=3, price=150),
                          B=dict(qty=2, price=45))

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    result = 0

    for sku in skus.split():
        qty = int(sku[0][:-1])
        item = sku[0][-1]

        special_offer_qty = 0

        # check special offers => uses /
        if item in DICT_SPECIAL_OFFER:
            special_offer_price = DICT_SPECIAL_OFFER[item]['price']
            special_offer_qty = DICT_SPECIAL_OFFER[item]['qty']

            # use / as I have integer => 
            result += qty/special_offer_qty*special_offer_price

        # check NO special offers => uses %
        if item in DICT_PRICE:
            print 'calculate normal price'
            # check % with special_offer_qty
        else:
            return -1


    raise NotImplementedError()
