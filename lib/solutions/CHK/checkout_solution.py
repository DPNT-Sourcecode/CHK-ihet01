class StoreItem:
    def __init__(self, name, price, offer=None):
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
            self.total_price = details[1]


our_supermarket = [
    StoreItem('A', 50, [3, 130]),
    StoreItem('B', 30, [2, 45]),
    StoreItem('C', 20),
    StoreItem('D', 15)
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    


