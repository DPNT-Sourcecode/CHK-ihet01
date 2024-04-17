class StoreItem:
    def __init__(self, name, price):
        if not (isinstance(name, str) and len(name) == 1 and isinstance(price, int)):
                raise TypeError("StoreItem class accepts a string of one letter for item name and an integer for item price.")
        
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item: {self.name} | Price: {self.price}"


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
    'A': StoreItem('A', 50),
    'B': StoreItem('B', 30),
    'C': StoreItem('C', 20),
    'D': StoreItem('D', 15),
    'E': StoreItem('E', 40),
    'F': StoreItem('F', 10)
}

offers = [
    Offer('A', 3, price=130),
    Offer('A', 5, price=200),
    Offer('B', 2, price=45),
    Offer('E', 2, free_quantity=1, free_item='B'),
    Offer('F', 2, free_quantity=1, free_item='F')
]

# offers_priority = sorted(offers, key=lambda x: (x.type, -x.quantity))
offers_priority = sorted(offers, key=lambda x: x.discounted_price, reverse=True)    # Based on the note that all offers are well-balanced (a bit unclear, but assuming)


# for item in supermarket_stock.values():
#     print(item)

# for offer in offers_priority:
#     print(offer)