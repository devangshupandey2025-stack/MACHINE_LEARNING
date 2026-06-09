class Car:
    company = "Toyota"
    def __init__(self,model,price):
        self.model = model
        self.price = price
c1 = Car("Fortuner", 4500000)
c2 = Car("Supra", 8500000)
print(c1.model,c1.price,c1.company)
print(c2.model,c2.price,c2.company)
Car.company = "Honda"
print(c1.model,c1.price,c1.company)
print(c2.model,c2.price,c2.company)
c1.company = "BMW"
print(c1.company)
print(c2.company)
print(Car.company)
