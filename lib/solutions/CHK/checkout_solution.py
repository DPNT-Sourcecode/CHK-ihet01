from . import *

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not (isinstance(skus, str) and len(skus) >= 0):
        return -1
    
    total_price = 0

    # counts the instances of each element and stores the counts in a dictionary
    skus_counter = Counter(skus)

    total_price, skus_counter = apply_group_offers(total_price, skus_counter)

    for sku, quantity in skus_counter.items():
        # print(f"{quantity} x {sku}")
        if not sku in supermarket_stock:
            return -1

        total_price += quantity * supermarket_stock[sku].price

    
    total_price = apply_offers(total_price, skus_counter)

    return total_price


def apply_group_offers(total_price, skus_counter):
    for group_offer in group_offers:
        counter = 0
        for group_item in group_offer.items_priority:
            counter += skus_counter[group_item]

        counter = counter - (counter % group_offer.quantity)
        claimed_offers = counter // group_offer.quantity
        total_price += claimed_offers * group_offer.price

        for group_item in group_offer.items_priority:
            if skus_counter[group_item] <= counter:
                counter -= skus_counter[group_item]
                skus_counter[group_item] = 0
            else:
                skus_counter[group_item] -= counter
                counter = 0

            if counter == 0:
                    break
            
    return total_price, skus_counter

def apply_offers(total_price, skus_counter):
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

