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
    'F': StoreItem('F', 10),
    'G': StoreItem('G', 20),
    'H': StoreItem('H', 10),
    'I': StoreItem('I', 35),
    'J': StoreItem('J', 60),
    'K': StoreItem('K', 70),
    'L': StoreItem('L', 90),
    'M': StoreItem('M', 15),
    'N': StoreItem('N', 40),
    'O': StoreItem('O', 10),
    'P': StoreItem('P', 50),
    'Q': StoreItem('Q', 30),
    'R': StoreItem('R', 50),
    'S': StoreItem('S', 20),
    'T': StoreItem('T', 20),
    'U': StoreItem('U', 40),
    'V': StoreItem('V', 50),
    'W': StoreItem('W', 20),
    'X': StoreItem('X', 17),
    'Y': StoreItem('Y', 20),
    'Z': StoreItem('Z', 21)
    
}

offers = [
    Offer('A', 3, price=130),
    Offer('A', 5, price=200),
    Offer('B', 2, price=45),
    Offer('E', 2, free_quantity=1, free_item='B'),
    Offer('F', 2, free_quantity=1, free_item='F'),
    Offer('H', 5, price=45),
    Offer('H', 10, price=80),
    Offer('K', 2, price=120),
    Offer('N', 3, free_quantity=1, free_item='M'),
    Offer('P', 5, price=200),
    Offer('Q', 3, price=80),
    Offer('R', 3, free_quantity=1, free_item='Q'),
    Offer('U', 3, free_quantity=1, free_item='U'),
    Offer('V', 2, price=90),
    Offer('V', 3, price=130),
    Offer('STXYZ', 3, price=45)
]

# offers_priority = sorted(offers, key=lambda x: (x.type, -x.quantity))
offers_priority = sorted(offers, key=lambda x: x.discounted_price, reverse=True)    # Based on the note that all offers are well-balanced (a bit unclear, but assuming)


# for item in supermarket_stock.values():
#     print(item)

for offer in offers_priority:
    print(offer)

