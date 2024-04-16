# from collections import Counter
# from . import supermarket_stock_prices
# from supermarket_stock_prices import supermarket_stock

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not (isinstance(skus, str) and len(skus) >= 0):
        return -1
    
    total_price = 0

    # counts the instances of each element and stores the counts in a dictionary
    skus_counter = Counter(skus)

    for sku, quantity in skus_counter.items():
        # print(f"{quantity} x {sku}")
        if not sku in supermarket_stock:
            return -1
        
        if supermarket_stock[sku].offer:
            no_offer_claimed = quantity // supermarket_stock[sku].offer.quantity
            rem_quantity = quantity % supermarket_stock[sku].offer.quantity
            total_item_price = (no_offer_claimed * supermarket_stock[sku].offer.price) + (rem_quantity * supermarket_stock[sku].price)
        else:
            total_item_price = quantity * supermarket_stock[sku].price

        total_price += total_item_price

    return total_price
