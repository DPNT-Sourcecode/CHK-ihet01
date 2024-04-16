from . import *

supermarket_stock = {
    'A': StoreItem('A', 50, [[3, 130], [5, 200]]),
    'B': StoreItem('B', 30, [[2, 45]]),
    'C': StoreItem('C', 20),
    'D': StoreItem('D', 15),
    'E': StoreItem('E', 40)      # No need to add this offer as it does not affect the total price.
}


for item in supermarket_stock.values():
    print(item)

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
        
        for offer in supermarket_stock[sku].offers:
            if offer:
                no_offer_claimed = quantity // offer.quantity
                rem_quantity = quantity % offer.quantity
                total_item_price = (no_offer_claimed * offer.price) + (rem_quantity * supermarket_stock[sku].price)
            else:
                total_item_price = quantity * supermarket_stock[sku].price

        total_price += total_item_price

    return total_price