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

DICT_SPECIAL_OFFER = dict(A=dict(qty=3, price=150),
                          B=dict(qty=2, price=45))

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    for sku in skus.split():
        qty = int(sku[0][:-1])
        item = sku[0][-1]

    # split skus


    # loop sku_list

        # check special offers => uses /

        # check NO special offers => uses %

    raise NotImplementedError()
