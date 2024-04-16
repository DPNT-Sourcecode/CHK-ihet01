from . import *

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
        
        total_item_price = 0
        rem_quantity = quantity
        if supermarket_stock[sku].offers:
            # Starting from the offer with the higher quantity as it is already sorted by descending
            for offer in supermarket_stock[sku].offers:
                no_offer_claimed = rem_quantity // offer.quantity
                rem_quantity = rem_quantity % offer.quantity
                total_item_price += (no_offer_claimed * offer.price)

        total_item_price += rem_quantity * supermarket_stock[sku].price

        total_price += total_item_price

    return total_price