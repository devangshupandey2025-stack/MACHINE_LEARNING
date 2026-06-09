class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_details(self):
        print("Product: ", self.name)
        print("Price: ", self.price)
class Electronics(Product):
    def __init__(self,name,price,warranty):
        self.warranty = warranty
        super().__init__(name,price)
    def show_warranty(self):
        print("Warranty: ", self.warranty)
        
e1 = Electronics("Laptop", 75000, "2 years")

e1.show_details()
e1.show_warranty()
