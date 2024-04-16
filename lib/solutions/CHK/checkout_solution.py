class StoreItem:
    def __init__(self, name, price, offer=None):
        self.name = name
        self.price = price
        if offer:
            self.offer = self.Offer(offer)

    def __str__(self):
        return f"Item: {self.name} | Price: {self.price} | Offer: {self.offer}"
    

    class Offer:
        def __init__(self, number, total_price):

            self.number = number
            self.total_price = total_price


our_supermarket = [
    StoreItem('A', 50, [3, 130]),
    StoreItem('B', 30, [2, 45]),
    StoreItem('C', 20),
    StoreItem('D', 15)
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    

