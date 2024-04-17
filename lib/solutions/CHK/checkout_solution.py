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

        total_price += quantity * supermarket_stock[sku].price


    for offer in offers_priority:
        if offer.item in skus_counter:
            if offer.type == 1 and (offer.free_item in skus_counter) and skus_counter[offer.free_item] != 0:
                while skus_counter[offer.item] >= offer.quantity:
                    skus_counter[offer.item] -= offer.quantity
                    free_quantity = offer.free_quantity if skus_counter[offer.free_item] >= offer.free_quantity else skus_counter[offer.free_item]
                    total_price -= free_quantity * supermarket_stock[offer.free_item].price
                    skus_counter[offer.free_item] -= free_quantity
                    
            elif offer.type == 2:
                while skus_counter[offer.item] >= offer.quantity:
                    total_price -= offer.discounted_price
                    skus_counter[offer.item] -= offer.quantity

    return total_price