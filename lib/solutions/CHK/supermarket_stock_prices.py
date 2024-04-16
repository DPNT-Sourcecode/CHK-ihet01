class StoreItem:
    def __init__(self, name, price, offers=None):
        if not (isinstance(name, str) and len(name) == 1 and isinstance(price, int) and (isinstance(offers, list) or offers is None)):
                raise TypeError("StoreItem class accepts a string of one letter for item name, an integer for item price and \
                                 optional offers list of type list of list with 2 integers [[int, int]].")
        
        self.name = name
        self.price = price
        self.offers = None
        if offers:
            self.offers = []
            for offer in offers:
                self.offers.append(self.Offer(offer))
            
            self.offers = sorted(self.offers, key=lambda x: x.quantity, reverse=True)

    def __str__(self):
        string = f"Item: {self.name} | Price: {self.price}"
        if self.offers:
            string += f" | Offers: {[str(offer) for offer in self.offers]}"

        return string

    class Offer:
        def __init__(self, details):
            if not (isinstance(details, list) and len(details) == 2 and isinstance(details[0], int) and isinstance(details[1], int)):
                raise TypeError("Offer class accepts a list of two integers ([int, int]) where the first element represents \
                                the quantity of the item and the second one the total offer price like [3, 150].")

            self.quantity = details[0]
            self.price = details[1]

        def __str__(self):
            return f"{self.quantity} for {self.price}"



supermarket_stock = {
    'A': StoreItem('A', 50, [[3, 130], [5, 200]]),
    'B': StoreItem('B', 30, [[2, 45]]),
    'C': StoreItem('C', 20),
    'D': StoreItem('D', 15),
    'E': StoreItem('E', 40)      # No need to add this offer as it does not affect the total price.
}

# for item in supermarket_stock.values():
#     print(item)