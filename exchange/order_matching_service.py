
def order_match():
    '''
    Traverse the order book looking for Active orders which match
    the specified price.

    *If the order is a buy, we look for a price less than or equal.
    *If the order is a sell, we look for a price greater than or equal.
    *If it’s a market order, we find the highest (sell) or lowest (buy) price.

    We sort matches ascending for buy orders, and descending for
    sell orders. Then we sort by date if the price matches.

    Generate Transaction as a result
    :return:
    '''
    return

def get_transaction_for_two_orders(order_buy, order_sell):
    '''
    Record the matching orders with a transaction
    :param order_buy: Buy order to be filled
    :param order_sell: Sell order to be filled
    :return:
    '''
    return

def handle_split_order(order_buy, order_sell):
    '''
    Handle the cases where the entire order isn't filled.
    :param order_buy:
    :param order_sell:
    :return:
    '''
    return

def process_order(transaction):
    '''
    Process the transaction to record the result.
    a: add the transaction and the split orders to the DB
    b: for both orders in the transaction:

    - subtract the debit access
    - increment the credit asset
    - record the commision in the commision account
    - unfreeze frozen balances
    - save changes

    :param transaction:
    :return:
    '''
    return