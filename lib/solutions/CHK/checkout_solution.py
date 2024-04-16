class StoreItem:
    def __init__(self, name, price, offer=None):
        if not (isinstance(name, str) and len(name) == 1 and isinstance(price, int)):
                raise TypeError("StoreItem class accepts a string of one letter for item name, an integer for item price and an \
                                 optional offer of type list [int, int].")
        
        self.name = name
        self.price = price
        if offer:
            self.offer = self.Offer(offer)

    def __str__(self):
        return f"Item: {self.name} | Price: {self.price} | Offer: {self.offer}"
    

    class Offer:
        def __init__(self, details):
            if not (isinstance(details, list) and len(details) == 2 and isinstance(details[0], int) and isinstance(details[1], int)):
                raise TypeError("Offer class accepts a list of two integers ([int, int]) where the first element represents \
                                the quantity of the item and the second one the total offer price like [3, 150].")

            self.quantity = details[0]
            self.offer_price = details[1]

        def __str__(self):
            return f"{self.quantity} for {self.offer_price}"

supermarket_stock = {
    'A': StoreItem('A', 50, [3, 130]),
    'B': StoreItem('B', 30, [2, 45]),
    'C': StoreItem('C', 20),
    'D': StoreItem('D', 15)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not (isinstance(skus, str) and len(skus) > 0):
        return -1
    
    total_price = 0
    for sku in skus:
        print(sku)
        if sku in supermarket_stock:


