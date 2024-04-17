class StoreItem:
    def __init__(self, name, price, offers=None):
        if not (isinstance(name, str) and len(name) == 1 and isinstance(price, int) and (isinstance(offers, list) or offers is None)):
                raise TypeError("StoreItem class accepts a string of one letter for item name, an integer for item price and \
                                 optional offers list of type list of list with 2 integers [[int, int]].")
        
        self.name = name
        self.price = price
        self.offers = None

    def __str__(self):
        string = f"Item: {self.name} | Price: {self.price}"


        return string


class Offer:
        def __init__(self, item, quantity, price=None, free_quantity=None, free_item=None):
            self.item = item
            self.quantity = quantity
            self.price = price
            self.free_quantity = free_quantity
            self.free_item = free_item

            self.type = 1 if free_item else 2
            self.discounted_price = self.calculate_discount()


        def calculate_discount(self):
            if self.type == 1:
                discount = supermarket_stock[self.free_item].price * self.free_quantity
            else:
                discount = (supermarket_stock[self.item].price * self.quantity) - self.price
            
            return discount

        def __str__(self):
            if self.type == 1:
                string = f"{self.quantity}{self.item} get {self.free_quantity}{self.free_item} free"
            else:
                string = f"{self.quantity}{self.item} for {self.price}"
                
            return string


supermarket_stock = {
    'A': StoreItem('A', 50, [[3, 130], [5, 200]]),
    'B': StoreItem('B', 30, [[2, 45]]),
    'C': StoreItem('C', 20),
    'D': StoreItem('D', 15),
    'E': StoreItem('E', 40, [[2, 1, 'B']]),
}

offers = [
    Offer('A', 3, price=130),
    Offer('A', 5, price=200),
    Offer('B', 2, price=45),
    Offer('E', 2, free_quantity=1, free_item='B')
]

# offers_priority = sorted(offers, key=lambda x: (x.type, -x.quantity))
offers_priority = sorted(offers, key=lambda x: x.discounted_price, reverse=True)    # Based on the note that all offers are well-balanced (a bit unclear, but assuming)


# for item in supermarket_stock.values():
#     print(item)

# for offer in offers_priority:
#     print(offer)