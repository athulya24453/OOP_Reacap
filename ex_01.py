class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name, price: int, quantity=0):
        # applies limitations to each instance
        assert price >= 0 , f"Invalid price. {price} should be a positive number"
        assert quantity >= 0 , f"Invalid quantity. {quantity} should be a positive number"

        # creates the instance
        self.name = name 
        self.price = price
        self.quantity = quantity

        # Creates a list with all items
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
item1 = Item("Oneplus 7 pro", 100000, 3)
item2 = Item("Iphone XS Max", 200000, 5)

item1.apply_discount()
# print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
# print(item2.price)

item3 = Item("Asus ROG", 500000, 4)

# print(item1.calculate_total_price())

print(Item.all)

# for instance in Item.all:
#     print(instance.name + " - " + str(instance.quantity))